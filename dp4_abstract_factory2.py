class Dog:
	"""One of the objects to be returned"""

	def speak(self):
		return "Woof!"

	def __str__(self):
		return "Dog"

class Cat:
	"""One of the objects to be returned"""

	def speak(self):
		return "Meow!"

	def __str__(self):
		return "Cat"
		
class DogFactory:
	"""Concrete Factory"""

	def get_pet(self):
		"""Returns a Dog object"""
		return Dog()

	def get_food(self):
		"""Returns a Dog Food object"""
		return "Dog Food!"

class CatFactory:
	"""Concrete Factory"""

	def get_pet(self):
		"""Returns a Cat object"""
		return Cat()

	def get_food(self):
		"""Returns a Cat  Food object"""
		return "Cat Food!"

class PetStore:
	""" PetStore houses our Abstract Factory """

	def __init__(self, pet_factory=None):
		""" pet_factory is our Abstract Factory """

		self._pet_factory = pet_factory


	def show_pet(self):
		""" Utility method to display the details of the objects retured by the DogFactory """

		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("Our pet is '{}'!".format(pet))
		print("Our pet says hello by '{}'".format(pet.speak()))
		print("Its food is '{}'!".format(pet_food))


#Create a Concrete Factory
dogfactory = DogFactory()
catfactory = CatFactory()

#Create a pet store housing our Abstract Factory
shop = PetStore(dogfactory)
shop2 = PetStore(catfactory)

#Invoke the utility method to show the details of our pet
shop.show_pet()
shop2.show_pet()

# Output
# (base) D:\>python dp4_abstract_factory2.py
# Our pet is 'Dog'!
# Our pet says hello by 'Woof!'
# Its food is 'Dog Food!'!
# Our pet is 'Cat'!
# Our pet says hello by 'Meow!'
# Its food is 'Cat Food!'!