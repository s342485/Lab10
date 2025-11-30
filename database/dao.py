from PIL.ImageOps import expand

from database.DB_connect import DBConnect
from model.compagnia import Compagnia
from model.spedizione import Spedizione
from model.hub import Hub

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    @staticmethod
    def get_hub():
        conn = DBConnect.get_connection()
        result =[]
        query = "SELECT * FROM hub"
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            hub = Hub(row["id"], row["codice"], row["nome"], row["citta"], row["stato"], row["latitudine"], row["longitudine"])
            result.append(hub)
        cursor.close()
        conn.close()
        return result



    #TRAMITE IL FILE SPEDIZIONE VERIFICA L'ESISTENZA DI CONNESSIONE TRA DUE HUB

    @staticmethod
    def exist_connessione_tra(u : Hub, v: Hub):
        conn = DBConnect.get_connection()
        result = []
        query = "SELECT * FROM spedizione s WHERE (s.id_hub_origine = %s AND s.id_hub_destinazione = %s) OR (s.id_hub_origine = %s AND s.id_hub_destinazione = %s)"

        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (u.id, v.id, v.id, u.id))
        for row in cursor:
            result.append(row)
            print(row)
        cursor.close()
        conn.close()
        return result





    @staticmethod
    def get_destinazioni():
        """
        Restituisce tutte le destinazioni
        """
        cnx = (DBConnect.get_connection())
        result = []

        if cnx is None:
            print("Errore di connessione al database")
            return None
        cursor = cnx.cursor()
        query = "SELECT * FROM spedizione"

        try:
            cursor.execute(query)
            for row in cursor:
                spedizione = {
                    "id" : row[0],
                    "id_compagnia" : row[1],
                    "numero_tracking" : row[2],
                    "stato" : row[3],
                    "id_hub_origine" : row[4],  #importantissimo
                    "id_hub_destinazione" : row[5], #importantissimo
                    "valore_merce": row[8] #importantissimo
                }
                result.append(spedizione)

        except Exception as e:
            print(f"Errore durante la query {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result #restituisce una lista di dizionari di spedizione

