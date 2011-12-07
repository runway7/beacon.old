import os, sys

current_path = os.path.abspath(os.path.dirname(__file__))

sys.path[0:0] = [
    current_path,
    os.path.join(current_path, 'lib'),
    os.path.join(current_path, 'lib', 'dist'),
    os.path.join(current_path, 'lib', 'dist.zip'),
]

from google.appengine.ext import webapp
from google.appengine.api import urlfetch

import logging, StringIO, functools, os
import zipfile, md_parser, jinja2

from models import Post



repo = 'runway7/hangar'

zip_path = 'https://github.com/%s/zipball/master' % repo

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

def render(template_file, data = {}):
    template = jinja_environment.get_template(template_file)
    response = webapp.get_request().app.response_class()
    response.out.write(template.render(data))
    return response
    
zip_stream = lambda s: zipfile.ZipFile(StringIO.StringIO(s), 'r')
fetch_as_zip = lambda url: zip_stream(urlfetch.fetch(url).content)

def _extract_posts(zip_file):
    md_files = md_parser.filter_markdown_files(zip_file.namelist())
    for md_file in md_files:
        with zip_file.open(md_file) as post:
            metadata, content = md_parser.parse(post)
            if metadata['publish']: yield Post.create(metadata, content) 
    

def refresh(request, zip_path = zip_path):    
    Post.delete_all()
    zip_file = fetch_as_zip(zip_path)
    Post.put_all(_extract_posts(zip_file))

def serve_post(request):
    post_url = request.path_info
    post = Post.get_by_id(post_url)
    if not post:
        webapp.abort(404)
    return render('post.html', dict(post = post))
    
def index(request):
    return render('index.html', dict(posts = Post.query().fetch()))

application = webapp.WSGIApplication([
    webapp.SimpleRoute('/_refresh/', handler = refresh),
    webapp.SimpleRoute('/', handler = index),
    webapp.SimpleRoute('/.*', handler = serve_post)
], debug=True)
