#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Edson Castro'
import twitter
import io
import json

#Es bueno crearse un módulo en el que estén las funciones que más vais a utilizar
#en el trabajo con el API de Twitter, como puede ser la conexión o la búsqueda
#de datos
#
#Todo el código de esta parte podría ir en un módulo parte llamado por ejemplo twitterAPI


#Función para la conexión.
def oauth_login():
    CONSUMER_KEY = 'vWRIn7cDDPqwNg0jpz9ej8klZ'
    CONSUMER_SECRET = 'UzQznpC8o3ylUfcbYhKwV6Kt3MoDOgnSxu9Jnn3tmEbKTaHRZe'
    OAUTH_TOKEN = '7730092-BvcE6lKJs8455JE8hyEhYHKXHX5g9X05izuuU47qIX'
    OAUTH_TOKEN_SECRET = 'xGzotzBjBImJNDLAogP60jb3GVlRnp3M9jtp3QSFgJDAI'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

def obtenercoordenadas2(palabra):
  twitter_api =  oauth_login()  
  
  search_results = twitter_api.search.tweets(q=palabra, geocode='37.333351,-4.5765007,1000km') #puede expresarse en el rango en mi.
  statuses = search_results['statuses']
  
  #Guardadndo los datos de la busqueda en el fichero.
  save_json('datosbusqueda', statuses)
  #Leyendo los datos en el fichero de la busqueda realizada.
  statuses = json.loads(open('datosbusqueda.json').read())

  #Obteniendo las coordenadas de los tweets en los cuales existen posicion del tweet y guardando en orden
  #inverso, los datos se guardan en una lista para mostrar en los marcadores.
  #print "Lista de coordenadas encontradas\n"
  lista = []
  for status in statuses:
    if status['coordinates']!= None:        
        coord = status['coordinates']        
        latlong=[coord.values()[1][1] , coord.values()[1][0]]
        lista.append(latlong)
        #print latlong
  return latlong


#Función para grabar la información en formato JSON
def save_json(filename, data):
    with io.open('{0}.json'.format(filename),'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))

#Función para leer el fichero JSON
def load_json(filename):
    with io.open('{0}.json'.format(filename),encoding='utf-8') as f:
        return f.read()