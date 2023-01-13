# -*- coding: utf-8 -*-
{
    'name': "template",

    'summary': """
        Contains payroll reports 
        """,

    'description': """
        Consists of ten payroll reports namely; Medical Summary, Pension Report, ZIMDEF Report, Tax Credit Summary, 
        Categorized Period Summary by Department, ITF16 Report, NSSA P4 Form, NSSA Remittance Form, Period Pay Summary (Long Detail)
        and Bank Summary
    """,

    'author': "Lloyd Vheremu",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical',
    'version': '0.6',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_payroll'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
