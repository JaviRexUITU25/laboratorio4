import tkinter as tk
class Participante:
    def __init__(self,nombre,institucion):
        self.nombre=nombre
        self.institucion=institucion
    def mostrar_info(self):
        return f"{self.nombre}|{self.institucion}"
class Banda(Participante):
    categorias_validas= ["primaria","básico","diversificado"]
    criterios= ["ritmo","uniformidad","coreografia","alineacion","puntualidad"]
    def __init__(self,nombre,institucion,categoria):
        super().__init__(nombre,institucion)
        self._categoria= categoria
        self._puntajes={}
    @property
    def categoria(self):
        return self.categoria
    @categoria.setter
    def categoria(self,categoria):
        if categoria not in Banda.categorias_validas:
            print("Categoria invalida")
        else:
            self.categoria=categoria
    @property
    def puntajes(self):
        return self._puntajes
    @puntajes.setter
    def puntajes(self,nuevo_puntaje):
        self._puntajes=nuevo_puntaje
    def registrar_puntajes(self,puntajes):
        for criterio, valor in puntajes.items():
            if not (0 <= valor <= 10):
                print(f"Puntaje inválido en {criterio}: {valor}")
        self.puntajes = puntajes
    def total(self):
        return sum(self.puntajes.values())
    def promedio(self):
        return self.total()/len(Banda.criterios)
    def mostrar_info(self):
        if self.puntajes:
            return super().mostrar_info()+f"| {self._categoria} | Total: {self.total}"
        return super().mostrar_info()+f"| {self._categoria} | Sin evaluar"

class Concurso:
    def __init__(self,nombre,fecha):
        self.nombre=nombre
        self.fecha=fecha
        self.bandas={}

    def inscribir_banda(self, banda):
        if banda.nombre in self.bandas:
            print("Banda ya inscrita")
        self.bandas[banda.nombre] = banda

    def registrar_evaluacion(self, nombre_banda, puntajes):
        pass

    def listar_bandas(self):
        if self.bandas:
            return [banda.mostrar_info() for banda in self.bandas.values()]
        else:
            return ["No hay bandas inscritas"]
    def ranking(self):
        pass
class ConcursoBandasApp:
    def __init__(self):
        self.concurso = Concurso("Concurso 14 de Septiembre", "14/09/2025")
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("500x300")

        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Bandas Escolares\nConcurso 14 de Septiembre - Quetzaltenango",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=50)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Inscribir Banda", command=self.inscribir_banda)
        opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion)
        opciones.add_command(label="Listar Bandas", command=self.listar_bandas)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_banda(self):
        ventana_inscribir = tk.Toplevel(self.ventana)
        ventana_inscribir.title("Inscribir Banda")

        etiqueta_nombre = tk.Label(ventana_inscribir, text="Nombre de la Banda:")
        etiqueta_nombre.pack(pady=3)
        entrada_nombre = tk.Entry(ventana_inscribir)
        entrada_nombre.pack(pady=3)

        etiqueta_institucion = tk.Label(ventana_inscribir, text="Institucion:")
        etiqueta_institucion.pack(pady=3)
        entrada_institucion = tk.Entry(ventana_inscribir)
        entrada_institucion.pack(pady=3)
        etiqueta_categoria = tk.Label(ventana_inscribir, text="Categoria (Primaria/Basico/Diversificado):")
        etiqueta_categoria.pack(pady=3)
        entrada_categoria = tk.Entry(ventana_inscribir)
        entrada_categoria.pack(pady=3)
        def guardar():
            nombre = entrada_nombre.get()
            institucion = entrada_institucion.get()
            categoria = entrada_categoria.get().lower()
            banda = Banda(nombre, institucion, categoria)
            self.concurso.inscribir_banda(banda)
            print(f" Banda inscrita: {banda.mostrar_info()}")
        tk.Button(ventana_inscribir, text="Guardar", command=guardar).pack(pady=10)
    def registrar_evaluacion(self):
        ventana_eval = tk.Toplevel(self.ventana)
        ventana_eval.title("Registrar Evaluación")

    def listar_bandas(self):
        ventana_listar = tk.Toplevel(self.ventana)
        ventana_listar.title("Listar Bandas")
        for info in self.concurso.listar_bandas():
            tk.Label(ventana_listar, text=info).pack(pady=3)

    def ver_ranking(self):
        ventana_ranking = tk.Toplevel(self.ventana)
        ventana_ranking.title("Ranking Final")


if __name__ == "__main__":
    ConcursoBandasApp()