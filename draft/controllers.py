# -*- coding: utf-8 -*-
from openerp import http

# class SriAts(http.Controller):
#     @http.route('/sri_ats/sri_ats/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sri_ats/sri_ats/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sri_ats.listing', {
#             'root': '/sri_ats/sri_ats',
#             'objects': http.request.env['sri_ats.sri_ats'].search([]),
#         })

#     @http.route('/sri_ats/sri_ats/objects/<model("sri_ats.sri_ats"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sri_ats.object', {
#             'object': obj
#         })