# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Frequently Asked Questions',
    'version': '12.0.1.1',
    'summary': 'Create FAQs',
    'author': 'FOSS INFOTECH PVT LTD',
    'live_test_url': 'https://www.youtube.com/watch?v=mO9EK9eMImg',
    'license': 'AGPL-3',
    'category': 'FAQ',
    'website': 'http://www.fossinfotech.com',
    'description': """
        It enables the feature for FAQ.
        """,
    'depends': [
        'base', 'web', 'mail'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/faq_view.xml',
        'views/category.xml',
        'views/tag.xml',
    ],
    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
        'static/description/index.html',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
