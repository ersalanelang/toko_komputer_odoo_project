from odoo import http, models, fields
from odoo.http import request
import json

class komputertoko(http.Controller):
    @http.route('/komputertoko/getkomponen', auth='public', method=['GET'])
    def getKomponen(self, **kw):
        # Mengambil semua barang
        komponen = request.env['komputertoko.komponen'].search([])
        isi = []
        for bb in komponen:
            isi.append({
                'nama_barang' : bb.name,
                'harga_jual' : bb.harga_jual,
                'stok' : bb.stok
            })
        return json.dumps(isi)

    @http.route('/komputertoko/getsupplier', auth='public', method=['GET'])
    def getSupplier(self, **kw):
        # Mengambil semua barang
        supplier = request.env['komputertoko.supplier'].search([])
        sup = []
        for s in supplier:
            sup.append({
                'nama_supplier' : s.name,
                'alamat' : s.alamat,
                'no telepon' : s.no_telp,
                'barang' : s.komponen_id[0].name # nama barang pertama saja
            })
        return json.dumps(sup)

# class Komputertoko(http.Controller):
#     @http.route('/komputertoko/komputertoko', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/komputertoko/komputertoko/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('komputertoko.listing', {
#             'root': '/komputertoko/komputertoko',
#             'objects': http.request.env['komputertoko.komputertoko'].search([]),
#         })

#     @http.route('/komputertoko/komputertoko/objects/<model("komputertoko.komputertoko"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('komputertoko.object', {
#             'object': obj
#         })
