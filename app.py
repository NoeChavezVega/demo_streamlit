import streamlit as st

st.set_page_config(
    page_title="EcoAprende",
    page_icon="🌱",
    layout="wide"
)

progreso = {
    "Solar": {"completado": False, "puntaje": 0},
    "Eolica": {"completado": False, "puntaje": 0},
    "Hidraulica": {"completado": False, "puntaje": 0},
    "Biomasa": {"completado": False, "puntaje": 0},
}

total_juegos = len(progreso)

def mostrar_dashboard():
    st.header("🌱 EcoAprende - Dashboard de Juegos")

    juegos_completados = sum(1 for data in progreso.values() if data["completado"])
    st.write(f"Progreso general: **{juegos_completados}/{total_juegos}** juegos completados")

    st.subheader("Selecciona un juego:")

    for juego in progreso.keys():
        if st.button(juego):
            st.session_state["pantalla"] = juego

#Energia solar
def juego_solar():
    st.title("🌞 Juego: Energía Solar")

    st.write("Responde las preguntas para ganar puntos:")

    p1 = st.radio(
        "¿Qué energía solar genera electricidad?",
        ["Solar Térmica", "Solar Fotovoltaica", "Solar Geotérmica"]
    )

    p2 = st.radio(
        "¿Cuál es el principal beneficio ambiental?",
        ["Genera pocos residuos", "Reduce CO2", "Funciona de noche"]
    )

    if st.button("Enviar respuestas"):
        puntaje = 0
        if p1 == "Solar Fotovoltaica":
            puntaje += 5
        if p2 == "Reduce CO2":
            puntaje += 5

        progreso["Solar"]["completado"] = True
        progreso["Solar"]["puntaje"] = puntaje

        st.success(f"Juego completado. Ganaste {puntaje} puntos.")
        st.balloons()

        if st.button("Volver al Dashboard"):
            st.session_state["pantalla"] = "dashboard"

if "pantalla" not in st.session_state:
    st.session_state["pantalla"] = "dashboard"

if st.session_state["pantalla"] == "dashboard":
    mostrar_dashboard()

elif st.session_state["pantalla"] == "Solar":
    juego_solar()






