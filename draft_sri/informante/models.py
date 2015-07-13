# -*- coding: utf-8 -*-
from openerp import models, fields, api

# class sri_ats(models.Model):
#     _name = 'sri_ats.sri_ats'

#     name = fields.Char()

# Identificacion
#   donde "_name" representa el nombre de la tabla en PostgreSQL
#   donde "name" representa los nombres de las columnas

class informante(models.Model):
     _name = 'sri.informante'

     TipoIdInformante = fields.Char(string="Tipo Id Informante", required=True)
     IdInformante = fields.Char(string="Número de Identificación del Informante", required=True)
     razonSocial = fields.Char(string="Razón o denominación social", required=True)
     Anio = fields.Char(string="Año - período informado", required=True)
     Mes = fields.Char(string="Mes - período informado", required=True)
     numEstabRuc = fields.Char(string="Número de Establecimientos del sujeto pasivo inscritos en el RUC", required=True)
     totalVentas = fields.Char(string="Total venta reportadas en el período informado", required=True)
     codigoOperativo = fields.Char(string="Código tipo de Operativo", required=True)

# class informante(models.Model):
#     _name = 'sri.informante'
#     _inherit = 'res.partner'

#     ruc = fields.Integer(string="RUC")