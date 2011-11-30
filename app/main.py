from google.appengine.ext import webapp
from google.appengine.api import urlfetch
import logging, StringIO
import zipfile

zip_path = 'https://github.com/runway7/hangar/zipball/master'

def refresh(request):    
    logging.info('Starting zip download from Github: %s' % zip_path)
    result = urlfetch.fetch(zip_path)
    file_stream = StringIO.StringIO(result.content)
    zip_file = zipfile.ZipFile(file_stream, 'r')
    [logging.info(f.filename) for f in zip_file.infolist()]
    

application = webapp.WSGIApplication([
    webapp.SimpleRoute('/refresh', handler = refresh)
], debug=True)
