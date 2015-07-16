# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ShowVat(models.Model):
     _inherit = 'account_invoice'
     vat = fields.related('partner_id', 'vat', type='many2one', relation='res.partner', string='Vat', store=True, readonly=True)