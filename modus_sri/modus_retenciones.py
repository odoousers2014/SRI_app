# -*- coding: utf-8 -*-
from openerp import models, fields, api

class ModusRetenciones(models.Model):
    _name = 'modus_retenciones'
    _description = "Retencion"
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)
    date_invoice = fields.Date(string='Fecha de Emisión', required=True)
