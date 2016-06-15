import statsout
def output(data,format="text"):
    output_function = getattr(statsout,"output_%s" % format, statsout.statsout_text)
    return output_function(data)
#. Teraz możemy wywołać funkcję wyjściową w taki sam sposób jak inne funkcje.
#Zmienna output function jest referencją do odpowiedniej funkcji w statsout.
#Na szczęście do funkcji getattr możemy podać trzeci, opcjonalny argument, czyli
#domyślnie zwracaną wartość, gdy podany atrybut nie istnieje.