import  clases

juan = clases.Persona()
juan.setNombre('Juan')
juan.setApellido('Riquelme')
juan.setAltura('190 cm')
juan.setEdad('80 años')

print(f'La persona es: {juan.getNombre()} Su apellido es: {juan.getApellido()} Mide: {juan.getAltura()} y su edad es: {juan.getedad()}')
print(juan.hablar())

print('-------------------Persona 2 ----------------------')

informatico = clases.Informatico()
informatico.setNombre('Gabriel')
informatico.setApellido('Riquelme')

print(f'La persona es: {informatico.getNombre()} Su apellido es: {informatico.getApellido()} ')
print(informatico.getLenguajes())
print(informatico.hablar())
print(informatico.experiencia)

print('-------------------Persona 3 ----------------------')
tecnico = clases.TecnicoRedes()
tecnico.setNombre('Lionel ')
print(tecnico.auditarRedes,tecnico.getNombre(),tecnico.getLenguajes())