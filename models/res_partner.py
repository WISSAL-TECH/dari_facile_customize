# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResPartner(models.Model):
    """Inherits 'res.partner' and adds fields"""
    _inherit = 'res.company'

    black_list = fields.Boolean(string='Client black listé',
                                       default='False')
    created_in = fields.Many2one(string='Client créer sur',
                                       required='True')
