from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    make = fields.Char()
    model = fields.Char()    
    year = fields.Integer()
    curb_weight = fields.Float()
    launch_date = fields.Date()

    horsepower = fields.Float()
    top_speed = fields.Float()
    torque = fields.Float()

    
    battery_capacity = fields.Selection(
        selection = [
            ('xs','Small'),
            ('0m','Medium'),
            ('0l','Large'),
            ('xl','Extra Large')
        ]
    )
    charge_time = fields.Float()
    range = fields.Float()

    #product_type
    detailed_type = fields.Selection(
        selection_add=[('motorcycle', 'Motorcycle')], 
        ondelete={'motorcycle': 'set service'}
    )

    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['motorcycle'] = 'service'
        return type_mapping
        