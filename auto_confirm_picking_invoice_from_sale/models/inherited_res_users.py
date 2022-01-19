# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
class InheritUser(models.Model):
	_inherit = "res.users"

	negative_qty_autorized = fields.Boolean(string="Autoriser stock négative")
