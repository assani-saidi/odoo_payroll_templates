# # -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class Calcs(models.Model):
#     _name = 'calculations.calc'
#     _description = 'This model allows us to rectify some calculations'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
