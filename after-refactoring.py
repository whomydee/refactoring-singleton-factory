"""
Problem 1:
----------
Everytime a new type of Trash is added, this client code needs to be changed
to append into the respective bin_storage. Factory design pattern comes into play.

---------------------------------

Problem 2:
----------
This client code is initializing the local_bin for Aluminum, Glass and Paper type trash.
This should be automatically handled at runtime. So, another Factory Design Patter comes into play
for dynamically returning the type of Trash Bin that a specific type of Trash will be put inside.

Now, unfortunately, factory creates an object and returns that newly created object everytime it is called,
but we want to initialize the three types local_bin once and use those. In technical terms, we want to initialize
the local_bin only once and use that initialized instance (i.e. object) everytime we need to put something in it.

So, we might initialize the AluminumBin, GlassBin and PaperBin object using a Singleton Design pattern, and
then use the factory to return the initialized objects from the Singleton.

---------------------------------

Problem 3:
----------
After resolving up to problem 2, one problem with calculating the sum of the weight of the trash
items inside a bin_storage is that it's getting a long chain of calls to access the list of the items inside of
a bin_storage. We might resolve this problem to a degree by putting the operations of Singleton class inside the
BinSingletonFactory class. Let's try it out.
"""

import abc
import random


class Trash(abc.ABC):
    def __init__(self, weight):
        self.weight = weight

    @abc.abstractmethod
    def get_value(self) -> float:
        pass

    def get_weight(self) -> float:
        return self.weight

    @staticmethod
    def sum_value(this_bin) -> None:
        value = 0.0

        for trash_item in this_bin:
            value += trash_item.get_weight() * trash_item.get_value()
            print("weight of " + type(trash_item).__name__ + " = " + str(trash_item.get_weight()))

        print("Total value = " + str(value))


class Aluminum(Trash):
    value = 1.67

    def __init__(self, weight: float):
        Trash.__init__(self, weight)

    def get_value(self) -> float:
        return self.value

    def set_value(self, new_value: float) -> None:
        self.value = new_value


class Paper(Trash):
    value = 0.10

    def __init__(self, weight: float):
        Trash.__init__(self, weight)

    def get_value(self) -> float:
        return self.value

    def set_value(self, new_value: float) -> None:
        self.value = new_value


class Glass(Trash):
    value = 0.23

    def __init__(self, weight: float):
        Trash.__init__(self, weight)

    def get_value(self) -> float:
        return self.value

    def set_value(self, new_value: float) -> None:
        self.value = new_value


class TrashFactory:
    def __init__(self, trash_type):
        self.trash_type = trash_type

    def get_trash_type(self) -> type(Trash):
        if isinstance(self.trash_type, Aluminum):
            return Aluminum
        elif isinstance(self.trash_type, Paper):
            return Paper
        elif isinstance(self.trash_type, Glass):
            return Glass


class Bin(abc.ABC):
    @abc.abstractmethod
    def add_trash(self, trash_item) -> None:
        pass


class AluminumBin(Bin):

    def __init__(self):
        self.bin_storage = []

    def add_trash(self, trash_item: Trash) -> None:
        self.bin_storage.append(trash_item)


class PaperBin(Bin):

    def __init__(self):
        self.bin_storage = []

    def add_trash(self, trash_item: Trash) -> None:
        self.bin_storage.append(trash_item)


class GlassBin(Bin):

    def __init__(self):
        self.bin_storage = []

    def add_trash(self, trash_item: Trash) -> None:
        self.bin_storage.append(trash_item)


class BinSingletonFactory:

    def __init__(self):
        self.aluminum_bin = AluminumBin()
        self.glass_bin = GlassBin()
        self.paper_bin = PaperBin()

    def get_trash_bin(self, trash_type: type(Trash)) -> Bin:
        trash_type = trash_type(random.random() * 100)

        if isinstance(trash_type, Aluminum):
            return self.aluminum_bin
        if isinstance(trash_type, Glass):
            return self.glass_bin
        if isinstance(trash_type, Paper):
            return self.paper_bin


class Recycle:

    def __init__(self):
        self.local_bin = []
        self.bin_factory = BinSingletonFactory()
        self.__populate_bin()

    def __populate_bin(self) -> None:
        for i in range(30):
            random_val = (int(random.random()) * 3)
            if random_val == 0:
                self.local_bin.append(Aluminum(random.random() * 100))
            elif random_val == 1:
                self.local_bin.append(Paper(random.random() * 100))
            elif random_val == 2:
                self.local_bin.append(Glass(random.random() * 100))

    def test(self) -> None:
        # Sort the bin_storage
        for trash_item in self.local_bin:
            trash_item_type = TrashFactory(trash_item).get_trash_type()
            trash_bin = self.bin_factory.get_trash_bin(trash_item_type)
            trash_bin.add_trash(trash_item)

        Trash.sum_value(self.bin_factory.aluminum_bin.bin_storage)
        Trash.sum_value(self.bin_factory.glass_bin.bin_storage)
        Trash.sum_value(self.bin_factory.paper_bin.bin_storage)
        Trash.sum_value(self.local_bin)


Recycle().test()

