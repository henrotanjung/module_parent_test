from odoo import models, fields, api

class MasterUom(models.Model):
    _name = 'master.uom'

    name = fields.Char(string='Name')