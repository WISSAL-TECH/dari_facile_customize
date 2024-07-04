
from odoo import api, fields, models, _


class SaleOrder(models.Model):
    """Inherits 'sale.order' and adds fields"""
    _inherit = 'sale.order'

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string="Client",
        required=True,
        change_default=True,
        index=True,
        tracking=1,
        domain="[('company_id', 'in', (False, company_id)), ('black_list', '=', False)]"
    )




