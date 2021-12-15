# -*- coding: utf-8 -*-
{
    'name': "POS Custom Receipt",
    'support': "am1rw@hotmail.com",
    'price': 0,
    'currency': "$",
    'summary': """
        This module Allows you to print POS receipt with qr
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '15.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],

    'assets': {
        'point_of_sale.assets': [
            'pos_custom_receipt/static/src/js/PosQRCode.js',
            'pos_custom_receipt/static/src/js/Models.js',
            'pos_custom_receipt/static/src/js/qrcode.js',
            'pos_custom_receipt/static/src/css/OrderReceipt.css',
        ],
        'web.assets_qweb': [
            'pos_custom_receipt/static/src/xml/OrderReceipt.xml',
        ],

    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
