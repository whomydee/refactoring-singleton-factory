import abc
import random


class Trash(abc.ABC):
    def __init__(self, wt):
        self.weight = wt

    @abc.abstractmethod
    def getValue(self):
        pass

    def getWeight(self):
        return self.weight
    # Sums the value of Trash in a bin_storage:

    def sumValue(it):
        val = 0.0
        while True:
            try:
                t = next(it)
                val += t.getWeight() * t.getValue()
                print (
                  "weight of " +
                  type(t).__name__ +
                  " = " + str(t.getWeight()))
            except StopIteration:
                break
        print("Total value = " + str(val))


class Aluminum(Trash):
    val  = 1.67

    def __init__(self, wt):
        Trash.__init__(self, wt)

    def getValue(self):
        return self.val

    def setValue(newval):
        val = newval


class Paper(Trash):
    val = 0.10

    def __init__(self, wt):
        Trash.__init__(self, wt)

    def getValue(self):
        return self.val

    def setValue(self, newval):
        val = newval


class Glass(Trash):
    val = 0.23

    def __init__(self, wt):
        Trash.__init__(self, wt)

    def getValue(self):
        return self.val

    def setValue(self, newval):
        val = newval


class RecycleA:

    def __init__(self):

        # Fill up the Trash bin_storage:
        self.bins = []
        self.glassBin = []
        self.paperBin = []
        self.alBin = []

        self.load_bins()

    def load_bins(self):
        for i in range(30):
            random_val = ((int)(random.random() * 3))
            if random_val == 0:
                self.bins.append(Aluminum(random.random() * 100))
            elif random_val == 1:
                self.bins.append(Paper(random.random() * 100))
            elif random_val == 2:
                self.bins.append(Glass(random.random() * 100))

    def test(self):
        sorter = iter(self.bins)
        # Sort the Trash:
        while True:

            try:
                # get the next item
                t = next(sorter)
                if isinstance(t, Aluminum):
                    self.alBin.append(t)
                if isinstance(t, Paper):
                    self.paperBin.append(t)
                if isinstance(t, Glass):
                    self.glassBin.append(t)
            except StopIteration:
                break

        Trash.sumValue(iter(self.alBin))
        Trash.sumValue(iter(self.paperBin))
        Trash.sumValue(iter(self.glassBin))
        Trash.sumValue(iter(self.bins))


RecycleA().test()
