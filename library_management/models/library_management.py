from odoo import models , fields
from odoo.exceptions import UserError,ValidationError
from dateutil.relativedelta import relativedelta


class LibraryManagement(models.Model) :
    _name = "library.books"
    _description = "Library data"

    name = fields.Char(required=True)
    description = fields.Text()
    image = fields.Image()
    category_id = fields.Many2one('books.category')
    isbn = fields.Integer()
    publisher = fields.Char()
    Copyright = fields.Char()
    edition = fields.Char()
    title = fields.Char()
    author = fields.Char()
    price = fields.Float(default=10)
    pages = fields.Integer()

    status = fields.Selection([
        ('available' , 'Available'),
        ('notavailable' , 'Not Available')], default = 'available')

    state = fields.Selection([
        ('issue' , 'Issue'),
        ('cancle' , 'Cancle')])


    def action_issue(self) :
        for record in self :
            record.state = 'issue'



class BookCategory(models.Model) :
    _name = "books.category"
    _description = "Book Category"

    name = fields.Char()


class BookRequest(models.Model) :
    _name = "book.request"
    _description = "Book Request"

    name = fields.Char()
    image = fields.Image()
    author = fields.Char()
    edition = fields.Char()
    publisher = fields.Char()
    request_by = fields.Many2one('res.users')
    request_date = fields.Date(default = lambda self: fields.Datetime.now(),copy=False)