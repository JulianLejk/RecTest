# -*-coding: utf -8 -*-
#import fileinfo
#info = fileinfo.MP3FileInfo("GrubSon - Na szczycie")
#print "\\n".join(["%s=%s" % (k,v) for k,v in info.items()])
#info = fileinfo.MP3FileInfo("/Music/",[".mp3"])

#print "\\n".join(["%s=%s" % (k,v)
    #              for k,v in fileinfo.listDirectory(info)])
#nie działa wyswietlanie atrybutów dla wszystkich .mp3 z pliku
class FileInfo(dict):
    u"przechowuje metadane pliku"
    def __init__(self, filename=None):
        dict.__init__(self)
        self["plik"] = filename
import fileinfo
f =fileinfo.FileInfo("Music/GrubSon - Na szczycie.mp3")
print f.__class__
print f.__doc__
print f
def leakmem():
    f=fileinfo.FileInfo("Music/GrubSon - Na szczycie.mp3")
for i in range(100):
    leakmem()


    class UserDict:
        def init(self, dict=None):

            self.data = {}
    if dict is not None:
        UserDict.self.update(dict)

def clear(self):self.data.clear()
def copy(self):
    if self.__class__ is UserDict:
        return UserDict(self.data)
    import copy
    return copy.copy(self)
def keys(self): return self.data.keys()
def items(self): return self.data.items()
def values(self): return self.data.values()

f =fileinfo.FileInfo("Music/GrubSon - Na szczycie.mp3")
print f
print f.__getitem__["plik"]
