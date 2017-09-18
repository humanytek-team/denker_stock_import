# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
import odoo.addons.decimal_precision as dp


class StockMove(models.Model):
    _inherit = "stock.move"

    in_date = fields.Date('Fecha de arribo')
    import_no = fields.Char('No. de Importacion')
    import_status = fields.Char('Status de Importacion')
    request_no = fields.Char('No. Pedimento')
    #customs = fields.Char('Agencia Aduana')    