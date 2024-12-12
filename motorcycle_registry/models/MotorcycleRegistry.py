from odoo import api,fields,models
from odoo.exceptions import ValidationError
import re

class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motorcycle Registry"
    _rec_name = "registry_number"

  
    registry_number = fields.Char(string="Registry Number", 
                                 default="MRN0000", readonly=True, required=True)
    
    date_registry = fields.Date(index=True)
    vin = fields.Char(string="VIN", required=True)    
    vin_make = fields.Char(string="Make", compute="_compute_from_vin")
    vin_model = fields.Char(string="Model", compute="_compute_from_vin")
    vin_year =fields.Char(string="Year", compute="_compute_from_vin")
    current_mileage = fields.Float()    
    license_plate = fields.Char(string="license_plate", required=True)
    
    owner_id = fields.Many2one(comodel_name="res.partner", string="Owner ID", ondelete="restrict")
    owner_email = fields.Char(related="owner_id.email")
    owner_phone = fields.Char(related="owner_id.phone")

    certificate_title = fields.Binary(string="Certificate Title")    
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MRN0000')) == ('MRN0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals_list)

        
    @api.depends("vin")
    def _compute_from_vin(self):
        registries_with_vin = self.filtered(lambda r: r.vin)
        for registry in registries_with_vin:
            registry.vin_make = registry.vin[:2]
            registry.vin_model = registry.vin[2:4]
            registry.vin_year = registry.vin[4:6]
        for registry in (self - registries_with_vin):
            registry.vin_make = False
            registry.vin_model = False
            registry.vin_year = False

    @api.constrains('license_plate','vin')
    def _check_patterns(self):
        patterns = {
            'license_plate': r"^[A-Z]{1,3}\d{1,4}[A-Z]{0,2}$",
            'vin': r"^[A-Z]{4}\d{2}[A-Z0-9]{2}\d{5}$"
        }
        for record in self:
            for field_name, pattern in patterns.items():
                record_field_name = getattr(record, field_name) #return value of record.field_name 
                if not re.match(pattern, record_field_name):
                    raise ValidationError(f"The {field_name.replace('_', ' ').title()} is not following the pattern.")
            