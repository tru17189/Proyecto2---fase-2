from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from metodos import *
 
db = GraphDatabase("http://localhost:7474", username="neo4j", password="Wasd")
# se crea los usuarios
user = db.labels.create("User")
u1 = db.nodes.create(name="Marco", tel="21341123")
user.add(u1)
u2 = db.nodes.create(name="Daniela", tel="33901234")
user.add(u2)
u3 = db.nodes.create(name="Paolo", tel="98001127")
user.add(u3)

#Se crea los restaurantes y hacemos sus categorias 
restaurantes = db.labels.create("Restaurantes")
r1 = db.nodes.create(name="Tre Fratelli", precio="Alto", tipo="Comida Italiana", tel="2493 8037")
r2 = db.nodes.create(name="Carls Jr", precio="Medio", tipo="Comida Rapida", tel="2361 8052")
r3 = db.nodes.create(name="Subway", precio="Bajo", tipo="Comida Rapida", tel="2386 8686")
r4 = db.nodes.create(name="Tapas y Canas", precio="Alto", tipo="Comida Española", tel="2473 7779")
r5 = db.nodes.create(name="Taco Bell", precio="Bajo", tipo="Comida Mexicana", tel="2202 0000")
r6 = db.nodes.create(name="Barista", precio="Medio", tipo="Café y postres", tel="2411 7272")
r7 = db.nodes.create(name="Los Cebollines", precio="Alto", tipo="Comida mexicana", tel="2256 2490")
r8 = db.nodes.create(name="Del Griego", precio="Alto", tipo="Comida Griega", tel="5945 0000")
r9 = db.nodes.create(name="Jacks Place", precio="Medio", tipo="Bar", tel="2474 5808")
#Agregamos todos los restaurantes
restaurantes.add(r1, r2, r3, r4, r5, r6, r7, r8, r9)

# Creamos relaciones de los restaurantes dependiendo su categorias
r3.relationships.create("Precios bajos", r5)

r2.relationships.create("Precios medios", r6)
r2.relationships.create("Precios medios", r9)
r9.relationships.create("Precios medios", r6)

r1.relationships.create("Precios altos", r4)
r1.relationships.create("Precios medios", r7)
r1.relationships.create("Precios medios", r8)
r4.relationships.create("Precios medios", r7)
r4.relationships.create("Precios medios", r8)
r7.relationships.create("Precios medios", r8)

r2.relationships.create("Comida Rapida", r3)
r5.relationships.create("Comida mexicana", r7)

#Creamos relaciones entre los usuarios y los restauramtes
u1.relationships.create("le gusta", r4)
u1.relationships.create("le gusta", r9)
u2.relationships.create("le gusta", r8)
u2.relationships.create("le gsuta", r4)
u3.relationships.create("le gusta", r2)
u3.relationships.create("le gsuta", r3)

#Menú
menu = True
while menu:
        print ("\tLa base de este proyecto muestra relaciones de los usuarios con los restauramtes que le gustan")
        print ("Desde aquí puedes seleccionar lo que desea hacer con el sistema de recoendaciones\n")                         
        print ("1.)Agregar nuevo usuario: ")                         
        print ("2.)Agregar nuevo Restaurante: ")                         
        print ("3.)Consultar restaurante por precio: ")                         
        print ("4.)Consultar restaurante por tipo: ")                         
        numero = input("Ingrese una opcion: ")
        if numero == "1":
            nombre = input("Ingresar nombre del usuario: ")
            number= input("Ingresar el numero del usuario: ")
            agregarUsuario(nombre, number, db)
        elif numero == "2":
            nombre = input("Ingresar nombre del restaurante: ")
            price= input("Ingresar el precio que maneja el restaurante: ")
            type1= input("Ingresar el tipo de que es restaurante: ")
            number= input("Ingresar el numero del restaurante: ")
            agregarRestaurante(nombre,price,type1, number, db)
        elif numero == "3":
             price = input("Ingresar el precio que busca: \nbusque Bajo, Medio o Alto")
             consultaPrecio(price,db)
        elif numero == "4":
             type1 = input("Ingresar el tipo de restaurante que busca: \nbEjemplo Comida Rapida, Comida mexicana")
             consultaTipo(type1,db)
        else:
            menu = False
        



