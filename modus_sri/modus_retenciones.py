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
    total_retencion = fields.Char('Total Retención', required=True)
    retencion_line_ids = fields.one2many('modus.retenciones.line', 'retencion_id', 'Retencion'),

class ModusRetencionesLine(models.Model):
    _name = 'modus.retenciones.line'
    retencion_id = fields.many2one('modus.retenciones', 'Retencion'),
    ejercicio_fiscal = fields.Char('Ejercicio Fiscal', required=True)
    base_imponible = fields.Char('Base Imponible', required=True)
    codigo_impuesto = fields.Char('Código Impuesto', required=True)
    impuesto_retencion = fields.Char('Impuesto', required=True)
    porcent_retencion = fields.Char('Porcentaje Retención', required=True)
    valor_retencion = fields.Char('Valor Retención', required=True)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: