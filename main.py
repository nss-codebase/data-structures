from stack import *
from que import *
from recursion import  *

food = Stack()
food.push('Hamburger')
food.push('Fries')
food.push('Cake')

print("1st off the Stack: {0}".format(food.pop()))

people = Que()
people.enqueue('Bob')
people.enqueue('Sara')
people.enqueue('Jill')

print("1st off the Queue: {0}".format(people.dequeue()))
print("2nd off the Queue: {0}".format(people.dequeue()))

print(fact(5))

for x in range(20):
    print('fib({0}) = {1}'.format(x, fib(x)))
