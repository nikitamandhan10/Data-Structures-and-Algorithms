'''
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
'''
class Solution:
  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
      stack = []
      for a in asteroids:
          while stack and a < 0 and stack[-1] > 0:
              diff = stack[-1] + a
              if diff < 0:
                  stack.pop()
              elif diff > 0:
                  a = 0
              else:
                  a = 0
                  stack.pop()
          
          if a:
              stack.append(a)
      return stack

        
