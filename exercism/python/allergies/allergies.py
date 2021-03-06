class Allergies(object):

    def __init__(self, score):
        self.score = score

        self.allergens = {
            'eggs': 1,
            'peanuts': 2,
            'shellfish': 4,
            'strawberries': 8,
            'tomatoes': 16,
            'chocolate': 32,
            'pollen': 64,
            'cats': 128
        }
    def is_allergic_to(self, item):
        return bool(self.score & self.allergens[item])

    @property
    def lst(self):
       return [allergen for allergen in self.allergens if self.is_allergic_to(allergen)]

