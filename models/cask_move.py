from odoo import api, fields, models

'''
cask statuses
empty = clean and ready for filling
full = filled with beer - ready for resale
dirty = Empty - requires cleaning before refilling
waste = full or part full of spoiled product. Product must be disposed before cask can be reused.
damaged = cask is damaged and cannot be reused. 
'''

class cask_move(models.Model):
    _name = 'cask.move'
    _description = 'Cask Movement'

    name = fields.Text('Description', index=True, required=True)
    date = fields.Datetime(
        'Date', default=fields.Datetime.now, index=True, required=True,
        readonly= True,compute='_compute_move',store=True)
    state = fields.Selection([
        ('empty','Empty'),('full','Full')
        ,('out','on loan')
        ,('dirty','Dirty'),('waste','Spoiled Product')
        ,('damaged','Damaged')],
        string='Status',default='dirty')
    product_id = fields.Many2one('product.template','Contents',domain="[('type', '!=', 'service'))")
    customer_id = fields.Many2one('res.partner','Customer')