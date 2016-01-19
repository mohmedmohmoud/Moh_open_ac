from openerp import fields,models
class partner(models.Model):
	_inherit = 'res.partner'

	instrector = fields.Boolean("instrector",default = False)
	session_ids = fields.Many2many("openacadamy.session", string="Attends session", readonly = True)
