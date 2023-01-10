# -*- coding: utf-8 -*-
{
    'name': "Calculations",

    'summary': """
        Update of payroll calculations and functionality
       """,

    'description': """
       This template seeks to easily rectify some errors in the
       payroll module associated with calculations by importing
       csv files on the time of installation.
    """,

    'author': "Rashid Designs",
    'website': "assanisaidi73@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_payroll'],

    # always loaded
    'data': [
        'data/hr.salary.rule.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
