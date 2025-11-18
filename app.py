import streamlit as st

st.set_page_config(
    page_title="EcoAprende",
    page_icon="🌱",
    layout="wide"
)

# ---------------------------
#      PROGRESO
# ---------------------------
progreso = {
    "Solar": {"completado": False, "puntaje": 0},
    "Eolica": {"completado": False, "puntaje": 0},
    "Hidraulica": {"completado": False, "puntaje": 0},
    "Biomasa": {"completado": False, "puntaje": 0},
}

# ---------------------------
#      DASHBOARD SIMPLE
# ---------------------------
def mostrar_dashboard():
    st.header("🌱 EcoAprende - Dashboard de Juegos")

    st.subheader("Selecciona un juego:")

    # Mostrar cada juego con ✔️ si ya está completo
    for juego, data in progreso.items():
        nombre_mostrar = f"{juego} {'✔️' if data['completado'] else ''}"
        if st.button(nombre_mostrar):
            st.session_state["pantalla"] = juego

# ---------------------------
#     JUEGO: SOLAR
# ---------------------------
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

# ---------------------------
#      MANEJO DE PANTALLAS
# ---------------------------
if "pantalla" not in st.session_state:
    st.session_state["pantalla"] = "dashboard"

if st.session_state["pantalla"] == "dashboard":
    mostrar_dashboard()

elif st.session_state["pantalla"] == "Solar":
    juego_solar()
