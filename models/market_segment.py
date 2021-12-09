from odoo import models, fields, api


class MarketSegment(models.Model):
    _name = 'res.market.segment'

    name = fields.Char('Nombre')
    description = fields.Char('Descripcion')
