# archivo: mini_test.py

import streamlit as st
from collections import defaultdict

st.title("Cuestionario: ¿Qué empresa del Grupo Calaf va más contigo?")

st.write("Responde las siguientes preguntas:")


# Diccionario para puntajes
puntajes = defaultdict(int)

# Mapas de relación entre respuestas y empresas
relaciones = {
    1: [
        ("Obra civil o edificación tradicional", ["Calaf Constructora", "Calaf Trenching"]),
        ("Taller mecánico o planta de fabricación", ["Calaf Industrial", "Nextrencher"]),
        ("Oficinas tecnológicas e innovación", ["PICVISA Machine Vision Systems", "CICSA", "CIC3"]),
        ("Espacios naturales o medioambientales", ["DAGA", "Transparenta", "Ambitek"])
    ],
    2: [
        ("Me gusta ver cómo las cosas toman forma desde cero", ["Calaf Constructora", "Calaf Trenching"]),
        ("Disfruto buscando soluciones técnicas a problemas complejos", ["Calaf Industrial", "Nextrencher"]),
        ("Me apasiona la sostenibilidad y el futuro verde", ["DAGA", "Transparenta", "Ambitek"]),
        ("Me interesa la robótica, la visión artificial o el software", ["PICVISA Machine Vision Systems", "CICSA", "CIC3"])
    ],
    3: [
        ("La construcción de un puente o carretera", ["Calaf Constructora"]),
        ("El diseño de maquinaria industrial", ["Calaf Industrial", "Nextrencher"]),
        ("Un sistema de tratamiento de agua", ["DAGA", "Transparenta"]),
        ("Un sistema de separación automática de residuos con IA", ["PICVISA Machine Vision Systems", "CIC3"])
    ],
    4: [
        ("Estructura", ["Calaf Constructora"]),
        ("Ingeniería", ["Calaf Industrial"]),
        ("Innovación", ["PICVISA Machine Vision Systems", "CICSA"]),
        ("Medio ambiente", ["DAGA", "Ambitek"])
    ],
    5: [
        ("Ver resultados físicos de tu esfuerzo", ["Calaf Constructora"]),
        ("Resolver problemas técnicos complejos", ["Calaf Industrial"]),
        ("Participar en el desarrollo de nuevas tecnologías", ["PICVISA Machine Vision Systems", "CICSA"]),
        ("Mejorar el impacto ambiental", ["DAGA", "Transparenta"])
    ],
    6: [
        ("Administraciones públicas y constructoras", ["Calaf Constructora", "Calaf Trenching"]),
        ("Empresas industriales", ["Calaf Industrial", "Nextrencher"]),
        ("Ayuntamientos o empresas de aguas", ["DAGA", "Ambitek"]),
        ("Centros de reciclaje o laboratorios", ["PICVISA Machine Vision Systems", "CIC3"])
    ],
    7: [
        ("Coordinar una obra", ["Calaf Constructora"]),
        ("Diseñar piezas en CAD", ["Calaf Industrial", "Nextrencher"]),
        ("Programar sistemas automáticos", ["CICSA", "PICVISA Machine Vision Systems"]),
        ("Supervisar una planta de tratamiento", ["DAGA", "Transparenta"])
    ],
    8: [
        ("Construcción sostenible", ["Calaf Constructora", "Ambitek"]),
        ("Tecnología industrial", ["Calaf Industrial", "Nextrencher"]),
        ("Gestión de agua", ["DAGA", "Transparenta"]),
        ("Inteligencia artificial aplicada al reciclaje", ["PICVISA Machine Vision Systems", "CIC3"])
    ],
    9: [
        ("Jefe/a de obra", ["Calaf Constructora"]),
        ("Técnico/a de diseño y fabricación", ["Calaf Industrial"]),
        ("Ingeniero/a de automatización", ["CICSA", "CIC3"]),
        ("Especialista en medioambiente o I+D", ["Ambitek", "DAGA"])
    ],
    10: [
        ("Ingeniería civil o arquitectura técnica", ["Calaf Constructora", "Calaf Trenching"]),
        ("Ingeniería mecánica o eléctrica", ["Calaf Industrial", "Nextrencher"]),
        ("Ingeniería ambiental o química", ["DAGA", "Transparenta"]),
        ("Robótica, IA o visión artificial", ["PICVISA Machine Vision Systems", "CIC3"])
    ]
}

# Función para registrar la respuesta
def registrar_respuesta(numero_pregunta, respuesta):
    for texto, empresas in relaciones[numero_pregunta]:
        if respuesta == texto:
            for empresa in empresas:
                puntajes[empresa] += 1

# Pregunta 1
pregunta1 = st.radio(
    "¿Qué tipo de entorno laboral te atrae más?",
    ["Obra civil o edificación tradicional", 
     "Taller mecánico o planta de fabricación", 
     "Oficinas tecnológicas e innovación",
     "Espacios naturales o medioambientales"],index=None
)
registrar_respuesta(1, pregunta1)

# Pregunta 2
pregunta2 = st.radio(
    "¿Con qué frase te identificas más?",
    ["Me gusta ver cómo las cosas toman forma desde cero", 
     "Disfruto buscando soluciones técnicas a problemas complejos", 
     "Me apasiona la sostenibilidad y el futuro verde",
     "Me interesa la robótica, la visión artificial o el software"],index=None
)
registrar_respuesta(2, pregunta2)


# Pregunta 3
pregunta3 = st.radio(
    "¿Qué tipo de proyecto te ilusiona más liderar?",
    ["La construcción de un puente o carretera", 
     "El diseño de maquinaria industrial", 
     "Un sistema de tratamiento de agua",
     "Un sistema de separación automática de residuos con IA"],index=None
)
registrar_respuesta(3, pregunta3)

pregunta4 = st.radio(
    "¿Cuál de estas palabras te representa mejor?",
    ["Estructura","Ingeniería","Innovación","Medio ambiente"],index=None
)
registrar_respuesta(4, pregunta4)


pregunta5 = st.radio(
    "¿Qué te motiva más de un trabajo?",
    ["Ver resultados físicos de tu esfuerzo",
     "Resolver problemas técnicos complejos",
     "Participar en el desarrollo de nuevas tecnologías",
     "Mejorar el impacto ambiental"],index=None
)
registrar_respuesta(5, pregunta5)


pregunta6 = st.radio(
    "¿Con qué tipo de clientes te gustaría trabajar?",
    ["Administraciones públicas y constructoras",
     "Empresas industriales", 
     "Ayuntamientos o empresas de aguas",
     "Centros de reciclaje o laboratorios"],index=None
)
registrar_respuesta(6, pregunta6)


pregunta7 = st.radio(
    "¿Qué preferirías hacer un día normal de trabajo?",
    ["Coordinar una obra",
     "Diseñar piezas en CAD", 
     "Programar sistemas automáticos",
     "Supervisar una planta de tratamiento"],index=None
)
registrar_respuesta(7, pregunta7)


pregunta8 = st.radio(
    "¿Qué te parece más atractivo?",
    ["Construcción sostenible", 
     "Tecnología industrial",
     "Gestión de agua",
     "Inteligencia artificial aplicada al reciclaje"],index=None
)
registrar_respuesta(8, pregunta8)


pregunta9 = st.radio(
    "¿Cuál sería tu papel ideal?",
    ["Jefe/a de obra",
     "Técnico/a de diseño y fabricación",
     "Ingeniero/a de automatización",
     "Especialista en medioambiente o I+D"],index=None
)
registrar_respuesta(9, pregunta9)


pregunta10 = st.radio(
    "¿Qué tipo de formación o intereses tienes?",
    ["Ingeniería civil o arquitectura técnica",
     "Ingeniería mecánica o eléctrica",
     "Ingeniería ambiental o química",
     "Robótica, IA o visión artificial"],index=None
)
registrar_respuesta(10, pregunta10)


# Botón para enviar
if st.button("Enviar respuestas"):
    st.subheader("Resultado:")
    max_puntaje = max(puntajes.values())
    empresas_afines = [empresa for empresa, puntos in puntajes.items() if puntos == max_puntaje]

    for empresa in sorted(puntajes, key=puntajes.get, reverse=True):
        st.write(f"{empresa}: {puntajes[empresa]} puntos")

    st.markdown("### 🏆 Empresa(s) más afín(es):")
    for empresa in empresas_afines:
        st.success(empresa)

    if max_puntaje == 10:
        st.balloons()
