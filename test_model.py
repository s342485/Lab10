from model.model import Model
from database.dao import DAO

m = Model() #devo prima creare un istanza di model prima di chiamare
# il metodo
risultato = m.costruisci_grafo(300)


archi_pesi = m.get_all_edges()


conto_nodi = m.get_num_nodes()
print(f"Numero di Hubs: {conto_nodi} ")


conto_archi = m.get_num_edges()
print(f"Numero tratte: {conto_archi}")





