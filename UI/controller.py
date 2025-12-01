from tkinter.tix import INTEGER
from tokenize import String

import flet as ft
from UI.view import View
from model.model import Model
from UI.alert import AlertManager

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model
        self._alert = AlertManager(page=self._view.page)

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia

        """
        lista_visualizzazione = self._view.lista_visualizzazione #ogni volta che schiaccio il pulsante pulisco la lista
        lista_visualizzazione.controls.clear()

        guadagno_medio = self._view.guadagno_medio_minimo.value

        #controllo 1
        if guadagno_medio is None or guadagno_medio.strip() == "":
            self._alert.show_alert("Non hai inserito nessun guadagno minimo")
            return
        #controllo 2
        if not guadagno_medio.isdigit():
            self._alert.show_alert("Il guadagno inserito non è valido "
                                   "(non puoi mettere valori negativi o parole, solo interi!)")
            return

        guadagno_medio = int(guadagno_medio)

        lista_connessioni = self._model.costruisci_grafo(guadagno_medio) # Dopo aver passato un guadagno medio valido creo il grafo in base a quest'ultimo

        numero_nodi = self._model.get_num_nodes()
        numero_tratte = self._model.get_num_edges()

        lista_visualizzazione.controls.clear()
        lista_visualizzazione.controls.append(ft.Text(f"Numero Hubs: {numero_nodi}"))
        lista_visualizzazione.controls.append(ft.Text(f"Numero Tratte: {numero_tratte}"))

        edges = self._model.get_all_edges(lista_connessioni)
        for linea in edges:
            lista_visualizzazione.controls.append(ft.Text(linea))

        self._view.update()









