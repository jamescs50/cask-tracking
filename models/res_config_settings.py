# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    cask_trackon_salseship=fields.Selection([
        ('off', 'Not Enabled'),
        ('optional','Optional'),
        ('on','Required')],
        string='Track Casks on Sales Shipments',
        help='Log cask numbers when dispatching from warehouse')