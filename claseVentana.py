import io
import tkinter as tk
from apiCogerJSON import getJSON
from PIL import Image, ImageTk
import urllib.request, urllib.error, urllib.parse


class Ventana:
    
    def __init__(self, personajes):
        self.personajes = personajes
        self.cargarVentana(personajes)

    def cargarVentana(self, personajes):
        #Para cargar imagenes desde la url
        def ImgFromUrl(url):
            global image
            with urllib.request.urlopen(url) as connection:
                raw_data = connection.read()
            im = Image.open(io.BytesIO(raw_data))
            image = ImageTk.PhotoImage(im)
            return image

        raiz = tk.Tk()
        raiz.title("Rick & Morty")
        raiz.iconbitmap("API-RickYMorty/resources/icono.ico")
        raiz.config(bg="#3c3e44")
        n = tk.IntVar()

        frame = tk.Frame(raiz)
        frame.config(bg="#3c3e44") 
        frame.grid(row=0, column=0)

        frame2 = tk.Frame(raiz)
        frame2.config(width=600,height=50, bg="#3c3e44") 
        frame2.grid(row=1, column=0)

        #Cada vez que cambie de indice en el json tengo que cargar los nuevos items de la ventana
        def cargarInfo(ind):

            imagen = tk.Label(frame, image=ImgFromUrl(personajes[ind]['image']))
            imagen.config(bg="#3c3e44")
            imagen.grid(row=0, column=0, rowspan=3)

            nombre = tk.Label(frame, text= personajes[ind]['name'])
            nombre.config(bg="#3c3e44", fg="white", width=45, font = 10)
            nombre.grid(row=0, column=1)

            status = tk.Label(frame, text= personajes[ind]['status'] + " - " + personajes[ind]['species'])
            status.config(bg="#3c3e44", fg="white", width=45)
            status.grid(row=1, column=1)

            url = personajes[ind]['episode'][0]
            jsonEpisodes = getJSON(url)

            episode = tk.Label(frame, text= "Episodio:\n" + jsonEpisodes['name'])
            episode.config(bg="#3c3e44", fg="white", width=45)
            episode.grid(row=2, column=1)

        cargarInfo(0)

        #Controles de los botones
        def siguiente():
            if n.get()>=len(personajes)-1:
                n.set(0)
            else:
                n.set(n.get()+1)
            cargarInfo(n.get())
        def anterior():
            if n.get()<0:
                n.set(len(personajes)-1)
            else:
                n.set(n.get()-1)
            cargarInfo(n.get())

        boton2 = tk.Button(frame2, text='Siguiente', command=siguiente)
        boton2.config(width = 50, bg="#3c3e44", fg="white", bd=0)
        boton2.grid(row=0, column=1)

        boton1 = tk.Button(frame2, text='Anterior')
        boton1.config(width = 50, bg="#3c3e44", fg="white", bd=0, command=anterior)
        boton1.grid(row=0, column=0)

        raiz.mainloop()
