import streamlit as st
import random
import datetime
from gtts import gTTS
import streamlit as st

# Custom styled header
st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>
         MindCare AI
    </h1>
   
    """,
    unsafe_allow_html=True
)

# Intro section with columns
col1, col2 = st.columns([2,1])
with col1:
    st.write("### Welcome to MindCare AI")
    st.write("""
    MindCare AI is designed to support your mental health journey.
    Explore quizzes, remedies, mood tracking, reminders, and fun games —
    all in one place.
    """)
    st.write("👉 Use the sidebar to select an app.")
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/2920/2920244.png", width=150)

# Divider
st.markdown("---")

# Feature highlights
st.write("## ✨ Features")
colA, colB, colC = st.columns(3)
with colA:
    st.markdown("#### 🧠 Quiz\nAssess your mental health with interactive questions.")
with colB:
    st.markdown("#### 💊 Remedies\nGet helpful precautions and cures for common conditions.")
with colC:
    st.markdown("#### 🎨 Mood Tracker\nLog your mood and visualize your emotional journey.")

colD, colE = st.columns(2)
with colD:
    st.markdown("#### ⏰ Pill Reminder\nStay on track with your medication schedule.")
with colE:
    st.markdown("#### ✊🖐️✌️ Game\nPlay Stone–Paper–Scissors for a quick break.")

# Footer
st.markdown(
    """
    <hr>
    <p style='text-align: center; color: #777; font-size:14px;'>
        © 2026 MindCare AI | Built with Streamlit
    </p>
    """,
    unsafe_allow_html=True
)
# Sidebar menu
st.sidebar.title("📂 App Launcher")
choice = st.sidebar.radio(
    "Select an app:",
    ["Depression Quiz", "Health Remedies", "Mood Tracker", "Pill Reminder", "Stone-Paper-Scissors"]
)

# ------------------ Depression Quiz ------------------
if choice == "Depression Quiz":
    st.title("🧠 Mental Health Quiz")

    intro_text = """
    Welcome to the Mental Health Quiz!
    Mental health is a crucial aspect of overall well-being. It refers to our emotional,
    psychological, and social well-being, affecting how we think, feel, and act.
    This quiz aims to provide a general assessment of your mental well-being.
    Please answer each question honestly on a scale of 1 to 10.
    """
    st.write(intro_text)

    questions = {
        'q1': "On a scale of 1 to 10, how often have you been feeling down or depressed?",
        'q2': "On a scale of 1 to 10, how often do you get the feeling of being hopeless or worthless?",
        'q3': "On a scale of 1 to 10, how often do you have little interest or pleasure in doing things?",
        'q4': "On a scale of 1 to 10, how often have you had trouble sleeping?",
        'q5': "On a scale of 1 to 10, how often do you have very low/no energy?",
        'q6': "On a scale of 1 to 10, how often do you feel anxious or have excessive worry?",
        'q7': "On a scale of 1 to 10, how often do you have difficulty concentrating?",
        'q8': "On a scale of 1 to 10, how often do you feel restless or agitated?",
        'q9': "On a scale of 1 to 10, how often do you have thoughts of self-harm?",
        'q10': "On a scale of 1 to 10, how often do you experience changes in appetite?",
        'q11': "On a scale of 1 to 10, how often do you feel guilty or blame yourself?",
        'q12': "On a scale of 1 to 10, how often do you find it hard to enjoy with friends or family?",
        'q13': "On a scale of 1 to 10, how often do you have trouble with memory?",
        'q14': "On a scale of 1 to 10, how often do you experience physical symptoms without medical cause?",
        'q15': "On a scale of 1 to 10, how often do you fear social judgment?",
        'q16': "On a scale of 1 to 10, how often do you feel lonely or isolated?",
        'q17': "On a scale of 1 to 10, how often do you struggle with daily tasks?",
        'q18': "On a scale of 1 to 10, how often do you experience irritability or anger?",
        'q19': "On a scale of 1 to 10, how often do you withdraw from social interactions?",
        'q20': "On a scale of 1 to 10, how often do you have difficulty managing stress?",
    }

    answers = {key: st.slider(q, 0, 10, 0) for key, q in questions.items()}
    score = sum(answers.values())

    def categorize(score):
        if score <= 20:
            return "Congratulations you are healthy."
        elif score <= 40:
            return "Mild Depression. Regular exercise, healthy diet, light therapy, and pets can help."
        elif score <= 120:
            return "Moderate Depression. Seek social support, recreational activities, light therapy, and spiritual practices."
        elif score <= 160:
            return "Severe Depression. Cognitive behavioral therapy and behavioral activation therapy are recommended."
        else:
            return "Very Severe Depression. Professional help is strongly advised. Call 988 for immediate support."

    if st.button("Submit"):
        result = categorize(score)
        st.write(f"Your score: {score}")
        st.write(result)

        tts = gTTS(result)
        tts.save("result.mp3")
        with open("result.mp3", "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3")

# ------------------ Health Remedies ------------------
elif choice == "Health Remedies":
    st.title("💊 Health Remedies")

    element_info = {
        "cold": "PRECAUTIONS: Wash hands frequently, cover your mouth and nose when sneezing or coughing, stay hydrated.CURES: Get plenty of rest, drink fluids, and take over-the-counter cold medication.",
    "flu": "PRECAUTIONS: Get a flu shot, wash hands frequently, avoid close contact with sick people. CURES: Get plenty of rest, drink fluids, and take over-the-counter flu medication.",
    "headache": "PRECAUTIONS: Stay hydrated, manage stress, get regular sleep.CURES: Take over-the-counter pain relievers, rest in a quiet, dark room.",
    "gastroenteritis":"PRECAUTIONS: Practice good hand hygiene, avoid contaminated food or water, maintain food safety. CURES: Rehydration with oral rehydration solutions, bland diet.",
    "allergie": "PRECAUTIONS:  Identify and avoid allergens, use air purifiers, follow prescribed allergy management plans.CURES: Antihistamines, decongestants, or allergy shots (immunotherapy).",
    "cuts and scrapes":"PRECAUTIONS: Clean the wound, apply an antiseptic, cover with a bandage. CURES: Keep wounds clean, use protective gear, be cautious to prevent injuries.",
    "sunburn": "PRECAUTIONS: Use sunscreen, wear protective clothing, avoid prolonged sun exposure. CURES: Apply aloe vera or moisturizing cream, take pain relievers, stay hydrated.",
    "acne": "PRECAUTIONS: Maintain good skin hygiene, avoid squeezing pimples, use non-comedogenic skincare products.,CURES: Topical creams, oral medications, or professional treatments.",
    "toothache": "PRECAUTIONS: Maintain good oral hygiene, including regular brushing and flossing. CURES: Visit a dentist for diagnosis and treatment, which may include fillings, extractions, or root canals.",
    "sprains and strains": "PRECAUTIONS:  Warm-up before physical activity, use proper techniques, wear protective gear. CURES:  R.I.C.E. (Rest, Ice, Compression, Elevation) and physical therapy if needed.",
    "asthma": "PRECAUTIONS:  Identify triggers, avoid smoking, and follow an asthma action plan.CURES: Medications such as bronchodilators and inhaled corticosteroids.",
    "diarrhea": "PRECAUTIONS: Maintain food and water hygiene, avoid contaminated food.CURES: Rehydration with oral rehydration solutions and identifying and treating the underlying cause.",
    "constipation": "PRECAUTIONS: Maintain a high-fiber diet, stay hydrated, and be physically active. CURES: Dietary changes, increased fluid intake, over-the-counter laxatives.",
    "hypertension": "PRECAUTIONS: Maintain a healthy diet, exercise regularly, limit sodium intake, and manage stress.CURES: Lifestyle changes, antihypertensive medications.",
    "urinary tract infection": "PRECAUTIONS: Stay hydrated, urinate regularly, wipe front to back.CURES: Antibiotics by doctor.",
    "sinusitis": "PRECAUTIONS:  Use a humidifier, avoid irritants, manage allergies.CURES:  Decongestants, saline nasal rinses, antibiotics (if bacterial)",
    "back pain": "PRECAUTIONS: Maintain good posture, lift with your legs, exercise core muscles.CURES: Rest, hot/cold therapy, physical therapy.",
    "stress": "PRECAUTIONS: Practice relaxation techniques, exercise, seek support.CURES: Practice relaxation techniques, exercise, seek support.",
    "insomnia": "PRECAUTIONS: Maintain a regular sleep schedule, create a calming bedtime routine.CURES: Maintain a regular sleep schedule, create a calming bedtime routine.",
    "ear infections": "PRECAUTIONS: Avoid inserting objects in the ear, keep ears dry.CURES: Antibiotics (if bacterial), pain relievers, ear drops.",
    "skin rashes": "PRECAUTIONS:  Keep skin clean and dry, avoid irritants, protect from the sun.CURES: Topical creams, antihistamines, avoiding irritants.",
    "acid reflux": "PRECAUTIONS: Avoid trigger foods, eat smaller meals, raise the head of your bed.CURES: Medications prescribed by a doctor, lifestyle changes.",
    "migraine": "PRECAUTIONS: Identify triggers, manage stress, maintain a regular schedule.CURES: Medications prescribed by a doctor, rest in a quiet, dark room.",
    "diabetes": "PRECAUTIONS: Maintain a balanced diet, regular exercise, monitor blood sugar levels, and follow medical advice.CURES: Lifestyle changes, medications (oral or insulin).",
    "jaundice": "PRECAUTIONS: taking a lot of fluids like radish juice. CURES: natural sunlight.",
    "food poisoning": "PRECAUTIONS:  Practice food safety, proper cooking, and storage.CURES: Rest, hydration, and, in severe cases, medical attention.",
    "heartburn": "PRECAUTIONS: Avoid trigger foods, maintain a healthy weight. CURES: Antacids, H2 blockers, lifestyle changes.",
    "Insect Bites": "PRECAUTIONS:  Use insect repellent, wear protective clothing.CURES: Antihistamines,topical ointments.",
    "hay fever": "PRECAUTIONS: Avoid allergens, use antihistamines.CURES: Antihistamines, decongestants.",
    "conjunctivitis": "PRECAUTIONS: Good hand hygiene, avoid touching your eyes. CURES: Antibiotic eye drops (if bacterial), antihistamines (if allergic).",
    "athlete's foot": "PRECAUTIONS: Keep feet clean and dry, wear clean socks and shoes.CURES: Antifungal creams or powders.",
    "cough": "PRECAUTIONS: Good hygiene practices, avoid irritants. CURES: Cough drops, expectorants, antitussives.",
    "anxiety": "PRECAUTIONS: Practice stress-reduction techniques, seek therapy. CURES: Therapy, medications (if severe).",
    "depression": "PRECAUTIONS: Seek support, talk to a mental health professional.CURES: Therapy, medications.",
    "common warts": "PRECAUTIONS: Avoid contact with warts, keep hands clean.CURES: Over-the-counter treatments, cryotherapy, laser therapy.",
    "eczema": "PRECAUTIONS: Moisturize skin, avoid trigger irritants. CURES: Topical corticosteroids, antihistamines, moisturizers",
    "osteoarthritis": "PRECAUTIONS: Maintain a healthy weight, regular exercise. CURES:  Pain relievers, physical therapy, joint injections.",
    "tonsillitis": "PRECAUTIONS: Good hand hygiene, avoid close contact with infected individuals. CURES: Antibiotics (for bacterial tonsillitis), rest, pain relievers.",
    "bronchitis": "PRECAUTIONS: Avoid irritants, maintain good hygiene. CURES: Rest, hydration, cough medicine (if needed).",
    "pneumonia": "PRECAUTIONS: Get vaccinated, maintain good hygiene. CURES: Antibiotics, rest, oxygen therapy (in severe cases).",
    "gout": "PRECAUTIONS: Maintain a healthy diet, avoid trigger foods.CURES: Medications, lifestyle changes, diet modifications.",
    "anemia": "PRECAUTIONS: Eat a diet rich in iron and vitamins.CURES: Iron supplements, vitamin supplements, dietary changes.",
    "high cholesterol": "PRECAUTIONS: Maintain a healthy diet, regular exercise. CURES: Medications, lifestyle changes.",
    "Sunstroke": "PRECAUTIONS: Stay hydrated, avoid excessive heat CURES: Immediate cooling, medical attention.",
    "covid-19": "PRECAUTIONS: Follow public health guidelines, get vaccinated, and practice good hygiene.CURES:  Consult with healthcare professionals for personalized cancer treatment.",
    "typhoid": "PRECAUTIONS: Practice good hygiene, including frequent handwashing and consuming only safe, clean water and food.CURES: Typhoid can be treated with antibiotics prescribed by a healthcare professional; early diagnosis and treatment are essential.",
    "cancer": "PRECAUTIONS:  Maintain a healthy lifestyle with a balanced diet, regular exercise, and avoid exposure to carcinogens.CURES: Early detection and medical intervention offer the best chance for cancer treatment; consult a healthcare professional for personalized care.",
    "frostbite": "PRECAUTIONS:  Dress warmly, avoid prolonged exposure to extreme cold.CURES: Gradual rewarming, medical attention",
    "dogbite": "PRECAUTIONS: Avoid approaching unfamiliar dogs, especially when they seem agitated or frightened.CURES: Clean the wound with soap and water, apply an antiseptic, and seek immediate medical attention to prevent infection.",
    "motion sickness":"PRECAUTIONS:  Sit in a forward-facing seat while traveling to reduce motion sickness.CURES: Close your eyes, focus on the horizon, and take slow, deep breaths if you start feeling motion sick",
    }

    condition = st.selectbox("Select a condition:", list(element_info.keys()))
    info = element_info[condition]

    st.write("### Info")
    st.write(info)

    if st.button("Play Audio"):
        tts = gTTS(info)
        tts.save("remedy.mp3")
        with open("remedy.mp3", "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3")

# ------------------ Mood Tracker ------------------
elif choice == "Mood Tracker":
    st.title("🎨 Mood Tracker")

    mood = st.slider("Enter Mood (1-5)", 1, 5, 3)
    emojis = ["😢", "😞", "😐", "🙂", "😊"]
    emoji = emojis[mood-1]

    st.write("### Your Mood")
    st.write(f"{emoji}  {mood}/5")
    st.write("⭐" * mood)

# ------------------ Pill Reminder ------------------
elif choice == "Pill Reminder":
    st.title("⏰ Pill Reminder")

    if "last_taken" not in st.session_state:
        st.session_state.last_taken = None

    if st.button("Log Pill Taken"):
        st.session_state.last_taken = datetime.datetime.now()
        st.success("Pill logged!")

    if st.session_state.last_taken:
        st.write("Last taken:", st.session_state.last_taken)
        next_due = st.session_state.last_taken + datetime.timedelta(hours=8)
        st.write("Next due:", next_due)

        reminder_text = "It's time to take your pills. Open pocket one for pills."
        tts = gTTS(reminder_text)
        tts.save("pill.mp3")
        with open("pill.mp3", "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3")

# ------------------ Stone-Paper-Scissors ------------------
elif choice == "Stone-Paper-Scissors":
    st.title("✊🖐️✌️ Stone-Paper-Scissors")

    choices = ["stone", "paper", "scissors"]
    user_choice = st.radio("Choose:", choices)

    if st.button("Play"):
        computer_choice = random.choice(choices)
        st.write("Computer chose:", computer_choice)

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "stone" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "stone") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
        else:
            result = "Computer wins!"

        st.write(result)

        tts = gTTS(result)
        tts.save("game.mp3")
        with open("game.mp3", "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3")
