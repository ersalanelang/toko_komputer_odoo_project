from odoo import api, fields, models

class person(models.Model):
    _name = 'komputertoko.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Datetime(string='Tanggal Lahir')


class pegawai(models.Model):
    _name = 'komputertoko.pegawai'
    _inherit = 'komputertoko.person'
    _description = 'New Description'

    id_pegawai = fields.Char(string='ID pegawai')

class teknisi(models.Model):
    _name = 'komputertoko.teknisi'
    _inherit = 'komputertoko.person'
    _description = 'New Description'

    id_teknisi = fields.Char(string='ID Teknisi')