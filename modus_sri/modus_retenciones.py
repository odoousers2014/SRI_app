# -*- coding: utf-8 -*-
from openerp import models, fields, api

class ModusRetenciones(models.Model):
    _name = 'modus.retenciones'
    name = fields.Char('Número de Factura', required=True)
#    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)
#    date_invoice = fields.Date(string='Fecha de Emisión', required=True)
    date_invoice = fields.Date(string='Fecha de Emisión', required=True)
    partner_name = fields.Char('Nombre', required=True)
    partner_ruc = fields.Char('RUC', required=True)
    partner_address = fields.Char('Dirección', required=True)
