# -*- coding: utf-8 -*-

from odoo import fields, models, api

class cask_type(models.Model):
    _name = 'cask.type'
    _description = 'Cask Type'

    name = fields.Text('Description', index=True, required=True)
    capacity = fields.Float('Capacity (Litres)')
    cask_ids = fields.One2many('cask.cask','cask_type', string='Casks')


'''
cask statuses
empty = clean and ready for filling
full = filled with beer - ready for resale
dirty = Empty - requires cleaning before refilling
waste = full or part full of spoiled product. Product must be disposed before cask can be reused.
damaged = cask is damaged and cannot be reused. 
missing = location (and state) of cask is unknown.
'''

class cask_cask(models.Model):
    _name = 'cask.cask'
    _description = 'Cask'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Text('Serial No.', index=True, required=True)
    alt_name = fields.Text('Alternate Serial No.',index=True)
    cask_type = fields.Many2one('cask.type','Type')
    move_ids = fields.One2many('cask.move','cask_id',string='Movements')
    state = fields.Selection([
        ('empty','Empty'),('full','Full')
        ,('out','On Loan')
        ,('dirty','Dirty'),('waste','Spoiled Product')
        ,('damaged','Damaged'),('missing','Missing')],
        string='Status')
    mrp_assigned_id = fields.Many2one('mrp.production','Manufacturing Order')
    


    #@api.multi
    def status2empty(self,withvalidation):
        for cask in self:
            if withvalidation:
                '''TODO
                If the cask was full we need to find out where the beer has gone!
                '''
                pass
            move_values = {
                'name':'Cask is ready',
                'cask_id':cask.id,
                'state':'empty',
                'product_id':False,
                'customer_id':False,
            }
            self.env['cask.move'].sudo().create(move_values)

    def status2emptybutton(self):
        self.status2empty(False)

    def status2full(self,product_id,description,withvalidation):
        for cask in self:
            move_values = {
                'name':description,
                'cask_id':cask.id,
                'state':'full',
                'product_id':product_id,
                'customer_id':False,
            }
            self.env['cask.move'].sudo().create(move_values)

