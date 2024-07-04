{
    'name': 'Dari facile customization',
    'version': '1.0',
    'summary': 'Add custom file to Odoo',
    'description': 'A module to add a custom files to Odoo.',
    'depends': ['base', 'sale'],
    'data': [
        'views/res_partner_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
        ],
    },
    'qweb': [
    ],
}
