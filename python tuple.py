Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list=[10,20,30,40]
>>> print(list)
[10, 20, 30, 40]
>>> list=[30,'ABC',1.0]
>>> print(list)
[30, 'ABC', 1.0]
>>> list=[3,7,5,2]
>>> print(list[0])
3
>>> list=[3,7,5,2]
>>> print(list[3])
2
>>> Z=[3,7,5,2]
>>> print(Z[-1])
2
>>> Z=[3,7,4,2]
>>> print(Z[0:2])
[3, 7]
>>> Z=[3,7,4,2]
>>> print(Z[ :3])
[3, 7, 4]
>>> Z=[3,7,4,2]
>>> print(Z[0: ])
[3, 7, 4, 2]
>>> Z=[3,7,4,2]
>>> print(Z[1: ])
[7, 4, 2]
>>> a=[1,2,3,4,5]
>>> a.append(6)
>>> print(a)
[1, 2, 3, 4, 5, 6]
>>> a=[1,2,3,4]
>>> a.append(5)
>>> print(a)
[1, 2, 3, 4, 5]
>>> a=[1,2,3,4,5]
>>> a[4]=10
>>> print(a)
[1, 2, 3, 4, 10]
>>> a=[1,2,3,4,5]
>>> del a[4]
>>> print(a)
[1, 2, 3, 4]
>>> a=[1,2,3,4,5]
>>> len(a)
5
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> print(a*2)
[1, 2, 3, 1, 2, 3]
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> print(a+b)
[1, 2, 3, 4, 5, 6]
>>> a=[1,2,3]
>>> max(a)
3
>>> a=[1,2,3]
>>> min(a)
1
>>> x=(1,2,3,4,5,5)
>>> x.count(5)
2
>>> x=(1,2,3,4,5)
>>> len(a)
3
>>> x=(1,2,3)
>>> y=(4,5,6)
>>> print(x+y)
(1, 2, 3, 4, 5, 6)
>>> x=(1,2,3)
>>> y=(4,5,6)
>>> print(a*2)
[1, 2, 3, 1, 2, 3]
>>> x=(1,2,3)
>>> max(x)
3
>>> x=(1,2,3)
>>> min(x)
1
>>> a={"A","B","C"}
>>>  print("A"in a)
 
SyntaxError: unexpected indent
>>> a={"A","B","C"}
>>> print("A" in a)
True
>>> print("D" in a)
False
>>> b={"A","B","C"}
>>> b.add("D")
>>> print(b)
{'D', 'B', 'A', 'C'}
>>> info=("name":"Manali","class":"fycs","roll no.":"48")
SyntaxError: invalid syntax
>>> 
