#-*-coding: utf -8 -*-
text = "Nie za długi tekst"
print(text)
text2=" napis bez polskich znakow"
print(text2)
text3 = "kolejny tekxt, \n ktory po przecinku bedzie w nastepnej lini"
print(text3)

k = "uid"
v= "sa"
print "%r=%s"% (k,v)

uid="sa"
pwd= "secret"
print pwd +" nie jest poprawnym hasłem dla " + uid
print "%s nie jest poprawnym haslem dla %s" %(pwd,uid)
userCount = 6
print "Uzytkownikow: %d" % (userCount,)
#print "Uzytkownikow :" + userCount
print " dzisiejsza cena akcji to: %f"%50.242424453454354
print " dzisiejsza cena akcji to: %.3f"%50.242424
print " Zmiana w stosunku do dnia wczorajszego +%+.2f" %1.5



