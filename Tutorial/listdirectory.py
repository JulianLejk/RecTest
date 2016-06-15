import os
import sys
from fileinfo import FileInfo
def listDirectory(directory, fileExtList): #(1)
    u"zwraca listę obiektów zawierających metadane dla plików o podanych rozszerzeniach"
    fileList = [os.path.normcase(f) for f in os.listdir(directory)]
    fileList = [os.path.join(directory, f) for f in fileList
        if os.path.splitext(f)[1] in fileExtList] #(2)
    def getFileInfoClass(filename, module=sys.modules[FileInfo. module ]): #(3)
        u"zwraca klasę metadanych pliku na podstawie podanego rozszerzenia"
        subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:] #(4)
        return hasattr(module, subclass) and getattr(module, subclass) or FileInfo #(5)
    return [getFileInfoClass(f)(f) for f in fileList]