'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
 

Example 1:

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]
'''

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.dq = deque()
        self.curr = 0

    def next(self, val: int) -> float:
        self.dq.append(val)
        self.curr += val
        if len(self.dq) > self.size:
            self.curr -= self.dq.popleft()
        
    	return self.curr / len(self.dq)