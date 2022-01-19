# -*- coding: utf-8 -*-
{
	'name': 'Automated Sale Order Processing',
	'version': '15.0.0.0',
	'summary': 'Auto sale to Invoice auto sale order processing automatic sales order process auto sales process Automatic sales Invoice confirmation processing automatic workflow for sales order auto process sale order auto workflow sale auto workflow sales single click',
	'description': '''
	odoo Automatic sale order Invoice and Delivery confirmation and processing auto sales odoo
	odoo Automatic sales Invoice Delivery confirmation processing auto
	odoo Automated Sales Order Processing Automated Sale Order Processing odoo
	odoo Automated Sales confirm Automated Sale confirm odoo
	odoo sale order auto confirm odoo automated sales order auto workflow odoo
	odoo automatic print for sales order auto sales order process sale order auto process odoo
	odoo sale auto print sale auto process sale automatic process odoo
	odoo sales auto print sales auto process sales automatic process odoo
	odoo sales order auto print sales order auto process sales order automatic process odoo
	odoo sale order auto print sale order auto process sale order automatic process odoo
	odoo auto sale order print automatic Sales Order confirm automatic Sale Order confirm
	odoo automatic Sales print automatic Sale confirm auto workflow for sales order
	odoo reduce sales order print reduce sale confirm reduce sale order process
	odoo automatic workflow for sales order automatic workflow for sale order
	 ''',
	"price": 20,
    "currency": "EUR",
	'author': 'medconsultantweb@gmail.com',
	'website': 'https://www.weblemon.org',
	'category': 'Sales',
	'depends': ['base','sale_management','stock', 'account'],
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
