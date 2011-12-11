from google.appengine.ext.ndb import model, key

lower_validator = lambda prop, val: val.lower()

class Config(model.Model):
    value = model.StringProperty(indexed = False)

class Post(model.Model):
    date = model.DateProperty()
    title = model.StringProperty(indexed = False)
    content = model.TextProperty(indexed = False)
    tags = model.StringProperty(repeated = True, validator = lower_validator)

    @classmethod
    def all(cls):
        return cls.query().fetch()
    
    @classmethod
    def create(cls, metadata, content):
        return cls(
            key = key.Key(cls, metadata['slug']),
            date = metadata['date'],
            title = metadata['title'],
            tags = metadata['tags'],
            content = content
        )

    @classmethod
    def delete_all(cls):
        return model.delete_multi(cls.query().fetch(keys_only = True))
    
    @classmethod
    def put_all(cls, posts):
        return model.put_multi(posts)