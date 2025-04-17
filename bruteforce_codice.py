import pyautogui
import time

print("Brute Force By Kite79")
print("Benvenuto nella mia app!")
# Imposta il range tramite due valori interi
# Input da console
inizio = int(input("Inserisci il valore iniziale del range: "))
fine = int(input("Inserisci il valore finale del range: "))
lunghezza = len(str(fine))

# Avviso iniziale per selezionare la finestra dove vuoi che venga eseguito lo script di brute force
print("Hai 5 secondi per cliccare sulla finestra dove inserire il codice...")
time.sleep(5)  # ti dà il tempo di cliccare sulla finestra target

# Inizia brute force dal valore che hai messo nelle variabili inizio e fine
for i in range(inizio, fine):
    codice = f"{i:0{lunghezza}d}"  # Formatta con zeri dinamicamente
    print(f"Inserisco codice: {codice}")
    pyautogui.write(codice)  # scrive il codice
    pyautogui.press("enter")  # preme invio
    time.sleep(0.5)  # attende 0.5 secondi prima del prossimo codice
0