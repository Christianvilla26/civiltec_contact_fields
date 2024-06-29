from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'

    nacionalidad = fields.Selection([
    ('argentina', 'Argentino/a'),
    ('australia', 'Australiano/a'),
    ('alemania', 'Alemán/ana'),
    ('brasil', 'Brasileño/a'),
    ('canada', 'Canadiense'),
    ('chile', 'Chileno/a'),
    ('colombia', 'Colombiano/a'),
    ('dominicana', 'Dominicano/a'),
    ('china', 'Chino/a'),
    ('corea_del_sur', 'Surcoreano/a'),
    ('espana', 'Español/a'),
    ('estados_unidos', 'Estadounidense'),
    ('francia', 'Francés/esa'),
    ('italia', 'Italiano/a'),
    ('japon', 'Japonés/esa'),
    ('mexico', 'Mexicano/a'),
    ('reino_unido', 'Británico/a'),
    ('rusia', 'Ruso/a'),
    ('venezuela', 'Venezolano/a'),
    ('portugal', 'Portugués/esa'),
    ('india', 'Indio/a'),
    ('sudafrica', 'Sudafricano/a'),
    ('nigeria', 'Nigeriano/a'),
    ('egipto', 'Egipcio/a'),
    ('turquia', 'Turco/a'),
    ('grecia', 'Griego/a'),
    ('noruega', 'Noruego/a'),
    ('suecia', 'Sueco/a'),
    ('finlandia', 'Finlandés/esa'),
    ('polonia', 'Polaco/a'),
    ('austria', 'Austriaco/a'),
    ('suiza', 'Suizo/a')
], string="Nacionalidad")

    bank_account_number = fields.Char(string='Cuenta Bancaria')
    bank_name = fields.Char(string='Entidad Bancaria')
    account_type = fields.Selection([
        ('savings', 'Ahorros'),
        ('checking', 'Corriente'),
        ('salary', 'Salario')
    ], string='Tipo de Cuenta')
    currency = fields.Char(string='Moneda')
    civil_status = fields.Selection([
        ('single', 'Soltero/a'),
        ('married', 'Casado/a'),
        ('divorced', 'Divorciado/a'),
        ('widowed', 'Viudo/a')
    ], string='Estado Civil')
    passport_number = fields.Char(string='Pasaporte')
