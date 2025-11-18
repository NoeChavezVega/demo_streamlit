import streamlit as st

st.title("EcoAprende 🌱")

# ---------------------------
# PROGRESO DE LOS JUEGOS
# ---------------------------
progreso = {
    "Solar": {"completado": False, "puntaje": 0},
    "Eolica": {"completado": False, "puntaje": 0},
    "Hidraulica": {"completado": False, "puntaje": 0},
    "Biomasa": {"completado": False, "puntaje": 0},
}

# ---------------------------
# DASHBOARD + JUEGOS
# ---------------------------
st.header("🌱 EcoAprende - Juegos Educativos")
st.subheader("Selecciona un juego para abrirlo:")

# -------- JUEGO SOLAR --------
with st.expander("🌞 Energía Solar"):
    st.write("Responde las preguntas:")

    p1 = st.radio(
        "¿Qué energía solar genera electricidad?",
        ["Solar Térmica", "Solar Fotovoltaica", "Solar Geotérmica"],
        key="p1_solar"
    )

    p2 = st.radio(
        "¿Cuál es el principal beneficio ambiental?",
        ["Genera pocos residuos", "Reduce CO2", "Funciona de noche"],
        key="p2_solar"
    )

    if st.button("Enviar respuestas ✔️", key="enviar_solar"):
        puntaje = 0

        if p1 == "Solar Fotovoltaica":
            puntaje += 5

        if p2 == "Reduce CO2":
            puntaje += 5

        progreso["Solar"]["completado"] = True
        progreso["Solar"]["puntaje"] = puntaje

        st.success(f"Juego completado. Ganaste {puntaje} puntos 🎉")
        st.balloons()

# -------- JUEGOS BLOQUEADOS --------
st.info("Los siguientes juegos estarán disponibles pronto:")

st.button("💨 Energía Eólica (bloqueado)", disabled=True)
st.button("💧 Energía Hidráulica (bloqueado)", disabled=True)
st.button("🌿 Biomasa (bloqueado)", disabled=True)
