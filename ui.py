from tkinter import Tk, Button, filedialog, Label
import backend

window = Tk()
window.title('Polyline Offset Calculator')
window.geometry("300x200")

def load_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            backend.loadData(file_path)
            file_name = file_path.split('/')[-1]  
            lbl_arquivo.config(text=f"File loaded: {file_name}")
            print("CSV file loaded!")
        except Exception as e:
            lbl_arquivo.config(text="Error to load CSV file")
            print(f"Error to load CSV file: {e}")


def generateGraph():
    backend.generateGraph()

btn_carregar = Button(window, text="Load CSV", command=load_csv)
btn_carregar.pack(pady=20)

lbl_arquivo = Label(window, text="No files loaded")
lbl_arquivo.pack(pady=10)

btn_gerar = Button(window, text="Generate Graph", command=generateGraph)
btn_gerar.pack(pady=20)

window.mainloop()