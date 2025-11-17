from odoo import models, fields

class ClientService(models.Model):
    _name = 'client.service'
    _description = 'Client Service'

    name = fields.Char(string="Service Name", required=True)
    description = fields.Text(string="Description")
    price = fields.Float(string="Price")
    active = fields.Boolean(string="Active", default=True)

    client_ids = fields.Many2many('client.client', string="Clients")
