d = {"server":"mpilgrim", "database":"master"}
print(d)
print(d["server"])
print(d["database"])
d["database"] = "pubs"
print(d["database"])
d["ui"] = "sa"
print d
c= {}
c["klucz"] = "wartosc"
c["klucz"] = "innawartosc"
print c
c["Klucz"] = "duzy"
print c
c.clear()
del d["ui"]
print c 
print d