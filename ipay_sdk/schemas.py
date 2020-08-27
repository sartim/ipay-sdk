from marshmallow import Schema, fields


class CardPayment(Schema):
    live = fields.Int(required=True)
    oid = fields.Str(required=True)
    inv = fields.Str(required=True)
    amount = fields.Float(required=True)
    tel = fields.Str(required=True)
    eml = fields.Str(required=True)
    vid = fields.Str(required=True)
    curr = fields.Str(required=True)
    p1 = fields.Str(required=True)
    p2 = fields.Str(required=True)
    p3 = fields.Str(required=True)
    p4 = fields.Str(required=True)
    cbk = fields.Str(required=True)
    cst = fields.Int(required=True)
