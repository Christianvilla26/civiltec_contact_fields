{
    'name': 'Partner Extensions',
    'version': '1.0',
    'summary': 'Adds nationality field to partners',
    'sequence': -100,
    'description': """Adds a new field to store the nationality of partners.""",
    'category': 'Customization',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['base'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
