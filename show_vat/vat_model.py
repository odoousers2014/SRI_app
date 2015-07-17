# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ShowVat(models.Model):
     _inherit = 'account.invoice'
     vat = fields.Char(related='res_partner.vat', store=True)