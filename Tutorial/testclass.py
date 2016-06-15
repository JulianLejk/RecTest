# -*-coding: utf -8 -*-
import fileinfo
class samochod(object):
    def __init__(self):
        pass
    dane = {"kolor" :"zielony",
                "rodzaj":"combi"
        }

d =fileinfo.MP3FileInfo("Music/Music/O.S.T.R.-Lubię być sam")
print samochod.dane.__getitem__("kolor")
d=fileinfo.MP3FileInfo()
d._MP3FileInfo__parse("Music/Music/O.S.T.R.-Lubię być sam")
print d
#atrybuty klasy defioniowane są w klasie a instancji po stworzeniu danej instancji
