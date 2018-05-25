def agregarUsuario(nombre, number):
    query = "CREATE (user:User {name:" +nombre+", numero:"+number+"});"
    db.query(query)
def agregarRestaurante(nombre, price, type1, number):
    query = "CREATE (patinet:Patient {name:" +nombre+", precio:"+price+", tipo:"+type1+", numero:"+number+"});"
    db.query(query)
