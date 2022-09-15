from odoo import api, fields, models

class service(models.Model):
    _name = 'komputertoko.service'
    _description = 'New Description'

    name = fields.Char(string='No. Nota')
    nama_service = fields.Many2one(comodel_name="res.partner",string='Nama Pembeli')
    device = fields.Selection(
        string="Device",
        selection=[('laptop', 'Laptop'),
                   ('komputer', 'Komputer')],
        required = True)
    tgl_service = fields.Datetime(
        string='Tanggal Masuk',
        default=fields.Datetime.now())
    masalah = fields.Char(string='Permasalahan')
    nama_teknisi = fields.Many2one(comodel_name="komputertoko.teknisi",string="Teknisi")
    state = fields.Selection([     # harus state kaga boleh di custom
        ('progress', 'Progress'),
        ('selesai', 'Selesai'),
        ('masuk', 'Masuk'),
        ('cancelled', 'cancelled'),
    ],  required=True, readonly=True, default='masuk')
    id_member = fields.Char(	
        compute="_compute_id_member",	
        string='Id_member',	
        required=False)

    @api.depends('nama_service')
    def _compute_id_member(self):
        for rec in self:
            rec.id_member = rec.nama_service.id_member

    #tombol untuk selesai
    def action_selesai(self):
        self.write({'state': 'selesai'})
    
    #tombol untuk progress
    def action_progress(self):
        self.write({'state': 'progress'})

    #tombol untuk masuk
    def action_masuk(self):
        self.write({'state': 'masuk'})
    
    #tombol untuk cancelled
    def action_cancelled(self):
        self.write({'state': 'cancelled'})

    def unlink(self):
        if self.filtered(lambda line: line.state != 'masuk'):
            raise ValidationError("Tidak dapat  menghapus jika status bukan masuk")