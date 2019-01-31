from copy import deepcopy

class Car:
	def __init__(self):
		self.__wheels = list()
		self.__engine = None
		self.__body = None
		
	def setBody(self,body):
		self.__body = body
		
	def attachWheel(self,wheel):
		self.__wheels.append(wheel)
		
	def setEngine(self, engine):
		self.__engine = engine
		
	def speficification(self):
		print("body: %s" % self.__body.shape)
		print("engine horsepower : %d" % self.__engine.horsepower)
		print("tire size : %d \'" % self.__wheels[0].size)
		
	def clone(self):
		return deepcopy(self)
	
class Wheel:
	size = None

class Engine:
	horsepower = None
	
class Body:
	shape = None
	
class Director:
	__builder = None
	
	def setBuilder(self,builder):
		self.__builder = builder
		
	def getCar(self):
		car = Car()
		
		# first get the body
		body = self.__builder.getBody()
		car.setBody(body)
		
		engine = self.__builder.getEngine()
		car.setEngine(engine)
		
		i = 0
		while i < 4:
			wheel = self.__builder.getWheel()
			car.attachWheel(wheel)
			i += 1
			
		return car
		
class BuilderInterface:
	def getWheel(self): pass
	def getBody(self): pass
	def getEngine(self): pass
	

class JeepBuilder(BuilderInterface):
	def getWheel(self):
		wheel = Wheel()
		wheel.size = 22
		return wheel

	def getEngine(self):
		engine = Engine()
		engine.horsepower = 400
		return engine

	def getBody(self):
		body = Body()
		body.shape = "SUV"
		return body


class NissanBuilder(BuilderInterface):
	def getWheel(self):
		wheel = Wheel()
		wheel.size = 16
		return wheel

	def getEngine(self):
		engine = Engine()
		engine.horsepower = 100
		return engine

	def getBody(self):
		body = Body()
		body.shape = "hatchback"
		return body

d = Director()
d.setBuilder(JeepBuilder())
jeep = d.getCar()
jeep.speficification()

jeep2 = jeep.clone()
jeep2.speficification()



from copy import deepcopy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print("({}, {})".format(self.x, self.y))

    def move(self, x, y):
        self.x += x
        self.y += y

    def clone(self, move_x, move_y):
        obj = deepcopy(self)
        obj.move(move_x, move_y)

        return obj

		
p0 = Point(0,0)
p0.__str__()
p1 = p0.clone(1,3)
p1.__str__()

