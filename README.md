# Mood Tracker (Aplicación CLI en Python)

## Descripción

Mood Tracker es una aplicación de línea de comandos desarrollada en Python para registrar, en un momento determinado del día, distintos factores relacionados con el bienestar: estado de ánimo, medicamentos, ejercicio, sueño, estrés, alimentación, consumo de sustancias y nivel de interacción social.

En base a las respuestas, el programa calcula un puntaje total y promedio, entrega una evaluación general del estado del día y sugiere recomendaciones simples para mejorar hábitos.

Este proyecto forma parte de mi proceso formativo en Python y está enfocado en practicar control de flujo, validaciones de entrada, lógica condicional y manejo de listas.

---

## Contexto

Este proyecto surgió como una exploración inicial de una herramienta sencilla para apoyar el registro emocional de pacientes en contextos clínicos. La idea nace a partir de una conversación con una profesional de la Unidad de Psiquiatría del Hospital de Coquimbo, donde se planteó la utilidad de contar con un sistema básico que permitiera observar, de manera simple, ciertos patrones diarios relacionados con el bienestar.

La versión actual es únicamente un prototipo de consola (CLI) con fines educativos y de práctica de programación, no una herramienta médica ni de uso clínico real.

---

## Características principales

- Pregunta por:
  - Estado de ánimo (escala del 1 al 10).
  - Toma de medicamentos (sí/no).
  - Actividad física (sí/no).
  - Calidad del sueño (escala del 1 al 10).
  - Nivel de estrés (sí/medianamente/no).
  - Calidad de la alimentación (buena/regular/mala).
  - Consumo de alcohol o drogas (sí/no).
  - Socialización (sí/no).
- Asigna un puntaje numérico a cada respuesta.
- Calcula:
  - Puntaje total.
  - Puntaje promedio.
- Entrega una evaluación general del día (por ejemplo: "Deprimido (Requiere atención)", "Estás bien", etc.).
- Muestra recomendaciones básicas según los factores que aparecen más débiles (medicación, ejercicio, sueño, estrés, alimentación, consumo de sustancias, socialización).

---

## Objetivos del proyecto

- Practicar fundamentos de Python en un contexto cercano a un caso de uso real.
- Trabajar con:
  - Ciclos `while`.
  - Validación de entrada del usuario.
  - Estructuras condicionales (`if/elif/else`).
  - Listas y operaciones de suma/promedio.
- Desarrollar una aplicación CLI legible, simple y extensible.
- Documentar el proyecto de forma clara y profesional.

---

## Tecnologías utilizadas

- Python 3.x
- Entrada/salida por consola (CLI)

---

## Cómo ejecutar el proyecto

1. Clonar este repositorio o descargar el archivo: https://github.com/felipeperezcortes/mood-tracker-python.git
2. Ejectuar el script principal: mood-tracker-v01
3. Seguir las instrucciones en la consola para completar el registro del día.
