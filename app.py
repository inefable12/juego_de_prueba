import streamlit as st
import joblib
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
    return joblib.load("mimodelo.pkl")


modelo = cargar_modelo()

# --------------------------------------------------
# Interfaz
# --------------------------------------------------

st.title("🌸 Clasificador de flores Iris")

st.write(
    "Ingresa las características de una flor Iris "
    "para predecir su variedad."
)

st.markdown(
    """
    **Variables utilizadas por el modelo:**

    - `sepal.length`
    - `sepal.width`
    - `petal.length`
    - `petal.width`
    """
)

st.divider()

# --------------------------------------------------
# Entrada de datos
# --------------------------------------------------

st.subheader("Características de la flor")

col1, col2 = st.columns(2)

with col1:

    sepal_length = st.number_input(
        "sepal.length",
        min_value=0.0,
        max_value=10.0,
        value=5.1,
        step=0.1
    )

    sepal_width = st.number_input(
        "sepal.width",
        min_value=0.0,
        max_value=10.0,
        value=3.5,
        step=0.1
    )

with col2:

    petal_length = st.number_input(
        "petal.length",
        min_value=0.0,
        max_value=10.0,
        value=1.4,
        step=0.1
    )

    petal_width = st.number_input(
        "petal.width",
        min_value=0.0,
        max_value=10.0,
        value=0.2,
        step=0.1
    )

# --------------------------------------------------
# Predicción
# --------------------------------------------------

if st.button("🔮 Realizar predicción", type="primary"):

    # Crear matriz con el mismo orden de variables
    datos = np.array([[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]])

    # Realizar predicción
    prediccion = modelo.predict(datos)[0]

    st.divider()

    st.subheader("Resultado")

    st.success(
        f"🌸 Variedad predicha: **{prediccion}**"
    )

    # --------------------------------------------------
    # Probabilidades
    # --------------------------------------------------

    if hasattr(modelo, "predict_proba"):

        probabilidades = modelo.predict_proba(datos)[0]

        st.subheader("Probabilidad de predicción")

        # Obtener nombres de las clases directamente
        # desde el modelo
        if hasattr(modelo, "classes_"):

            clases = modelo.classes_

            for clase, probabilidad in zip(
                clases,
                probabilidades
            ):

                st.write(
                    f"**{clase}:** "
                    f"{probabilidad * 100:.2f}%"
                )

                st.progress(float(probabilidad))
