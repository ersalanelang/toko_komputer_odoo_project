from odoo import api, fields, models


class kelompokkomponen(models.Model):
    _name = 'komputertoko.kelompokkomponen'
    _description = 'New Description'

    name = fields.Selection([
        ('processor', 'PROCESSOR'),  # (<name>, <value>)
        ('vga', 'VGA'),
        ('ssd', 'SSD'),
        ('harddsik', 'HARDDISK'),
        ('motherboard', 'MOTHERBOARD'),
        ('rampc', 'RAM PC'),
        ('casing', 'CASING'),
        ('lcd', 'LCD')
        ], string='Komponen PC', required="1")
    kode_komponen = fields.Char(string='Kode Komponen')

    @api.onchange('name')
    def _compute_kode_komponen(self):
        if (self.name == 'processor'):
            self.kode_komponen = 'PCR'
        elif (self.name == 'vga'):
            self.kode_komponen= 'VGA'
        elif (self.name == 'ssd'):
            self.kode_komponen = 'SSD' 
        elif (self.name == 'harddsik'):
            self.kode_komponen = 'HDD' 
        elif (self.name == 'motherboard'):
            self.kode_komponen = 'MBD' 
        elif (self.name == 'rampc'):
            self.kode_komponen = 'RAM' 
        elif (self.name == 'casing'):
            self.kode_komponen = 'CSG' 
        elif (self.name == 'lcd'):
            self.kode_komponen = 'LCD'

    komponen_ids = fields.One2many(comodel_name='komputertoko.komponen',
                                    inverse_name='kelompokkomponen_id',
                                    string='Nama Komponen')
    
    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')

    @api.depends('komponen_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['komputertoko.komponen'].search([('kelompokkomponen_id','=',rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a

    daftar = fields.Char(string='Daftar isi')

# class brand(models.Model):
#     _name = 'komputertoko.kelompokkomponen'
#     _description = 'New Description'

#     name = fields.Selection([
#         ('processor', 'PROCESSOR'),  # (<name>, <value>)
#         ('vga', 'VGA'),
#         ('ssd', 'SSD'),
#         ('harddsik', 'HARDDISK'),
#         ('motherboard', 'MOTHERBOARD'),
#         ('rampc', 'RAM PC'),
#         ('casing', 'CASING'),
#         ('lcd', 'LCD')
#         ], string='Komponen PC', required="1")
    
#     Komponen_ids = fields.One2many(comodel_name='komputertoko.komponen',
#                                     inverse_name='kelompokkomponen_id',
#                                     string='Nama Komponen')