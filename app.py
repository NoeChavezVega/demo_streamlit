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

    for juego, data in progreso.items():
        nombre = f"{juego} {'✔️' if data['completado'] else ''}"

        # SOLO Solar está habilitado
        if juego == "Solar":
            if st.button(nombre, use_container_width=True):
                st.session_state["pantalla"] = juego
                st.rerun()
        else:
            st.button(nombre, disabled=True, use_container_width=True)

# ---------------------------
#     JUEGO: SOLAR
# ---------------------------
def juego_solar():
    st.title("🌞 Juego: Energía Solar")

    p1 = st.radio(
        "¿Qué energía solar genera electricidad?",
        ["Solar Térmica", "Solar Fotovoltaica", "Solar Geotérmica"]
    )

    p2 = st.radio(
        "¿Cuál es el principal beneficio ambiental?",
        ["Genera pocos residuos", "Reduce CO2", "Funciona de noche"]
    )

    if st.button("Enviar respuestas ✔️"):
        puntaje = 0
        if p1 == "Solar Fotovoltaica":
            puntaje += 5
        if p2 == "Reduce CO2":
            puntaje += 5

        progreso["Solar"]["completado"] = True
        progreso["Solar"]["puntaje"] = puntaje

        st.success(f"Juego completado. Ganaste {puntaje} puntos.")
        st.balloons()

        st.session_state["pantalla"] = "dashboard"
        st.rerun()

    if st.button("⬅️ Volver al Dashboard"):
        st.session_state["pantalla"] = "dashboard"
        st.rerun()

# ---------------------------
#      MANEJO DE PANTALLAS
# ---------------------------
if "pantalla" not in st.session_state:
    st.session_state["pantalla"] = "dashboard"

pantalla = st.session_state["pantalla"]

if pantalla == "dashboard":
    mostrar_dashboard()
elif pantalla == "Solar":
    juego_solar()

