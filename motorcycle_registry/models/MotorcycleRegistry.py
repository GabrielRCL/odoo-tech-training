from odoo import fields,models

class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motorcycle Registry"
    _rec_name = "registry_number"

    certificate_title = fields.Binary(string="Certificate Title")
    current_mileage = fields.Float()
    date_registry = fields.Date(index=True)
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    license_plate = fields.Char(string="license_plate")
    registry_number = fields.Char(string="registry_number", required=True)
    vin = fields.Char(string="VIN")