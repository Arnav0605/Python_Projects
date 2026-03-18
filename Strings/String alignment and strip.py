#ljust - leftjust ljust(width,fillchar)
#rjust - rightjust
#center
#zfill - zfill(argument)
s='Hello'
x1=s.ljust(7,'*')
print(x1)
x2=s.rjust(9,'-')
print(x2)
x3=s.center(7,'+')
print(x3)
x4=s.zfill(9)
print(x4)
#>>>>>>>>>>>>>>>>>>>>>>>>Strip<<<<<<<<<<<<<<<<<<<<<<<<<#
#lstrip(char)
#rstrip(char)
#strip*char)
s1='  Hello'
s2='Hello  '
s3='  Hello  '
s4='!#Hello+*#'
x1=s1.lstrip(' ')
print(x1)
x2=s2.rstrip(' ')
print(x2)
x3=s3.strip(' ')
print(x3)
x4=s4.strip('!#*+')
print(x4)