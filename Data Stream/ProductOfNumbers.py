'''
Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

Implement the ProductOfNumbers class:

ProductOfNumbers() Initializes the object with an empty stream.
void add(int num) Appends the integer num to the stream.
int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.
The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

Example:
Input
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

Output
[null,null,null,null,null,null,20,40,0,null,32]
'''


class ProductOfNumbers:
  def __init__(self):
      self.prefix_product = [1]
  
  def add(self, num):
      if num == 0:
          self.prefix_product = [1]
      else:
          self.prefix_product.append(self.prefix_product[-1] * num)
  
  def getProduct(self, k):
      if len(self.prefix_product) <= k:
          return 0
      else:
          return self.prefix_product[-1] // self.prefix_product[-k-1]






# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
