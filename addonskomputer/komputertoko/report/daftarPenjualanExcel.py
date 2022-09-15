from odoo import models, fields

class PartnerXlsx(models.AbstractModel):
    _name = 'report.komputertoko.report_penjualan_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'New Description'
    tgl_laporan = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, penjualan):
        # One sheet by partner
        sheet = workbook.add_worksheet('Daftar Penjualan')
        # Menambahkan informasi tanggal laporan

        # Text style bold, jjika tidak perlu bisa dihapus
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_laporan))
        sheet.write(1, 0, 'No Nota', bold)
        sheet.write(1, 1, 'Nama Pembeli', bold)
        sheet.write(1, 2, 'Tgl Transaksi', bold)
        sheet.write(1, 3, 'Quantity', bold)
        sheet.write(1, 4, 'Total Pembelian', bold)
        
        row = 2
        col = 0
        for obj in penjualan:
            col = 0
            # write(row, col, title, style)
            # style bersifat opsional
            # sheet.write(0, 0, obj.name, bold)
            sheet.write(row, col, obj.name)
            for item in obj.nama_pembeli:
                sheet.write(row, col + 1, item.display_name)
            sheet.write(row, col + 2, obj.tgl_penjualan)
            # sheet.write(row, col + 3, obj.detailpenjualan_ids.qty)
            sheet.write(row, col + 4, obj.total_bayar)
            row += 1

    # def generate_xlsx_report(self, workbook, data, detailpenjualan):
    #     # One sheet by partner
    #     sheet = workbook.add_worksheet('Daftar Penjualan')
    #     # Menambahkan informasi tanggal laporan

    #     # Text style bold, jjika tidak perlu bisa dihapus
    #     bold = workbook.add_format({'bold': True})
    #     sheet.write(1, 3, 'Quantity', bold)

    #     row = 2
    #     col = 0

        # for a in detailpenjualan:
        #     col = 3
        #     # write(row, col, title, style)
        #     # style bersifat opsional
        #     # sheet.write(0, 0, obj.name, bold)
        #     sheet.write(row, col, a.qty)
        #     row += 1