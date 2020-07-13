{
    'name':'Cask Tracking',
    'description':'Keep track of the state and location of your cask and kegs',
    'author':'James Carr-Saunders',
    'website':'kodoo.co.uk',
    'license':'LGPL-3',
    'category':'Operations',
    'depends':['base','product','stock','mrp'],
    'application':True,
    'installable': True,
    'data': [
        'security/cask_security.xml',
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'views/cask_menu.xml',
        'views/cask_views.xml',
        'views/mrp_views.xml',
    ],
}