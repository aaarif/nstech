from odoo import fields, models 

class Material(models.Model):
    _name = "sale_management.material"
    code = fields.Char(string="Code")
    name = fields.Char(String="Name")
    type = fields.Selection([
        (1, "Fabric"),
        (2, "Jeans"),
        (3, "Cotton"),
    ], default=1)
    buy_price = fields.Integer(Integer="Buy Price")
    related_supplier = fields.Selection([(1,"Supplier 1"),
                                         (2,"Supplier 2"),], default = 1)
    