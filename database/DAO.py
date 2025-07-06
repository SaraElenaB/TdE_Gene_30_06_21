from database.DB_connect import DBConnect
from model.genes import Genes
from model.interaction import Interaction


class DAO():

    @staticmethod
    def getAllGenes():

        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        ris = []

        query = """select *
                    from genes g  """

        cursor.execute(query)
        for row in cursor:
            ris.append( Genes(**row))

        cursor.close()
        cnx.close()
        return ris

    @staticmethod
    def getAllInteraction():

        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        ris = []

        query = """ select *
                    from interactions i  """

        cursor.execute(query)
        for row in cursor:
            ris.append( Interaction(**row))

        cursor.close()
        cnx.close()
        return ris

    @staticmethod
    def getAllNodes( map):

        cnx= DBConnect.get_connection()
        cursor = cnx.cursor( dictionary=True )
        ris=[]

        query=""" select distinct g.GeneID
                  from genes g 
                  where g.Essential = "Essential"
                  order by g.GeneID"""

        cursor.execute(query)
        for row in cursor:
            idGene = row["GeneID"]
            if idGene in map:
                ris.append( map[idGene] )

        cursor.close()
        cnx.close()
        return ris

    @staticmethod
    def getWeight(idGene1, idGene2):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        ris = []

        query = """ select distinct g.GeneID
                          from genes g 
                          where g.Essential = "Essential" """

        cursor.execute(query)
        for row in cursor:
            idGene = row["GeneID"]
            if idGene in map:
                ris.append(map[idGene])

        cursor.close()
        cnx.close()
        return ris




