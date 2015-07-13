# -*- coding: utf-8 -*-
{
    'name': "SRI Anexo Transaccional",
    'version': '0.2',

    'summary': """
        Modulo de integracion de Odoo 8.0 para exportar a MS
        Excel los datos del ATS en formato noviembre de 2014
    """,

    'description': """
        Modulo de integracion de Odoo 8.0 para exportar a MS
        Excel los datos del ATS en formato noviembre de 2014
    """,

    'author': "Modus S.A.",
    'website': "http://www.oksigeno.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting & Finance',
    'version': '0.1',

    # Sequence is a number that will show your module in the list of modules. 1, it will be up, 100 it will be down
    'sequence': 3,

    # any module necessary for this one to work correctly
    'depends': ['base', 'account_accountant'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'informante/views/informante_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'auto_install': False,
    'application': True,
    'installable': True,
}