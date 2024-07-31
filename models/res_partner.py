# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    """Inherits 'res.partner' and adds fields"""
    _inherit = 'res.partner'

    black_list = fields.Boolean(string='Client black listé',default=False)
    created_in = fields.Many2one("res.company", string='Client créer sur',required=True,default=lambda self: self.env.company)
    ccp = fields.Integer(string="CCP", required=True, copy=False)
    start_date = fields.Selection([
        ('1', 'Le 1er'),
        ('13', 'Le 13'),
        ('17', 'Le 17'),
    ], string="Date de début de prélèvement")
    surname = fields.Char('Prénom')
    num_card = fields.Integer(string="Numéro de carte nationale/Numéro de permis")

    _sql_constraints = [
        ('ccp_unique', 'unique(ccp)', 'Numéro de CCP doit être unique.')
    ]
    arabic_name = fields.Char(string='الاسم')
    arabic_job = fields.Char(string='الوظيفة')
    arabic_birthdate = fields.Date(string='تاريخ الميلاد')
    def _check_ccp_length(self, vals):
        ccp = vals.get('ccp')
        if ccp and len(ccp) != 21:
            raise UserError("Veuillez vérifier le numéro CCP.")