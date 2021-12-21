# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosConfig(models.Model):
    _inherit = 'pos.config'


    pos_custom_receipt= fields.Boolean('Custom Receipt', default=True)
    show_company_contact_address = fields.Boolean(string='show_company_contact_address', help="Enables show_company_contact_address.")
    show_company_phone = fields.Boolean(string='show_company_phone', help="Enables show_company_phone.")
    show_company_email = fields.Boolean(string='show_company_email', help="Enables show_company_email.")
    show_company_website = fields.Boolean(string='show_company_website', help="Enables show_company_website.")
    show_qr_code = fields.Boolean(string="Show QR Code in Receipt", default=True)

class POSOrder(models.Model):
    _inherit = 'pos.order'

    order_refunded = fields.Char(string="Order Refunded", required=False, )

    @api.model
    def create(self, values):
        res = super(POSOrder, self).create(values)
        print(values)
        if len(res.refunded_order_ids) != 0:
            res.order_refunded = ','.join(res.refunded_order_ids.mapped('pos_reference'))
        print(res.order_refunded)
        return res