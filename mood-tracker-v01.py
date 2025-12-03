while True:  # Estado de animo
    animo = input(
        "- En la escala del 1 al 10 ¿Como te has sentido hoy?: ")
    if not animo.isdigit():
        print("Error! Ingresa un número, no una letra \n")
        continue

    animo = int(animo)
    if animo < 1 or animo > 10:
        print("Error! Elige un número entre 1 y 10")

    if animo == 1:
        print("> Evaluación: Te sentiste muy mal")
    elif 2 <= animo <= 4:
        print("> Evaluación: Te sentiste mal")
    elif animo == 5:
        print("> Evaluación: Te sentiste plano")
    elif 6 <= animo <= 9:
        print("> Evaluación: Te sentiste bien")
    elif animo == 10:
        print("> Evaluación: Te sentiste muy bien")
    else:
        print("Ingresa un número válido \n")
        continue
    break

while True:  # Medicamentos
    medicamentos = input(
        "\n- ¿Hoy tomaste tus medicamentos (si/no): ").strip().lower()
    if not medicamentos.isalpha():
        print("Error! Ingresa (si o no), no números")
        continue
    if medicamentos == "si":
        medicamentos_valor = 10
        print("> ¡Felicitaciones! Tomaste tus medicamentos")
    elif medicamentos == "no":
        medicamentos_valor = 1
        print("> ¡Ojo! No tomaste tus medicamentos")
    else:
        print("Error! Escribe si o no")
        continue
    break

while True:  # Ejercicio
    ejercicio = input(
        "\n- ¿Hiciste actividad física (si/no): ").strip().lower()
    if not ejercicio.isalpha():
        print("Error! Ingresa (si o no), no números")
        continue
    if ejercicio == "si":
        print("> ¡Felicitaciones! Hiciste actividad física")
        ejercicio_valor = 10
    elif ejercicio == "no":
        print("> ¡Ojo! No hiciste actividad física")
        ejercicio_valor = 1
    else:
        print("Error! Escribe si o no")
        continue

    break

while True:  # Sueño
    sueño = input(
        "\n- En la escala del 1 al 10 ¿Como dormiste hoy?: ")
    if not sueño.isdigit():
        print("Error! Ingresa un número del 1 al 10")
        continue

    sueño = int(sueño)
    if 1 > sueño > 10:
        print("Error! Elige un número entre 1 y 10")

    if sueño == 1:
        print("> Evaluación: Dormiste muy mal")
    elif 2 <= sueño <= 4:
        print("> Evaluación: Dormiste mal")
    elif sueño == 5:
        print("> Evaluación: Dormiste regular")
    elif 6 <= sueño <= 9:
        print("> Evaluación: Dormiste bien")
    elif sueño == 10:
        print("> Evaluación: Dormiste excelente")
    else:
        print("Ingresa un número válido")
        continue

    break

while True:  # Estres
    stress = input(
        "\n- ¿Te has sentido estresado (si/medianamente/no): ").strip().lower()
    if not stress.isalpha():
        print("Error! Ingresa letras, no números")
        continue
    if stress == "si":
        stress_valor = 1
        print("> Evaluación: Te sientes estresado")
    elif stress == "medianamente":
        stress_valor = 5
        print("> Evaluación: Te sientes medianamente estresado")
    elif stress == "no":
        stress_valor = 10
        print("> Evaluación: No te sientes estresado")
    else:
        print("Error! Escribe si, medianamente o no")
        continue
    break

while True:  # Alimentacion
    alimentacion = input(
        "\n- ¿Como fue la calidad de tu alimentacion hoy? (buena/regular/mala): ").strip().lower()
    if not alimentacion.isalpha():
        print("Error! Ingresa letras, no números")
        continue
    if alimentacion == "buena":
        alimentacion_valor = 10
        print("> ¡Felicitaciones! Comiste balanceadamente")
    elif alimentacion == "regular":
        alimentacion_valor = 5
        print("> ¡Ojo! Te puedes alimentar mejor")
    elif alimentacion == "mala":
        alimentacion_valor = 1
        print("> ¡Ojo! No cuidaste tu alimentación")
    else:
        print("Error! Escribe bien o mal")
        continue

    break

while True:  # Alcohol o drogas
    drogas = input(
        "\n- ¿Has consumo alcohol o drogas? (si/no): ").strip().lower()
    if not drogas.isalpha():
        print("Error! Ingresa letras, no números")
        continue
    if drogas == "no":
        drogas_valor = 10
        print("> ¡Excelente! No hubo consumo de alcohol o drogas")
    elif drogas == "si":
        drogas_valor = 1
        print("""> ¡Cuidado! El Alcohol o las drogas pueden incrementar
    las fluctuaciones de tu estado de animo""")
    else:
        print("Error! Escribe si o no")
        continue
    break

while True:  # Social
    social = input(
        "\n- ¿Has socializado hoy? (si/no): ").strip().lower()
    if not social.isalpha():
        print("Error! Ingresa letras, no números")
        continue
    if social == "no":
        social_valor = 1
        print("> ¡Ojo! El aislarte puede incrementar tus sintomas depresivos")
    elif social == "si":
        social_valor = 10
        print("""> Excelente! El socializar te ayuda a sentirte parte de la sociedad""")
    else:
        print("Error! Escribe si o no")
        continue
    break

# Resultado Final
puntajes = [
    animo,
    medicamentos_valor,
    ejercicio_valor,
    sueño,
    stress_valor,
    alimentacion_valor,
    drogas_valor,
    social_valor
]

total = sum(puntajes)
promedio = total / len(puntajes)

if promedio < 5:
    estado = "Deprimido (Requiere atención)"
elif promedio == 5:
    estado = "Estás plano"
elif 5 < promedio <= 9:
    estado = "Estás bien"
elif promedio <= 10:
    estado = "Estás excelente, sigue así"
else:
    estado = "Fuera de rango"

print("\nRESULTADOS")
print(f"Puntaje total: {total}")
print(f"Puntaje promedio: {promedio}")
print(f"Estado General: {estado}")

# Recomendaciones
recomendaciones = []

if medicamentos_valor <= 5:
    recomendaciones.append(
        "💊 Recuerda tomar tus medicamentos todos los días según lo indicado por tu médico.")
if ejercicio_valor <= 5:
    recomendaciones.append(
        "🏃‍♂️ Intenta moverte más hoy: una caminata de 20 minutos puede mejorar tu ánimo.")
if sueño <= 5:
    recomendaciones.append(
        "😴 Intenta dormir mejor esta noche. Evita pantallas 1 hora antes de acostarte.")
if stress_valor <= 5:
    recomendaciones.append(
        "🧘‍♂️ Practica respiración o meditación breve para reducir el estrés.")
if alimentacion_valor <= 5:
    recomendaciones.append(
        "🥗 Trata de incluir frutas, verduras o comidas caseras hoy.")
if drogas_valor <= 5:
    recomendaciones.append(
        "🚫 Evita el alcohol o drogas, ya que pueden afectar tu estabilidad emocional.")
if social_valor <= 5:
    recomendaciones.append(
        "🤝 Habla con alguien de confianza o sal a caminar acompañado.")

if recomendaciones:
    print("\nRECOMENDACIONES PARA HOY:")
    for r in recomendaciones:
        print("-", r)
else:
    print("\nNo hay recomendaciones, ¡vas muy bien hoy!")
