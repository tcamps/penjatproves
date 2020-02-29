# Rep nom de jugador i nombre de paraules encertades
# Guarda una nova entrada a "puntuacions.txt" amb el format "nom:paraules"
def nova_puntuacio(nom_jugador, paraules_encertades):
    	fitxer_puntuacions = open("puntuacions.txt", "a")
	fitxer_puntuacions.write(nom_jugador+":"+str(paraules_encertades)+"\n")
	fitxer_puntuacions.close()


# Recupera totes les puntuacions del fitxer "puntuacions.txt"
# Ordena els resultats de major a menor puntuacions
# Mostra els resultats per pantalla
def mostra_puntuacions():
    # Llegim i mostrem puntuacions
    pass
