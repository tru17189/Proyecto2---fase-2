from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from metodos import *

def agregarUsuario (nombre, number, db):
    Doctor = db.nodes.create(name=nombre, tel=number)
    Doctor.labels.add("User")
    print ("\nSe ha ingresado un usuario correctamente\n")

def agregarRestaurante (nombre, price, type1, number, db):
    Paciente = db.nodes.create(name=nombre, precio=price, tipo=type1, tel=number) 
    Paciente.labels.add("Restaurantes")
    print ("\nSe ha ingresado un restaurente correctamente\n")
    
def consultaPrecio (price, client, db):
    q = 'MATCH (u: Restaurantes) WHERE u.precio="'+price+'" RETURN u'
    resultsD = db.query(q, returns=(client.Node, str, client.Node))

def consultaTipo (type1, client, db):
    q = 'MATCH (u: Restaurantes) WHERE u.tipo="'+type1+'" RETURN u'
    resultsD = db.query(q, returns=(client.Node, str, client.Node))

#def recomedacionPrecio(restaurante, price):
 #   q = 'MATCH (u:Restaurante)-[r:PRECIO]->(m:Restaurente) WHERE u.name="'+restaurante+'" RETURN u, type(r),m'
  #  resultsP = db.query(q, returns=(client.Node, str, client.Node))
   #/ q = 'MATCH (u: Restaurante) WHERE u.Precio="'+price+'" RETURN u, type(r),m'
    #resultsD = db.query(q, returns=(client.Node, str, client.Node))
   # restaurantes={} #Se crea un diccionacio
    #for j in resultsD:
     #   restaurantes[j]=0 
    #for i in resultsP:
    #    restaurantes[i]=restaurantes[i]+1
     #   #Valores de los conocidos de los conocidos
      #  q = 'MATCH (u:Restaurantes)-[r:Knows]->(m:Restaurantes) WHERE u.name="'+restaurantes+" RETURN u, type(r),m'
       # resultsP2 = db.query(q, returns=(client.Node, str, client.Node))
        #for k in resultsP2:    
         #   q = 'MATCH (u:User)-[r:Busca]->(m:Restaurante) WHERE u.name="'+k+'" m.precio="'+price+'" RETURN u'
          #  restaurantes = db.query(q, returns=(client.Node))
            #Se agregan valores a los doctores que estan
           # for element in Restaurantes:
           #     restaurantes[element]=restaurantes[element]+1
   # for key, value in sorted(restaurantes.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    #    print "%s: %s" % (key, value)
