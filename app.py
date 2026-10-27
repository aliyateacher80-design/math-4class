import streamlit as st

# Беттің баптаулары
st.set_page_config(
    page_title="4-сынып Математика: Есептер жинағы",
    page_icon="🎒",
    layout="centered"
)

# Анимацияланған CSS дизайн және Жылтыраған жұлдыздар
st.markdown("""
<style>
    /* Негізгі фон анимациясы */
    .stApp {
        background: linear-gradient(-45deg, #e0c3fc, #8ec5fc, #e0c3fc, #fbc2eb);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Басты контейнер стилі */
    .main {
        background: rgba(255, 255, 255, 0.92);
        padding: 25px;
        border-radius: 25px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.12);
        backdrop-filter: blur(8px);
    }

    /* Анимациялы Инфографикалық Баннер */
    .hero-banner {
        position: relative;
        text-align: center;
        padding: 30px 20px;
        border-radius: 20px;
        background: linear-gradient(135deg, rgba(255,255,255,0.85) 0%, rgba(240,248,255,0.85) 100%);
        border: 3px solid #74b9ff;
        box-shadow: 0 10px 20px rgba(0,0,0,0.08);
        margin-bottom: 25px;
        animation: floatBanner 4s ease-in-out infinite;
        overflow: hidden;
    }

    @keyframes floatBanner {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-6px); }
        100% { transform: translateY(0px); }
    }

    /* Ұшып жүрген уақ жұлдыздар анимациясы */
    .floating-star {
        position: absolute;
        font-size: 1.2rem;
        animation: flyStar 3s ease-in-out infinite;
    }

    .star1 { top: 10%; left: 15%; animation-delay: 0s; }
    .star2 { top: 20%; right: 12%; animation-delay: 1s; }
    .star3 { bottom: 15%; left: 20%; animation-delay: 1.5s; }
    .star4 { bottom: 20%; right: 18%; animation-delay: 0.5s; }

    @keyframes flyStar {
        0% { transform: translateY(0px) scale(1) rotate(0deg); opacity: 0.5; }
        50% { transform: translateY(-12px) scale(1.3) rotate(180deg); opacity: 1; }
        100% { transform: translateY(0px) scale(1) rotate(360deg); opacity: 0.5; }
    }

    /* Деңгей бағандарының тақырыбы */
    .level-card-header {
        background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
        color: white;
        padding: 12px;
        border-radius: 12px 12px 0 0;
        text-align: center;
        font-size: 1.1rem;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    }

    /* Қанатты сөз бөлімі */
    .quote-box {
        background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
        padding: 15px;
        border-radius: 18px;
        text-align: center;
        font-weight: bold;
        color: #2d3436;
        margin-bottom: 25px;
        font-size: 1.1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }

    /* 3D Анимациялы Батырмалар */
    .stButton>button {
        border-radius: 20px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(255,107,107,0.3);
        background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);
        color: white;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        transform: scale(1.03) translateY(-2px);
        box-shadow: 0 6px 18px rgba(255,107,107,0.5);
    }
</style>
""", unsafe_allow_html=True)

# Жұлдыздары ұшып жүрген Pixar стиліндегі басты баннер
st.markdown("""
<div class="hero-banner">
    <div class="floating-star star1">🌟</div>
    <div class="floating-star star2">✨</div>
    <div class="floating-star star3">⭐</div>
    <div class="floating-star star4">💫</div>
    <h1 style="color: #0984e3; margin: 0; font-size: 2.4rem;">🎒 4-сынып Математика</h1>
    <p style="color: #636e72; font-size: 1.2rem; margin-top: 8px; font-weight: 600;">
        Интерактивті есептер жинағы 🌟
    </p>
    <p style="color: #e84393; font-size: 1rem; margin-top: 5px; font-weight: bold;">
        👩‍🏫 Дайындаған: Сұлтанова Мейрамгүл
    </p>
</div>
""", unsafe_allow_html=True)

# Жылтырайтын қанатты сөз
st.markdown("""
<div class="quote-box">
    ✨ «Математика – ақыл-ойды шынықтыратын, ойлауды жүйелейтін ғылым!» ✨
</div>
""", unsafe_allow_html=True)

# 🎬 ЖИ арқылы жасалған видеоны қоятын орын
st.markdown("### 🎬 ЖИ Видеосабақ & Таныстырылым")
st.info("💡 Ертең ЖИ арқылы жасалған видеоңызды осы жерге қоса аласыз (мысалы: st.video('url'))")
# st.video("СІЗДІҢ_ЖИ_ВИДЕО_СІЛТЕМЕСІ")

st.markdown("---")
st.markdown("### 📚 Деңгейлік тапсырмалар жинағы")

# Сессия күйін сақтау
if 'results_state' not in st.session_state:
    st.session_state.results_state = {}

# 3 деңгейді қатар орналастыру үшін Streamlit columns (бағандар) қолданамыз
col1, col2, col3 = st.columns(3)

# ================= I ДЕҢГЕЙ (Баған 1) =================
with col1:
    st.markdown('<div class="level-header" style="background: linear-gradient(135deg, #00b894, #55efc4);">🟢 I деңгей</div>', unsafe_allow_html=True)
    
    with st.expander("📌 1-тапсырма. Өлшем бірлік"):
        st.markdown("**Шарт:**\nа) 6 м² = ? дм²\nә) 5 м³ = ? см³\nб) 3 т = ? кг\nв) 2 сағ 30 мин = ? мин")
        btn_key = "task_1"
        if btn_key not in st.session_state.results_state: st.session_state.results_state[btn_key] = False
        if st.button("✨ Шешуі", key="btn_1"): st.session_state.results_state[btn_key] = not st.session_state.results_state[btn_key]
        if st.session_state.results_state[btn_key]:
            st.info("а) 600 дм²\nә) 5000 см³\nб) 3000 кг\nв) 150 мин")

    with st.expander("📌 2-тапсырма. Салыстыру"):
        st.markdown("**Шарт:**\nа) 350 см □ 3 м 5 см\nә) 2 т □ 1950 кг\nб) 4000 м² □ 40 ар\nв) 180 мин □ 3 сағ")
        btn_key = "task_2"
        if btn_key not in st.session_state.results_state: st.session_state.results_state[btn_key] = False
        if st.button("✨ Шешуі", key="btn_2"): st.session_state.results_state[btn_key] = not st.session_state.results_state[btn_key]
        if st.session_state.results_state[btn_key]:
            st.info("а) >\nә) >\nб) =\nв) =")

    with st.expander("📌 3-тапсырма. Уақыт"):
        st.markdown("**Шарт:**\nСаяхат 2 тәулік 8 сағ. Нақты сапар 72 сағ. Неше сағатқа ұзақ болды?")
        btn_key = "task_3"
        if btn_key not in st.session_state.results_state: st.session_state.results_state[btn_key] = False
        if st.button("✨ Шешуі", key="btn_3"): st.session_state.results_state[btn_key] = not st.session_state.results_state[btn_key]
        if st.session_state.results_state[btn_key]:
            st.info("Жоспар: 56 сағ.\nАйырмасы: 72 - 56 = **16 сағат**")

# ================= II ДЕҢГЕЙ (Баған 2) =================
with col2:
    st.markdown('<div class="level-header" style="background: linear-gradient(135deg, #fdcb6e, #ffeaa7); color: #2d3436;">🟡 II деңгей</div>', unsafe_allow_html=True)
    
    with st.expander("📌 4-тапсырма. Дүкен есебі"):
        st.markdown("**Шарт:**\n3 кг алма (1 кг - 850 тг) + 2 шырын (әрқ. 620 тг). 5000 тг берсе қанша қайтарылады?")
        btn_key = "task_4"
        if btn_key not in st.session_state.results_state: st.session_state.results_state[btn_key] = False
        if st.button("✨ Шешуі", key="btn_4"): st.session_state.results_state[btn_key] = not st.session_state.results_state[btn_key]
        if st.session_state.results_state[btn_key]:
            st.info("Барлығы: 3790 тг.\nҚайтарым: 5000 - 3790 = **1210 тг**")

    with st.expander("📌 5-тапсырма. Валюта"):
        st.markdown("**Шарт:**\n1 доллар = 6 рубль. 200 доллар неше рубль?")
        btn_key = "task_5"
        if btn_key not in st.session_state.results_state: st.session_state.results_state[btn_key] = False
        if st.button("✨ Шешуі", key="btn_5"): st.session_state.results_state[btn_key] = not st.session_state.results_state[btn_key]
        if st.session_state.results_state[btn_key]:
            st.info("200 × 6 = **1200 рубль**")

    with st.expander("📌 6-тапсырма. Төлем"):
        st.markdown("**Шарт:**\nАзық-түлікке 18 500 тг жұмсалып, 20 000 тг берілді. Қайтарым қанша?")
        btn_key = "task_6"
        if btn_key not in st.session_state.results_state: st.session_state.results_state[btn_key] = False
        if st.button("✨ Шешуі", key="btn_6"): st.session_state.results_state[btn_key] = not st.session_state.results_state[btn_key]
        if st.session_state.results_state[btn_key]:
            st.info("Қайтарым: 20000 - 18500 = **1500 теңге**")

# ================= III ДЕҢГЕЙ (Баған 3) =================
with col3:
    st.markdown('<div class="level-header" style="background: linear-gradient(135deg, #ff7675, #d63031);">🔴 III деңгей</div>', unsafe_allow_html=True)
    
    with st.expander("📌 7-тапсырма. Аудан"):
        st.markdown("**Шарт:**\nҰзындығы 50 м, ені 30 м бақшаның 1/4 бөлігіне көкөніс егілді. Ауданды армен тап.")
        btn_key = "task_7"
        if btn_key not in st.session_state.results_state: st.session_state.results_state[btn_key] = False
        if st.button("✨ Шешуі", key="btn_7"): st.session_state.results_state[btn_key] = not st.session_state.results_state[btn_key]
        if st.session_state.results_state[btn_key]:
            st.info("Толық аудан: 1500 м².\nТөрттен бірі: 375 м² = **3,75 ар**")

    with st.expander("📌 8-тапсырма. Логика"):
        st.markdown("**Шарт:**\n3 қорапта 84 қарындаш бар. 1-ші 2-шілктен 2 есе көп, 3-ші 2-шілктен 12 артық.")
        btn_key = "task_8"
        if btn_key not in st.session_state.results_state: st.session_state.results_state[btn_key] = False
        if st.button("✨ Шешуі", key="btn_8"): st.session_state.results_state[btn_key] = not st.session_state.results_state[btn_key]
        if st.session_state.results_state[btn_key]:
            st.info("Екінші қорапта: **18 қарындаш**")

    with st.expander("📌 9-тапсырма. Жеңілдік"):
        st.markdown("**Шарт:**\n40000 тг сөмкеге 10% жеңілдік жасалды + 2000 тг жеткізу. Барлығы қанша?")
        btn_key = "task_9"
        if btn_key not in st.session_state.results_state: st.session_state.results_state[btn_key] = False
        if st.button("✨ Шешуі", key="btn_9"): st.session_state.results_state[btn_key] = not st.session_state.results_state[btn_key]
        if st.session_state.results_state[btn_key]:
            st.info("Жеңілдетілген баға: 36000 тг.\nЖеткізумен: **38 000 теңге**")

# Ең астындағы 10-тапсырма (Тесттер) толық енге созылады
with st.expander("📌 10-тапсырма. Тест сұрақтары (Барлық деңгейді қорытындылау)"):
    st.markdown("""
    **Сұрақтар:**
    1. 480 санының 25%-ы нешеге тең? (A: 100, B: 120, C: 125, D: 140)
    2. Үшбұрыштың периметрі 36 см. Бір қабырғасы? (A: 9 см, B: 10 см, C: 12 см, D: 18 см)
    3. Қатарды жалғастыр: 3, 6, 12, 24, ... (A: 30, B: 36, C: 42, D: 48)
    4. Тауар 8000 тг, 10% жеңілдікпен жаңа бағасы? (A: 7200 тг, B: 7000 тг, C: 7800 тг, D: 7600 тг)
    5. Санды 4-ке көбейтіп, 8-ді қосқанда 32 шықты. Сан? (A: 4, B: 5, C: 6, D: 8)
    """)
    btn_key = "task_10"
    if btn_key not in st.session_state.results_state: st.session_state.results_state[btn_key] = False
    if st.button("✨ Тест жауаптарын көрсету", key="btn_10"): st.session_state.results_state[btn_key] = not st.session_state.results_state[btn_key]
    if st.session_state.results_state[btn_key]:
        st.info("1) B) 120\n2) C) 12 см\n3) D) 48\n4) A) 7200 тг\n5) C) 6")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #636e72;'>© 2026 4-сынып Математика платформасы | Авторы: Сұлтанова Мейрамгүл 🚀</p>", unsafe_allow_html=True)
