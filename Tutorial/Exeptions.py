#-*-coding: utf -8 -*-

"""try:
    import termios, TERMIOS
except ImportError:
    try:
        import msvcrt
    except ImportError:
        try:
            from EasyDialogs import AskPassword
        except ImportError:
            getpass = AskPassword.default_getpass
        else:
            getpass = AskPassword
    else:
        getpass = msvcrt.win_getpass
else:
    getpass = termios.unix_getpass

• Próba użycia nieistniejącego klucza w słowniku rzuci wyjątek KeyError
• Wyszukiwanie w liście nieistniejącej wartości rzuci wyjątek ValueError
• Wywołanie nieistniejącej metody obiektu rzuci wyjątek AttributeError
• Użycie nieistniejącej zmiennej rzuci wyjątek NameError
• Mieszanie niezgodnych typów danych spowoduje wyjątek TypeError
"""
try:
    f= open("C:/Temp/t.txt","rb")
    try:
        print f
        print f.mode
        print f.name
        print f.tell()
        print f.seek(-128,2)#poruszanie sie po otwartym pliku
        print f.tell()
        tagData = f.read(64)
        print  tagData
    finally:
            print f.closed
            f.close()
            print f.closed
            #f.seek(0)
except IOError:
    pass

logfile = open("test.log","w")
logfile.write("udanytest")

logfile.close()
print open("test.log").read()
logfile = open("test.log","a")
logfile.write("\nlinia2")
logfile.close()
print open("test.log").read()
li = ["a","b","c","d"]
for s in li:
    print s
print "\n".join(li)
for i in range(5):
    print i
for i in range(len(li)):
    print li[i]






