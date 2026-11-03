import streamlit as st
import os

# Беттің баптаулары
st.set_page_config(
    page_title="ЗЕРДЕVERSE: Жасанды интеллект пен математика әлемі",
    page_icon="🧠",
    layout="centered"
)

# Анимацияланған CSS дизайн
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(-45deg, #1e3c72, #2a5298, #0f2027, #203a43);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
        color: #ffffff;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .main {
        background: rgba(15, 23, 42, 0.85);
        padding: 25px;
        border-radius: 25px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
    }
    .hero-banner {
        position: relative;
        text-align: center;
        padding: 30px 20px;
        border-radius: 20px;
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 2px solid #38bdf8;
        box-shadow: 0 10px 25px rgba(56, 189, 248, 0.2);
        margin-bottom: 25px;
    }
    .level-header {
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
        color: white;
        padding: 12px 20px;
        border-radius: 15px;
        margin-top: 30px;
        margin-bottom: 20px;
        font-size: 1.3rem;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    .quote-box {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #38bdf8;
        padding: 15px;
        border-radius: 18px;
        text-align: center;
        font-weight: bold;
        color: #e2e8f0;
        margin-bottom: 25px;
        font-size: 1.1rem;
    }
    .stButton>button {
        border-radius: 20px;
        font-weight: bold;
        background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%);
        color: white;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# Баннер
st.markdown("""
<div class="hero-banner">
    <h1 style="color: #38bdf8; margin: 0; font-size: 2.5rem; letter-spacing: 2px;">ЗЕРДЕVERSE</h1>
    <p style="color: #f1f5f9; font-size: 1.2rem; margin-top: 8px; font-weight: 600;">
        Жасанды интеллект пен математика әлемі
    </p>
    <p style="color: #94a3b8; font-size: 1rem; margin-top: 5px; font-weight: 500;">
        Математика пәнінен жасанды интеллект арқылы оқушылардың функционалдық сауаттылығын дамыту
    </p>
    <p style="color: #38bdf8; font-size: 1.05rem; margin-top: 10px; font-weight: bold;">
        👩‍🏫 Автор: Сұлтанова М.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="quote-box">
    🚀 🧠 Ойлан • Есепте • Талда • Өмірде қолдан! 💡
</div>
""", unsafe_allow_html=True)

# Видеоларды қауіпсіз шығару функциясы
def safe_video(path):
    if os.path.exists(path):
        st.video(path)
    else:
        st.warning(f"⚠️ `{path}` файлы серверде табылмады. 'videos' папкасын және видеоларды GitHub-қа жүктегеніңізге көз жеткізіңіз.")

st.markdown("### 🎬 ЖИ Видеосабақтар & Таныстырылымдар")

st.markdown("#### 🎒 Сабаққа кіріспе және есептер")
col1, col2 = st.columns(2)
with col1:
    safe_video("videos/1.mp4")
    safe_video("videos/3.mp4")
    safe_video("videos/5.mp4")
with col2:
    safe_video("videos/2.mp4")
    safe_video("videos/4.mp4")
    safe_video("videos/6.mp4")

st.markdown("#### 🏆 Қорытынды және марапаттау")
safe_video("videos/7.mp4")

st.markdown("---")

if 'results_state' not in st.session_state:
    st.session_state.results_state = {}

# =====================================================================
# 1-БӨЛІМ: БАСТЫ ДЕҢГЕЙЛІК ТАПСЫРМАЛАР (Өлшем бірліктері, қаржы, логика)
# =====================================================================

# ----------------- I ДЕҢГЕЙ -----------------
st.markdown('<div class="level-header" style="background: linear-gradient(135deg, #059669, #10b981);">🟢 I деңгей (Өлшем бірліктері, шамалар және уақыт)</div>', unsafe_allow_html=True)

tasks_level_1 = [
    {
        "id": 1,
        "title": "1-тапсырма. Өлшем бірліктерін түрлендір",
        "condition": "а) 6 м² = ? дм² \nә) 5 м³ = ? см³ \nб) 3 т = ? кг \nв) 2 сағ 30 мин = ? мин",
        "solution": "**📝 Толық шығарылу жолы:**\n• а) 1 м² = 100 дм² болғандықтан, 6 × 100 = **600 дм²**\n• ә) 1 м³ = 1 000 000 см³\n• б) 1 т = 1000 кг ➔ 3 × 1000 = **3000 кг**\n• в) 1 сағ = 60 мин ➔ 2 сағ = 120 мин, үстіне 30 мин қоссақ: **150 мин**\n\n🎉 **Жауабы:** а) 600 дм²; ә) 5 000 000 см³; б) 3000 кг; в) 150 минут."
    },
    {
        "id": 2,
        "title": "2-тапсырма. Шамаларды салыстыр",
        "condition": "Тиісті >, <, = таңбаларын қой:\nа) 350 см □ 3 м 5 см\nә) 2 т □ 1950 кг\nб) 4000 м² □ 40 ар\nв) 180 мин □ 3 сағ",
        "solution": "**📝 Толық шығарылу жолы:**\n• а) 350 см > 305 см\n• ә) 2000 кг > 1950 кг\n• б) 4000 м² = 40 ар\n• в) 180 мин = 3 сағ\n\n🎉 **Жауабы:** а) >; ә) >; б) =; в) =."
    },
    {
        "id": 3,
        "title": "3-тапсырма. Уақытты есепте",
        "condition": "Саяхат 2 тәулік 8 сағатқа жоспарланды. Нақты сапар 72 сағатқа созылды. Сапар жоспарланған уақыттан неше сағатқа ұзақ болды?",
        "solution": "**📝 Толық шығарылу жолы:**\n1) 2 тәулік = 48 сағат. Жоспарланған уақыт: 48 + 8 = 56 сағат.\n2) 72 – 56 = 16 сағат.\n\n🎉 **Жауабы:** Сапар жоспарланған уақыттан **16 сағатқа** ұзақ болды."
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
st.markdown('<div class="level-header" style="background: linear-gradient(135deg, #d97706, #f59e0b);">🟡 II деңгей (Дүкен, валюта және қаржылық есептер)</div>', unsafe_allow_html=True)

tasks_level_2 = [
    {
        "id": 4,
        "title": "4-тапсырма. Дүкендегі есеп",
        "condition": "Айдана 3 кг алма сатып алды (1 кг – 850 тг) және 2 шырын алды (әрқайсысы 620 тг). Кассаға 5000 теңге берсе, қанша теңге қайтарым алады?",
        "solution": "**📝 Толық шығарылу жолы:**\n1) 3 × 850 = 2550 тг (алма).\n2) 2 × 620 = 1240 тг (шырын).\n3) 2550 + 1240 = 3790 тг (барлығы).\n4) 5000 – 3790 = 1210 тг.\n\n🎉 **Жауабы:** **1210 теңге** қайтарылады."
    },
    {
        "id": 5,
        "title": "5-тапсырма. Валютаны есепте",
        "condition": "Шартты бағам бойынша 1 доллар = 6 рубль. 200 доллар неше рубль болады?",
        "solution": "**📝 Толық шығарылу жолы:** 200 × 6 = 1200 рубль.\n\n🎉 **Жауабы:** **1200 рубль**."
    },
    {
        "id": 6,
        "title": "6-тапсырма. Төлемді жоспарла",
        "condition": "Отбасы азық-түлікке 18 500 теңге жұмсады, 20 000 теңгелік банкнотпен төледі. Қанша қайтарым алады?",
        "solution": "**📝 Толық шығарылу жолы:** 20 000 – 18 500 = 1500 тг.\n\n🎉 **Жауабы:** **1500 теңге** қайтарылады."
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
st.markdown('<div class="level-header" style="background: linear-gradient(135deg, #dc2626, #ef4444);">🔴 III деңгей (Аудан, логика, пайыз және тесттер)</div>', unsafe_allow_html=True)

tasks_level_3 = [
    {
        "id": 7,
        "title": "7-тапсырма. Аудан және үлес",
        "condition": "Бақшаның ұзындығы 50 м, ені 30 м. Төрттен бір бөлігіне көкөніс егілді. Ауданын армен өрнектеңіз.",
        "solution": "**📝 Толық шығарылу жолы:**\n1) 50 × 30 = 1500 м².\n2) 1500 : 4 = 375 м².\n3) 375 : 100 = 3,75 ар.\n\n🎉 **Жауабы:** **3,75 ар**."
    },
    {
        "id": 8,
        "title": "8-тапсырма. Логикалық есеп",
        "condition": "Үш қорапта 84 қарындаш бар. 1-ші қорапта 2-шіге қарағанда 2 есе көп, 3-шіде 2-шіге қарағанда 12 қарындаш артық. 2-ші қорапта неше қарындаш бар?",
        "solution": "**📝 Толық шығарылу жолы:** 2x + x + (x + 12) = 84 ➔ 4x = 72 ➔ x = 18.\n\n🎉 **Жауабы:** **18 қарындаш**."
    },
    {
        "id": 9,
        "title": "9-тапсырма. Пайыздық жеңілдік",
        "condition": "Сөмкенің бастапқы бағасы 40 000 теңге, 10% жеңілдік жасалды. Жеткізу құны 2000 теңге. Барлығы қанша төлеу керек?",
        "solution": "**📝 Толық шығарылу жолы:** (40000 : 100) × 10 = 4000 тг жеңілдік. 36000 + 2000 = 38000 тг.\n\n🎉 **Жауабы:** **38 000 теңге**."
    }
]

for task in tasks_level_3:
    with st.expander(f"📌 {task['title']}", expanded=False):
        st.markdown(f"**Есеп шарты:**\n\n{task['condition']}")
        btn_key = f"task_{task['id']}"
        if btn_key not in st.session_state.results_state:
            st.session_state.results_state[btn_key] = False
        if st.button(f"✨ Нәтижесін / Шығарылу жолын көрсету", key=f"btn_{task['id']}"):
            st.session_state.results_state[btn_key] = not st.session_state.results_state[btn_key]
        if st.session_state.results_state[btn_key]:
            st.info(task['solution'])


# =====================================================================
# 2-БӨЛІМ: ҚОСЫМША ТАПСЫРМАЛАР ТІЗБЕСІ
# =====================================================================

topics = [
    {
        "title": "Нөлдермен аяқталатын көптаңбалы сандарды жазбаша бөлу",
        "levels": [
            {
                "level_name": "🟢 1-деңгей. Базалық деңгей – қарапайым есептер",
                "color": "#059669",
                "tasks": [
                    {
                        "id": 101,
                        "title": "Тапсырма. Бөлуді орында",
                        "condition": "• 840 : 2 = ?\n• 960 : 3 = ?\n• 4800 : 4 = ?\n• 6300 : 7 = ?\n• 9600 : 30 = ?",
                        "solution": "**📝 Толық шығарылу жолы мен жауабы:**\n• 840 : 2 = **420**\n• 960 : 3 = **320**\n• 4800 : 4 = **1200**\n• 6300 : 7 = **900**\n• 9600 : 30 = **320**"
                    }
                ]
            },
            {
                "level_name": "🟡 2-деңгей. Орта деңгей – өмірмен байланысты есептер",
                "color": "#d97706",
                "tasks": [
                    {
                        "id": 102,
                        "title": "Тапсырма. Есепті шығар",
                        "condition": "Мектепке 12 600 дәптер әкелінді. Дәптерлерді 30 сыныпқа тең бөліп берді. Әр сынып неше дәптерден алды?",
                        "solution": "**📝 Толық шығарылу жолы:**\n12 600 : 30 = 420 (дәптер).\n\n🎉 **Жауабы:** әр сынып **420 дәптерден** алды."
                    }
                ]
            },
            {
                "level_name": "🔴 3-деңгей. Жоғары деңгей – талдау, логика",
                "color": "#dc2626",
                "tasks": [
                    {
                        "id": 103,
                        "title": "Тапсырма. Заңдылықты анықта",
                        "condition": "Бірінші өрнектің мәні 240-қа тең. Келесі өрнектердің бөліндісін тап:\n• 4800 : 20 = ?\n• 9600 : 40 = ?\n• 14 400 : 60 = ?\n• 19 200 : 80 = ?\n\nБарлық өрнектердегі заңдылықты түсіндір.",
                        "solution": "**📝 Толық шығарылу жолы:**\n• 4800 : 20 = 240\n• 9600 : 40 = 240\n• 14 400 : 60 = 240\n• 19 200 : 80 = 240\n\n💡 **Заңдылық:** бөлінгіш пен бөлгіш бірдей есе артқандықтан, бөлінді өзгермейді."
                    }
                ]
            }
        ]
    },
    {
        "title": "Көптаңбалы сандарды жазбаша бөлу",
        "levels": [
            {
                "level_name": "🟢 1-деңгей. Базалық деңгей – қарапайым есептер",
                "color": "#059669",
                "tasks": [
                    {
                        "id": 201,
                        "title": "Тапсырма. Бөлуді орында",
                        "condition": "• 864 : 4 = ?\n• 936 : 3 = ?\n• 848 : 8 = ?\n• 975 : 5 = ?\n• 3276 : 6 = ?",
                        "solution": "**📝 Толық шығарылу жолы мен жауабы:**\n• 864 : 4 = **216**\n• 936 : 3 = **312**\n• 848 : 8 = **106**\n• 975 : 5 = **195**\n• 3276 : 6 = **546**"
                    }
                ]
            },
            {
                "level_name": "🟡 2-деңгей. Орта деңгей – өмірмен байланысты есептер",
                "color": "#d97706",
                "tasks": [
                    {
                        "id": 202,
                        "title": "Тапсырма. Есепті шығар",
                        "condition": "Фермер 6480 кг картоп жинады. Ол картопты әрқайсысына 24 кг-нан салатындай қаптарға бөлді. Фермерге барлығы неше қап қажет болды?",
                        "solution": "**📝 Толық шығарылу жолы:**\n6480 : 24 = 270 (қап).\n\n🎉 **Жауабы:** **270 қап** қажет болды."
                    }
                ]
            },
            {
                "level_name": "🔴 3-деңгей. Жоғары деңгей – талдау, логика",
                "color": "#dc2626",
                "tasks": [
                    {
                        "id": 203,
                        "title": "Тапсырма. Ойлан, тап!",
                        "condition": "Үш оқушы бірдей санды әртүрлі сандарға бөлді:\n• Бірінші оқушы: 8640 : 24\n• Екінші оқушы: 8640 : 12\n• Үшінші оқушы: 8640 : 48\n1. Әр оқушының жауабын тап.\n2. Ең үлкен бөлінді қай оқушыда шықты?\n3. Бөлгіш артқан сайын бөлінді қалай өзгеретінін түсіндір.",
                        "solution": "**📝 Толық шығарылу жолы:**\n• 8640 : 24 = 360\n• 8640 : 12 = 720\n• 8640 : 48 = 180\n\n🥇 **Ең үлкен бөлінді** екінші оқушыда шықты (720).\n\n💡 **Қорытынды:** бөлінгіш өзгермеген жағдайда бөлгіш артса, бөлінді кемиді."
                    }
                ]
            }
        ]
    },
    {
        "title": "Екі таңбалы санға жазбаша бөлу",
        "levels": [
            {
                "level_name": "🟢 1-деңгей. Базалық деңгей – қарапайым есептер",
                "color": "#059669",
                "tasks": [
                    {
                        "id": 301,
                        "title": "Тапсырма. Бөлуді орында",
                        "condition": "• 360 : 12 = ?\n• 560 : 14 = ?\n• 720 : 24 = ?\n• 840 : 21 = ?\n• 3456 : 16 = ?",
                        "solution": "**📝 Толық шығарылу жолы мен жауабы:**\n• 360 : 12 = **30**\n• 560 : 14 = **40**\n• 720 : 24 = **30**\n• 840 : 21 = **40**\n• 3456 : 16 = **216**"
                    }
                ]
            },
            {
                "level_name": "🟡 2-деңгей. Орта деңгей – өмірмен байланысты есептер",
                "color": "#d97706",
                "tasks": [
                    {
                        "id": 302,
                        "title": "Тапсырма. Есепті шығар",
                        "condition": "Мектепке 5376 дәптер әкелінді. Дәптерлер 32 сыныпқа тең бөлініп берілді. Әр сынып неше дәптерден алды?",
                        "solution": "**📝 Толық шығарылу жолы:**\n5376 : 32 = 168 (дәптер).\n\n🎉 **Жауабы:** әр сынып **168 дәптерден** алды."
                    }
                ]
            },
            {
                "level_name": "🔴 3-деңгей. Жоғары деңгей – талдау, логика",
                "color": "#dc2626",
                "tasks": [
                    {
                        "id": 303,
                        "title": "Тапсырма. Қатені тап!",
                        "condition": "Оқушы төмендегі бөлуді орындады: 4752 : 24 = 208\n1. Оқушының жауабы дұрыс па?\n2. Бөлуді тексеру арқылы қатені анықта.\n3. Дұрыс жауабын жаз.",
                        "solution": "**📝 Толық шығарылу жолы:**\nОқушының жауабы қате.\n• **Тексеру:** 208 × 24 = 4992 (4992 ≠ 4752).\n• **Дұрыс шешуі:** 4752 : 24 = 198.\n• **Тексеру:** 198 × 24 = 4752.\n\n🎉 **Жауабы:** Дұрыс мәні **198**."
                    }
                ]
            }
        ]
    },
    {
        "title": "Өнімділік. Үш таңбалы санға жазбаша көбейту және бөлу алгоритмдері",
        "levels": [
            {
                "level_name": "🟢 1-деңгей. Базалық деңгей – қарапайым есептер",
                "color": "#059669",
                "tasks": [
                    {
                        "id": 401,
                        "title": "Тапсырма. Амалдарды орында",
                        "condition": "• 124 × 3 = ?\n• 213 × 4 = ?\n• 125 × 6 = ?\n• 636 : 3 = ?\n• 848 : 4 = ?\n• 936 : 3 = ?",
                        "solution": "**📝 Толық шығарылу жолы мен жауабы:**\n• 124 × 3 = **372**\n• 213 × 4 = **852**\n• 125 × 6 = **750**\n• 636 : 3 = **212**\n• 848 : 4 = **212**\n• 936 : 3 = **312**"
                    }
                ]
            },
            {
                "level_name": "🟡 2-деңгей. Орта деңгей – өмірмен байланысты есептер",
                "color": "#d97706",
                "tasks": [
                    {
                        "id": 402,
                        "title": "Тапсырма. Есепті шығар",
                        "condition": "Наубайханада бір сағатта 125 бөлке нан пісіріледі. Наубайхана 8 сағат жұмыс істеді. Дайындалған барлық нанды әр қорапқа 25 бөлкеден салды. Барлығы неше қорап қажет болды?",
                        "solution": "**📝 Толық шығарылу жолы:**\n1) 125 × 8 = 1000 (бөлке нан).\n2) 1000 : 25 = 40 (қорап).\n\n🎉 **Жауабы:** **40 қорап** қажет болды."
                    }
                ]
            },
            {
                "level_name": "🔴 3-деңгей. Жоғары деңгей – талдау, логика",
                "color": "#dc2626",
                "tasks": [
                    {
                        "id": 403,
                        "title": "Тапсырма. Ойлан, есепте!",
                        "condition": "Екі жұмысшы бірдей уақыт жұмыс істеді. Бірінші жұмысшы сағатына 125 бөлшек, ал екінші жұмысшы сағатына 115 бөлшек дайындайды. Олар 6 сағат бірге жұмыс істеді.\n1. Әр жұмысшы 6 сағатта неше бөлшектен дайындайды?\n2. Екеуі барлығы неше бөлшек дайындайды?\n3. Бірінші жұмысшы екінші жұмысшыдан қанша бөлшек артық дайындады?\n4. Егер барлық дайындалған бөлшектерді 40-тан қораптарға салса, неше қорап қажет болады?",
                        "solution": "**📝 Толық шығарылу жолы:**\n1) Бірінші жұмысшы: 125 × 6 = 750 (бөлшек).\n2) Екінші жұмысшы: 115 × 6 = 690 (бөлшек).\n3) Барлығы: 750 + 690 = 1440 (бөлшек).\n4) Айырмасы: 750 – 690 = 60 (бөлшек).\n5) Қорап саны: 1440 : 40 = 36 (қорап).\n\n🎉 **Жауабы:** Екі жұмысшы барлығы 1440 бөлшек дайындады. Бірінші жұмысшы 60 бөлшек артық дайындады. Барлығы **36 қорап** қажет."
                    }
                ]
            }
        ]
    }
]

# Тақырыптар мен деңгейлерді экранға шығару
for topic in topics:
    st.markdown(f"## 📚 {topic['title']}")
    for level in topic['levels']:
        st.markdown(f'<div class="level-header" style="background: linear-gradient(135deg, {level["color"]}, {level["color"]}dd);">{level["level_name"]}</div>', unsafe_allow_html=True)
        for task in level['tasks']:
            with st.expander(f"📌 {task['title']}", expanded=False):
                st.markdown(f"**Есеп шарты:**\n\n{task['condition']}")
                btn_key = f"task_{task['id']}"
                if btn_key not in st.session_state.results_state:
                    st.session_state.results_state[btn_key] = False
                if st.button(f"✨ Нәтижесін / Шығарылу жолын көрсету", key=f"btn_{task['id']}"):
                    st.session_state.results_state[btn_key] = not st.session_state.results_state[btn_key]
                if st.session_state.results_state[btn_key]:
                    st.info(task['solution'])

st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8;'>© 2026 ЗЕРДЕVERSE платформасы | Авторы: Сұлтанова М. 🚀</p>", unsafe_allow_html=True)
