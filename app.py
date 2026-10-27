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

    /* Деңгей тақырыптарының стилі */
    .level-header {
        background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
        color: white;
        padding: 12px 20px;
        border-radius: 15px;
        margin-top: 30px;
        margin-bottom: 20px;
        font-size: 1.3rem;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
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
st.info("💡 Ертең ЖИ арқылы жасалған видеоңызды осы жерге қоса аласыз.")
# st.video("СІЗДІҢ_ЖИ_ВИДЕО_СІЛТЕМЕСІ")

st.markdown("---")

# Сессия күйін сақтау
if 'results_state' not in st.session_state:
    st.session_state.results_state = {}

# ----------------- I ДЕҢГЕЙ -----------------
st.markdown('<div class="level-header" style="background: linear-gradient(135deg, #00b894, #55efc4);">🟢 I деңгей (Өлшем бірліктері, шамалар және уақыт)</div>', unsafe_allow_html=True)

tasks_level_1 = [
    {
        "id": 1,
        "title": "1-тапсырма. Өлшем бірліктерін түрлендір",
        "condition": "а) 6 м² = ? дм²  \nә) 5 м³ = ? см³  \nб) 3 т = ? кг  \nв) 2 сағ 30 мин = ? мин",
        "solution": "**📝 Толық шығарылу жолы:**\n• а) 1 м² = 100 дм² болғандықтан, 6 × 100 = **600 дм²**\n• ә) 1 м³ = 1 000 000 см³, бірақ 1 дм³ = 1000 см³. Есеп шартындағы әдеттегі мектеп бағдарламасы бойынша: 5 м³ = **5 000 000 см³** (немесе дм³ арқылы: 5 × 1000 = 5000 дм³)\n• б) 1 т = 1000 кг ➔ 3 × 1000 = **3000 кг**\n• в) 1 сағ = 60 мин ➔ 2 сағ = 120 мин, үстіне 30 мин қоссақ: 120 + 30 = **150 мин**\n\n🎉 **Жауабы:** а) 600 дм²; ә) 5 000 000 см³; б) 3000 кг; в) 150 минут."
    },
    {
        "id": 2,
        "title": "2-тапсырма. Шамаларды салыстыр",
        "condition": "Тиісті >, <, = таңбаларын қой:\nа) 350 см □ 3 м 5 см\nә) 2 т □ 1950 кг\nб) 4000 м² □ 40 ар\nв) 180 мин □ 3 сағ",
        "solution": "**📝 Толық шығарылу жолы:**\n• а) 3 м 5 см = 300 см + 5 см = 305 см. Салыстырамыз: 350 см > 305 см ➔ **350 см > 3 м 5 см**\n• ә) 2 т = 2000 кг. Салыстырамыз: 2000 кг > 1950 кг ➔ **2 т > 1950 кг**\n• б) 1 ар = 100 м². 40 ар = 40 × 100 = 4000 м². Салыстырамыз: **4000 м² = 40 ар**\n• в) 3 сағ = 3 × 60 мин = 180 мин. Салыстырамыз: **180 мин = 3 сағ**\n\n🎉 **Жауабы:** а) >; ә) >; б) =; в) =."
    },
    {
        "id": 3,
        "title": "3-тапсырма. Уақытты есепте",
        "condition": "Саяхат 2 тәулік 8 сағатқа жоспарланды. Нақты сапар 72 сағатқа созылды. Сапар жоспарланған уақыттан неше сағатқа ұзақ болды?",
        "solution": "**📝 Толық шығарылу жолы:**\n1) 1 тәулік = 24 сағат екенін білеміз.\n2) 2 тәулікті сағатқа айналдырамыз: 2 × 24 = 48 сағат.\n3) Жоспарланған жалпы уақыт: 48 сағат + 8 сағат = 56 сағат.\n4) Нақты сапар уақыты 72 сағат. Олардың айырмасын табамыз: 72 – 56 = 16 сағат.\n\n🎉 **Жауабы:** Сапар жоспарланған уақыттан **16 сағатқа** ұзақ болды."
    }
]

for task in tasks_level_1:
    with st.expander(f"📌 {task['title']}", expanded=False):
        st.markdown(f"**Есеп шарты:**\n\n{task['condition']}")
        btn_key = f"task_{task['id']}"
        if btn_key not in st.session_state.results_state:
            st.session_state.results_state[btn_key] = False
        if st.button(f"✨ Нәтижесін / Шығарылу жолын көрсету", key=f"btn_{task['id']}"):
            st.session_state.results_state[btn_key] = not st.session_state.results_state[btn_key]
        if st.session_state.results_state[btn_key]:
            st.info(task['solution'])


# ----------------- II ДЕҢГЕЙ -----------------
st.markdown('<div class="level-header" style="background: linear-gradient(135deg, #fdcb6e, #ffeaa7); color: #2d3436;">🟡 II деңгей (Дүкен, валюта және қаржылық есептер)</div>', unsafe_allow_html=True)

tasks_level_2 = [
    {
        "id": 4,
        "title": "4-тапсырма. Дүкендегі есеп",
        "condition": "Айдана 3 кг алма сатып алды. 1 кг алманың бағасы – 850 теңге. Ол тағы 2 шырын алды, әрқайсысы 620 теңге. Айдана кассаға 5000 теңге берсе, қанша теңге қайтарым алады?",
        "solution": "**📝 Толық шығарылу жолы:**\n1) Алманың жалпы құнын есептейміз: 3 кг × 850 теңге = 2550 теңге.\n2) Шырындардың жалпы құнын есептейміз: 2 дана × 620 теңге = 1240 теңге.\n3) Сатып алынған барлық заттардың құнын қосамыз: 2550 + 1240 = 3790 теңге.\n4) Кассадан қайтарылатын ақшаны табамыз: 5000 теңге – 3790 теңге = 1210 теңге.\n\n🎉 **Жауабы:** Айданаға **1210 теңге** қайтарылады."
    },
    {
        "id": 5,
        "title": "5-тапсырма. Валютаны есепте",
        "condition": "Шартты бағам бойынша 1 доллар = 6 рубль. 200 доллар неше рубль болады?",
        "solution": "**📝 Толық шығарылу жолы:**\n1 доллардың құны 6 рубль болса, 200 доллардың тең бағасын табу үшін көбейту амалын қолданамыз:\n200 × 6 = 1200 рубль.\n\n🎉 **Жауабы:** 200 доллар = **1200 рубль**."
    },
    {
        "id": 6,
        "title": "6-тапсырма. Төлемді жоспарла",
        "condition": "Отбасы азық-түлікке 18 500 теңге жұмсады. Олар 20 000 теңгелік банкнотпен төледі.\nа) Қанша теңге қайтарым алады?\nә) Егер қолдарында 20 000 теңгелік 1 банкнот, 10 000 теңгелік 2 банкнот және 2000 теңгелік 5 банкнот болса, барлығы неше теңге бар?",
        "solution": "**📝 Толық шығарылу жолы:**\n• а) Қайтарылатын ақшаны есептейміз: 20 000 – 18 500 = **1500 теңге**.\n• ә) Қолдағы бар ақшаларды жеке-жеке есептеп қосамыз:\n  - 20 000 теңгелік 1 банкнот = 1 × 20 000 = 20 000 теңге.\n  - 10 000 теңгелік 2 банкнот = 2 × 10 000 = 20 000 теңге.\n  - 2000 теңгелік 5 банкнот = 5 × 2000 = 10 000 теңге.\n  - Жалпы сомасы: 20 000 + 20 000 + 10 000 = 50 000 теңге.\n\n🎉 **Жауабы:** а) **1500 теңге** қайтарылады; ә) барлығы **50 000 теңге** бар."
    }
]

for task in tasks_level_2:
    with st.expander(f"📌 {task['title']}", expanded=False):
        st.markdown(f"**Есеп шарты:**\n\n{task['condition']}")
        btn_key = f"task_{task['id']}"
        if btn_key not in st.session_state.results_state:
            st.session_state.results_state[btn_key] = False
        if st.button(f"✨ Нәтижесін / Шығарылу жолын көрсету", key=f"btn_{task['id']}"):
            st.session_state.results_state[btn_key] = not st.session_state.results_state[btn_key]
        if st.session_state.results_state[btn_key]:
            st.info(task['solution'])


# ----------------- III ДЕҢГЕЙ -----------------
st.markdown('<div class="level-header" style="background: linear-gradient(135deg, #ff7675, #d63031);">🔴 III деңгей (Аудан, логика, пайыз және тесттер)</div>', unsafe_allow_html=True)

tasks_level_3 = [
    {
        "id": 7,
        "title": "7-тапсырма. Аудан және үлес",
        "condition": "Бақшаның ұзындығы 50 м, ені 30 м. Бақшаның төрттен бір бөлігіне көкөніс егілді. Көкөніс егілген жердің ауданын армен өрнектеңіз. (1 ар = 100 м²)",
        "solution": "**📝 Толық шығарылу жолы:**\n1) Бақшаның толық ауданын табамыз (Тіктөртбұрыштың ауданы S = a × b): 50 м × 30 м = 1500 м².\n2) Оның төрттен бір бөлігін (1/4) есептейміз: 1500 : 4 = 375 м².\n3) Шыққан мәнді арға айналдырамыз (1 ар = 100 м²): 375 : 100 = 3,75 ар.\n\n🎉 **Жауабы:** Көкөніс егілген жердің ауданы **3,75 ар**."
    },
    {
        "id": 8,
        "title": "8-тапсырма. Логикалық есеп",
        "condition": "Үш қорапта барлығы 84 қарындаш бар. Бірінші қораптағы қарындаш саны екінші қораптағыдан 2 есе көп, ал үшінші қорапта екінші қораптағыдан 12 қарындаш артық. Екінші қорапта неше қарындаш бар?",
        "solution": "**📝 Толық шығарылу жолы:**\n1) Екінші қораптағы қарындаш санын **x** деп белгілейміз.\n2) Онда бірінші қораптағы қарындаш саны – **2x**.\n3) Үшінші қораптағы қарындаш саны – **x + 12**.\n4) Барлығын қосып, теңдеу құрамыз: 2x + x + (x + 12) = 84\n5) Теңдеуді шешеміз: \n   4x + 12 = 84\n   4x = 84 – 12\n   4x = 72\n   x = 72 : 4\n   x = 18\n\n🎉 **Жауабы:** Екінші қорапта **18 қарындаш** бар."
    },
    {
        "id": 9,
        "title": "9-тапсырма. Пайыздық жеңілдік",
        "condition": "Сөмкенің бастапқы бағасы 40 000 теңге. Дүкенде оған 10% жеңілдік жасалды. Жеткізу құны 2000 теңге. Сөмкені жеткізумен бірге алу үшін барлығы қанша төлеу керек?",
        "solution": "**📝 Толық шығарылу жолы:**\n1) Сөмкеге жасалған 10% жеңілдік сомасын табамыз: (40 000 : 100) × 10 = 4000 теңге.\n2) Жеңілдетілгеннен кейінгі сөмке бағасы: 40 000 – 4000 = 36 000 теңге.\n3) Үстіне жеткізу құнын қосамыз: 36 000 + 2000 = 38 000 теңге.\n\n🎉 **Жауабы:** Барлығы **38 000 теңге** төлеу керек."
    },
    {
        "id": 10,
        "title": "10-тапсырма. Тест сұрақтары",
        "condition": """**Сұрақтар тізбегі:**
1. 480 санының 25%-ы нешеге тең?
   A) 100
   B) 120
   C) 125
   D) 140

2. Үшбұрыштың периметрі 36 см (қабырғалары өзара тең). Оның бір қабырғасы неге тең?
   A) 9 см
   B) 10 см
   C) 12 см
   D) 18 см

3. Сандар қатарын жалғастыр: 3, 6, 12, 24, ...
   A) 30
   B) 36
   C) 42
   D) 48

4. Тауардың бағасы 8000 теңге, 10% жеңілдікпен сатылса, жаңа бағасы қандай болады?
   A) 7200 тг
   B) 7000 тг
   C) 7800 тг
   D) 7600 тг

5. Белгісіз санды 4-ке көбейтіп, нәтижесіне 8-ді қосқанда 32 шықты. Бұл қай сан?
   A) 4
   B) 5
   C) 6
   D) 8""",
        "solution": """**📝 Тесттің толық шешу жолдары мен жауаптары:**
1) **B) 120** (Түсіндірме: 480 санының 25%-ы немесе төрттен бірі ➔ 480 : 4 = 120)
2) **C) 12 см** (Түсіндірме: Үш қабырғасы тең үшбұрыштың бір қабырғасын табу үшін периметрін 3-ке бөлеміз ➔ 36 : 3 = 12 см)
3) **D) 48** (Түсіндірме: Әрбір сан алдыңғы саннан 2 есе артық ➔ 24 × 2 = 48)
4) **A) 7200 тг** (Түсіндірме: 8000-ның 10%-ы 800 тг. Жаңа бағасы: 8000 – 800 = 7200 тг)
5) **C) 6** (Түсіндірме: Кері амал арқылы есептейміз: (32 – 8) : 4 = 24 : 4 = 6)"""
    }
]

for task in tasks_level_3:
    with st.expander(f"📌 {task['title']}", expanded=False):
        st.markdown(f"**Есеп шарты мен сұрақтар:**\n\n{task['condition']}")
        btn_key = f"task_{task['id']}"
        if btn_key not in st.session_state.results_state:
            st.session_state.results_state[btn_key] = False
        if st.button(f"✨ Нәтижесін / Шығарылу жолын көрсету", key=f"btn_{task['id']}"):
            st.session_state.results_state[btn_key] = not st.session_state.results_state[btn_key]
        if st.session_state.results_state[btn_key]:
            st.info(task['solution'])

st.markdown("---")
st.markdown("<p style='text-align: center; color: #636e72;'>© 2026 4-сынып Математика платформасы | Авторы: Сұлтанова Мейрамгүл 🚀</p>", unsafe_allow_html=True)
