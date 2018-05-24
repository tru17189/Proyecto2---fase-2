from neo4jrestclient.client import GraphDatabase
 
db = GraphDatabase("http://localhost:7474", username="neo4j", password="Wasd")
 
# Create some nodes with labels
user = db.labels.create("User")
u1 = db.nodes.create(name="Marco")
user.add(u1)
u2 = db.nodes.create(name="Daniela")
user.add(u2)
 
restaurantes = db.labels.create("Restaurantes")
r1 = db.nodes.create(name="Tre Fratelli")
r2 = db.nodes.create(name="Carls Jr")
r3 = db.nodes.create(name="Subway")
r4 = db.nodes.create(name="Tapas y Canas")
r5 = db.nodes.create(name="Pecorinos")
r6 = db.nodes.create(name="Barista")
r7 = db.nodes.create(name="Los Cebollines")
r8 = db.nodes.create(name="Del Griego")
r9 = db.nodes.create(name="Jacks Place")
# You can associate a label with many nodes in one go
restaurantes.add(r1, r2, r3, r4, r5, r6, r7, r8, r9)

categorias = db.labels.create("Categorias")
c1 = db.nodes.create(name="parqueo")
c2 = db.nodes.create(name="tiempo")
c3 = db.nodes.create(name="precio")
c4 = db.nodes.create(name="zona")
c5 = db.nodes.create(name="tipo")
c6 = db.nodes.create(name="saludable")
categorias.add(c1, c2, c3, c4, c5, c6)  



# Relationships
u1.relationships.create("likes", r1)
u1.relationships.create("likes", r2)
u2.relationships.create("likes", r1)
# Bi-directional relationship?
u1.relationships.create("friends", u2)

r1.relationships.create("1", c1)
r1.relationships.create("1", c2)
r1.relationships.create("4", c3)
r1.relationships.create("11",c4)
r1.relationships.create("Formal", c5)
r1.relationships.create("2", c6)

r2.relationships.create("1", c1)
r2.relationships.create("1", c2)
r2.relationships.create("3", c3)
r2.relationships.create("9",c4)
r2.relationships.create("Comida Rapida", c5)
r2.relationships.create("2", c6)

r3.relationships.create("1", c1)
r3.relationships.create("1", c2)
r3.relationships.create("3", c3)
r3.relationships.create("11",c4)
r3.relationships.create("Formal", c5)
r3.relationships.create("2", c6)

r4.relationships.create("1", c1)
r4.relationships.create("1", c2)
r4.relationships.create("3", c3)
r4.relationships.create("11",c4)
r4.relationships.create("Formal", c5)
r4.relationships.create("2", c6)

r5.relationships.create("1", c1)
r5.relationships.create("1", c2)
r5.relationships.create("3", c3)
r5.relationships.create("11",c4)
r5.relationships.create("Formal", c5)
r5.relationships.create("2", c6)

r6.relationships.create("1", c1)
r6.relationships.create("1", c2)
r6.relationships.create("3", c3)
r6.relationships.create("11",c4)
r6.relationships.create("Formal", c5)
r6.relationships.create("2", c6)

r7.relationships.create("1", c1)
r7.relationships.create("1", c2)
r7.relationships.create("3", c3)
r7.relationships.create("11",c4)
r7.relationships.create("Formal", c5)
r7.relationships.create("2", c6)

r8.relationships.create("1", c1)
r8.relationships.create("1", c2)
r8.relationships.create("3", c3)
r8.relationships.create("11",c4)
r8.relationships.create("Formal", c5)
r8.relationships.create("2", c6)

r9.relationships.create("1", c1)
r9.relationships.create("1", c2)
r9.relationships.create("3", c3)
r9.relationships.create("11",c4)
r9.relationships.create("Formal", c5)
r9.relationships.create("2", c6)
