# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    """Inherits 'res.partner' and adds fields"""
    _inherit = 'res.partner'

    black_list = fields.Boolean(string='Client black listé',default=False)
    created_in = fields.Many2one("res.company", string='Client créer sur',required=True,default=lambda self: self.env.company)
    ccp = fields.Char(string="CCP", required=True, copy=False)
    key_ccp = fields.Char(string="Clé", required=True, copy=False)
    start_date = fields.Selection([
        ('1', 'Le 1er du mois'),
        ('13', 'Le 13 du mois'),
        ('17', 'Le 17 du mois'),
    ], string="Date de début de prélèvement")
    surname = fields.Char('Prénom')
    num_card = fields.Char(string="Numéro de carte nationale/Numéro de permis")
    date_card = fields.Date(string="Date de carte nationale/Numéro de permis")

    _sql_constraints = [
        ('ccp_unique', 'unique(ccp)', 'Numéro de CCP doit être unique.')
    ]
    arabic_name = fields.Char(string='الاسم')
    arabic_job = fields.Char(string='المهنة')
    arabic_birthdate = fields.Date(string='تاريخ الميلاد')
    street_arabic = fields.Char(string="العنوان")
    wilaya_arabic = fields.Char(string="الولاية")
    commune_arabic = fields.Char(string="البلدية")

    @api.constrains('ccp','key')
    def _check_ccp_length(self):
        if self.ccp and (len(self.ccp) != 8 or not self.ccp.isdigit()):
            raise UserError("Le numéro de CCP doit comporter exactement 8 chiffres.")
        if self.key_ccp and (len(self.key_ccp) != 2 or not self.key_ccp.isdigit()):
            raise UserError("La clé de CCP doit comporter exactement 2 chiffres.")

    @api.constrains('num_card')
    def _check_num_card(self):
        if self.num_card and  not self.num_card.isdigit():
            raise UserError("Le numéro de carte nationale/Numéro de permis doit être des chiffres.")
     