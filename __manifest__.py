{
    'name': 'Dari facile customization',
    'version': '1.0',
    'summary': 'Add custom file to Odoo',
    'description': 'A module to add a custom files to Odoo.',
    'depends': ['base', 'sale','sales_contract_and_recurring_invoices'],
    'data': [
        'views/res_partner_views.xml',
        'views/res_company_views.xml',
        'views/subscription_contracts_views.xml',
        'views/account_move.xml'
        'reports/account_move_report.xml',
        'reports/sale_order_report.xml',
        'reports/stock_picking_report.xml'

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
