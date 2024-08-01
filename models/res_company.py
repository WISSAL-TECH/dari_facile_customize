# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ResCompany(models.Model):
    """Inherits 'res.company' and adds fields"""
    _inherit = 'res.company'

    marge_12 = fields.Float(string='Marge sur facilité 12 mois')
    marge_18 = fields.Float("Marge sur facilité 18 mois")
    marge_24 = fields.Float("Marge sur facilité 24 mois")
    ccp = fields.Char(string="CCP", required=True, copy=False)
    key_ccp = fields.Char(string="Clé", required=True, copy=False)

    _sql_constraints = [
        ('ccp_unique', 'unique(ccp)', 'Numéro de CCP doit être unique.')
    ]
    @api.constrains('ccp', 'key')
    def _check_ccp_length(self):
        if self.ccp and (len(self.ccp) != 8 or not self.ccp.isdigit()):
            raise UserError("Le numéro de CCP doit comporter exactement 8 chiffres.")
        if self.key_ccp and (len(self.key_ccp) != 2 or not self.key_ccp.isdigit()):
            raise UserError("La clé de CCP doit comporter exactement 2 chiffres.")