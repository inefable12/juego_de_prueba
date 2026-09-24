import streamlit as st
import pickle
import numpy as np

# --------------------------------------------------
# Configuración de la página
# --------------------------------------------------

st.set_page_config(
    page_title="Clasificador Iris",
    page_icon="🌸",
    layout="centered"
)

# --------------------------------------------------
# Cargar modelo
# --------------------------------------------------

@st.cache_resource
def cargar_modelo():
    with open("mimodelo.pkl", "rb") as archivo:
        modelo = pickle.load(archivo)
    return modelo

modelo = cargar_modelo()

# --------------------------------------------------
# Interfaz
# --------------------------------------------------

st.title("🌸 Clasificación de flores Iris")

st.write(
    "Ingresa las medidas de una flor Iris para predecir "
    "si pertenece a **Setosa, Versicolor o Virginica**."
)

st.subheader("Datos de la flor")

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input(
        "Longitud del sépalo (cm)",
        min_value=0.0,
        max_value=10.0,
        value=5.1,
        step=0.1
    )

    sepal_width = st.number_input(
        "Ancho del sépalo (cm)",
        min_value=0.0,
        max_value=10.0,
        value=3.5,
        step=0.1
    )

with col2:
    petal_length = st.number_input(
        "Longitud del pétalo (cm)",
        min_value=0.0,
        max_value=10.0,
        value=1.4,
        step=0.1
    )

    petal_width = st.number_input(
        "Ancho del pétalo (cm)",
        min_value=0.0,
        max_value=10.0,
        value=0.2,
        step=0.1
    )

# --------------------------------------------------
# Predicción
# --------------------------------------------------

if st.button("🔮 Realizar predicción", type="primary"):

    datos = np.array([[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]])

    prediccion = modelo.predict(datos)[0]

    # Si el modelo devuelve números 0, 1 y 2
    nombres = {
        0: "Setosa",
        1: "Versicolor",
        2: "Virginica"
    }

    especie = nombres.get(prediccion, str(prediccion))

    st.success(f"🌸 La especie predicha es: **{especie}**")

    # Mostrar probabilidades si el modelo las permite
    if hasattr(modelo, "predict_proba"):
        probabilidades = modelo.predict_proba(datos)[0]

        st.subheader("Probabilidad de cada clase")

        clases = getattr(
            modelo,
            "classes_",
            [0, 1, 2]
        )

        for clase, probabilidad in zip(clases, probabilidades):

            nombre = nombres.get(clase, str(clase))

            st.write(
                f"**{nombre}:** "
                f"{probabilidad * 100:.2f}%"
            )

            st.progress(float(probabilidad))
