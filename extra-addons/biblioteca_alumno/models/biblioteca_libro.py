from odoo import models, fields

class BibliotecaLibro(models.Model):
    _name = "biblioteca.libro"
    _description = "Libro de la biblioteca (práctica DAM)"

    name = fields.Char("Titulo", required=True)
    autor = fields.Char("Autor")
    fecha_publicacion = fields.Date("Fecha de publicación")
    paginas = fields.Integer("Número de páginas")
    disponible = fields.Boolean("Disponible", default=True)
