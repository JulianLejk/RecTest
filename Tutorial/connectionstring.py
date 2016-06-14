#-*-coding: utf -8 -*-
import odbchelper
params = { "server":"mpilgrim", "databse":"master","uid":"sa","pwd":"secret"}
"""print params.keys()
print params.values()
print params.items()
print odbchelper.buildConnectionString(params)
print odbchelper.buildConnectionString.__doc__
print params.items()
print [k for k, v in params.items()]
print [v for v, k in params.items()]
print [" %s : %s " %(k ,v) for k ,v in params.items()]
print [" %s : %s " %(v ,k) for k ,v in params.items()]
print [" %s : %s " %(v ,k) for v ,k in params.items()]
li = ["pwd=secret", "database=master", "uid=sa", "server=mpilgrim"]

print li
s= ";".join(li)
print s
s.split(";")
print s
print s.split(";",2)
print ord("a")
print chr(99)
print ord(u"ą")
print unichr(378)"""
errmsg= "nie można otworzyć pliku"
mag = errmsg.encode("utf-8")
print mag.decode("utf-8")

