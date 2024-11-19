import streamlit as st
import csv
import random

# Percorso al file CSV
file_path = "archivio.csv"

# Genera una sestina casuale (6 numeri distinti da 1 a 49)
def genera_sestina():
    return set(random.sample(range(1, 50), 6))

# Legge il file CSV e verifica la presenza della sestina
def verifica_sestina(file_path, sestina_da_verificare):
    try:
        with open(file_path, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                # Converti la riga in un set di interi, ignorando celle vuote
                estrazione = set(int(num) for num in row if num.isdigit())
                if estrazione == sestina_da_verificare:
                    return True
        return False
    except Exception as e:
        st.error(f"Errore durante la lettura del file: {e}")
        return False

# Interfaccia Streamlit
st.title("Verifica Sestine")

# Bottone per generare e verificare la sestina
if st.button("Genera e verifica sestina"):
    # Genera la sestina casuale
    sestina_da_verificare = genera_sestina()
    sestina_ordinata = sorted(sestina_da_verificare)

    # Esegui la verifica
    if verifica_sestina(file_path, sestina_da_verificare):
        st.success(f"Sestina generata: {sestina_ordinata}. La sestina è già in archivio!")
    else:
        st.info(f"Sestina generata: {sestina_ordinata}. La sestina non è mai stata estratta.")
