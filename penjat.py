import os
import paraules
import puntuacions

# Variables globals de joc
paraula_actual = ''
tipus_paraula = ''
# Utilizarem un 'set' per les lletres introduides. Els 'set' no permeten duplicats.
lletres_escrites = set()
paraules_encertades = 0
errors = 0
max_errors = 6


def neteja_terminal():
    os.system('clear')


# Elegeix nova paraula i la posa a les variables globals tipus_paraula i paraula_actual
# inicialitza lletres_escrites
# Aquesta funció es cridarà a l'inici i cada cop que s'encerti una paraula
# Retorna un True si encara tenim paraules i un False quan s'acabin
def inicialitza_paraula():
    pass


# Funció que dibuixa el penjat, depenent del nombre d'errors
def dibuixa_penjat():
    pass


# Funció que introdueix nova lletra a llista_lletres i comprova si és un error
def nova_lletra(lletra):
    pass


# CODI PRINCIPAL DEL JOC
inicialitza_paraula()

# Bucle principal del joc
joc = True
while joc:
    neteja_terminal()

    print("******** JOC DEL PENJAT ********")
    print()
    print("Paraules encertades: {}".format(paraules_encertades))
    print()
    dibuixa_penjat()
    print()
    if errors >= max_errors:
        print("GAME OVER!!")
        joc = False
    else:
        if paraules.dibuixa_paraula(tipus_paraula, paraula_actual, lletres_escrites):
            # Ha retornat un True --> paraula encertada
            # Nova paraula i saltem a següent passada bucle
            pass
            # ... codi aquí ...

        print()
        nova_lletra(input("Introdueix una lletra: "))

# Guardem puntuació
paraules_encertades = 8
nom = "Aina"
puntuacions.nova_puntuacio(nom, paraules_encertades)

# Mostrem puntuacions
# ... codi aquí ...
