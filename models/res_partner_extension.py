from odoo import models, fields, api
from datetime import date
import logging

_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_custom_code = fields.Char(string='Custom Code', help='Custom CRM code for demo')
    follow_up_date = fields.Date(string='Follow-Up Date')
    follow_up_done = fields.Boolean(string='Follow-Up Done')

    def action_mark_followup_done(self):
        for rec in self:
            rec.follow_up_done = True
            _logger.info(f"Manually marked follow-up done for Contact: {rec.name}")

    @api.model
    def _cron_check_followup_dates(self):
        today = date.today()
        contacts = self.search([
            ('follow_up_date', '=', today),
            ('follow_up_done', '=', False)
        ])
        for contact in contacts:
            contact.follow_up_done = True
            _logger.info(f"✅ Follow-up marked done for: {contact.name}")
