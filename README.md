# AI Voice Market Analyzer

A real-time voice-driven market analysis assistant. This application allows users to interact with an AI financial assistant using their voice, leveraging real-time transcription, LLM-powered responses, and market data integration.

## Features

- Real-time voice recording and transcription (Deepgram)
- AI-powered financial conversation using OpenAI's GPT-3.5
- Stock price and market data retrieval via Alpha Vantage
- Text-to-speech responses (OpenAI TTS)
- LiveKit integration for real-time audio streaming (optional)
- Session history logging

## Prerequisites

- Python 3.8 or higher
- Deepgram API key
- OpenAI API key
- Alpha Vantage API key
- (Optional) LiveKit server and credentials

## Installation

1. Clone the repository:
```bash
git clone https://github.com/RohitMudili/AI-voice-market-analyser.git
cd AI-voice-market-analyser
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your API keys:
```
DEEPGRAM_API_KEY=your_deepgram_api_key
OPENAI_API_KEY=your_openai_api_key
TTS_API_KEY=your_openai_tts_api_key
TTS_API_BASE_URL=https://api.openai.com/v1/audio/speech
ALPHAVANTAGE_API_KEY=your_alphavantage_api_key
LIVEKIT_API_KEY=your_livekit_api_key  # Optional, for LiveKit integration
LIVEKIT_API_SECRET=your_livekit_api_secret  # Optional
LIVEKIT_URL=your_livekit_server_url  # Optional
```

## Usage

1. Start the token server (for LiveKit integration):
```bash
python token_server.py
```

2. Start the Streamlit application:
```bash
streamlit run app.py
```

3. Open your web browser and navigate to the provided URL (usually http://localhost:8501)

4. Click "Start Recording" to begin a voice conversation with the AI market assistant.

## Project Structure

- `app.py`: Main Streamlit application for voice interaction, transcription, LLM, and TTS
- `livekit_client.py`: Handles LiveKit audio streaming (optional)
- `token_server.py`: Flask server to generate LiveKit tokens
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (not tracked in git)
- `transcriptions.txt`: Log of conversations (generated during use)
- `.gitignore`: Files and folders ignored by git

## License

MIT License - see LICENSE file for details 