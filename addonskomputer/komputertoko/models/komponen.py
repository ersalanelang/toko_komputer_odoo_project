from odoo import api, fields, models


class komponen(models.Model):
    _name = 'komputertoko.komponen'
    _description = 'New Description'

    name = fields.Char(string='Nama Komponen')
    brand = fields.Char(string='Brand')
    harga_jual = fields.Integer(string='Harga Jual', required=True)
    kelompokkomponen_id = fields.Many2one(comodel_name='komputertoko.kelompokkomponen',
                                            string='Kategori',
                                            ondelete='cascade')

    # supplier_id = fields.Many2many(comodel_name='ersamart.supplier', string='Supplier')
    stok = fields.Integer(string='Stok') # string=stok ini buat yang di panggil di field view
    supplier_id = fields.Many2many(comodel_name='komputertoko.supplier', string='Supplier')

