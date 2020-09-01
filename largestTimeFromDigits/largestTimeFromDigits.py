from typing import List
import itertools

class LargestTimeFromDigits:
    def largest_time(self, A: List[int]) -> str:
        times = list(itertools.permutations(A))
        # lexographically compare tuples
        valid_times = [t for t in times if t < (2,4,0,0) and t[2:] < (6,0)]

        if not valid_times: return ''
        # remove each digit from max value tuple
        a, b, c, d = max(valid_times)
        return f'{a}{b}:{c}{d}'