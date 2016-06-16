# -*-coding: utf -8 -*-
import fileinfo

class counter(object):
    count = 0
    def __init__(self):
        self.__class__.count+=1

print counter
print counter.count
c = counter()
print c.count
print counter.count
d= counter()
print d.count

print c.count
print counter.count
e = counter()
print e.count
print c.count
m= fileinfo.MP3FileInfo()
m._MP3FileInfo__parse("Music/Music/O.S.T.R.-Lubię być sam")
print m
"""f =fileinfo.FileInfo("Music/GrubSon - Na szczycie.mp3")
#print f
#print f.__getitem__["plik"]
#print f["plik"]
#f.__setitem("gatunek",31)
#print f
mp3file = fileinfo.MP3FileInfo()
print mp3file
mp3file["plik"]= "Music/Music/GrubSon - Na szczycie.mp3"
print mp3file
mp3file["plik"]= "Music/Music/O.S.T.R.-Lubię być sam"
print mp3file
li="dsds","dsdsds","sssss"
print repr(li)
print len(li)
print fileinfo.FileInfo
print fileinfo.MP3FileInfo.tagDataMap
m=fileinfo.MP3FileInfo()
print m.tagDataMap"""