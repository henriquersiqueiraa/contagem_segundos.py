segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
totalSegundos = int(segundos)

# Calculando os dias
dias = totalSegundos // 86400

# Calculando as horas
segs_restantes = totalSegundos % 86400
horas = segs_restantes // 3600

# Calculando os minutos
segs_restantes = segs_restantes % 3600
minutos = segs_restantes // 60

# Calculando os segundos restantes finais
segs_restantes_finais = segs_restantes % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segs_restantes_finais, "segundos")