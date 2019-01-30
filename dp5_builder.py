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
d.getCar().speficification()
d.setBuilder(NissanBuilder())
d.getCar().speficification()


# (base) D:\>python dp5_builder.py
# body: SUV
# engine horsepower : 400
# tire size : 22 '
# body: hatchback
# engine horsepower : 100
# tire size : 16 '
