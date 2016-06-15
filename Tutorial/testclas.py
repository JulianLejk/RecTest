# -*-coding: utf -8 -*-
def sum(a,b):
    u"""finkcja bedzie zwracala sume"""
    return a*b
print sum(3,4)
slownik = {"imie":"kkk", "nazwisko":"myszka"}
lista = ["a","b","c"]
krotka = ("1","2","3","4")
print krotka[1]
print slownik.values()
print slownik["imie"]
lista.append("grzyb")
print lista

from apihelper import info
print info(krotka,20,1)
c= 2323
d="dsdss"
#print d+c
d= d +str(c)
print d
li=["JJ","Moris"]
print  li.pop
print getattr(li,"pop")
getattr(li,"append")("Mort")
li.append(u"CzerwonyWiewór")
print li
getattr({},"clear")
print li
li.append("Eminem")
print li
g = lambda g: li.__doc__
print lambda s:s

def silnia(a):
        suma=1
        while a>0:
            suma=suma*a
            a=a-1
        return suma
print silnia(10)
d = silnia
print d(10)






"""def foo():print 2
foo()
foo.__doc__
print foo.__doc__ is None
print unicode(foo.__doc__)
li = []
print li.append.__doc__
s= "buildConnectionString"
print s.ljust(30)
print s.ljust(20)

li = ["a", "b", "c"]
print "\n".join(li)
from apihelper import  info
import  apihelper
li = ["kalafaktor","mieszanka","dzwig","a","b","b","ass","1212"]
print info(object)
#str 95
#print info(unicode(li),30,0)
#print info(unicode(li))
from odbchelper import buildConnectionString
#print unicode(u"jeździectwo","utf-8")#z tym jest problem
print " ".join(str(li))
print getattr.__doc__
print getattr(apihelper,"info")
print li
print [lis for lis in li if len(lis) >1 ]
print [lis for lis in li if li.count(lis) ==2]

a = ""
b = "tabaluga"
print 1 and a or b
a =[""]
print 1 and a or b
print sum(3,4)"""



