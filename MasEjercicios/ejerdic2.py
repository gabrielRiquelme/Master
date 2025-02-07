verduleria ={
    'Banana': 1.35,
    'Manzana':0.80,
    'Pera': 0.85,
    'Naranja':0.70
}

verdura=input(f'Ingrese el nombre de alguna de estas frutas para averiguar el precio.{verduleria.keys()}')
print(verduleria[verdura])