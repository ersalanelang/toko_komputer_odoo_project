from odoo import models, fields

class PartnerXlsx(models.AbstractModel):
    _name = 'report.komputertoko.report_supplier_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'New Description'
    tgl_laporan = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, supplier):
        # One sheet by partner
        sheet = workbook.add_worksheet('Daftar Supplier')
        # Menambahkan informasi tanggal laporan

        # Text style bold, jjika tidak perlu bisa dihapus
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_laporan))
        sheet.write(1, 0, 'Nama Perusahaan', bold)
        sheet.write(1, 1, 'Alamat', bold)
        sheet.write(1, 2, 'No. Telepon', bold)
        sheet.write(1, 3, 'Produk', bold)
        
        row = 2
        col = 0
        for obj in supplier:
            col = 0
            # write(row, col, title, style)
            # style bersifat opsional
            # sheet.write(0, 0, obj.name, bold)
            sheet.write(row, col, obj.name)
            sheet.write(row, col + 1, obj.alamat)
            sheet.write(row, col + 2, obj.no_telp)

            for item in obj.komponen_id:
                sheet.write(row, col + 3, item.name)
                col += 1
            row += 1