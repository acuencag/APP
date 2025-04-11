# archivo: mini_test.py

import streamlit as st

st.title("Mini Test de Conocimiento")

st.write("Responde las siguientes preguntas:")

# Pregunta 1
pregunta1 = st.radio(
    "¿Cuál es la capital de Francia?",
    ["Madrid", "París", "Roma"]
)

# Pregunta 2
pregunta2 = st.radio(
    "¿Cuánto es 5 x 6?",
    ["30", "11", "56"]
)

# Pregunta 3
pregunta3 = st.radio(
    "¿Qué lenguaje se usa con Streamlit?",
    ["Python", "JavaScript", "C++"]
)

# Botón para enviar
if st.button("Enviar respuestas"):
    puntaje = 0
    if pregunta1 == "París":
        puntaje += 1
    if pregunta2 == "30":
        puntaje += 1
    if pregunta3 == "Python":
        puntaje += 1

    st.success(f"Tu puntaje es: {puntaje}/3")

    if puntaje == 3:
        st.balloons()
