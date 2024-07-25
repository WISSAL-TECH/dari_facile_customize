
from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    """Inherits 'product.template' and adds fields"""
    _inherit = 'product.template'

    detailed_type = fields.Selection([
        ('consu', 'Consommable'),
        ('service', 'Service'), ('product', 'Article stockable')], string="Type d'article", default='product',
        required=True,
        help=
        "Un produit stockable est un produit dont on gère le stock. L'application \"Inventaire\" doit être installée. \n"
        "Un produit consommable, d'un autre côté, est un produit pour lequel le stock n'est pas géré.\n"
        "Un service est un produit immatériel que vous fournissez.")



