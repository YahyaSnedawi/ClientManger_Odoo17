from odoo import models, fields

class Client(models.Model):
    _name = 'client.client'
    _description = 'Client'

    name = fields.Char(string="Full Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    company = fields.Char(string="Company")
    
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], string="Status", default='active')

    client_type = fields.Selection([
        ('current', 'Current'),
        ('potential', 'Potential')
    ], string="Type", default='current')

    notes = fields.Text(string="General Notes")
    create_date = fields.Datetime(string="Date Added", readonly=True)

    interaction_ids = fields.One2many('client.interaction', 'client_id', string="Interactions")
    opportunity_ids = fields.One2many('client.opportunity', 'client_id', string="Opportunities")
    service_ids = fields.Many2many('client.service', string="Interested Services")
    
    user_id = fields.Many2one('res.users', string="Responsible User")




