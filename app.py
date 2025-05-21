import streamlit as st
import random
import time

# Título de la página
st.title("Aprendiendo Python: Bucles y Condicionales")
st.write("En esta página aprenderás sobre `while`, `for` e `if` en Python.")

# Sección informativa
st.header("🔍 Conceptos Claves")

st.subheader("Bucles `while`")
st.write("El bucle `while` ejecuta un bloque de código mientras una condición sea verdadera.")
st.code("""
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
""", language="python")

st.subheader("Bucles `for`")
st.write("El bucle `for` se usa para iterar sobre secuencias como listas o rangos.")
st.code("""
for i in range(5):
    print("Iteración número:", i)
""", language="python")

st.subheader("Condicionales `if`")
st.write("Las estructuras `if` permiten tomar decisiones en el código.")
st.code("""
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
""", language="python")

# Cuestionario interactivo
st.header("📋 Cuestionario")

preguntas = [
    ("¿Cuál es la sintaxis correcta para un bucle `while` en Python?", ["while condicion:", "for i in range()", "if condicion:", "print()"], "while condicion:"),
    ("¿Para qué se usa el bucle `for`?", ["Ejecutar código una sola vez", "Iterar sobre secuencias", "Tomar decisiones", "Declarar variables"], "Iterar sobre secuencias"),
    ("¿Cuál es la estructura básica de un `if` en Python?", ["if condicion:", "for condicion in range()", "print(condicion)", "while condicion:"], "if condicion:"),
    ("¿Cómo se detiene un bucle `while`?", ["Con `break`", "Con `return`", "Con `stop`", "No se puede detener"], "Con `break`"),
    ("¿Cuál de estas es una estructura condicional?", ["while", "for", "if", "range"], "if"),
    ("¿Qué operador se usa para comparar igualdad?", ["==", "=", "!=", "<>"], "=="),
    ("¿Cuál de estas opciones genera un bucle infinito?", ["while True:", "for i in range(10):", "if x > 10:", "print('Hola')"], "while True:"),
    ("¿Qué hace el `else` en un `if`?", ["Define variables", "Se ejecuta si `if` es falso", "Imprime resultados", "Crea un bucle"], "Se ejecuta si `if` es falso"),
    ("¿Qué palabra clave usamos para salir de un bucle `for`?", ["stop", "exit", "break", "pass"], "break"),
    ("¿Cuál es la mejor estructura para recorrer una lista?", ["while", "for", "if", "print"], "for"),
]

# Diccionario para respuestas del usuario
respuestas = {}

for idx, (pregunta, opciones, respuesta_correcta) in enumerate(preguntas):
    respuestas[idx] = st.radio(pregunta, opciones)

if st.button("📝 Calcular puntaje"):
    puntaje = sum([1 for idx, (_, _, respuesta_correcta) in enumerate(preguntas) if respuestas[idx] == respuesta_correcta])
    st.write(f"Tu puntaje es: {puntaje}/10")

    # Mostrar animación de globos si el puntaje es perfecto
    if puntaje == 10:
        st.balloons()

