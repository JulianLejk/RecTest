#-*-coding: utf -8 -*-
li=[]
"""print type(li)
print type("sads")
print type('222')
c= u"22"
print type(c)
import  odbchelper
print type(odbchelper)
import types
print type(odbchelper)== types.ModuleType
print str(1)
horseman = ["war", "pestilence","famine"]
print  horseman
horseman.append("powerbuider")
print str(horseman)
print horseman
print str(odbchelper)
print str(None)
print str(types)
print unicode(1)
print unicode(odbchelper)
print unicode(horseman[0])
print unicode(u"jeździectwo","utf-8")
li = []
print dir(li)
d= {}
print dir(d)
print dir(odbchelper)
import string
print string.punctuation
print  string.join
print  callable(string.punctuation)
print callable(string.join)
print string.join.__doc__
#79 strona
li = [ "Larry", "Curly"]
print li.pop
getattr(li,"pop")
getattr(li,"append")("Moe")
print li
print getattr({},"clear")
#getattr((),"pop")"""
import odbchelper
print odbchelper.buildConnectionString
print getattr(odbchelper,"buildConnectionString")
object = odbchelper
method ="buildConnectionString"
print getattr(object,method)
print type(getattr(object,method))
import types
print type(getattr(object,method))== types.FunctionType
print callable((getattr(object,method)))


