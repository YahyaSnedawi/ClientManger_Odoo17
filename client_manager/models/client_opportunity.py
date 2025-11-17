from odoo import models, fields

class Opportunity(models.Model):
    _name = 'client.opportunity'
    _description = 'Sales Opportunity'

    client_id = fields.Many2one('client.client', string="Client", required=True)
    opportunity_name = fields.Char(string="Opportunity Name", required=True)
    expected_value = fields.Float(string="Expected Value")
    stage = fields.Selection([
        ('new', 'New'),
        ('negotiation', 'Negotiation'),
        ('closed_won', 'Closed - Won'),
        ('closed_lost', 'Closed - Lost')
    ], string="Stage", default='new')
    follow_up_date = fields.Date(string="Follow-Up Date")
    notes = fields.Text(string="Notes")
