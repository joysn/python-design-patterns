""" Builder Design Pattern

       |-----------|
       |  Product  |
       |-----------|
  
  |------------------|        |--------------------|
  |    Intreface     |        |      Concrete      |
  |  Product Builder |<-------|  Product Builder   |
  |------------------|        | Returns "products" |
                              |--------------------|

  |-----------------|
  |     Director    |
  | Build each part |
  | of the specific |
  |    product      |
  |-----------------|

"""

from abc import ABCMeta, abstractstaticmethod

class House():
    """The Product with default values"""

    def __init__(self, building_type="Apartment", doors=1, windows=2, wall_material="Brick"):
        #brick, wood, ice, mud
        self.wall_material = wall_material
        # Apartment, Bungalow, Caravan, Hut, Castle, Duplex, HouseBoat, Igloo
        self.building_type = building_type
        self.doors = doors
        self.windows = windows

    def __str__(self):
        return "This is a {0} {1} with {2} door(s) and {3} window(s).".format(
            self.wall_material, self.building_type, self.doors, self.windows
        )

class InterfaceHouseBuilder(metaclass=ABCMeta):
	""" The builder interface """
	
	@abstractstaticmethod
	def set_wall_material(self,value):
		""" set wall material """
		
	@abstractstaticmethod
	def set_building_type(self,value):
		""" set building type """
		
	@abstractstaticmethod
	def set_number_windows(self,value):
		""" set number of windows """
		
	@abstractstaticmethod
	def set_number_doors(self,value):
		""" set number of doors """
		
	@abstractstaticmethod
	def get_house(self):
		""" return house """
		
		
class HouseBuilder(InterfaceHouseBuilder):
	"""The Concrete Builder."""
	
	def __init__(self):
		self.house = House()
		
	def set_wall_material(self,value):
		self.house.wall_material = value
		return self
		
	def set_building_type(self,value):
		self.house.building_type = value
		return self
		
	def set_number_windows(self,value):
		self.house.windows = value
		return self
		
	def set_number_doors(self,value):
		self.house.doors = value
		return self
		
	def get_house(self):
		return self.house
		
	
class IglooDirector:
    """The Director, building a different representation."""
    @staticmethod
    def construct():
        return HouseBuilder()\
            .set_building_type("Igloo")\
            .set_wall_material("Ice")\
            .set_number_doors(1)\
            .set_number_windows(0)\
            .get_house()
	
if __name__ == "__main__":
			
    IGLOO = IglooDirector.construct()

    HUT = HouseBuilder()\
        .set_building_type("Hut")\
        .set_wall_material("Mud")\
        .set_number_doors(1)\
        .set_number_windows(1)\
        .get_house()
			
    HOUSEBOAT = HouseBuilder()\
        .set_building_type("Houseboat")\
        .set_wall_material("Wood")\
        .set_number_doors(1)\
        .set_number_windows(3)\
        .get_house()
		
		
    print(IGLOO)
    print(HUT)
    print(HOUSEBOAT)

	
# (base) D:\>python dp5_builder2.py
# This is a Ice Igloo with 1 door(s) and 0 window(s).
# This is a Mud Hut with 1 door(s) and 1 window(s).
# This is a Wood Houseboat with 1 door(s) and 3 window(s).
