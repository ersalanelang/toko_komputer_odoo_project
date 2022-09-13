from odoo import models, fields

class PartnerXlsx(models.AbstractModel):
    _name = 'report.komputertoko.report_komponen_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'New Description'
    tgl_laporan = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, komponen):
        # One sheet by partner
        sheet = workbook.add_worksheet('Daftar Komponen')
        # Menambahkan informasi tanggal laporan

        # Text style bold, jjika tidak perlu bisa dihapus
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_laporan))
        sheet.write(1, 0, 'Nama Komponen', bold)
        sheet.write(1, 1, 'Brand', bold)
        sheet.write(1, 2, 'Stok', bold)
        sheet.write(1, 3, 'Harga', bold)
        sheet.write(1, 4, 'Kategori', bold)
        
        row = 2
        col = 0
        for obj in komponen:
            col = 0
            # write(row, col, title, style)
            # style bersifat opsional
            # sheet.write(0, 0, obj.name, bold)
            sheet.write(row, col, obj.name)
            sheet.write(row, col + 1, obj.brand)
            sheet.write(row, col + 2, obj.stok)
            sheet.write(row, col + 3, obj.harga_jual)
            sheet.write(row, col + 4, obj.kelompokkomponen_id.name)
            row += 1