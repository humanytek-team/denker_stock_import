# -*- coding: utf-8 -*-
{
    'name' : 'Campos de importacion en Productos a recibir',
    'version' : '1',
    'author': 'Humanytek',
    'description': """
        Agrega campos de importacion en compras->productos a recibir
    """,
    'category' : 'Stock',
    'depends' : ['purchase','stock'],
    'data': [
        'stock_view.xml',
        #'security/groups.xml',
        #'security/ir.model.access.csv',
        
    ],
    'demo': [

    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
