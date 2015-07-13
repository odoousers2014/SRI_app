# -*- coding: utf-8 -*-
from openerp import models, fields, api

class ModusRetenciones(models.Model):
    _name = 'modus_retenciones'
    partner_id = fields.Many2one('res.partner', string='Partner', change_default=True,
        required=True, readonly=True)