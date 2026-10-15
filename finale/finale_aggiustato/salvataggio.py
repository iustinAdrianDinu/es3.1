import csv
import os


def salva_sala(sala):
    with open("sala.csv", "w", newline="") as file:       
        writer = csv.writer(file)                           
        writer.writerows(sala)                            
    print("Stato della sala salvato in sala.csv")

# Funzione carica sala
 
def carica_sala():
    if os.path.exists("sala.csv"):            
        with open("sala.csv", "r") as file:    
            reader = csv.reader(file)          
            sala = [row for row in reader]   
        print("Stato della sala caricato da sala.csv")
        return sala
 
 
