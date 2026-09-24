import random
import streamlit as st

# ---------------------------------------------------------
# CONFIGURACIÓN
# ---------------------------------------------------------
st.set_page_config(
    page_title="Disney Villains Trivia",
    page_icon="🖤",
    layout="centered",
)

# ---------------------------------------------------------
# ESTILOS
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Poppins:wght@400;600;700&display=swap');

    .stApp {
        background:
            radial-gradient(circle at top, #35145c 0%, #160d2c 40%, #080711 100%);
        color: white;
    }

    .main-title {
        font-family: 'Cinzel', serif;
        text-align: center;
        font-size: 3rem;
        font-weight: 900;
        color: #f6d365;
        text-shadow:
            0 0 10px #8a2be2,
            0 0 25px #8a2be2;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        color: #ddd0ef;
        font-family: 'Poppins', sans-serif;
        font-size: 1.05rem;
        margin-bottom: 30px;
    }

    .question-card {
        background: rgba(20, 13, 40, 0.92);
        border: 1px solid #8b5cf6;
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 0 25px rgba(139, 92, 246, 0.25);
    }

    .question-number {
        color: #f6d365;
        font-weight: bold;
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .question {
        font-family: 'Cinzel', serif;
        font-size: 1.45rem;
        font-weight: 700;
        margin-top: 8px;
    }

    .result-box {
        background: linear-gradient(135deg, #5b21b6, #be185d);
        border-radius: 25px;
        padding: 35px;
        text-align: center;
        box-shadow: 0 0 40px rgba(236, 72, 153, 0.45);
    }

    .result-title {
        font-family: 'Cinzel', serif;
        font-size: 2.5rem;
        color: #ffe08a;
    }

    .result-score {
        font-size: 1.5rem;
        font-weight: bold;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        border: 1px solid #a78bfa;
        background: linear-gradient(90deg, #6d28d9, #9333ea);
        color: white;
        font-weight: 700;
        padding: 12px;
        transition: 0.2s;
    }

    div.stButton > button:hover {
        border-color: #f6d365;
        box-shadow: 0 0 15px rgba(246, 211, 101, 0.5);
        transform: scale(1.01);
    }

    .footer {
        text-align: center;
        color: #8f83a8;
        margin-top: 35px;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# BANCO DE PREGUNTAS
# ---------------------------------------------------------
QUESTIONS = [
    {
        "question": "¿Qué villana desea robar la voz de Ariel?",
        "options": [
            "Úrsula",
            "Maléfica",
            "Cruella de Vil",
            "La Reina Malvada",
        ],
        "answer": "Úrsula",
    },
    {
        "question": "¿Qué villana quiere convertir a los cachorros dálmatas en un abrigo?",
        "options": [
            "Madame Medusa",
            "Cruella de Vil",
            "Úrsula",
            "Lady Tremaine",
        ],
        "answer": "Cruella de Vil",
    },
    {
        "question": "¿Quién lanza una maldición sobre la princesa Aurora?",
        "options": [
            "Maléfica",
            "Yzma",
            "La Reina de Corazones",
            "Gothel",
        ],
        "answer": "Maléfica",
    },
    {
        "question": "¿Qué villana quiere mantenerse joven utilizando la magia del cabello de Rapunzel?",
        "options": [
            "Madame Medusa",
            "Lady Tremaine",
            "Madre Gothel",
            "Cruella de Vil",
        ],
        "answer": "Madre Gothel",
    },
    {
        "question": "¿Quién gobierna Wonderland y ordena constantemente que le corten la cabeza a sus súbditos?",
        "options": [
            "La Reina Malvada",
            "La Reina de Corazones",
            "Maléfica",
            "Úrsula",
        ],
        "answer": "La Reina de Corazones",
    },
]


# ---------------------------------------------------------
# INICIALIZACIÓN DEL JUEGO
# ---------------------------------------------------------
def initialize_game():
    # Copiamos las preguntas para no modificar el banco original
    questions = [q.copy() for q in QUESTIONS]

    # Orden aleatorio de preguntas
    random.shuffle(questions)

    # Orden aleatorio de alternativas
    for q in questions:
        q["options"] = q["options"].copy()
        random.shuffle(q["options"])

    st.session_state.questions = questions
    st.session_state.answers = {}
    st.session_state.finished = False


if "questions" not in st.session_state:
    initialize_game()


# ---------------------------------------------------------
# CABECERA
# ---------------------------------------------------------
st.markdown(
    '<div class="main-title">🖤 Disney Villains Trivia 🖤</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">¿Cuánto sabes sobre las villanas más icónicas de Disney?</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# TRIVIA
# ---------------------------------------------------------
if not st.session_state.finished:

    for i, q in enumerate(st.session_state.questions):

        st.markdown(
            f"""
            <div class="question-card">
                <div class="question-number">
                    Pregunta {i + 1} de 5
                </div>
                <div class="question">
                    {q["question"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        selected = st.radio(
            "Selecciona una respuesta:",
            q["options"],
            key=f"question_{i}",
            index=None,
            label_visibility="collapsed",
        )

        st.session_state.answers[i] = selected

    st.write("")

    if st.button("✨ TERMINAR TRIVIA ✨"):

        unanswered = [
            i for i in range(5)
            if st.session_state.answers.get(i) is None
        ]

        if unanswered:
            st.warning(
                f"⚠️ Aún te faltan {len(unanswered)} pregunta(s) por responder."
            )
        else:
            st.session_state.finished = True
            st.rerun()


# ---------------------------------------------------------
# RESULTADO
# ---------------------------------------------------------
else:

    score = 0

    for i, q in enumerate(st.session_state.questions):
        if st.session_state.answers[i] == q["answer"]:
            score += 1

    if score == 5:

        st.balloons()

        st.markdown(
            """
            <div class="result-box">
                <div class="result-title">
                    👑 ¡PERFECTO! 👑
                </div>
                <div class="result-score">
                    Has conseguido 5 de 5 respuestas correctas.
                </div>
                <p>
                    Las villanas de Disney estarían orgullosas... o
                    probablemente planeando su venganza. 🖤✨
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Segunda animación después de un pequeño efecto visual
        st.snow()

    else:

        st.markdown(
            f"""
            <div class="result-box">
                <div class="result-title">
                    🖤 Resultado 🖤
                </div>
                <div class="result-score">
                    Has conseguido {score} de 5.
                </div>
                <p>
                    ¡Casi lo tienes! Vuelve a intentarlo y demuestra
                    que eres una verdadera experta en villanas Disney.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")
        st.subheader("🔮 Revisa tus respuestas")

        for i, q in enumerate(st.session_state.questions):

            user_answer = st.session_state.answers[i]

            if user_answer == q["answer"]:
                st.success(
                    f"Pregunta {i + 1}: ✅ {user_answer}"
                )
            else:
                st.error(
                    f"Pregunta {i + 1}: ❌ Tu respuesta: "
                    f"{user_answer} | Correcta: {q['answer']}"
                )

    st.write("")

    if st.button("🔄 JUGAR DE NUEVO"):

        initialize_game()
        st.rerun()


st.markdown(
    '<div class="footer">Disney Villains Trivia • Hecho con Streamlit 🖤</div>',
    unsafe_allow_html=True
)
