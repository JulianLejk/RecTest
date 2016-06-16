from singleton import Cars
Ford = []
Ford  = Cars("Ford","zielony",2002)
print Ford.__repr__()
Ford =("Ford","czarny",2001)
print Ford.__repr__()
Mercedes = Cars("Mercedes","czarny",2013)
print Mercedes.__repr__()
Mercedes.__set__("Mercedes","yellow",1999)
print Mercedes.__repr__()
