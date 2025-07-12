{
    'name': 'Custom Odoo Addon',
    'version': '15.0.1.0.0',
    'author': 'Kavin Chandrasekar',
    'website': 'https://github.com/KavinChandrasekar/odoo-custom-addon',
    'category': 'Sales/CRM',
    'depends': ['base', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'data/followup_cron.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
