import streamlit as st
import time

# -------------------------------
# APP TITLE AND INTRO
# -------------------------------
st.set_page_config(page_title="Healthy Lungs Breathing App", page_icon="🌬️", layout="centered")

st.title("🌬️ Healthy Lungs Breathing App")
st.markdown("""
Breathe deeply and calmly to strengthen your lungs and relax your mind.  
This app guides you through **inhale–hold–exhale** cycles and includes a simple **breath-hold test**.
""")

st.divider()

# -------------------------------
# SECTION 1: BREATH HOLD TEST
# -------------------------------
st.header("❤️ Lung Capacity Check (Breath-Hold Test)")
st.write("Try holding your breath as long as you can to see your lung strength!")

if "start_time" not in st.session_state:
    st.session_state.start_time = None

col1, col2 = st.columns(2)

# Placeholders for progress bar and messages
progress_placeholder = st.empty()
message = st.empty()
timer_placeholder = st.empty()

with col1:
    if st.button("Start Test"):
        st.session_state.start_time = time.time()
        st.success("🌬️ Timer started! Hold your breath... and click Stop when you exhale.")
        st.session_state.stop_test = False

        for second in range(41):  # progress for up to 40 seconds
            if st.session_state.start_time is None or st.session_state.stop_test:
                break

            timer_placeholder.markdown(f"⏱️ **Time:** {second} sec")

            # Determine color based on time
            if second < 10:
                color = "red"
                msg = "🔥 Great start! Focus and stay calm."
            elif second < 20:
                color = "orange"
                msg = "💪 Doing great! Keep it steady."
            elif second < 30:
                color = "blue"
                msg = "🌊 Excellent control! You’re doing really well."
            else:
                color = "green"
                msg = "🌟 Amazing! You’re almost at full lung strength!"

            # Create color-changing progress bar using HTML
            progress_html = f"""
            <div style='width: 100%; background-color: lightgray; border-radius: 10px;'>
                <div style='width: {(second/40)*100}%;
                             background-color: {color};
                             height: 25px;
                             border-radius: 10px;'>
                </div>
            </div>
            """
            progress_placeholder.markdown(progress_html, unsafe_allow_html=True)
            message.markdown(f"**{msg}**")

            time.sleep(1)

with col2:
    if st.button("Stop Test"):
        if st.session_state.start_time:
            st.session_state.stop_test = True
            duration = time.time() - st.session_state.start_time
            st.session_state.start_time = None
            st.info(f"⏱️ You held your breath for **{duration:.1f} seconds!**")

            # Lung health feedback
            if duration >= 40:
                st.success("🌟 Excellent lung strength!")
            elif duration >= 25:
                st.warning("😊 Good! Keep practicing deep breathing.")
            else:
                st.error("🌱 Below average — try daily breathing exercises to improve.")
        else:
            st.warning("You need to start the test first!")

st.divider()

# -------------------------------
# SECTION 2: BREATHING CYCLE
# -------------------------------
st.header("🧘 Guided Breathing Exercise")

col1, col2 = st.columns(2)
with col1:
    inhale = st.number_input("Inhale time (seconds)", min_value=2, max_value=10, value=4)
    hold = st.number_input("Hold time (seconds)", min_value=2, max_value=10, value=7)
with col2:
    exhale = st.number_input("Exhale time (seconds)", min_value=2, max_value=10, value=8)
    cycles = st.slider("Number of cycles", min_value=1, max_value=10, value=3)

start_breathe = st.button("🌿 Start Breathing")

if start_breathe:
    st.write("Follow the guide below 👇")
    breathe_placeholder = st.empty()
    progress = st.progress(0)
    total_time = (inhale + hold + exhale) * cycles
    step = 100 / total_time
    count = 0

    for i in range(cycles):
        # INHALE
        breathe_placeholder.markdown(f"### 🌬️ Inhale – {inhale} seconds")
        for s in range(inhale):
            progress.progress(min(int(count * step), 100))
            time.sleep(1)
            count += 1

        # HOLD
        breathe_placeholder.markdown(f"### ✋ Hold – {hold} seconds")
        for s in range(hold):
            progress.progress(min(int(count * step), 100))
            time.sleep(1)
            count += 1

        # EXHALE
        breathe_placeholder.markdown(f"### 😮‍💨 Exhale – {exhale} seconds")
        for s in range(exhale):
            progress.progress(min(int(count * step), 100))
            time.sleep(1)
            count += 1

        breathe_placeholder.markdown("---")

    breathe_placeholder.markdown("### 💚 Breathing session complete! Great job!")
    st.balloons()

st.divider()

# -------------------------------
# FOOTER DISCLAIMER
# -------------------------------
st.markdown("""
> ⚠️ **Disclaimer:**  
> This app is for relaxation and general wellness awareness only.  
> It is **not a medical test**. For any health concerns, please consult a healthcare professional.
""")

