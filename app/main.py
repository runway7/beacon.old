import os, sys

current_dir = os.path.dirname(__file__)
current_path = os.path.abspath(current_dir)

sys.path[0:0] = [
    current_path,
    os.path.join(current_path, 'lib'),
    os.path.join(current_path, 'lib', 'dist'),
    os.path.join(current_path, 'lib', 'dist.zip'),
]

from google.appengine.ext import webapp
from google.appengine.api import urlfetch
from google.appengine.ext.ndb import context

import logging, StringIO, functools, os
import zipfile, md_parser, jinja2

from models import Post

repo = 'runway7/hangar'

zip_path = 'https://github.com/%s/zipball/master' % repo

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(current_dir, 'templates')))

def render(template_file, data = {}):
    template = jinja_environment.get_template(template_file)
    response = webapp.get_request().app.response_class()
    response.out.write(template.render(data, url_for = webapp.uri_for))
    return response
    
zip_stream = lambda stream: zipfile.ZipFile(StringIO.StringIO(stream), 'r')
fetch_as_zip = lambda url: zip_stream(urlfetch.fetch(url).content)

def _extract_posts(zip_file):
    md_files = md_parser.filter_markdown_files(zip_file.namelist())
    for md_file in md_files:
        with zip_file.open(md_file) as post:
            metadata, content = md_parser.parse(post)
            if metadata['publish']: yield Post.create(metadata, content) 
    

def refresh(request, zip_path = zip_path):        
    zip_file = fetch_as_zip(zip_path)
    posts = [post for post in _extract_posts(zip_file)]
    Post.delete_all()
    Post.put_all(posts)

def serve_post(request):
    post_url = request.path_info
    post = Post.get_by_id(post_url)
    if not post: webapp.abort(404)
    return render('post.html', dict(post = post))

def tagged(request, tag):
    return render('index.html', dict(posts = Post.query(Post.tags == tag), without_intro = True))

def index(request):
    return render('index.html', dict(posts = Post.all()))

application = context.toplevel(webapp.WSGIApplication([
    webapp.SimpleRoute('/_refresh/', handler = refresh),
    webapp.Route('/tags/<tag>', handler = tagged, name = 'by-tag'), 
    webapp.SimpleRoute('/', handler = index), 
    webapp.SimpleRoute('/.*', handler = serve_post)
], debug=True).__call__)
