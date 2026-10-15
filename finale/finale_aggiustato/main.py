from gestione_sala import mostra_sala, prenota, carica_sala
from salvataggio import salva_sala, crea_sala
 
# 4. MAIN PROGRAMMA
 
while True:
    
    print("1. Carica sala")
    print("2. Nuova sala")
    opzione = input("Scegli un'opzione (1 o 2 o q per uscire): \n")
    
    if opzione == "1":
        sala = carica_sala()
        if sala is None:
            print("Creazione di una nuova sala.")
            sala = crea_sala()
            break
        break
    elif opzione == "2":
        sala = crea_sala()
        break
    elif opzione == "q":
        print("Uscita dal programma.")
        exit()
    elif opzione!="1" and opzione!="2" and opzione!="q":
        print("Opzione non valida. Riprova.")
    continue
 
 
 
# creo la sala
incasso = 0
 
while True:
    mostra_sala(sala)                                                    
    
    fila = input("\nInserisci la fila (1-5) oppure q per uscire: \n").strip()  
    
    if fila.lower() == 'q':
        print("Vuoi salvare lo stato della sala prima di uscire? (s/n)\n")
        risposta = input().lower()
        if risposta == 's':
            salva_sala(sala)
        print("Uscita dal programma.\n")
        break                                                
    
    posto_input = input("Inserisci il posto (1-10): ").strip()        
    
    # Verifica che siano stati inseriti numeri interi
    
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
    elif risultato == "VIP":                       # messaggio per la prenotazione di un posto VIP
        print("Prenotazione VIP effettuata!\n")
        incasso += 10
    elif risultato is False:
        print("Posto già occupato.\n")
    else:
        print("Coordinate non valide.\n")
 
    print("INCASSO TOTALE: \n", incasso)