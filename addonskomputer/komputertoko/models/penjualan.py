from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class penjualan(models.Model):
    _name = 'komputertoko.penjualan'
    _description = 'New Description'

    name = fields.Char(string='No. Nota')
    nama_pembeli = fields.Many2one(comodel_name="res.partner",string='Nama Pembeli')
    id_member = fields.Char(	
        compute="_compute_id_member",	
        string='Id_member',	
        required=False)
    tgl_penjualan = fields.Datetime(
        string='Tanggal Transaksi',
        default=fields.Datetime.now())
    total_bayar = fields.Integer(
        string='Total Pembayaran',
        compute='_compute_totalbayar')
    detailpenjualan_ids = fields.One2many(
        comodel_name='komputertoko.detailpenjualan',
        inverse_name='penjualan_id',
        string='Detail Penjualan')
    state = fields.Selection([
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
        ('draft', 'Draft'),
    ],  required=True, readonly=True, default='draft')

    # untuk ngebuat id_member bisa di panggil di respartner
    # id member jadi bagian nama pembeli yang mana
    # nama_pembeli many20ne ke respartner
    @api.depends('nama_pembeli')
    def _compute_id_member(self):
        for rec in self:
            rec.id_member = rec.nama_pembeli.id_member

    #tombol untuk done
    def action_done(self):
        self.write({'state': 'done'})
    
    #tombol untuk confirm
    def action_confirm(self):
        self.write({'state': 'confirm'})

    #tombol untuk cancelled
    def action_cancelled(self):
        self.write({'state': 'cancelled'})

    #tombol untuk draft
    def action_draft(self):
        self.write({'state': 'draft'})

    
    # menghitung total bayar
    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for line in self:
            result = sum(self.env['komputertoko.detailpenjualan'].search(
                [('penjualan_id', '=', line.id)]).mapped('subtotal'))
            line.total_bayar = result

    # menghapus penjualan, tapi gk bisa semua harus 1-1
    # @api.ondelete(at_uninstall=False)
    # def __ondelete_penjualan(self):
    #     if self.detailpenjualan_ids:
    #         a=[]
    #         for rec in self:
    #             a = self.env['komputertoko.detailpenjualan'].search([('penjualan_id', '=', rec.id)])
    #             print(a)
    #         for ob in a:
    #             print(str(ob.komponen_id.name) + '' + str(ob.qty))
    #             ob.komponen_id.stok += ob.qty

    # untuk odoo 14
    def unlink(self):
        if self.filtered(lambda line: line.state != 'draft'):
            raise ValidationError("Tidak dapat  menghapus jika status bukan draft dan cancelled")
        # elif self.filtered(lambda line: line.state != 'cancelled'):
        #     raise ValidationError("Tidak dapat  menghapus jika status bukan draft dan cancelled")
        elif self.detailpenjualan_ids:
            a=[]
            for record in self:
                a = self.env['komputertoko.detailpenjualan'].search([('penjualan_id','=',record.id)])
            for ob in a:
                print(str(ob.komponen_id.name) + '' + str(ob.qty))
                ob.komponen_id.stok += ob.qty
        record = super(penjualan,self).unlink()

    # edit -> save
    # sistemnya, misal beli barang a, lalu di edit, maka barang yang di beli a akan dkembailkan dullu
    # lalu akan dikurangi dengan edit
    def write(self, vals):
        # Balikin dulu stok barangnya
        for rec in self:
            a = self.env['komputertoko.detailpenjualan'].search([('penjualan_id','=',rec.id)])
            print(a)
            for data in a:
                print(str(data.komponen_id.name)+' '+str(data.komponen_id.stok))
                data.komponen_id.stok += data.qty
        record = super(penjualan, self).write(vals)
        # Baru edit qty barang akan berhasil
        for rec in self:
            b = self.env['komputertoko.detailpenjualan'].search([('penjualan_id','=',rec.id)])
            print(b)
            for databaru in b:
                if databaru in a:
                    print(str(databaru.komponen_id.name)+' '+str(databaru.komponen_id.stok))
                    databaru.komponen_id.stok -= databaru.qty
                else:
                    pass
        return record

    # membuat contrainst
    _sql_constraints = [
        ('unique_name','unique (name)', 'Nomor Nota tidak boleh sama!! ') # <nama constrain> <constrainnya> <pesan constrain>
    ]

class detailpenjualan(models.Model):
    _name = 'komputertoko.detailpenjualan'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    penjualan_id = fields.Many2one(
        comodel_name='komputertoko.penjualan',
        string='Detail Penjualan')
    komponen_id = fields.Many2one(  # ke komponen
        comodel_name='komputertoko.komponen',
        string='List Komponen')
    harga_satuan = fields.Integer(
        string='Harga Satuan',
        onchange='_onchange_komponen_id')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')
    
    # menghitung barang qty X harga barang
    @api.depends('harga_satuan','qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.harga_satuan
    
    # membuat Variabel harga satuan menjadi harga jual
    @api.onchange('komponen_id')
    def _onchange_komponen_id(self):
        if self.komponen_id.harga_jual:
            self.harga_satuan = self.komponen_id.harga_jual

    # mengurangi stok - qty ketika telah transaksi
    @api.model
    def create(self,vals):
        record = super(detailpenjualan,self).create(vals)
        if record.qty:
            self.env['komputertoko.komponen'].search([('id','=',record.komponen_id.id)]).write({'stok' : record.komponen_id.stok - record.qty})
        return record

    # membuat constraint jika barang kurang 0 dan stok kosng dengan python
    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty < 1 :
                raise ValidationError(f"Barang yang dibeli tidak boleh kosong")
            elif (rec.komponen_id.stok < rec.qty):
                raise ValidationError(f"Stok {rec.komponen_id.name} barang ini tidak mencukupi, hanya tersedia {rec.komponen_id.stok}")
    
    # cara dengan constraint
    # _sql_constraints = [
    #     ('check_quantity1','CHECK(qty < 1)', 'Tidak boleh 1') 
    #     ('check_quantity2','CHECK(stok < qty)', 'barang tidak mencukupi') 
    # ]
