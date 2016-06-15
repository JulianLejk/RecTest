# -*-coding: utf -8 -*-
"""import os
#dzialanie na nazwach i katalogach
print os.path.join("g:\\Muza\\ostr\\","01. O.S.T.R. - Od Autora - Prolegomena.mp3")
print os.path.join("g:\\Muza\\ostr","01. O.S.T.R. - Od Autora - Prolegomena.mp3")
print os.path.expanduser("`")
print os.path.join(os.path.expanduser("`"),"Python27")

print os.path.split("g:\\Muza\\ostr\\01. O.S.T.R. - Od Autora - Prolegomena.mp3")
(filepath,filename) =  os.path.split("g:\\Muza\\ostr\\01. O.S.T.R. - Od Autora - Prolegomena.mp3")
print filepath
(shortname,extension) = os.path.splitext(filename)
print shortname
print extension
print os.listdir("g:\\Muza\\ostr\\")
dirname = "c:\\"
print os.listdir(dirname)
li = [[f for f in os.listdir(dirname)
    if os.path.isfile(os.path.join(dirname,f))]]
print li

print os.listdir("g:\\Muza\\ostr\\")
import glob
print "\n".join(glob.glob("g:\\Muza\\ostr\\1*.mp3"))"""
print "--------------===----listdirectory------------------------------"
dirname = "c:\\"
import listdirectory
li= [listdirectory(dirname,".txt")]
print li




