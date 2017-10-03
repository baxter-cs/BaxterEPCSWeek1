import random
ingredients = [


]

class Sandwich():
  def __init__(self, crust="bread"):
    self.crust = crust
    self.ingredients = []

  def printInstructions(self):
    print ("add " + self.crust)
    self.printIngredients()
    print ("add " + self.crust)


  def addIngredient(self, ingredient):
    self.ingredients.append(ingredient)
  def printIngredients(self):
    for ingredient in ingredients:
      print(ingredient)

wiches = []
halsWich = Sandwich("sourdough")
halsWich
wiches.append(sourdough)

for sammie in wiches:
  sammie.printInstructions()
