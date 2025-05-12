# AI Voice Market Analyzer

A sophisticated voice-driven market analysis assistant that enables users to interact with an AI financial assistant using voice commands. The application leverages cutting-edge technologies including Deepgram for speech-to-text, OpenAI's GPT-3.5 for intelligent responses, and Alpha Vantage for real-time market data.

## 🌟 Features

### Core Functionality
- **Voice Processing**
  - WAV file upload support
  - High-accuracy speech-to-text conversion using Deepgram
  - Support for various accents and speech patterns

### AI Integration
- **OpenAI GPT-3.5 Integration**
  - Contextual understanding of financial queries
  - Natural language processing for market analysis
  - Intelligent response generation

### Market Data
- **Real-time Market Information**
  - Live stock price retrieval via Alpha Vantage
  - Support for major stock exchanges
  - Real-time market data integration

### Audio Response
- **Text-to-Speech Capabilities**
  - High-quality voice synthesis using OpenAI TTS
  - Automatic audio playback of responses
  - Natural-sounding voice output

## 🛠️ Prerequisites

### System Requirements
- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)
- Stable internet connection
- Modern web browser (Chrome, Firefox, or Edge)

### API Keys Required
1. **Deepgram API Key**
   - Sign up at [Deepgram](https://deepgram.com)
   - Free tier available with limited usage
   - Required for speech-to-text conversion

2. **OpenAI API Key**
   - Sign up at [OpenAI](https://openai.com)
   - Required for both GPT-3.5 and TTS services
   - Free tier available with limited usage

3. **Alpha Vantage API Key**
   - Sign up at [Alpha Vantage](https://www.alphavantage.co)
   - Free tier available with limited API calls
   - Required for stock market data

## 📥 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/RohitMudili/AI-voice-market-analyser.git
cd AI-voice-market-analyser
````

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root with the following structure:

```env
# Deepgram Configuration
DEEPGRAM_API_KEY=your_deepgram_api_key

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key
TTS_API_KEY=your_openai_tts_api_key
TTS_API_BASE_URL=https://api.openai.com/v1/audio/speech

# Alpha Vantage Configuration
ALPHAVANTAGE_API_KEY=your_alphavantage_api_key
```

## 🚀 Usage

### Starting the Application

1. Ensure your virtual environment is activated
2. Start the Streamlit application:

```bash
streamlit run app.py
```

3. Access the application at `http://localhost:8501`

### Using the Application

1. **Prepare Your Voice Query**

   * Record your voice query in **WAV format**.
   * Keep queries clear and concise.
   * Recommended duration: 5-30 seconds.

2. **Upload a WAV File of Your Choice**

   * Click the upload button on the application interface.
   * Select a **WAV file** from your local device that contains the voice query.
   * The file will be uploaded and processed.

3. **Upload and Process**

   * After uploading, wait for the application to process the audio.
   * The transcription of your query will appear first.
   * Then, the AI-generated response will follow.

4. **View Results**

   * After processing, the transcription of your query will be shown.
   * The AI’s response will appear below the transcription.
   * **Audio playback** of the response will start automatically for a seamless experience.

### Example Queries

* "What is the current price of AAPL stock?"
* "Give me a market analysis for Tesla"
* "What are the latest trends in the tech sector?"

## 📁 Project Structure

```
AI-voice-market-analyser/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not tracked in git)
├── .gitignore         # Git ignore file
└── README.md          # Project documentation
```

## 🔧 Troubleshooting

### Common Issues

1. **API Key Errors**

   * Verify all API keys are correctly set in `.env`
   * Check API key validity in respective dashboards
   * Ensure proper formatting of API keys

2. **Audio Processing Issues**

   * Verify WAV file format
   * Check file size (recommended < 10MB)
   * Ensure clear audio quality

3. **Connection Problems**

   * Check internet connectivity
   * Verify API service status
   * Check firewall settings

## 📝 API Usage Guidelines

### Deepgram

* Free tier: 100 hours/month
* Supports multiple languages
* Real-time transcription

### OpenAI

* GPT-3.5: Free tier available
* TTS: Pay-as-you-go pricing
* Rate limits apply

### Alpha Vantage

* Free tier: 5 API calls/minute
* 500 API calls/day
* Real-time and historical data

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.