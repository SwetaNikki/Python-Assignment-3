"""
Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists


['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

"""

#1
res = [ x*i for x in ['x','y','z'] for i in range(1,5)  ]
print("['x','y','z'] ....=>  " +   str(res)) 
print()

#2
res = [ x*i for i in range(1,5) for x in ['x','y','z']  ]
print("['x','y','z'] ....=>  " +   str(res)) 
print()

#3
res = [ [x+i] for x in [2,3,4] for i in range(0,3)]
print("[2,3,4]       ....=>  " +   str(res))
print()

#4
res = [ [x+i for i in range(0,4)] for x in [2,3,4,5]]
print("[2,3,4,5]     ....=>  " +   str(res)) 
print()

#5
res = [(y, x) for x in [1,2,3] for y in [1,2,3] ]
print("[1,2,3]       ....=>  " +   str(res) )
print()

