# -*- coding: utf-8 -*-
# Part of Browseinfo. See LICENSE file for full copyright and licensing details.
{
	'name': 'Automated Sale Order Processing',
	'version': '15.0.0.0',
	'summary': 'Auto sale to Invoice auto sale order processing automatic sales order process auto sales process Automatic sales Invoice confirmation processing automatic workflow for sales order auto process sale order auto workflow sale auto workflow sales single click',
	'description': '''
	 Automatic sale order Invoice and Delivery confirmation and processing auto sales odoo
	 ''',
	'author': 'Mohamed Rahmouni',
	'website': 'https://www.cadrinsitu.com',
	'category': 'Sales',
	'depends': ['base','sale_management','stock', 'sale_easy', 'account'],
	'data': [
		'security/ir.model.access.csv',
		'views/inherited_sale_order.xml',
		'views/inherited_res_user.xml',
		],
	'installable': True,
	'application': True,
	'qweb': [
			],
    "images":['static/description/Banner.png'],
}
