#startswith - startswith(prefix,start,end)
s1='Hello World'
x1=s1.startswith('Hello')
print(x1)

#endswith - endswith(suffix,start,end)
s2='Hello How Are You'
x2=s2.endswith('You')
print(x2)

#removeprefix - removeprefix(prefix)
s3='HHello World'
x3=s3.removeprefix('H')
print(x3)
#Similarly remove suffix is also present

#split - split(sep,maxsplit)
s4='Hello World How Are You'
x3=s4.split()
print(x3)

#partition - partition(sep)
s5='Python is easy'
x4=s5.partition('is')
print(x4) #rpartition partitions from the given element starting from right side and only on the first occurring element