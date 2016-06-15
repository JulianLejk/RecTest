import os
for k,v in os.environ.items():
    print "%s=%s" % (k,v)
print "\n".join(["%s=%s"%(k,v)
                     for k,v in os.environ.items()])
import sys
print "\n".join(sys.modules.keys())
#print "\n".join(sys.getrecursionlimit)
import fileinfo
print "-----------------------------------"
print "\n".join(sys.modules.keys())
print  fileinfo
sys.modules["fileinfo"]
from fileinfo import MP3FileInfo
print MP3FileInfo.__module__
print sys.modules[MP3FileInfo.__module__]
#getattr(module, subclass) zwraca referencje do obiektu poprzez nazwe
"""def getFileInfoClass(filename, module=sys.modules[FileInfo.__module__]): #(1)
u"zwraca klasę metadanych pliku na podstawie podanego rozszerzenia"
subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:] #(2)
return hasattr(module, subclass) and getattr(module, subclass) or FileInfo
„Jeśli ten moduł posiada klasę o nazwie zawartej w zmiennej subclass, to ją
zwróć, w przeciwnym wypadku zwróć klasę FileInfo”."""