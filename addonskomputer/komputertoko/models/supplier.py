from odoo import api, fields, models


class supplier(models.Model):
    _name = 'komputertoko.supplier'
    _description = 'New Description'

    name = fields.Char(string='Nama Perushaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telepon')
    komponen_id = fields.Many2many(comodel_name='komputertoko.komponen', string='komponen')
