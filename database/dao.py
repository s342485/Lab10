from database.DB_connect import DBConnect
from model.hub import Hub

class DAO:

    @staticmethod
    def get_hub():
        conn = DBConnect.get_connection()
        result =[]
        query = "SELECT * FROM hub" #seleziono tutto
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
