import streamlit as st
st.title("⚡EcoAprende🌱")

Progreso={"Energia Solar":{"Hecho": False, "Puntaje":0},
          "Energia Eolica":{"Hecho": False,"Puntaje":0},
          "Energia Hidraulica":{"Hecho": False,"Puntaje":0},
          "Energia por Biomasa":{"Hecho": False,"Puntaje":0},}
Juegos_totales:len(Progreso)

Juegos_completadas = sum(1 for data in progreso.values() if data["Hecho"])
    insignias = Juegos_completadas
Juegos_completas=sum(1 for data in progreso.values() if data["Hecho"])


