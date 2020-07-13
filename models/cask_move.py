from odoo import api, fields, models

'''
cask statuses
empty = clean and ready for filling
full = filled with beer - ready for resale
dirty = Empty - requires cleaning before refilling
waste = full or part full of spoiled product. Product must be disposed before cask can be reused.
damaged = cask is damaged and cannot be reused. 
missing = location (and state) of cask is unknown.
'''

class cask_move(models.Model):
    _name = 'cask.move'
    _description = 'Cask Movement'

    name = fields.Text('Description', index=True, required=True)
    cask_id = fields.Many2one('cask.cask','Cask')
    state = fields.Selection([
        ('empty','Empty'),('full','Full')
        ,('out','on loan')
        ,('dirty','Dirty'),('waste','Spoiled Product')
        ,('damaged','Damaged'),('missing','Missing')],
        string='Status')
    product_id = fields.Many2one('product.template','Contents',domain="[('type', '!=', 'service'))")
    customer_id = fields.Many2one('res.partner','Customer')
    next_create_date = fields.Date('Next State Date',compute='_compute_next_create_date',readonly=True)

    @api.depends('name')
    def _compute_next_create_date(self):
        self.flush()
        for cm in self:
            nextcm = self.env['cask.move'].search([('id','>',cm.id),
                ('cask_id','=',cm.cask_id.id)],limit=1,order='id')
            cm.next_create_date = nextcm.create_date
            
