from odoo import models, fields

class Interaction(models.Model):
    _name = 'client.interaction'
    _description = 'Client Interaction'

    client_id = fields.Many2one('client.client', string="Client", required=True)
    date = fields.Datetime(string="Date", default=fields.Datetime.now)
    interaction_type = fields.Selection([
        ('call', 'Call'),
        ('meeting', 'Meeting'),
        ('email', 'Email'),
        ('note', 'Note')
    ], string="Interaction Type", required=True)
    note = fields.Text(string="Note") 
    responsible_employee = fields.Many2one('hr.employee', string="Responsible Employee")
    user_id = fields.Many2one('res.users', string="Responsible User")  
