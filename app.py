import streamlit as st

# Page configuration
st.set_page_config(page_title="Mari-Length", layout="wide")

# Initialize session state
if "game_running" not in st.session_state:
    st.session_state.game_running = False
if "wavelength_revealed" not in st.session_state:
    st.session_state.wavelength_revealed = False
if "category" not in st.session_state:
    st.session_state.category = ""
if "extreme_left" not in st.session_state:
    st.session_state.extreme_left = ""
if "extreme_right" not in st.session_state:
    st.session_state.extreme_right = ""
if "wavelength_position" not in st.session_state:
    st.session_state.wavelength_position = 50
if "guesses" not in st.session_state:
    st.session_state.guesses = []
if "current_guesser" not in st.session_state:
    st.session_state.current_guesser = ""

st.title("🌊 Mari-Length")

# Game Setup Section
st.header("Game Setup")
col1, col2, col3 = st.columns(3)

with col1:
    category = st.text_input(
        "Category/Message",
        value=st.session_state.category,
        help="e.g., 'clothes-warmth', 'intelligence', 'flavor'"
    )
    st.session_state.category = category

with col2:
    extreme_left = st.text_input(
        "Left Extreme",
        value=st.session_state.extreme_left,
        help="e.g., 'cold', 'stupid', 'bland'"
    )
    st.session_state.extreme_left = extreme_left

with col3:
    extreme_right = st.text_input(
        "Right Extreme",
        value=st.session_state.extreme_right,
        help="e.g., 'hot', 'genius', 'spicy'"
    )
    st.session_state.extreme_right = extreme_right

col1, col2 = st.columns(2)
with col1:
    wavelength_position = st.slider(
        "Wavelength Position (Answer)",
        min_value=0,
        max_value=100,
        value=st.session_state.wavelength_position,
        help="Where is the correct answer on the spectrum?"
    )
    st.session_state.wavelength_position = wavelength_position

with col2:
    current_guesser = st.text_input(
        "Current Guesser Name",
        value=st.session_state.current_guesser,
        placeholder="Enter player name"
    )
    st.session_state.current_guesser = current_guesser

# Game Control Buttons
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🎮 Start Round"):
        if category and extreme_left and extreme_right:
            st.session_state.game_running = True
            st.session_state.wavelength_revealed = False
            st.session_state.guesses = []
            st.success("Round started! Other players, look away! 👀")
        else:
            st.error("Please fill in all setup fields")

with col2:
    if st.button("🚨 REVEAL WAVELENGTH"):
        if st.session_state.game_running:
            st.session_state.wavelength_revealed = True
        else:
            st.warning("Please start a round first")

with col3:
    if st.button("🔄 Reset Game"):
        st.session_state.game_running = False
        st.session_state.wavelength_revealed = False
        st.session_state.category = ""
        st.session_state.extreme_left = ""
        st.session_state.extreme_right = ""
        st.session_state.wavelength_position = 50
        st.session_state.guesses = []
        st.session_state.current_guesser = ""
        st.rerun()

# Game Display
st.divider()

if st.session_state.game_running:
    st.header(f"Category: {st.session_state.category}")
    
    if not st.session_state.wavelength_revealed:
        # Hidden wavelength phase
        st.info("🙈 **Wavelength is hidden!** Other players, look away! One player will make a guess when ready.")
        st.warning("Click 'REVEAL WAVELENGTH' when the guesser is ready!")
    else:
        # Show the wavelength spectrum
        st.subheader("📊 The Spectrum")
        
        # Create the spectrum visualization
        col1, col2, col3 = st.columns([1, 4, 1])
        
        with col1:
            st.markdown(f"### {st.session_state.extreme_left}")
        
        with col2:
            # Create progress bar visualization
            st.markdown("---")
            
            # Display the spectrum with the wavelength
            spectrum_html = f"""
            <div style="margin: 20px 0;">
                <div style="background: linear-gradient(to right, #FF6B6B, #FFD93D, #6BCB77); 
                            height: 40px; 
                            border-radius: 10px; 
                            position: relative;
                            border: 2px solid #333;">
                    <div style="position: absolute; 
                                left: {st.session_state.wavelength_position}%; 
                                top: -10px; 
                                width: 30px; 
                                height: 60px; 
                                background: #333; 
                                border-radius: 5px;
                                transform: translateX(-50%);
                                box-shadow: 0 0 15px rgba(0,0,0,0.5);">
                    </div>
                </div>
                <div style="text-align: center; margin-top: 30px; font-size: 18px; color: #666;">
                    ← {st.session_state.wavelength_position}% → {100 - st.session_state.wavelength_position}% →
                </div>
            </div>
            """
            st.markdown(spectrum_html, unsafe_allow_html=True)
            st.markdown("---")
        
        with col3:
            st.markdown(f"### {st.session_state.extreme_right}")
        
        # Guessing interface
        st.subheader(f"Player: {st.session_state.current_guesser}")
        
        guess = st.slider(
            "Make your guess:",
            min_value=0,
            max_value=100,
            value=50,
            help="Where do you think the wavelength answer is?"
        )
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📍 Submit Guess"):
                distance = abs(guess - st.session_state.wavelength_position)
                st.session_state.guesses.append({
                    "player": st.session_state.current_guesser or "Anonymous",
                    "guess": guess,
                    "distance": distance
                })
                st.success(f"Guess submitted! Distance from wavelength: {distance}%")
        
        with col2:
            if st.button("➕ Add Another Guesser"):
                st.info("Setup the next guesser and submit their guess!")
        
        with col3:
            if st.button("📋 End Round"):
                st.session_state.game_running = False
                st.session_state.wavelength_revealed = False
        
        # Display all guesses
        if st.session_state.guesses:
            st.subheader("Guesses Made:")
            
            # Sort by closest to wavelength
            sorted_guesses = sorted(st.session_state.guesses, key=lambda x: x["distance"])
            
            for i, g in enumerate(sorted_guesses, 1):
                col1, col2, col3 = st.columns([2, 1, 1])
                with col1:
                    st.write(f"**{g['player']}**: {g['guess']}%")
                with col2:
                    st.write(f"Distance: {g['distance']}%")
                with col3:
                    if g['distance'] <= 5:
                        st.success("✅ Close!")
                    elif g['distance'] <= 15:
                        st.info("😐 Warm")
                    else:
                        st.warning("❌ Cold")
else:
    st.info("👆 Set up a game above and click 'Start Round' to begin!")
