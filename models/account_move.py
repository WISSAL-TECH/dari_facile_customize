import math

from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    """Inherits 'account.move' and adds fields"""
    _inherit = 'account.move'

    reglement = fields.Selection([
        ('convention', 'Convention'),
        ('facilite', 'Traite Facilité'),
        ],
        string="Réglement")
    recurring_period = fields.Selection([
        ('12', '12'),
        ('18', '18'),
        ('24', '24'),
    ], string='Période', default='18')

    payment_dates_amount = fields.Float()
    payment_dates_first_date = fields.Date()
    payment_dates = fields.One2many('account.move.payment.date', 'move_id', string='Payment Dates')
    discount_amount = fields.Float(string='Discount Amount', compute='_compute_discount_amount', store=True)

    @api.depends('recurring_period', 'amount_total', 'company_id.marge_12', 'company_id.marge_18',
                 'company_id.marge_24')
    def _compute_discount_amount(self):
        for move in self:
            if move.recurring_period == '12' and move.company_id.marge_12:
                move.discount_amount = move.amount_total * (move.company_id.marge_12 / 100.0)
            elif move.recurring_period == '18' and move.company_id.marge_18:
                move.discount_amount = move.amount_total * (move.company_id.marge_18 / 100.0)
            elif move.recurring_period == '24' and move.company_id.marge_24:
                move.discount_amount = move.amount_total * (move.company_id.marge_24 / 100.0)
            else:
                move.discount_amount = 0.0

    def apply_discount_on_total_amount(self):
        for move in self:
            _logger.warning("applyiing discount")

            if move.recurring_period == '12' and move.company_id.marge_12:
                for line in move.invoice_line_ids:
                    line.price_unit += (line.price_unit * (move.company_id.marge_12 ) / 100)
            elif move.recurring_period == '18' and move.company_id.marge_18:
                for line in move.invoice_line_ids:
                    line.price_unit += (line.price_unit * (move.company_id.marge_18) / 100)

            elif move.recurring_period == '24' and move.company_id.marge_24:
                for line in move.invoice_line_ids:
                    line.price_unit += (line.price_unit * (move.company_id.marge_24) / 100)

    @api.depends('recurring_period', 'amount_total', 'invoice_date_due')
    def compute_payment_dates(self):
        self.apply_discount_on_total_amount()
        for move in self:
            _logger.info("Processing move: %s", move)
            _logger.info("Invoice Date: %s, Amount Total: %s, Recurring Period: %s", move.invoice_date_due,
                         move.amount_total, move.recurring_period)
            # Clear previous payment dates
            move.payment_dates.unlink()
            move.payment_dates_amount = 0
            move.payment_dates_first_date = False

            if not move.recurring_period or not move.invoice_date_due or move.amount_total == 0:
                _logger.warning("Missing data to compute payment dates")
                continue

            period = int(move.recurring_period)
            total_amount = move.amount_total
            payment_dates = []
            current_date = move.invoice_date_due

            # Get start date from the partner
            start_date = int(move.partner_id.start_date)
            _logger.info("Using start date: %s", start_date)

            # Calculate base amount per period
            amount_per_period = total_amount / period

            # Round amount_per_period according to the specified rules
            amount_per_period_rounded = []
            rounded_total = 0

            move.payment_dates_first_date = self.calculate_next_payment_date(current_date, start_date)
            move.payment_dates_amount = self.round_to_nearest_hundred(amount_per_period)
            for i in range(period):
                rounded_amount = self.round_to_nearest_hundred(amount_per_period)
                amount_per_period_rounded.append(rounded_amount)
                rounded_total += rounded_amount

                if i == period - 1:  # Adjust last payment to ensure total amount consistency
                    difference = total_amount - rounded_total
                    amount_per_period_rounded[i] += difference

                # Determine the next payment date based on start_date
                next_payment_date = self.calculate_next_payment_date(current_date, start_date)
                payment_dates.append((0, 0, {
                    'payment_date': next_payment_date,
                    'amount': amount_per_period_rounded[i],
                }))
                current_date = next_payment_date

            move.payment_dates = payment_dates
            
            _logger.info("Computed payment dates: %s", move.payment_dates)

    def round_to_nearest_hundred(self, amount):
        """
        Round the amount according to the specified rules:
        - If the tens digit is less than 4, round down to the nearest hundred.
        - If the tens digit is 4 or more, round up to the nearest hundred.
        """
        tens = int((amount % 100) / 10)
        if tens < 4:
            rounded_amount = math.floor(amount / 100) * 100
        else:
            rounded_amount = math.ceil(amount / 100) * 100
        return rounded_amount

    def calculate_next_payment_date(self, current_date, start_date):
        """
        Calculate the next payment date based on the current date and the specified start date.
        """
        # Determine the day of the current date
        current_day = current_date.day

        if current_day <= 25:
            # Move to the specified day in the next month
            next_payment_date = current_date + relativedelta(months=1)
        else:
            # Move to the specified day in the month after next
            next_payment_date = current_date + relativedelta(months=2)

        # Adjust the day to the start_date provided by the partner
        next_payment_date = next_payment_date.replace(day=start_date)
        return next_payment_date

class AccountMovePaymentDate(models.Model):
    _name = 'account.move.payment.date'
    _description = 'Payment Date for Account Move'

    move_id = fields.Many2one('account.move', string='Account Move', required=True)
    payment_date = fields.Date(string='Date de paiement', required=True)
    amount = fields.Float(string='Montant', required=True)
    statut = fields.Selection([
        ('payed', 'Payé'),
        ('not', 'Non payé'),
        ],
        string="Statut")