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
r1 = db.nodes.create(name="Tre Fratelli", price="Alto", type1="Comida Italiana", tel="2493 8037", zone="11", parking="Gratis", saludable="S", timing="Tenedor", score="0")
r2 = db.nodes.create(name="Carls Jr", price="Medio", type1="Hamburguesas", tel="2361 8052", zone="7", parking="Gratis", saludable="NS", timing="Rapida", score="0")
r3 = db.nodes.create(name="Subway", price="Bajo", type1="Panes", tel="2386 8686", zone="12", parking="Gratis", saludable="S", timing="Rapida", score="0")
r4 = db.nodes.create(name="Tapas y Canas", price="Alto", type1="Comida Española", tel="2473 7779", zone="15", parking="Pagado", saludable="S", timing="Tenedor", score="0")
r5 = db.nodes.create(name="Taco Bell", price="Bajo", type1="Comida Mexicana", tel="2202 0000", zone="16", parking="Gratis", saludable="NS", timing="Rapida", score="0")
r6 = db.nodes.create(name="Barista", price="Medio", type1="Café y postres", tel="2411 7272", zone="9", parking="Gratis", saludable="S", timing="Rapida", score="0")
r7 = db.nodes.create(name="Los Cebollines", price="Alto", type1="Comida mexicana", tel="2256 2490", zone="11", parking="Pagado", saludable="S", timing="Tenedor", score="0")
r8 = db.nodes.create(name="Del Griego", price="Alto", type1="Comida Griega", tel="5945 0000", zone="10", parking="Gratis", saludable="S", timing="Tenedor", score="0")
r9 = db.nodes.create(name="Jacks Place", price="Medio", type1="Bar", tel="2474 5808", zone="5", parking="Pagado", saludable="NS", timing="Rapida", score="0")
#Agregamos todos los restaurantes
restaurantes.add(r1, r2, r3, r4, r5, r6, r7, r8, r9)

# Creamos relaciones de los restaurantes dependiendo su categorias
r3.relationships.create("Precios bajos", r5)

r2.relationships.create("Precios medios", r6)
r2.relationships.create("Precios medios", r9)
r9.relationships.create("Precios medios", r6)

r1.relationships.create("Precios altos", r4)
r1.relationships.create("Precios altos", r7)
r1.relationships.create("Precios altos", r8)
r4.relationships.create("Precios altos", r7)
r4.relationships.create("Precios altos", r8)
r7.relationships.create("Precios altos", r8)

r1.relationships.create("S", r3)
r1.relationships.create("S", r6)
r1.relationships.create("S", r7)
r1.relationships.create("S", r8)
r3.relationships.create("S", r6)
r3.relationships.create("S", r7)
r3.relationships.create("S", r8)
r6.relationships.create("S", r7)
r6.relationships.create("S", r8)

r2.relationships.create("S", r4)
r2.relationships.create("S", r5)
r4.relationships.create("S", r5)

r1.relationships.create("11", r2)
r1.relationships.create("11", r7)
r1.relationships.create("11", r6)
r2.relationships.create("11", r7)
r2.relationships.create("11", r6)
r6.relationships.create("11", r7)
r4.relationships.create("10", r8)
r2.relationships.create("9", r4)
r1.relationships.create("16", r6)

r4.relationships.create("Pagado", r7)
r4.relationships.create("Pagado", r9)
r7.relationships.create("Pagado", r9)


r1.relationships.create("Gratis", r2)
r1.relationships.create("Gratis", r3)
r1.relationships.create("Gratis", r5)
r1.relationships.create("Gratis", r6)
r1.relationships.create("Gratis", r8)
r2.relationships.create("Gratis", r3)
r2.relationships.create("Gratis", r5)
r2.relationships.create("Gratis", r6)
r2.relationships.create("Gratis", r8)
r3.relationships.create("Gratis", r5)
r3.relationships.create("Gratis", r6)
r3.relationships.create("Gratis", r8)
r6.relationships.create("Gratis", r8)

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
        print ("5.)Recomendar un restaurante: ") 
        print ("6.)Salir")                        
                        
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
             price = input("Ingresar el precio que busca: \n busque Bajo, Medio o Alto: ")
             price = price.capitalize()
             cuales = consultaPrecio(price, client, db)
             print(cuales)
        elif numero == "4":
             type1 = input("Ingresar el tipo de restaurante que busca: \nbEjemplo Comida Rapida, Comida mexicana")
             type1 = type1.capitalize()
             consultaTipo(type1,db)
        elif numero == "5":
        	type1 = input("Ingresar el tipo de restaurante que necesita: \n Ejemplo Comida Rapida, Comida mexicana")
        	type1 = type1.capitalize()
        	price = input("Ingresar el precio que necesita: \n busque Bajo, Medio o Alto: ")
        	price = price.capitalize()
        	zone = input("Ingrese la zona de restaurante que necesita (de 1 a 16)")
        	zone = price.capitalize()
        	parking = input("Ingresar un tipo de parqueo: Gratis o Pagado")
        	parking = parking.capitalize()
        	timing = input("Ingresar que tipo de comida: Rapida o Tenedor")
        	timing = timing.capitalize()
        	saludable = input("Ingresar que tipo de comida desea: saludable (S) o no saludable (NS)")
        	saludable = saludable.capitalize()
        	recomendar(price,type1,zone,parking,saludable, timing, client,db)
        else:
            menu = False
        



