# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResCompany(models.Model):
    """Inherits 'res.company' and adds fields"""
    _inherit = 'res.company'

    marge_12 = fields.Float(string='Marge sur facilité 18 mois')
    marge_18 = fields.Float("Marge sur facilité 18 mois")
    marge_24 = fields.Float("Marge sur facilité 24 mois")
