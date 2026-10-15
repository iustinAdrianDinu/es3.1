import os

from gestione_sala import crea_sala, mostra_sala, prenota
from salvataggio import salva_sala, carica_sala, salva_incasso

incasso = 0

while True:
   
   print("1. Carica sala")
   print("2. Nuova sala")
   opzione = input("Scegli un'opzione (1 o 2 o q per uscire): \n")
   
   if opzione == "1":
      sala, incasso = carica_sala(incasso)
      
      if sala is None:
            print("Creazione di una nuova sala.")
            incasso = 0
            sala = crea_sala()
      break
      

   elif opzione == "2":
      incasso = 0
      sala = crea_sala()
      break
   elif opzione == "q":
      print("Uscita dal programma.")
      exit()
   elif opzione!="1" and opzione!="2" and opzione!="q":
      print("Opzione non valida. Riprova.")
   continue



# Creazione sala


while True:
   mostra_sala(sala)                                                    
   
   fila = input("\nInserisci la fila (1-5) oppure q per uscire: \n").strip()  
   
   if fila.lower() == 'q':
      print("Vuoi salvare lo stato della sala prima di uscire? (s/n)\n")
      risposta = input().lower()
      if risposta == 's':
            salva_sala(sala)
            salva_incasso(str(incasso))
      print("Uscita dal programma.\n")
      break                                                
   
   posto_input = input("Inserisci il posto (1-10): ").strip()        
   
   # Verifica numeri interi
   
   try:
      fila = int(fila)
      posto = int(posto_input)
   except ValueError:
      print("Coordinate non valide.\n")
      continue
   
   
   risultato = prenota(sala, fila, posto)
   if risultato is True:
      print("Prenotazione effettuata.\n")
      incasso += 5
   elif risultato == "VIP":                       
      print("Prenotazione VIP effettuata!\n")
      incasso += 10
   elif risultato is False:
      print("Posto già occupato.\n")
   else:
      print("Coordinate non valide.\n")

   print("INCASSO TOTALE: \n", incasso)