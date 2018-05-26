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
    q = 'MATCH (n: Restaurantes) WHERE n.price="'+price+'" RETURN n'
    resultsD = db.query(q, returns=(client.Node, str, client.Node))
    for r in resultsD:
    	print(r[0]["name"])
    return r
    	

def consultaTipo (type1, client, db):
    q = 'MATCH (n: Restaurantes) WHERE n.type="'+type1+'" RETURN n'
    resultsD = db.query(q, returns=(client.Node, str, client.Node))
    for r in resultsD:
    	print(r[0]['name'])

def recomendar (price, type1, zone, parking, saludable, timing, client, db):
    q = 'MATCH (n: Restaurantes) WHERE n.price="'+price+'" RETURN n'
    resultsP = db.query(q, returns=(client.Node, str, client.Node))
    restaurantes = []
    for r in resultsP:
    	if restaurantes.count(r)<1:
    		restaurantes.append(r)

    q = 'MATCH (n: Restaurantes) WHERE n.type1="'+type1+'" RETURN n'
    resultsT = db.query(q, returns=(client.Node, str, client.Node))
    for r in resultsT:
    	if restaurantes.count(r)<1:
    		restaurantes.append(r)
    q = 'MATCH (n: Restaurantes) WHERE n.zone="'+zone+'" RETURN n'
    resultsZ = db.query(q, returns=(client.Node, str, client.Node))
    for r in resultsZ:
    	if restaurantes.count(r)<1:
    		restaurantes.append(r)
    q = 'MATCH (n: Restaurantes) WHERE n.parking="'+parking+'" RETURN n'
    resultsPa = db.query(q, returns=(client.Node, str, client.Node))
    for r in resultsPa:
    	if restaurantes.count(r)<1:
    		restaurantes.append(r)
    q = 'MATCH (n: Restaurantes) WHERE n.saludable="'+saludable+'" RETURN n'
    resultsS = db.query(q, returns=(client.Node, str, client.Node))
    for r in resultsS:
    	if restaurantes.count(r)<1:
    		restaurantes.append(r)
    q = 'MATCH (n: Restaurantes) WHERE n.timing="'+timing+'" RETURN n'
    resultsTi = db.query(q, returns=(client.Node, str, client.Node))
    for r in resultsTi:
    	if restaurantes.count(r)<1:
    		restaurantes.append(r)
    ## Punteo
    for r in restaurantes:
    	if r[0]['price'] == price:
    		numero = int(r[0]['score'])
    		numero = numero + 10
    		r[0]['score'] = str(numero)
    for r in restaurantes:
    	if r[0]['type1'] == type1:
    		numero = int(r[0]['score'])
    		numero = numero + 30
    		r[0]['score'] = str(numero)
    for r in restaurantes:
    	if r[0]['zone'] == zone:
    		numero = int(r[0]['score'])
    		numero = numero + 30
    		r[0]['score'] = str(numero)
    for r in restaurantes:
    	if r[0]['parking'] == parking:
    		numero = int(r[0]['score'])
    		numero = numero + 10
    		r[0]['score'] = str(numero)
    for r in restaurantes:
    	if r[0]['timing'] == timing:
    		numero = int(r[0]['score'])
    		numero = numero + 30
    		r[0]['score'] = str(numero)
    restaurantes.sort(key=lambda r:r[0]['score'])
    for r in restaurantes:
    	print("Restaurante: "+r[0]['name']+" 	Score: "+r[0]['score'])

def recomendar1(type1,price,zone,parking,timing,saludable, client,db):
	q = 'MATCH (n: Restaurantes) WHERE n.price="'+price+'" RETURN n'
	resultsP1 = db.query(q, returns=client.Node)
	q = 'MATCH (n: Restaurantes) WHERE n.type="'+type1+'" RETURN n'
	resultsT1 = db.query(q, returns=(client.Node, str, client.Node))
	q = 'MATCH (n: Restaurantes) WHERE n.zone="'+zone+'" RETURN n'
	resultsZ1 = db.query(q, returns=(client.Node, str, client.Node))
	q = 'MATCH (n: Restaurantes) WHERE n.parking="'+zone+'" RETURN n'
	resultsPa1 = db.query(q, returns=(client.Node, str, client.Node))
	q = 'MATCH (n: Restaurantes) WHERE n.timing="'+timing+'" RETURN n'
	resultsTi1 = db.query(q, returns=(client.Node, str, client.Node))
	q = 'MATCH (n: Restaurantes) WHERE n.saludable="'+sdaludable +'" RETURN n'
	resultsS1 = db.query(q, returns=(client.Node, str, client.Node))
	restaurantes = []
	## restauran unique
	for r in resultsP:
		if restaurantes.count(r) < 1:
			restaurantes.append(r)
	for r in resultsT1:
		if restaurantes.count(r) < 1:
			restaurantes.append(r)
	for r in resultsZ1:
		if restaurantes.count(r) < 1:
			restaurantes.append(r)
	for r in resultsPa1:
		if restaurantes.count(r) < 1:
			restaurantes.append(r)
	for r in resultsTi1:
		if restaurantes.count(r) < 1:
			restaurantes.append(r)
	for r in resultsS1:
		if restaurantes.count(r) < 1:
			restaurantes.append(r)
	## Punteo
	for r in restaurantes:
		## verificar si esta
		if r[0]['price'] == price:
			numero = int(r[0]['score'])
			numero = numero + 10
			r[0]['score'] = str(numero)
	for r in restaurantes:
		## verificar si esta
		if r[0]['type1'] == type1:
			numero = int(r[0]['score'])
			numero = numero + 30
			r[0]['score'] = str(numero)
	for r in restaurantes:
		## verificar si esta
		if r[0]['zone'] == zone:
			numero = int(r[0]['score'])
			numero = numero + 30
			r[0]['score'] = str(numero)
	for r in restaurantes:
		## verificar si esta
		if r[0]['parking'] == parking:
			numero = int(r[0]['score'])
			numero = numero + 10
			r[0]['score'] = str(numero)
	for r in restaurantes:
		## verificar si esta
		if r[0]['timing'] == timing:
			numero = int(r[0]['score'])
			numero = numero + 30
			r[0]['score'] = str(numero)
	ordenados = sorted(restaurantes, key=lambda restaurant:restaunrant[0]['score'], reverse=False)
	for o in ordenados:
		print("Restaurante: "+o[0]['name']+" 	Score: "+ o[0]['score'])
	































	+'" RETURN n'
	resultsT = db.query(q, returns=(client.Node, str, client.Node))
	delPrecio = []
	for r in resultsP:
		delPrecio.append(r[0]['name'])
		print(delPrecio)
	delTipo = []
	for r in resultsT:
		delTipo.append(r[0]['name'])
		print(delTipo)





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
