import random



class Ingredient():
  def __init__(self, name, price=0.75):
    self.name = name
    self.price = price


class Condiment(Ingredient):
  price = 0.0
  def __init__(self, name):
    self.name = name

ingredients = [
  Condiment("ketchup"),
  Condiment("mustard"),
  Ingredient("lettuce", 0.25),
  Ingredient("onion", 0.25),
  Ingredient("extraLettuce", 0.25),
  Ingredient("truffles", 10.25),
  Ingredient("gold leaf", 12),
  Ingredient("foi gras", 30),
  Ingredient("gummy bears", 0.99),
]

def getIngredientByName(name):
  for ingredient in ingredients:
    if ingredient.name == name:
      return ingredient

  newIngredient = Ingredient(name)
  ingredients.append(newIngredient)
  return newIngredient


class Sandwich():
  basePrice = 2.0
  def __init__(self, crust="bread"):
    self.crust = crust
    self.ingredients = []

  def printInstructions(self):
    print ("add " + self.crust)
    self.printIngredients()
    print ("add " + self.crust)

  def getPrice(self):
    price = self.basePrice
    for ingredient in ingredients:
      price = price + ingredient.price
    return price

  def addIngredient(self, ingredient):
    self.ingredients.append(ingredient)

  def addIngredients(self, ingredients):
    self.ingredients.extend(ingredients)

  def printIngredients(self):
    for ingredient in self.ingredients:
      print(ingredient.name)

def getUserBread():
  print("GIVE ME BREDD")
  return input("TYPE BREDD PRESS ENTER:")

def getUserIngredients():
  howMany = int(input("how many ingredients?"))

  outIngredients = []
  for i in range(0, howMany):
    print("GIVE ME STUFF")
    ingredientName = input("TYPE STUFF PRESS ENTER:")
    ingredient = getIngredientByName(ingredientName)
    outIngredients.append(ingredient)
  return outIngredients


wiches = []
bread = getUserBread()
yourWich = Sandwich(bread)
ingredients = getUserIngredients()
yourWich.addIngredients(ingredients)
wiches.append(yourWich)

for sammie in wiches:
  print(sammie.getPrice())
  sammie.printInstructions()
