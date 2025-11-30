from networkx.algorithms import threshold

from database import dao
from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    #il grafo che devo costruire:
    # semplice (non ci sono archi doppi tra due nodi, e archi che partono e arrivano allo stesso nodo)
    # non orientato (non ha direzione)
    # pesato (guadagno medio)

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        self._nodes = DAO.get_hub()
        for hub in self._nodes: # popolo il grafo con gli hub
            self.G.add_node(hub)

        for u in self.G:
            for v in self.G:
                if u != v:
                    risultato = DAO.exist_connessione_tra(u, v) #restituisce una lista delle connessioni tra u e v e controlla se c'è una relazione tra i due nodoi
                    if risultato:
                        num_spedizioni = len(risultato)
                        somma_spedizioni = sum(row["valore_merce"] for row in risultato)
                        valore_medio = somma_spedizioni / num_spedizioni
                        if valore_medio >= threshold:
                            self.G.add_edge(u, v, weight=valore_medio)
        return self.G

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        return self.G.number_of_edges()


    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        """sum = 0
        for n in self.G.nodes():
            if self.G.degree(n) > 0 : #degree è il numero di archi che toccano il nodo
                sum += 1
        return sum """

        return self.G.number_of_nodes() #fa il ritorno di tutti i nodi anche senza arco


    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        for u,v,d in self.G.edges(data=True): #data = True permette di avere accesso al peso dell'arco
            print("Arco:", u, "-", v, "; valore_medio:", d['weight'] )



