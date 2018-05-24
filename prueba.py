from neo4jrestclient.client import GraphDatabase
 
db = GraphDatabase("http://localhost:7474", username="neo4j", password="Wasd")
 
# Create some nodes with labels 

parqueo = db.labels.create("Parqueo")
# Parqueo cobrado
p0 = db.nodes.create(name="0")
# Parqueo gratis
p1 = db.nodes.create(name="1")
parqueo.add(p0, p1)


saludable = db.labels.create('Saludable')
# no saludable
s0 = db.node.create(name='0')
# con opciones saludable
s1 = db.node.create(name='1')
# Saludable
s2 = db.node.create(name='2')
saludable.add(s0,s1,s2)


tiempo = db.labels.create('Tiempo')
# comida rapida
t0 = db.node.create(name='0')
# comida de tenedonr
t1 = db.node.create(name='1')
tiempo.add(t0,t1)


precio = db.labels.create('Precio')
# 1 mas barato
p1 = db.node.create(name='1')
p2 = db.node.create(name='2')
p3 = db.node.create(name='3')
p4 = db.node.create(name='4')
# 5 mas caro
p5 = db.node.create(name='5')
precio.add(p1,p2,p3,p4,p5)


zona = db.labels.create('Zona')
z1 = db.node.create(name='1')
z2 = db.node.create(name='2')
z3 = db.node.create(name='3')
z4 = db.node.create(name='4')
z5 = db.node.create(name='5')
z6 = db.node.create(name='6')
z7 = db.node.create(name='7')
z8 = db.node.create(name='8')
z9 = db.node.create(name='9')
z10 = db.node.create(name='10')
z11 = db.node.create(name='11')
z12 = db.node.create(name='12')
z13 = db.node.create(name='13')
z14 = db.node.create(name='14')
z15 = db.node.create(name='15')
z16 = db.node.create(name='16')
z17 = db.node.create(name='17')
zona.add(z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11,z12,z13,z14,z15,z16,z17)


tipo = db.labels.create('Tipo')
t1 = db.node.create(name='Italiana')
t2 = db.node.create(name='Mexicana')
t3 = db.node.create(name='Hamburguesas')
t4 = db.node.create(name='Tacos')
t5 = db.node.create(name='Panes')
t6 = db.node.create(name='Pastas')
t7 = db.node.create(name='Carnes')
t8 = db.node.create(name='Crepas')
t9 = db.node.create(name='Gourmet')
t10 = db.node.create(name='Ensaladas')
t11 = db.node.create(name='Sushi')
t12 = db.node.create(name='Chino')


tipo.add(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12)

restaurante = db.labels.create("Restaurante")
r1 = db.nodes.create(name="Taco Bell")
r2 = db.nodes.create(name="Taco Inn")
r3 = db.nodes.create(name="Italiannis")
r4 = db.nodes.create(name="Sushiito")
r5 = db.nodes.create(name="Bagel Bros")
r6 = db.nodes.create(name="Tony Romas")
r7 = db.nodes.create(name="Skillets")
r8 = db.nodes.create(name="Saul")
r9 = db.nodes.create(name="Panda")
r10 = db.nodes.create(name="Tre Fratelli")
restaurante.add(r1,r2,r3,r4,r5,r6,r7,r8,r9, r10)

## Taco Bell
# Restaurant-parqueo gratis->Parqueo relationships
r1.relationships.create("parqueo gratis", p1)
# Restaurant-saludable->Saludable relationships
r1.relationships.create("saludable", s0)
# Restaurant-tiempo->Tiempo relationships
r1.relationships.create("tiempo", t0)
# Restaurant-precio->Precio relationships
r1.relationships.create("precio", p1)
# Restaurant-zona->Zona relationships
r1.relationships.create("zona", z11)
r1.relationships.create("zona", z10)
r1.relationships.create("zona", z16)
r1.relationships.create("zona", z15)
r1.relationships.create("zona", z13)
r1.relationships.create("zona", z9)
# Restaurant-tipo->Tipo relationships
r1.relationships.create("tipo", t2)
r1.relationships.create("tipo", t4)

## Taco inn
# Restaurant-parqueo gratis->Parqueo relationships
r2.relationships.create("parqueo gratis", p1)
# Restaurant-saludable->Saludable relationships
r2.relationships.create("saludable", s1)
# Restaurant-tiempo->Tiempo relationships
r2.relationships.create("tiempo", t1)
# Restaurant-precio->Precio relationships
r2.relationships.create("precio", p3)
# Restaurant-zona->Zona relationships
r2.relationships.create("zona", z11)
r2.relationships.create("zona", z10)
# Restaurant-tipo->Tipo relationships
r2.relationships.create("tipo", t5)
r2.relationships.create("tipo", t4)

## Italianis
# Restaurant-parqueo gratis->Parqueo relationships
r3.relationships.create("parqueo gratis", p1)
# Restaurant-saludable->Saludable relationships
r3.relationships.create("saludable", s1)
# Restaurant-tiempo->Tiempo relationships
r3.relationships.create("tiempo", t1)
# Restaurant-precio->Precio relationships
r3.relationships.create("precio", p5)
# Restaurant-zona->Zona relationships
r3.relationships.create("zona", z10)
# Restaurant-tipo->Tipo relationships
r3.relationships.create("tipo", t1)
r3.relationships.create("tipo", t5)
r3.relationships.create("tipo", t6)
r3.relationships.create("tipo", t7)
r3.relationships.create("tipo", t9)
r3.relationships.create("tipo", t10)


## Sushiito
# Restaurant-parqueo gratis->Parqueo relationships
r4.relationships.create("parqueo gratis", p1)
# Restaurant-saludable->Saludable relationships
r4.relationships.create("saludable", s1)
# Restaurant-tiempo->Tiempo relationships
r4.relationships.create("tiempo", t1)
# Restaurant-precio->Precio relationships
r4.relationships.create("precio", p3)
# Restaurant-zona->Zona relationships
r4.relationships.create("zona", z7)
r4.relationships.create("zona", z10)
r4.relationships.create("zona", z16)
# Restaurant-tipo->Tipo relationships
r4.relationships.create("tipo", t12)
r4.relationships.create("tipo", t11)
r4.relationships.create("tipo", t9)

## Sushiito
# Restaurant-parqueo gratis->Parqueo relationships
r4.relationships.create("parqueo gratis", p1)
# Restaurant-saludable->Saludable relationships
r4.relationships.create("saludable", s1)
# Restaurant-tiempo->Tiempo relationships
r4.relationships.create("tiempo", t1)
# Restaurant-precio->Precio relationships
r4.relationships.create("precio", p3)
# Restaurant-zona->Zona relationships
r4.relationships.create("zona", z7)
r4.relationships.create("zona", z10)
r4.relationships.create("zona", z16)
# Restaurant-tipo->Tipo relationships
r4.relationships.create("tipo", t12)
r4.relationships.create("tipo", t11)
r4.relationships.create("tipo", t9)

## Bagel bros
# Restaurant-parqueo gratis->Parqueo relationships
r5.relationships.create("parqueo gratis", p0)
# Restaurant-saludable->Saludable relationships
r5.relationships.create("saludable", s2)
# Restaurant-tiempo->Tiempo relationships
r5.relationships.create("tiempo", t0)
# Restaurant-precio->Precio relationships
r5.relationships.create("precio", p2)
# Restaurant-zona->Zona relationships
r5.relationships.create("zona", z7)
r5.relationships.create("zona", z10)
r5.relationships.create("zona", z16)
# Restaurant-tipo->Tipo relationships
r5.relationships.create("tipo", t5)
r5.relationships.create("tipo", t10)

## Tony Romas
# Restaurant-parqueo gratis->Parqueo relationships
r6.relationships.create("parqueo gratis", p1)
# Restaurant-saludable->Saludable relationships
r6.relationships.create("saludable", s1)
# Restaurant-tiempo->Tiempo relationships
r6.relationships.create("tiempo", t1)
# Restaurant-precio->Precio relationships
r6.relationships.create("precio", p4)
# Restaurant-zona->Zona relationships
r6.relationships.create("zona", z11)
# Restaurant-tipo->Tipo relationships
r6.relationships.create("tipo", t3)
r6.relationships.create("tipo", t6)
r6.relationships.create("tipo", t8)
r6.relationships.create("tipo", t9)
r6.relationships.create("tipo", t10)

## Skillets
# Restaurant-parqueo gratis->Parqueo relationships
r7.relationships.create("parqueo gratis", p1)
# Restaurant-saludable->Saludable relationships
r7.relationships.create("saludable", s1)
# Restaurant-tiempo->Tiempo relationships
r7.relationships.create("tiempo", t1)
# Restaurant-precio->Precio relationships
r7.relationships.create("precio", p3)
# Restaurant-zona->Zona relationships
r7.relationships.create("zona", z11)
r7.relationships.create("zona", z10)
r7.relationships.create("zona", z17)
r7.relationships.create("zona", z15)
# Restaurant-tipo->Tipo relationships
r7.relationships.create("tipo", t1)
r7.relationships.create("tipo", t2)
r7.relationships.create("tipo", t3)
r7.relationships.create("tipo", t4)
r7.relationships.create("tipo", t5)
r7.relationships.create("tipo", t10)
r7.relationships.create("tipo", t7)
r7.relationships.create("tipo", t9)

## Saul
# Restaurant-parqueo gratis->Parqueo relationships
r8.relationships.create("parqueo gratis", p1)
# Restaurant-saludable->Saludable relationships
r8.relationships.create("saludable", s2)
# Restaurant-tiempo->Tiempo relationships
r8.relationships.create("tiempo", t1)
# Restaurant-precio->Precio relationships
r8.relationships.create("precio", p4)
# Restaurant-zona->Zona relationships
r8.relationships.create("zona", z6)
r8.relationships.create("zona", z3)
r8.relationships.create("zona", z11)
r8.relationships.create("zona", z15)
r8.relationships.create("zona", z11)
r8.relationships.create("zona", z16)
r8.relationships.create("zona", z14)
r8.relationships.create("zona", z12)
# Restaurant-tipo->Tipo relationships
r8.relationships.create("tipo", t5)
r8.relationships.create("tipo", t6)
r8.relationships.create("tipo", t7)
r8.relationships.create("tipo", t8)
r8.relationships.create("tipo", t9)
r8.relationships.create("tipo", t10)

## Panda
# Restaurant-parqueo gratis->Parqueo relationships
r9.relationships.create("parqueo gratis", p0)
# Restaurant-saludable->Saludable relationships
r9.relationships.create("saludable", s1)
# Restaurant-tiempo->Tiempo relationships
r9.relationships.create("tiempo", t0)
# Restaurant-precio->Precio relationships
r9.relationships.create("precio", p3)
# Restaurant-zona->Zona relationships
r9.relationships.create("zona", z7)
r9.relationships.create("zona", z11)
r9.relationships.create("zona", z9)
r9.relationships.create("zona", z10)
# Restaurant-tipo->Tipo relationships
r9.relationships.create("tipo", t11)
r9.relationships.create("tipo", t6)
r9.relationships.create("tipo", t7)
r9.relationships.create("tipo", t12)

## Tre Fratelli
# Restaurant-parqueo gratis->Parqueo relationships
r10.relationships.create("parqueo gratis", p0)
# Restaurant-saludable->Saludable relationships
r10.relationships.create("saludable", s1)
# Restaurant-tiempo->Tiempo relationships
r10.relationships.create("tiempo", t0)
# Restaurant-precio->Precio relationships
r10.relationships.create("precio", p3)
# Restaurant-zona->Zona relationships
r10.relationships.create("zona", z7)
r10.relationships.create("zona", z11)
r10.relationships.create("zona", z9)
r10.relationships.create("zona", z10)
# Restaurant-tipo->Tipo relationships
r10.relationships.create("tipo", t11)
r10.relationships.create("tipo", t6)
r10.relationships.create("tipo", t7)
r10.relationships.create("tipo", t12)


#Usuarios
user = db.labels.create("Usuarios")
u1 = db.nodes.create(name = "Juan")
u2 = db.nodes.create(name = "Carlos")
u3 = db.nodes.create(name = "Julia")
u4 = db.nodes.create(name = "Afedo")
u5 = db.nodes.create(name = "Nicolle")
u6 = db.nodes.create(name = "Ana")
u7 = db.nodes.create(name = "Luis")
u8 = db.nodes.create(name = "Pedro")
u9 = db.nodes.create(name = "David")
u10 = db.nodes.create(name = "Lucia")
user.add(u1, u2, u3, u4, u5, u6, u7, u8, u9, u10)

#Relaciones de usuarios
##Usuario 1
u1.relationships.create("Parqueo", p1)
u1.relationships.create("Saludable", s1)
u1.relationships.create("Tiempo", t0)
u1.relationships.create("Precio", p2)
u1.relationships.create("Zona", z7)
u1.relationships.create("Tipo", t2)

##Usuario 2
u2.relationships.create("Parqueo", p0)
u2.relationships.create("Saludable", s2)
u2.relationships.create("Tiempo", t0)
u2.relationships.create("Precio", p3)
u2.relationships.create("Zona", z10)
u2.relationships.create("Tipo", t1)

##Usuario 3
u3.relationships.create("Parqueo", p0)
u3.relationships.create("Saludable", s2)
u3.relationships.create("Tiempo", t1)
u3.relationships.create("Precio", p4)
u3.relationships.create("Zona", z15)
u3.relationships.create("Tipo", t9)

##Usuario 4
u4.relationships.create("Parqueo", p1)
u4.relationships.create("Saludable", s0)
u4.relationships.create("Tiempo", t0)
u4.relationships.create("Precio", p1)
u4.relationships.create("Zona", z1)
u4.relationships.create("Tipo", t2)

##Usuario 5
u5.relationships.create("Parqueo", p0)
u5.relationships.create("Saludable", s2)
u5.relationships.create("Tiempo", t0)
u5.relationships.create("Precio", p3)
u5.relationships.create("Zona", z14)
u5.relationships.create("Tipo", t11)

##Usuario 6
u1.relationships.create("Parqueo", p1)
u1.relationships.create("Saludable", s1)
u1.relationships.create("Tiempo", t1)
u1.relationships.create("Precio", p4)
u1.relationships.create("Zona", z3)
u1.relationships.create("Tipo", t8)

##Usuario 7
u1.relationships.create("Parqueo", p1)
u1.relationships.create("Saludable", s1)
u1.relationships.create("Tiempo", t0)
u1.relationships.create("Precio", p2)
u1.relationships.create("Zona", z7)
u1.relationships.create("Tipo", t2)

##Usuario 8
u1.relationships.create("Parqueo", p1)
u1.relationships.create("Saludable", s1)
u1.relationships.create("Tiempo", t0)
u1.relationships.create("Precio", p1)
u1.relationships.create("Zona", z11)
u1.relationships.create("Tipo", t11)

##Usuario 9
u1.relationships.create("Parqueo", p1)
u1.relationships.create("Saludable", s1)
u1.relationships.create("Tiempo", t0)
u1.relationships.create("Precio", p2)
u1.relationships.create("Zona", z10)
u1.relationships.create("Tipo", t5)

##Usuario 10
u1.relationships.create("Parqueo", p0)
u1.relationships.create("Saludable", s1)
u1.relationships.create("Tiempo", t1)
u1.relationships.create("Precio", p3)
u1.relationships.create("Zona", z4)
u1.relationships.create("Tipo", t7)
