from odoo import api, fields, models, _


class SubscriptionContracts(models.Model):
    _inherit = 'subscription.contracts'


    def action_download_arabic_contract_pdf(self):

        return {
            'type': 'ir.actions.act_url',
            'url': 'https://imtech-product.s3.eu-west-2.amazonaws.com/contract_dari.pdf',
            'target': 'new',
        }


    def action_download_prelevement1_pdf(self):

        return {
            'type': 'ir.actions.act_url',
            'url': 'https://imtech-product.s3.eu-west-2.amazonaws.com/dari_prelevement1.pdf',
            'target': 'new',
        }


    def action_download_prelevement2_pdf(self):

        return {
            'type': 'ir.actions.act_url',
            'url': 'https://imtech-product.s3.eu-west-2.amazonaws.com/dari_prelevement2.pdf',
            'target': 'new',
        }





