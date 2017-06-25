from mmgmt_server.interactors import Interactor
from mmgmt_server.models import Ingredient


class IngredientInteractor(Interactor):
    def write_from_json(self, ingredients_dic, db):
        added_ingredients = []
        for ingredient in ingredients_dic:
            added_ingredients.append(Ingredient(name=ingredient["name"],
                                                kcal_100=ingredient["kcal_100"],
                                                kj_100=ingredient["kj_100"],
                                                protein_100=ingredient["protein_100"],
                                                fat_100=ingredient["fat_100"],
                                                fat_saturated_100=ingredient["fat_saturated_100"],
                                                carbs_100=ingredient["carbs_100"],
                                                carbs_sugar_100=ingredient["carbs_sugar_100"],
                                                salt_100=ingredient["salt_100"],
                                                fibers_100=ingredient["fibers_100"]))
            db.session.add(added_ingredients[len(added_ingredients) - 1])
        db.session.commit()
        self.logger.info('Ingredients written to DB - {}'.format(ingredients_dic))
        return added_ingredients
