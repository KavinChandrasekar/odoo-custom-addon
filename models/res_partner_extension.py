from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_custom_code = fields.Char(string='Custom Code', help='Custom CRM code for demo')
