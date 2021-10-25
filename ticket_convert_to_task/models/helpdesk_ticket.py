# Copyright 2019 Xavier Jimenez <xavier.jimenez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HelpDeskTicket(models.Model):
    
    _inherit = "helpdesk.ticket"
    
    task_id = fields.Many2one('project.task')
    