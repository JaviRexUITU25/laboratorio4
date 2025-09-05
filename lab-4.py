import tkinter as tk
ventana = tk.Tk()
ventana.title("Concurso de Bandas - Quetzaltenango")
ventana.geometry("500x300")
class Concurso:
    def __init__(self):
        self.bandas= {}
    def inscribir_banda(self):
        ventana_inscribir = tk.Toplevel(ventana)
        ventana_inscribir.title("Inscribir Banda")
        ventana_inscribir.geometry("400x300")
        try:
            nombre=tk.Label(ventana_inscribir,text="Nombre: ")
            nombre.pack(pady=3)
            entrada_nombre=tk.Entry(ventana_inscribir)
            entrada_nombre.pack(pady=3)
            if nombre in self.bandas:
                print("Nombre de la banda ya registrado")
                return
            institucion = tk.Label(ventana_inscribir, text="Institucion: ")
            institucion.pack(pady=3)
            entrada_institucion = tk.Entry(ventana_inscribir)
            entrada_institucion.pack(pady=3)
            categoria = tk.Label(ventana_inscribir, text="Categoria: ")
            categoria.pack(pady=3)
            entrada_categoria = tk.Entry(ventana_inscribir)
            entrada_categoria.pack(pady=3)
            self.bandas[nombre]= {
                "nombre":nombre,
                "institucion":institucion,
                "categoria":categoria
            }
        except Exception as e:
            print(f"Error: {e}")
        print("Se abrió la ventana: Inscribir Banda")

    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        ventana_eval = tk.Toplevel(ventana)
        ventana_eval.title("Registrar Evaluación")
        ventana_eval.geometry("400x300")

    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        ventana_listado = tk.Toplevel(ventana)
        ventana_listado.title("Listado de Bandas")
        ventana_listado.geometry("400x300")


    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        ventana_ranking = tk.Toplevel(ventana)
        ventana_ranking.title("Ranking Final")
        ventana_ranking.geometry("400x300")

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
        print("Se abrió la ventana: Inscribir Banda")
        tk.Toplevel(self.ventana).title("Inscribir Banda")

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