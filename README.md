# 🌊 WaveLength Game

A Streamlit app for playing the WaveLength party game! Players create custom categories with two extremes, and try to guess where on the spectrum the correct answer lies.

## 🎮 How to Play

1. **Setup**: Enter a category (e.g., "clothes-warmth") and define the two extremes (e.g., "cold" ↔ "hot")
2. **Set the Answer**: Position the wavelength on the spectrum (0-100)
3. **Hide the Answer**: Click "Start Round" - other players must look away!
4. **Reveal & Guess**: When players are ready, click "READY TO GUESS?" to show the spectrum
5. **Score**: Players who guess closest to the wavelength win points!

## 🚀 Setup & Installation

### Create Virtual Environment
```bash
cd mari-length
python -m venv wave-length
.\wave-length\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Running the App

With the virtual environment activated, run:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 🎯 Features

- **Custom Categories**: Create any category you want
- **Multi-player**: Support for multiple players per round
- **Hidden Wavelength**: Built-in pause mechanism so players don't see answers early
- **Real-time Feedback**: See how close each guess is to the correct answer
- **Beautiful Spectrum**: Visual gradient spectrum with marked wavelength position

## 📝 Example Categories

- **clothes-warmth**: cold ↔ hot
- **beverage-strength**: weak ↔ strong  
- **weather-severity**: sunny ↔ stormy
- **personality-vibe**: introvert ↔ extrovert

Enjoy! 🎉