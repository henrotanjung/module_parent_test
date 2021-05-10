from odoo import models, fields, api

class Product(models.Model):
    _name = 'product.product'

    name = fields.Char(string='Product Name', required=True)
    uom = fields.Many2one('master.uom', string='UOM')
    qty = fields.Integer()