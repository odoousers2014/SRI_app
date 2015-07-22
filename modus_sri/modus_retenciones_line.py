# -*- coding: utf-8 -*-
from openerp import models, fields, api

class ModusRetencionesLine(models.Model):
    _name = 'modus.retenciones.line'
    retencion_id = fields.Many2one('modus.retenciones', 'Master'),
    ejercicio_fiscal = fields.Char('Ejercicio Fiscal')
    base_imponible = fields.Char('Base Imponible')
    codigo_impuesto = fields.Char('Código Impuesto')
    impuesto_retencion = fields.Char('Impuesto')
    porcent_retencion = fields.Char('Porcentaje Retención')
    valor_retencion = fields.Char('Valor Retención')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: