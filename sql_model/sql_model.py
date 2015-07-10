# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp import tools

class sql_model(models.Model):
    _name = 'sql.report'
    _auto = False
    nombre = fields.Char('Cliente', readonly=True)
    total = fields.Integer('Total', readonly=True)

    def init(self, cr):
        tools.sql.drop_view_if_exists(cr, 'sql_report')
        cr.execute("""
                    CREATE OR REPLACE VIEW "sql_report" AS (
                    SELECT
                    ROW_NUMBER() over (order by "public".res_partner."name") AS "id",
                    "public".res_partner."name" AS "nombre",
                    Sum("public".account_invoice.amount_total) AS "total"
                    FROM (account_invoice
                    JOIN res_partner ON (((account_invoice.commercial_partner_id = res_partner.id) AND (account_invoice.partner_id = res_partner.id))))
                    WHERE ((account_invoice.type)::text = 'out_invoice'::text)
                    GROUP BY
                    "nombre"
                    )
        """)

sql_model()