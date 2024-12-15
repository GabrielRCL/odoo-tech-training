from odoo import http

class Academy(http.Controller):

    @http.route('/hello_world/', auth='public', website=True, sitemap=True)
    def hello_world(self, **kw):
        return 'HelloWorld!'

    @http.route('/compare', auth='public', website=True, sitemap=True)
    def motorcycle_compare(self, **kw):
        motorcycles = http.request.env['product.template'].search([('detailed_type', '=', 'motorcycle')])
        values = {
            'products': motorcycles.with_context(display_default_code=False)
        }
        return http.request.render('motorcycle_website.motorcycle_compare', values)