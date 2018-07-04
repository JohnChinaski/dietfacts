
#Dietfacts aplication
from odoo import models, fields, api

# Extend product.template model with calories

class DietFacts_product_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    calories = fields.Integer('Calories')
    servingsize = fields.Float('Serving Size')
    lastupdated = fields.Date('Last Updated')
    dietitem = fields.Boolean('Diet Item')
    nutrients_id = fields.One2many('product.template.nutrient', 'product_id')
    nutrition_score = fields.Float(string="Nutrition Score", store=True, compute='_calcscore')

    @api.one
    @api.depends('nutrients_id', 'nutrients_id.value')
    def _calcscore(self):
        currentscore = 0
        for nutrient in self.nutrients_id:
            currentscore += nutrient.value
        self.nutrition_score = currentscore


class DietFacts_res_user_meal(models.Model):
    _name = 'res.users.meal'
    name = fields.Char('Meal Name')
    meal_date = fields.Datetime('Menu Date')
    item_ids = fields.One2many('res.user.mealitem', 'meal_id')
    user_id = fields.Many2one('res.users', 'Meal User')
    largemeal = fields.Boolean('Large Meal')
    totalcalories = fields.Integer('Total Meal Calories', storage=True, compute= '_calccalories')
    notes = fields.Text('Meal Notes')

    @api.onchange('totalcalories')
    def check_totalcalories(self):
        if self.totalcalories > 500:
            self.largemeal = True
        else:
            self.largemeal = False

    @api.one
    @api.depends('item_ids', 'item_ids.servings')

    def _calccalories(self):
        currentcalories = 0
        for mealitem in self.item_ids:
            currentcalories += mealitem.item_id.calories
        self.totalcalories = currentcalories


class DietFacts_res_users_mealitem(models.Model):
    _name = 'res.user.mealitem'
    meal_id = fields.Many2one('res.users.meal')
    item_id = fields.Many2one('product.template', 'Menu Item')
    servings = fields.Float('Serving')
    calories = fields.Integer(related= 'item_id.calories', string= 'Calories per serving', store= True, readonly= True)
    notes = fields.Text('Meal item notes')

class DietFacts_product_nutrient(models.Model):
    _name = 'product.nutrient'
    product_id = fields.Many2one('product.template','ID Nutrients')
    name = fields.Char('Nutrient Name')
    description = fields.Text('Description')

class DietFacts_product_nutrient_template(models.Model):
    _name = 'product.template.nutrient'
    nutrient_id = fields.Many2one('product.nutrient', string='Product Nutrient')
    product_id = fields.Many2one('product.template')
    value = fields.Float('Nutrients Value')
    uom_id = fields.Many2one('product.uom', 'Unit of Meassure')
    dailypercent = fields.Float('Daily Recomnended Value')