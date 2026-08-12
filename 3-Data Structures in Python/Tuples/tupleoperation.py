# You create tuples of different data types, 
# add an item using the + operator since tuples 
# cannot be changed directly, count how many times 
# a value appears, and slice out ranges of items.
tuplex=(9,6.7,"nine",True)
print(tuplex)
tuplex1_0=(1,2,3,4,5,6,7)
tuplex1_0=tuplex1_0 +(8,9,10)
print(tuplex1_0)
tuplex2_0=(50,51,50,52,50,53)
a=tuplex2_0.count(50)
print(a)
print(tuplex2_0[:3], "   ,", tuplex2_0[-2])



