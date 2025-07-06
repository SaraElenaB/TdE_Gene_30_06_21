import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDGene(self):

        gene = self._model.getAllNodes()
        for g in gene:
            self._view.ddGene.options.append( ft.dropdown.Option( g.GeneID ))

    def handleCreaGrafo(self, e):

        self._model.buildGraph()
        self.fillDDGene()
        numNodi, numArchi = self._model.getDetailsGraph()

        self._view.txtOut.controls.clear()
        self._view.txtOut.controls.append( ft.Text(f"Grafo creato con {numNodi} vertici e {numArchi} archi.") )
        self._view.update_page()


    def handleGeniAdiacenti(self, e):

        idNodo = self._view.ddGene.value

        if idNodo == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append( ft.Text(f"Attenzione, inserire un gene per continuare!", color="red") )
            self._view.update_page()
            return

        lista = self._model.getAdiacenti(idNodo)
        self._view.txtOut.controls.append(ft.Text(f"Geni adiacenti a: {idNodo}"))
        for t in lista:
            self._view.txtOut.controls.append(ft.Text(f"{t[0]} - {t[1]}"))

        self._view.update_page()

