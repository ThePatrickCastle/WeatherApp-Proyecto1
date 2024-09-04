
"""
from apiRequests import APIRequest
from jsontoCsv import JSONtoCSV 
from cityDataBaseFinder import CityDataBaseFinder as cdbf

key = "310e40947f292086c33d04e2f959e7f8"


json4 = APIRequest.get_formatedJSON(key, 18.8333, -98, "")
json5 = APIRequest.get_formatedJSON(key, 0, 0, "Puebla")
json6 = APIRequest.get_formatedJSON(key, 0, 0, "Madrid")
JSONtoCSV.appendJSON(json4)
JSONtoCSV.appendJSON(json5)
JSONtoCSV.appendJSON(json6)

ciudadconespacios = APIRequest.get_formatedJSON(key, 0, 0, "Miguel Hidalgo")
JSONtoCSV.appendJSON(ciudadconespacios)


if cdbf.buscarCiudad("Madrid"):
    indice = cdbf.getIndiceCiudad("Madrid")
    listaParametros = cdbf.getParametros(indice)
    print(indice)
    print(listaParametros)

if cdbf.buscarCoordenadas(18.8333, -98):
    indice = cdbf.getIndiceCoordenadas(18.8333, -98)
    listaParametros = cdbf.getParametros(indice)
    print(indice)
    print(listaParametros)

"""


from recommendations import Recommendations

recomendacion1 = Recommendations("Miguel Hidalgo")

recomendacion2 = Recommendations(18.8333, -98)

print(recomendacion1.get_recommendations())
print(recomendacion2.get_recommendations())
