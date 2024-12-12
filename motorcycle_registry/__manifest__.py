{
    'name': 'Motorcycle Registry',
    'summary': 'Manage Registration of Motorcycles',
    'description': 'Motorcycle Registry This Module is used do keep track of the Motorcycle Registration and Onwership of each motorcycle of the brand',
    'author': 'GabrielRCL',
    'license': 'LGPL-3',
    'version': '0.0.1',
    'category': 'Kawiil/Custom Modules',
    'website': 'www.github.com/GabrielRCL/odoo-training2',
    'depends': ['base'],
    'data': [
        'security/motorcycle_registry_groups.xml',
        'security/ir.model.access.csv',
        'views/motorcycle_registry_menuitems.xml',
        'data/motorcycle_registry_data.xml',
        'views/motorcycle_registry_views.xml',
    ],
    'demo': [
        'demo/motorcycle_registry_demo.xml',
    ],
    'application': True,
}