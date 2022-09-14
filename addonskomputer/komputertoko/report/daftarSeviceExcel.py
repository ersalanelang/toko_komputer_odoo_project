from odoo import models, fields

class PartnerXlsx(models.AbstractModel):
    _name = 'report.komputertoko.report_service_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'New Description'
    tgl_laporan = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, service):
        # One sheet by partner
        sheet = workbook.add_worksheet('Daftar service')
        # Menambahkan informasi tanggal laporan

        # Text style bold, jjika tidak perlu bisa dihapus
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_laporan))
        sheet.write(1, 0, 'No Nota', bold)
        sheet.write(1, 1, 'Nama Konsumen', bold)
        sheet.write(1, 2, 'device', bold)
        sheet.write(1, 3, 'Tgl Masuk', bold)
        sheet.write(1, 4, 'Permasalahan', bold)
        sheet.write(1, 5, 'Nama_teknisi', bold)
        
        row = 2
        col = 0
        for obj in service:
            col = 0
            sheet.write(row, col, obj.name)
            for item in obj.nama_service:
                sheet.write(row, col + 1, item.display_name)
            # sheet.write(row, col + 1, obj.nama_service)
            sheet.write(row, col + 2, obj.device)
            sheet.write(row, col + 3, obj.tgl_service)
            sheet.write(row, col + 4, obj.masalah)
            for item in obj.nama_teknisi:
                sheet.write(row, col + 5, item.name)
            # sheet.write(row, col + 5, obj.nama_teknisi)
            row += 1