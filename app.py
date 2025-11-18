import streamlit as st
st.title("⚡EcoAprende🌱")

Progreso={"Energia Solar":{"Echo": False, "Puntaje":0},
          "Energia Eolica":{"Echo": False,"Puntaje":0},
          "Energia Hidraulica":{"Echo": False,"Puntaje":0},
          "Energia por Biomasa":{"Echo": False,"Puntaje":0},}
Lecciones_totales:len(Progreso)
def mostrar_dashboard():
    """Pantalla Principal: Dashboard del Estudiante."""
    st.header("🌱 EcoAprende: Tu Aventura Ecológica")
