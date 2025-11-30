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
        guadagno_medio = int(self._view.guadagno_medio_minimo.value)
        if guadagno_medio is None:
            self._alert.show_alert("Non hai inserito nessun guadagno minimo")
        if guadagno_medio <= 0:
            self._alert.show_alert("Il guadagno inserito è negativo o nullo")

        lista_visualizzazione = self._view.lista_visualizzazione
        lista_connessioni = self._model.costruisci_grafo(guadagno_medio) #passo il guadagno medio selezionato dall'utente
        numero_nodi = self._model.get_num_nodes()
        numero_tratte = self._model.get_num_edges()

        lista_visualizzazione.controls.append(ft.Text(f"Numero Hubs: {numero_nodi}"))
        lista_visualizzazione.controls.append(ft.Text(f"Numero Tratte: {numero_tratte}"))

        lista_visualizzazione.controls.append(ft.Text("Lista tratte:"))

        for u, v, d in lista_connessioni.edges(data=True):
            lista_visualizzazione.controls.append(
                ft.Text(f"{u} ↔ {v} | valore medio: {d['weight']}")
            )

        self._view.update()








