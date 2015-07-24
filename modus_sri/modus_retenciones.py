# -*- coding: utf-8 -*-
from openerp import models, fields, api

class ModusRetencionesLine(models.Model):
    _name = 'modus.retenciones.line'
    name = fields.Char('Item')
#    item_id = fields.Many2one('modus.retenciones', 'Número de Retención')
    ejercicio_fiscal = fields.Char('Ejercicio Fiscal')
    base_imponible = fields.Float('Base Imponible', required=True)
    codigo_impuesto = fields.Char('Código Impuesto')
    impuesto_retencion = fields.Char('Impuesto')
    porcent_retencion = fields.Float('Porcentaje Retención', required=True)
    valor_retencion = fields.Float('Valor Retención', compute='_compute_valor_retencion', store=True)

    @api.one
    @api.depends('base_imponible', 'porcent_retencion')
    def _compute_valor_retencion(self):
        for record in self:
            record.valor_retencion = record.base_imponible * (record.porcent_retencion / 100)

class ModusRetenciones(models.Model):
    _name = 'modus.retenciones'
    name = fields.Char('Número de Retención', required=True)
    items = fields.One2many('modus.retenciones.line', 'name', 'Items')
#    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)
#    date_invoice = fields.Date(string='Fecha de Emisión', required=True)
    date_invoice = fields.Date(string='Fecha de Emisión', required=True)
    partner_name = fields.Char('Nombre', required=True)
    partner_ruc = fields.Char('RUC', required=True)
    partner_address = fields.Char('Dirección', required=True)
    total_retencion = fields.Float('Total Retención', compute='_compute_total_retencion', store=True)

    @api.one
    @api.depends('modus_retenciones_line.valor_retencion')
    def _compute_total_retencion(self):
#        self.total_retencion = sum(line.valor_retencion for line in self.modus_retenciones_line)
        for record in self:
            record.total_retencion = sum(line.valor_retencion for line in record.modus_retenciones_line)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: