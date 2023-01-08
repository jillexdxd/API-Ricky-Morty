from apiCogerJSON import getJSON
from claseVentana import Ventana

dat = dict(getJSON("https://rickandmortyapi.com/api/character"))

personajes = dat['results']

ventana = Ventana(personajes)
