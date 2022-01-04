from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import copy


class ICompare:

    @staticmethod
    def compare(x, y, reverse) -> int:

        if reverse:
            x, y = y, x

        if x > y:
            return 1
        elif x < y:
            return -1
        else:
            return 0


class Context():

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self, array, keys, reverse) -> None:
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(array, keys, reverse)
        print(result)


class Strategy(ABC):

    @abstractmethod
    def do_algorithm(self, array: List, keys: List, reverse: bool):
        pass


class InsertionSort(Strategy):
    def do_algorithm(self, array: List, keys: List, reverse: bool) -> List:
        compare = ICompare()
        for i in range(1, len(keys)):
            temp = array[keys[i] - 1][1]
            j = i - 1
            while compare.compare(array[keys[j] - 1][1], temp, reverse) > 0 and j >= 0:
                array[keys[j + 1] - 1][1] = array[keys[j] - 1][1]
                j = j - 1
            array[keys[j + 1] - 1][1] = temp
        return array


class SelfReferencingArray:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:

    def __init__(self, some_array, some_circular_ref):
        self.some_array = some_array
        self.some_circular_ref = some_circular_ref

    def __deepcopy__(self, memo={}):

        some_list_of_objects = copy.deepcopy(self.some_array, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        new = self.__class__(
            some_list_of_objects, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


if __name__ == "__main__":

    parent_array = [[1, "c"], [2, "b"], [3, "e"], [4, "d"], [5, "a"]]
    circular_ref = SelfReferencingArray()
    component_array = SomeComponent(parent_array, circular_ref)
    circular_ref.set_parent(component_array)

    deep_copied_array = copy.deepcopy(component_array)

    context = Context(InsertionSort())
    print("Insertion Sort")
    context.do_some_business_logic(deep_copied_array.some_array, [1, 3, 5], False)
    context.do_some_business_logic(deep_copied_array.some_array, [2, 4], True)
