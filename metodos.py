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

