from odoo import api, fields, models

'''
Membuat model BarangDarang yang inherit
ke Transient Model, Odoo 14 ke atas harus
di daftarkan di security
'''
class komponendatang(models.TransientModel):
    _name = 'komputertoko.komponendatang'
    _description = 'New Description'

    komponen_id = fields.Many2one(comodel_name='komputertoko.komponen', string='Nama komponen', required=True)
    jumlah = fields.Integer(string='Jumlah', required=False)

    def button_barangdatang(self):
        for line in self:
            self.env['komputertoko.komponen']\
            .search([('id', '=', line.komponen_id.id)])\
            .write({'stok': line.komponen_id.stok +  line.jumlah})