from google.appengine.ext.ndb import model

class Config(model.Model):
    value = model.StringProperty(indexed = False)
