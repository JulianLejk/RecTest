#-*-coding: utf -8 -*-
t= ("a", "b", "trzeci", "z", "element")
print t
print t[2]
print t[1:3]
#krotki nie posiadaja żadnych metod
print "b" in t
#Można jednak wykorzystać operator in,
#  aby sprawdzić, czy krotka zawiera dany element
# coś nie działą!!!!!!! #-*-coding: utf -8 -*- i działa
"""Pamiętasz, jak powiedzieliśmy, że klucze w słowniku mogą być łańcuchami znaków,
liczbami całkowitymi i “kilkoma innymi typami”? Krotki są jednym z tych
“innych typów”. W przeciwieństwie do list, mogą one zostać użyte jako klucz
w słowniku. Dlaczego? Jest to dosyć skomplikowane. Klucze w słowniku muszą
być niezmienne. Krotki same w sobie są niezmienne, jednak jeśli wewnątrz krotki
znajdzie się lista, to krotka ta nie będzie mogła zostać użyta jako klucz, ponieważ
lista jest zmienna. W takim przypadku krotka nie byłaby słownikowo-bezpieczna.
Aby krotka mogła zostać wykorzystana jako klucz, musi ona zawierać wyłącznie
łańcuchy znaków, liczby i inne słownikowo-bezpieczne krotki.
plusdo formatowania tekstu"""