import streamlit as st
st.title("⚡EcoAprende🌱")
progreso = {
    "Energia Solar": {"Hecho": False, "Puntaje": 0},
    "Energia Eolica": {"Hecho": False, "Puntaje": 0},
    "Energia Hidraulica": {"Hecho": False, "Puntaje": 0},
    "Energia por Biomasa": {"Hecho": False, "Puntaje": 0},}

Juegos_totales = len(progreso)

def mostrar_dashboard():
    """Pantalla Principal: Dashboard del Jugador."""

    Juegos_completados = sum(1 for data in progreso.values() if data["Hecho"])

    st.header("EcoAprende - Dashboard")
    st.write(f"Progreso general: {Juegos_completados} / {Juegos_totales} Juegos")

    st.subheader("Juegos disponibles:")

    for juego in progreso.keys():
        if st.button(juego):
            st.session_state["pantalla_actual"] = juego





