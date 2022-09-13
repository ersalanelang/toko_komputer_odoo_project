from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    poin        = fields.Integer(string='Poin')
    # level       = fields.Char(string='Level')
    is_konsumen = fields.Boolean(string='Is Konsumen')
    is_direksi  = fields.Boolean(string='Is Direksi')
