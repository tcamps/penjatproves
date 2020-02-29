import random

# Llegim l'arxiu de paraules per línies
arxiu = open("paraules.txt", "r")
linies = arxiu.readlines()
arxiu.close

# Treiem el salt de línia final de cada línia
linies = [linia.replace("\n", "") for linia in lines]

# Creem la llista llista_paraules on cada element és una llista de dos elements [tipus_paraula, paraula]
llista_paraules = []
for linia in linies:
	llista_paraules.append(linia.split(":"))


# Retorna una paraula de la llista demanera aleatoria
# Elimina la paraula de la llista
# Retorna un "None" si ja no queden paraules
def retorna_paraula():
	if len(llista_paraules) == 0:
		return None	
	else:
		paraula = random.choice(llista_paraules)
		llista_paraules.remove(paraula)
		return paraula


# Dibuixa per pantalla la pista (Tipus de x lletres)
# Dibuixa les lletres encertades i doble guiox baix "__" per cada lletra restant
# Retorna True si ja s'ha encertat la paraula, False en cas negatiu
def dibuixa_paraula(tipus_paraula, paraula_actual, lletres_escrites):
    # Per defecte s'ha encertat la paraula, en el moment que posem un
    # caracter en blanc "_" voldrà dir que la paraula no s'ha encertat
    pass
