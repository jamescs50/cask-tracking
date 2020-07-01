# -*- coding: utf-8 -*-

from odoo import fields, models, api

class cask_type(models.Model):
    _name = 'cask.type'
    _description = 'Cask Type'

    name = fields.Text('Description', index=True, required=True)
    capacity = fields.Float('Capacity (Litres)')

class cask_cask(models.Model):
    _name = 'cask.cask'
    _description = 'Cask'

    name = fields.Text('Serial No.', index=True, required=True)
    alt_name = fields.Text('Alternate Serial No.',index=True)
    cask_type = fields.Many2one('cask.type','Type')

