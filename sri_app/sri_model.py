# -*- coding: utf-8 -*-

from openerp import models, fields, api

class res_partner(models.Model):
    _inherit = 'res.partner'
    numeroRuc = fields.Integer('RUC', help="Ingrese el número RUC", required=True)