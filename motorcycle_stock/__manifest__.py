# -*- coding: utf-8 -*-
{
    'name': "motorcycle_stock",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "GabrielRCL",
    'website': "https://www.github.com/GabrielRCL/odoo-training2",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Kawiil/Custom Modules',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['motorcycle_registry','sale_management'],

    # always loaded
    'data': [
        'views/motorcycle_stock_menuitems.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
    'auto_install': True,
}

