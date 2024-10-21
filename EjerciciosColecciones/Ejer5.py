juegos = [
    {
        'categoria':'Accion',
        'juegos':["GTA","COD","PUBG"]
    },
    {
        'categoria':'Aventura',
        'juegos':["Assasind Creed","CRASH","Prince of Persia"]
    },
    {
        'categoria':'Deporte',
        'juegos':["FIFA","PES","Moto gp"]
    }

]

for categoria in juegos:
    print(f'-----------{categoria['categoria']}----------')
    for juego in categoria['juegos']:
        print(juego)
