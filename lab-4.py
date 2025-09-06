import tkinter as tk
class Participante:
    def __init__(self,nombre,institucion):
        self.nombre=nombre
        self.institucion=institucion
    def mostrar_info(self):
        return f"{self.nombre}|{self.institucion}"
class Banda(Participante):
    def __init__(self,nombre,institucion,categoria):
        super().__init__(nombre,institucion)
        self.categoria= categoria
        self.puntajes={}
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
            pass
        def ranking(self):
            pass
class ConcursoBandasApp:
    def __init__(self):
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
    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        tk.Toplevel(self.ventana).title("Registrar Evaluación")

    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        tk.Toplevel(self.ventana).title("Listado de Bandas")

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        tk.Toplevel(self.ventana).title("Ranking Final")


if __name__ == "__main__":
    ConcursoBandasApp()