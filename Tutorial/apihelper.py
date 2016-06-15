# -*-coding: utf -8 -*-
def info(object, spacing=20, collapse=0):
    u"""Wypisuje metody i ich notki dokumentacyjne
    Argumentem mozebyc modul, klasa, lista, slownik czy  tez lancuch zanków"""
    methodList = [e for e in dir(object) if callable(getattr(object, e))]
    procesFunc = collapse and (lambda s: " ".join(s.split())) \
                 or (lambda s: s)
    print "\n".join(["%s %s" % \
                     (method.ljust(spacing), \
                      procesFunc(unicode(getattr(object, method).__doc__))) \
                     for method in methodList])



if __name__ == "__main__":
    print info.__doc__
"""import odbchelper
print info(odbchelper)
print info(odbchelper,collapse=0)
print info(spacing=15,object=odbchelper)
spacing oraz collapse są argumentami opcjonalnymi, ponieważ mają przypisane
wartości domyślne. Argument object jest wymagany, ponieważ nie posiada warto-
ści domyślnej. Jeżeli info zostanie wywołana tylko z jednym argumentem, spacing
przyjmie wartości 10, a collapse wartość 1. Jeżeli wywołamy tę funkcję z dwoma
argumentami, jedynie collapse przyjmuje wartość domyślną (czyli 1)."""
