from openerp import models,fields,api

class course(models.Model):
	_name = "openacadamy.course"

	name = fields.Char(string = "Title",required = True)
	desc = fields.Text(string = "description")
	responsible_id = fields.Many2one('res.users', ondelete='set null' ,string='Resposibilty', index = True)
	session_ids = fields.One2many('openacadamy.session','course_id',string='Session')


class session(models.Model):
	_name = "openacadamy.session"

	name = fields.Char(required = True)
	start_date = fields.Date()
	duration = fields.Float(digits=(6,2),help = "duration in day")
	seats = fields.Integer(string = "Number of seats")

	instructor_id = fields.Many2one('res.partner', string = 'Instructor')
	course_id = fields.Many2one('openacadamy.course' ,string = 'course', ondelete = 'cascade',required = True)
	attandee_ids = fields.Many2many('res.partner',string='Attandee')
