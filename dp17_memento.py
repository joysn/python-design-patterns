import copy

class Memento:

    def __init__(self, data):
        # make a deep copy of every variable in the given class
        for attribute in vars(data):
            setattr(self, attribute, copy.deepcopy(getattr(data, attribute)))


# Originator
class Undoable:

    def __init__(self):
        # each instance keeps the latest saved copy so that there is only one
        # copy of each in memory
        self.__last = None

    def save(self):
        self.__last = Memento(self)

    def undo(self):
        for attribute in vars(self):
            setattr(self, attribute, getattr(self.__last, attribute))


class Data(Undoable):

    def __init__(self):
        super(Data, self).__init__()
        self.numbers = []

		
d = Data()
repeats = 10

for i in range(repeats):
	d.save()
	d.numbers.append(i)
	
d.save()
print(d.numbers)
for i in range(repeats):
	d.undo()
	print(d.numbers)


# Output
# (base) D:\>python dp17_memento.py
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8]
# [0, 1, 2, 3, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 5, 6]
# [0, 1, 2, 3, 4, 5]
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3]
# [0, 1, 2]
# [0, 1]
# [0]
# []
