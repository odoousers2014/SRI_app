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

class ModusRetencionesLine(models.Model):
    _name = 'modus.retenciones.line'
    ejercicio_fiscal = fields.Char('Ejercicio Fiscal', required=True)
    base_imponible = fields.Char('Base Imponible', required=True)
    codigo_impuesto = fields.Char('Código Impuesto', required=True)
    impuesto_retencion = fields.Char('Impuesto', required=True)
    porcentaje_retencion = ('Porcentaje de Retención', required=True)
    valor_retencion = fields.Char('Valor Retención', required=True)