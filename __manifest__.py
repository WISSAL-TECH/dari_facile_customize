{
    'name': 'Dari facile customization',
    'version': '1.0',
    'summary': 'Add custom file to Odoo',
    'description': 'A module to add a custom files to Odoo.',
    'depends': ['base','stock', 'sale','sales_contract_and_recurring_invoices'],
    'data': [
        'views/res_partner_views.xml',
        'views/res_company_views.xml',
        'views/subscription_contracts_views.xml',
        'views/account_move.xml',
        'security/ir.model.access.csv',
        'reports/account_move_report.xml',
        'reports/sale_order_report.xml',
        'reports/stock_picking_report.xml',

        'reports/paperformat_report.xml',
        # 'reports/report_layout.xml',
        'reports/report_contract.xml',
        'reports/report_prelevement.xml'

    ],
    'installable': True,
    'application': False,
    'auto_install': False,

}
