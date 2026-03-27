import streamlit as st
import random
import datetime
from gtts import gTTS

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
        "cold": "PRECAUTIONS: Wash hands frequently, cover mouth when sneezing. CURES: Rest, fluids.",
        "flu": "PRECAUTIONS: Get flu shot, avoid sick people. CURES: Rest, fluids.",
        "headache": "PRECAUTIONS: Stay hydrated, manage stress. CURES: Pain relievers, rest.",
        "stress": "PRECAUTIONS: Practice relaxation. CURES: Exercise, support.",
        # Add your full dictionary here
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