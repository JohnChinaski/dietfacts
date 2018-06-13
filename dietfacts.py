
#Dietfacts aplication
from odoo import models, fields

# Extend product.template model with calories

class DietFacts_product_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    calories = fields.Integer('Calories')
    servingsize = fields.Float('Serving Size')
    lastupdated = fields.Date('Last Updated')
    dietitem = fields.Boolean('Diet Item')

class DietFacts_res_user_meal(models.Model):
    _name = 'res.users.meal'
    name = fields.Char('Meal Name')
    meal_date = fields.Datetime('Menu Date')
    item_ids = fields.One2many('res.user.mealitem', 'meal_id')
    user_id = fields.Many2one('res.users', 'Meal User')
    notes = fields.Text('Meal Notes')

class DietFacts_res_users_mealitem(models.Model):
    _name = 'res.user.mealitem'
    meal_id = fields.Many2one('res.users.meal')
    item_id = fields.Many2one('product.template', 'Menu Item')
    servings = fields.Float('Serving')
    calories = fields.Integer(related= 'item_id.calories', string= 'Calories per serving', store= True, readonly= True)
    notes = fields.Text('Meal item notes')
