from collections import OrderedDict
sas = input("cmon")
ses = input('noni')
print("Ordered Dict")
a = OrderedDict()

a[1] = 'e'
a[2] = 'd'
a[3] = 'u'
a[4] = 'r'
a[5] = 'e'
a[6] = 'k'
a[7] = 'a'

a[1] = 'p'
print(a)
a[1235436] = 'john'
a[sas] = ses
print(a)
from collections import Counter
print("Counter")
a = [1,2,2,1,3,2,5,4,3,3,2,5,6]
c = Counter(a)
print(c)

print(list(c.elements()))


print(c.most_common())


from collections import ChainMap
print("Chain map")
a = {1 : "edureka" , 2 : "python"}
b = {3 : "ML" , 4 :"AI"}

a1 = ChainMap(a,b)
print(a1)
# a.("1,python")
print(a)


from collections import deque
print("deqe")
a = ['h', 'e', 'l', 'l', 'o', 'w']
d = deque(a)
print(d)

d.appendleft("whats up")
d.append("python")
print(d)
d.pop()
print(d)




from collections import namedtuple
print("tuple")
a = namedtuple("cources", "name, technology")
s = a("data science", "python")
print(s)


a = namedtuple("cources", "name, technology")
s = a._make(["artificial intelegence", "python"])
print(s)






'''''
A={"key": "value1",
   "key2":"value2",
   "key3":"value3",}

print(A.get("key"))
A["key"] = "hello"
print(A.get("key"))
A["key3"] = "bye"
print(A.get("key3"))
#A.clear()
print(A)
#b=A.copy()

print(A.values())
print(A.update())
print(A.items())
print(A.keys())
print(A.pop("key"))
print(A.popitem())
print(A.setdefault("key2"))
print(A)

#use case     '''
