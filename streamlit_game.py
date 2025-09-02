import streamlit as st
import random

# Set the title
st.title("🎯 Guess the Number Game (1 to 100)")

# Initialize session state variables
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.max_attempts = 7
    st.session_state.game_over = False
    st.session_state.message = ""

# Display attempts
st.write(f"Attempts remaining: {st.session_state.max_attempts - st.session_state.attempts}")

# Input from user
if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess == st.session_state.number:
            st.session_state.message = f"✅ Correct! The number was {st.session_state.number}."
            st.session_state.game_over = True
        elif guess < st.session_state.number:
            st.session_state.message = "📉 Too low!"
        else:
            st.session_state.message = "📈 Too high!"

        # Check if out of attempts
        if st.session_state.attempts >= st.session_state.max_attempts and guess != st.session_state.number:
            st.session_state.message = f"❌ Out of attempts! The number was {st.session_state.number}."
            st.session_state.game_over = True

# Show message
if st.session_state.message:
    st.info(st.session_state.message)

# Restart game button
if st.session_state.game_over:
    if st.button("🔄 Play Again"):
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.message = ""
