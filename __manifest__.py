# -*- coding: utf-8 -*-
# Part of TigernixERP. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Parent Inventory test',
    'version' : '1.0',
    'summary': 'Manage Inventory',
    'sequence': 100,
    'description': """
        Manage Inventory.
    """,
    'category': 'Warehouse',
    'website': '',
    'depends' : [],
    'data': [
        'views/product_view.xml',
        'views/product_menu_view.xml'
    ],    
    
    'installable': True,
    'application': True,
    'auto_install': False,
    
} 

# test