import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):

        self._grafo = nx.Graph()
        self._nodes = []

        self._genes = DAO.getAllGenes()
        self._idMapGenes = {}
        for g in self._genes:
            self._idMapGenes[g.GeneID] = g

        self._interaction = DAO.getAllInteraction()
        self._idMapInteraction = {}
        for i in self._interaction:
            self._idMapInteraction[i.GeneID1, i.GeneID2] = i

    def getMapGenes(self):
        return self._idMapGenes

    def getMapInteraction(self):
        return self._idMapInteraction

    def getAllNodes(self):
        return DAO.getAllNodes(self._idMapGenes)

    def buildGraph(self):

        self._grafo.clear()
        self._nodes = DAO.getAllNodes(self._idMapGenes)
        self._grafo.add_nodes_from(self._nodes)

        for i in self._interaction:
            idGene1 = i.GeneID1
            idGene2 = i.GeneID2

            # Controllo di esistenza
            if idGene1 not in self._idMapGenes or idGene2 not in self._idMapGenes:
                print(f"ATTENZIONE: Gene mancante nell'idMapGenes: {idGene1} o {idGene2}")
                continue

            # Salta i cappi
            if idGene1 == idGene2:
                continue

            gene1 = self._idMapGenes[idGene1]
            gene2 = self._idMapGenes[idGene2]
            if gene1 in self._grafo.nodes and gene2 in self._grafo.nodes:
                if not self._grafo.has_edge(gene1, gene2):
                    if gene1.Chromosome == gene2.Chromosome:
                        peso = 2*abs(i.Expression_Corr)
                    else:
                        peso = abs(i.Expression_Corr)
                    self._grafo.add_edge(gene1, gene2, weight=peso)

    def getDetailsGraph(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def getAdiacenti(self, idnodo):

        gene = self._idMapGenes[idnodo]
        lista=[]

        for vicino in self._grafo.neighbors(gene):
            lista.append( (vicino, self._grafo[gene][vicino]["weight"] ) )

        lista.sort( key = lambda x: x[1], reverse=True )
        return lista


if __name__ == "__main__":
    m = Model()
    m.buildGraph()
    print(m.getDetailsGraph())
    print(m.getAdiacenti("G234194"))
    # print("AAAAAA")
    # print(m.getMapGenes())
    # print("BBBBBBB")
    # print(m.getMapInteraction())