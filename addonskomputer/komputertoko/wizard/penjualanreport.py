from odoo import fields, models, api


class penjualanreport(models.TransientModel):
    _name = 'komputertoko.penjualanreport'
    _description = 'Description'

    konsumen_id = fields.Many2one(
        comodel_name='res.partner',
        string='Konsumen',
        required=False)
    dari_tgl = fields.Date(
        string='Dari Tanggal',
        required=False)
    ke_tgl = fields.Date(
        string='Ke tanggal',
        required=False)

    def action_penjualan_report(self):
        filter = []
        konsumen_id = self.konsumen_id
        dari_tgl = self.dari_tgl
        ke_tgl = self.ke_tgl
        if konsumen_id:
            filter += [('nama_pembeli', '=', konsumen_id.id)]
        if dari_tgl:
            filter += [('tgl_penjualan', '>=', dari_tgl)]
        if ke_tgl:
            filter += [('tgl_penjualan', '<=', ke_tgl)]
        print(filter)
        penjualan = self.env['komputertoko.penjualan'].search_read(filter) # search readdalem nya objek
        print(penjualan)
        data = {
            'form': self.read()[0],
            'penjualanxx': penjualan,
        }
        print(data)
        return self.env.ref('komputertoko.report_komputertoko_penjualanreport_pdf').report_action(self, data=data) #record id="report_ersamart_penjualanreport_pdf" di report.xml