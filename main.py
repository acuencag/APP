# archivo: mini_test.py

import streamlit as st
from collections import defaultdict

st.image("logo1.png", width=150)

st.title("Qüestionari: Quina empresa del Grup Calaf encaixa més amb tu?")

st.write("Respon les preguntes següents:")


# Diccionario para puntajes
puntajes = defaultdict(int)

# Mapas de relación entre respuestas y empresas
relaciones = {
    1: [
        ("Edificació residencial o pública", ["Calaf Constructora", "Serom"]),
        ("Obra civil i urbanitzacions", ["Calaf Constructora", "Serom"]),
        ("Instal·lació de xarxes de serveis bàsics ", ["Calaf Trenching"]),
        ("Tractament i gestió d’aigües", ["DAGA", "Transparenta"]),
        ("Automatització de processos industrials", ["Calaf Industrial"])
    ],
    2: [
        ("Projectes de construcció d’habitatges", ["Calaf Constructora", "Serom"]),
        ("Sectors d’energia i sostenibilitat", ["PICVISA"]),
        ("Tecnologia d'automatització i indústria", ["Calaf Industrial", "PICVISA"]),
        ("Gestió de residus i reciclatge innovador", ["PICVISA"]),
        ("Producció i distribució de materials de construcció", ["Pemacsa"])
    ],
    3: [
        ("Constructora gran amb projectes d’infraestructures", ["Calaf Constructora","Serom"]),
        ("Empresa de tecnologia aplicada a processos industrials", ["Calaf Industrial", "PICVISA"]),
        ("Especialistes en medi ambient i tractament d’aigües", ["DAGA", "Transparenta"]),
        ("Empresa de gestió i subministrament de materials per a obrae", ["Pemacsa"])
    ],

    4: [
        ("Liderar obres de construcció en obra civil", ["Serom","Calaf Constructora"]),
        ("Desenvolupar nous sistemes d’automatització ", ["Calaf Industrial"]),
        ("Innovar en la separació òptica de materials", ["PICVISA"]),
        ("Participar en la gestió sostenible de l'aigua", ["DAGA", "Transparenta"])
    ],
    5: [
        ("Obra exterior i moviment de terres", ["Calaf Trenching"]),
        ("Oficines tècniques d’enginyeria i projectes", ["Calaf Industrial","DAGA"]),
        ("Laboratoris de recerca i desenvolupament", ["PICVISA"]),
        ("Entorns comercials de materials i equipaments", ["Pemacsa"])
    ],
    6: [
        ("Participar en l'execució d'una obra important", ["Calaf Constructora", "Serom"]),
        ("Formar part d'un equip d'innovació tecnològica ", ["Calaf Industrial", "PICVISA"]),
        ("Desenvolupar solucions per a la gestió d'aigua sostenible", ["DAGA", "Transparenta"]),
        ("Gestionar projectes de promoció residencial", ["Calaf Constructora", "Serom"])
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
    "En quin tipus de projecte t'agradaria començar a treballar?",
    ["Edificació residencial o pública", 
     "Obra civil i urbanitzacions", 
     "Instal·lació de xarxes de serveis bàsics",
     "Tractament i gestió d’aigües",
     "Automatització de processos industrials"],index=None
)
registrar_respuesta(1, pregunta1)

# Pregunta 2
pregunta2 = st.radio(
    "Quin àmbit creus que pot impulsar més la teva carrera professional inicial?",
    ["Projectes de construcció d’habitatges", 
     "Sectors d’energia i sostenibilitat", 
     "Tecnologia d'automatització i indústria",
     "Gestió de residus i reciclatge innovador",
     "Producció i distribució de materials de construcció"],index=None
)
registrar_respuesta(2, pregunta2)


# Pregunta 3
pregunta3 = st.radio(
    "A quin tipus d'empresa t’agradaria per fer pràctiques o començar la teva primera feina?",
    ["Constructora gran amb projectes d’infraestructures", 
     "Empresa de tecnologia aplicada a processos industrials", 
     "Especialistes en medi ambient i tractament d’aigües",
     "Empresa de gestió i subministrament de materials per a obra"],index=None
)
registrar_respuesta(3, pregunta3)

pregunta4 = st.radio(
    "Quin repte t’interessa més per començar la teva trajectòria?",
    ["Liderar obres de construcció en obra civil",
     "Desenvolupar nous sistemes d’automatització",
     "Innovar en la separació òptica de materials",
     "Participar en la gestió sostenible de l'aigua"],index=None
)
registrar_respuesta(4, pregunta4)


pregunta5 = st.radio(
    "En quin entorn de treball et veus creixent?",
    ["Obra exterior i moviment de terres",
     "Oficines tècniques d’enginyeria i projectes",
     "Laboratoris de recerca i desenvolupament",
     "Entorns comercials de materials i equipaments"],index=None
)
registrar_respuesta(5, pregunta5)


pregunta6 = st.radio(
    "Quin objectiu professional a curt termini t'agradaria assolir?",
    ["Participar en l'execució d'una obra important",
     "Formar part d'un equip d'innovació tecnològica", 
     "Desenvolupar solucions per a la gestió d'aigua sostenible",
     "Gestionar projectes de promoció residencial"],index=None
)
registrar_respuesta(6, pregunta6)



# Botón para enviar
if st.button("Enviar respostes"):
    st.subheader("Resultat:")
    max_puntaje = max(puntajes.values())
    empresas_afines = [empresa for empresa, puntos in puntajes.items() if puntos == max_puntaje]

    for empresa in sorted(puntajes, key=puntajes.get, reverse=True):
        st.write(f"{empresa}: {puntajes[empresa]} punts")

    st.markdown("### 🏆 Empresa(s) més afí(ns):")
    for empresa in empresas_afines:
        st.success(empresa)

    if max_puntaje == 10:
        st.balloons()
