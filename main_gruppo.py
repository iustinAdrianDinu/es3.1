#===========================
# Esercitazione 3 - Gruppo 1
#===========================
 
# funzione per creare la sala come liste di liste
 
def crea_sala():
  sala = []
  for i in range(5):
    fila = ["L"] * 10
    sala.append(fila)
  return sala
     

# funzione per visualizzare su terminale la disposizione attuale
 
def mostra_sala(sala):
    print('\nStato sala:')
    print("       ", end="")
    for posto in range(1, 11):
        print(f"{posto:2}", end=' ')
    print()
    for i,fila in enumerate(sala, start=1):
        print(f"Fila {i}: ", end="")
        for posto in fila:
            print(f"{posto:2}", end=' ')
        print()
 
# prenotazione posto con annessi controlli sulla validità dei dati inseriti 

def prenota(sala, fila, posto):
    if fila < 1 or fila > 5 or posto < 1 or posto > 10:
        print("Coordinate non valide.")
        return False
    if sala[fila - 1][posto - 1] == "X":
        print("Posto già occupato.")
        return False
    sala[fila - 1][posto - 1] = "X" # si può assegnare perche i controlli sono gia stati fatti dagli if sopra
    print(f"Prenotazione effettuata: Fila {fila}, Posto {posto}")
    return True
 
# Main del programma

sala = crea_sala()



while True:
   mostra_sala(sala)
   fila = input("Inserisci il numero della fila (1-5) o q per uscire: ")
        
   if fila.lower() == 'q':
      print("Uscita dal programma.")
      break
   posto = input("Inserisci il numero del posto (1-10): ")

   # controllo che i valori siano interi
   try:
      fila = int(fila)
      posto = int(posto)
   except ValueError:
      print("Input non valido. Inserisci numeri.")
      continue
 
   prenotazione = prenota(sala, fila, posto)
 
 