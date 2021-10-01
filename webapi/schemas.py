import marshmallow as msh

class WeddingImageSchema(msh.Schema):
    s3_key = msh.fields.Str()
    url = msh.fields.Str()