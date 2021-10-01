import mongoengine as me

class WeddingImage(me.Document):
    s3_key = me.StringField(unique=True)
    url = me.StringField()
    approved = me.BooleanField(default=False)
    