"""print "a" and "b"
print "" and "b"
print "a"and "b"and "c"
print "a"and ""
print "---------------------------"
print "a" or "b"
print "" or "b"
print "a"or "b"and "c"
print "a"or
def sidefx():
    print "in sidefx()"
    return 1
print "a" and sidefx()
a= "first"
b= "second"
print 1 and a or b
print 0 and a or b"""
a=""
b= "second"
#print 1 and a or b#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
c=(1 and [a] or [b])[0]
print c
print(1 and [a] or [b])[0]
#w wyrazeniach lambda lipaa
def f(x):
    return x*2
print f(3)
g = lambda  x: x*2
print g(3)
print (lambda  x:x*2)(3)
#processFunc = collapse and (lambda s: " ".join(s.split()))
#  or (lambda s: s)
s= "this is\na\ttest"
print s
print s.split()
print " ".join(s.split())
#W Pythonielogikę wyboru możemy wyprowadzić poza funkcję i zdefiniować funkcję lambda, która
#jest dostosowana do tego, aby dać nam dokładnie to (i tylko to), co chcemy. Takie
#podejście jest bardziej efektywne, bardziej eleganckie i mniej podatne na błędy typu
#“Ups! Te argumenty miały być w odwrotnej kolejności...”.





