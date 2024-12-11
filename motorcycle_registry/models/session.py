from odoo import api, fields, models
from odoo.exceptions import ValidationError
import re

class Session(models.Model):
    _name = 'motorcycle.session'
    _description = 'Session Info'    
    _sql_constraints = [('vin_unique', 'UNIQUE(vin)', 'Can not exist two records with the same VIN.')]

    registry_number = fields.Char(string="Registry Number", 
                                 default="MRN0000", copy=False, readonly=True, required=True)
    
    license_plate = fields.Char(string="license_plate")
    vin = fields.Char(string="VIN", default="0")
    vin_make = fields.Char(string="Make", compute="_compute_vin")
    vin_model = fields.Char(string="Model", compute="_compute_vin")
    vin_year =fields.Char(string="Year", compute="_compute_vin")
    
    owner_id = fields.Many2one(comodel_name="res.partner", string="Owner ID", ondelete="restrict")
    owner_email = fields.Char(related="owner_id.email")
    owner_phone = fields.Char(related="owner_id.phone")


    @api.depends("vin")
    def _compute_vin(self):
        for record in self:
            if record.vin:
                record.vin_make = record.vin[:2]
                record.vin_model = record.vin[2:4]
                record.vin_year = record.vin[4:6]
        
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MRN0000')) == ('MRN0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
            return super().create(vals_list)

    
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
        