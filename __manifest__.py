
{
    'name': 'Market Segmnet',
    'category': 'Crm',
    'summary': 'Categories of segment market',
    'version': '13.0.1.0',
    'description': """Agregar mantenimiento a segmentos de mercado.
""",
    'depends': ['crm'],
    'data': [
        'views/crm_lead.xml',
        'views/res_market_segment.xml',
    ],
    'installable': True,
    'auto_install': False,
}
