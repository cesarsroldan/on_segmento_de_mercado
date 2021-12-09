from odoo import models, fields, api

class CrmLeads(models.Model):
    _inherit = 'crm.lead'

    market_segment_ids = fields.Many2one('res.market.segment', string="Segmento de mercando",ondelete='cascade')

