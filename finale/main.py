import csv
import os
 
 
def salva_sala(sala):
    with open("sala.csv", "w", newline="") as file:       
        writer = csv.writer(file)                           
        writer.writerows(sala)                            
    print("Stato della sala salvato in sala.csv")
 
 
# 1. Creazione sala: per ognuna delle 5 file abbiamo creato fila con 10 posti liberi L e aggiunto ogni fila alla sala
 
def crea_sala():
    sala = []
    for i in range(5):
        if i == 3:                    
            fila = ['V'] * 10         
        else:
            fila = ['L'] * 10        
        sala.append(fila)
    return sala
 
 
 
# 2. Visualizzazione della sala
 
def mostra_sala(sala):
    print("\n========= SALA CINEMA PARADISO ========")
    print("      ", end="")
    
    for posto in range(1, 11):                        
        print(f"{posto:2}", end=" ")
    print()
    
    for i, fila in enumerate(sala, start=1):          
        print(f"Fila {i}: ", end="")                  
        for posto in fila:                           
            print(f"{posto:2}", end=" ")
        print()
    print("==========================================")
    print("L = libero  V = VIP libero  X = occupato")
 
 
 
# 3. Prenotazione di un posto
 
def prenota(sala, fila, posto):
   
    if fila < 1 or fila > 5 or posto < 1 or posto > 10:      
        return None                                         
    
    # Conversione delle coordinate in indici Python
    fila = fila - 1
    posto = posto - 1
    
    # Controllo della disponibilità
    if sala[fila][posto] == "X":       
        return False                   
 
    if sala[fila][posto] == "V":
        risposta = input(f"Hai selezionato un posto VIP ( Fila {fila}, Posto{posto}). Sei sicuro? (s/n): ").strip().lower()
        
        if risposta == 's':
            sala[fila][posto] = "X"
            return "VIP"
        else:
            print("Prenotazione VIP annullata.")
            return False
 
    sala[fila][posto] = "X"            
    return True
 
    
    
 
# Funzione carica sala
 
def carica_sala():
    if os.path.exists("sala.csv"):            
        with open("sala.csv", "r") as file:    
            reader = csv.reader(file)          
            sala = [row for row in reader]   
        print("Stato della sala caricato da sala.csv")
        return sala
 
 
# 4. Programma principale
 
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