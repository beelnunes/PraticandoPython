segundos_str = input("Por favor, entre com o número de segundos que deseja converter:")
total_segundos = int(segundos_str)

dias = total_segundos // 86400
dias_resto = total_segundos % 86400

horas = dias_resto // 3600
horas_resto = dias_resto % 3600

minutos = horas_resto // 60
minutos_resto = horas_resto % 60

segundos = minutos_resto

print (dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")
