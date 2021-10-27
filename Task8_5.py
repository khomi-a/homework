from random import shuffle
from typing import List, Optional


class ShuffleIterator:
    def __init__(self, values: List[int], num_shuffles: Optional[int] = None):
        self.values = values
        self.num_shuffles = num_shuffles
        self._current_num_times = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num_shuffles is not None and \
                self._current_num_times >= self.num_shuffles:
            raise StopIteration()

        shuffle(self.values)
        self._current_num_times += 1

        return self.values


for permutation in ShuffleIterator([1, 2, 3], num_shuffles=5):
    print(permutation)
