# -*- coding: utf-8 -*-
from openerp import models, fields, api

class ModusRetenciones(models.Model):
    _name = 'modus.retenciones'
    name = fields.Char('Número de Retención', required=True)
    retencion_detalle = fields.Many2one('modus.retenciones.line', 'Productos y/o Servicios')
#    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)
#    date_invoice = fields.Date(string='Fecha de Emisión', required=True)
    date_invoice = fields.Date(string='Fecha de Emisión', required=True)
    partner_name = fields.Char('Nombre', required=True)
    partner_ruc = fields.Char('RUC', required=True)
    partner_address = fields.Char('Dirección', required=True)
#    total_retencion = fields.Char('Total Retención', required=True)

class ModusRetencionesLine(models.Model):
    _name = 'modus.retenciones.line'
    name = fields.Char('Productos y/o Servicios')
    retenciones_name = fields.Many2one('modus.retenciones', 'Número de Retención', required=True)
    ejercicio_fiscal = fields.Char('Ejercicio Fiscal')
    base_imponible = fields.Char('Base Imponible')
    codigo_impuesto = fields.Char('Código Impuesto')
    impuesto_retencion = fields.Char('Impuesto')
    porcent_retencion = fields.Char('Porcentaje Retención')
    valor_retencion = fields.Char('Valor Retención')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: