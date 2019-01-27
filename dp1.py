>>> list = [1,2,3]
>>> for i in list:
...     print(i)
...
1
2
3
>>> iter = list.__iter__()
>>> iter
<list_iterator object at 0x000002197DEA5208>
>>> iter.__next__()
1
>>> iter.__next__()
2
>>> numbers = [1,2,3,4,5]
>>> numbers_again = [n for n in numbers]
>>> print(numbers_again)
[1, 2, 3, 4, 5]
>>> even_numbers = [n for n in numbers if n%2 == 0]
>>> even_numbers
[2, 4]
>>> odd_squares = [n**2 for n in numbers if n%2 != 0]
[1, 9, 25]
>>> matrix = [[1,2,3],[4,5,6],[7,8,9]]
>>> flat = [n for row in matrix for n in row]
>>> flat
[1, 2, 3, 4, 5, 6, 7, 8, 9]