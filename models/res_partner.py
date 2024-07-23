# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResPartner(models.Model):
    """Inherits 'res.partner' and adds fields"""
    _inherit = 'res.partner'

    black_list = fields.Boolean(string='Client black listé',default=False)
    created_in = fields.Many2one("res.company", string='Client créer sur',required=True,default=lambda self: self.env.company)
    ccp = fields.Char(string="CCP", required=True, copy=False)

    _sql_constraints = [
        ('ccp_unique', 'unique(ccp)', 'The CCP must be unique.')
    ]
    arabic_name = fields.Char(string='الاسم')
    arabic_job = fields.Char(string='الوظيفة')
    arabic_birthdate = fields.Date(string='تاريخ الميلاد')