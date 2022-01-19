# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import time

class InheritSale(models.Model):
    _inherit = "sale.order"
    category_compte = fields.Char()


    def action_confirm_bl(self):
        picking_confirm = self.action_confirm()

        for order in self:
            picking_obj = self.env['stock.picking'].search([('origin', '=', order.name)])

            for pick in picking_obj:
                for qty in pick.move_lines:
                    if not self.user_id.negative_qty_autorized and qty.product_id.qty_available <= 0:
                        raise ValidationError('Vous avez pas du stock pour livrée certain pieces')

                for qty in pick.move_lines:
                    qty.write({
                        'quantity_done': qty.product_uom_qty
                    })

                pick.button_validate()
                pick._action_done()

                for line in order.order_line:
                    line.write({
                        'qty_delivered': line.product_uom_qty,
                    })


    def action_confirm_invoice(self):
        picking_confirm = self.action_confirm()

        for order in self:
            picking_obj = self.env['stock.picking'].search([('origin', '=', order.name)])

            for pick in picking_obj:
                for qty in pick.move_lines:
                    if not self.user_id.negative_qty_autorized and qty.product_id.qty_available <= 0:
                        raise ValidationError('Vous avez pas du stock pour livrée certain pieces')

                for qty in pick.move_lines:
                    qty.write({
                        'quantity_done': qty.product_uom_qty
                    })

                pick.button_validate()
                pick._action_done()

                for line in order.order_line:
                    line.write({
                        'qty_delivered': line.product_uom_qty,
                    })


        create_invoice = self._create_invoices()
        invoice_obj = self.env['account.move'].search([('invoice_origin', '=', self.name)])

        validate = invoice_obj.action_post()



    def print_picking(self):
        picking = self.picking_ids.filtered(
                lambda m: m.state not in ["cancel"]
            )
        return self.env.ref('stock.action_report_delivery').report_action(picking)

    def print_invoice(self):
        invoice = self.invoice_ids.filtered(
                lambda m: m.state not in ["done", "cancel"]
            )
        return self.env.ref('account.account_invoices').report_action(invoice)
