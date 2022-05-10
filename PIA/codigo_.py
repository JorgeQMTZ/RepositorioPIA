dias =["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
nombre = []
kms = []
while True:
    num_alumnos = int(input("¿Cuántos alumnos han entrenado con Francisco?: "))
    if num_alumnos>0: break

for indice_cond in range(0,num_alumnos):
    nombre.append(input("Ingrese el nombre del alumno %d: " % (indice_cond + 1)))
    km_dias = []
    for indice_dias in range(0,7):
        km_dias.append(int(input("¿Cuántos km ha corrido el %s?: " % dias[indice_dias])))
    kms.append(km_dias)

total_kms = []
for km in kms:
    total_kms.append(sum(km))

for nombre, km in zip(nombre, total_kms):
    print("%s  ha realizado %d kms en toda la semana." % (nombre,km))
