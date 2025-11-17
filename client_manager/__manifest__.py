{
    'name': "Client Manager",
    'version': '1.0',
    'depends': ['base', 'hr'],
    'author': "Yahya Snedawi",
    'category': 'Sales',
    'description': """
        Client Manager is a custom Odoo module to manage:
        - Clients
        - Interactions with clients
        - Opportunities and services
    """,
    'data': [
        'security/user_groups.xml',
        'security/client_security.xml',
        'security/ir.model.access.csv',

        'views/client_view.xml',
        'views/interaction_view.xml',
        'views/opportunity_view.xml',
        'views/opportunity_action.xml',
        'views/service_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
