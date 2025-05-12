import streamlit as st
import os
from dotenv import load_dotenv
import json
import requests
import re
from datetime import datetime

# Load environment variables
load_dotenv()

class VoiceAssistant:
    def __init__(self):
        self.deepgram_api_key = os.getenv("DEEPGRAM_API_KEY")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.tts_api_key = os.getenv("TTS_API_KEY")
        self.tts_api_base_url = os.getenv("TTS_API_BASE_URL")
        self.alphavantage_api_key = os.getenv("ALPHAVANTAGE_API_KEY")

    def transcribe_audio(self, audio_data):
        try:
            url = "https://api.deepgram.com/v1/listen"
            headers = {
                "Authorization": f"Token {self.deepgram_api_key}",
                "Content-Type": "audio/wav"
            }
            response = requests.post(url, headers=headers, data=audio_data)
            if response.status_code != 200:
                st.error(f"Deepgram API error: {response.status_code} - {response.text}")
                return None
            result = response.json()
            if "results" in result and result["results"].get("channels"):
                channels = result["results"]["channels"]
                if channels and channels[0].get("alternatives"):
                    return channels[0]["alternatives"][0].get("transcript", "")
            st.error("Could not find transcript in response")
            return None
        except Exception as e:
            st.error(f"Error during transcription: {str(e)}")
            return None

    def get_stock_price(self, symbol):
        url = f"https://www.alphavantage.co/query"
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol,
            "apikey": self.alphavantage_api_key
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            try:
                price = data["Global Quote"]["05. price"]
                return price
            except KeyError:
                return None
        else:
            return None

    def get_llm_response(self, text):
        if not text:
            return "I couldn't understand the audio. Please try again."
        stock_match = re.search(r"stock price of ([A-Za-z]+)", text, re.IGNORECASE)
        if stock_match and self.alphavantage_api_key:
            symbol = stock_match.group(1).upper()
            price = self.get_stock_price(symbol)
            if price:
                text = f"The current price of {symbol} is {price} USD. {text}"
            else:
                text = f"I could not retrieve the price for {symbol}. {text}"
        try:
            headers = {
                "Authorization": f"Bearer {self.openai_api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are a financial assistant. Always provide market data in numbers when possible."},
                    {"role": "user", "content": text}
                ],
                "max_tokens": 100
            }
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=data
            )
            if response.status_code != 200:
                st.error(f"OpenAI API error: {response.status_code} - {response.text}")
                return "Sorry, I encountered an error while processing your request."
            try:
                response_json = response.json()
                if "choices" in response_json and len(response_json["choices"]) > 0:
                    return response_json["choices"][0]["message"]["content"]
                else:
                    st.error(f"Unexpected OpenAI response format: {response_json}")
                    return "Sorry, I couldn't process the response properly."
            except json.JSONDecodeError as e:
                st.error(f"Failed to parse OpenAI response: {str(e)}")
                return "Sorry, I couldn't understand the response from the AI."
        except Exception as e:
            st.error(f"Error getting OpenAI response: {str(e)}")
            return "Sorry, I encountered an error while processing your request."

    def text_to_speech(self, text):
        if not text:
            return None
        try:
            headers = {
                "Authorization": f"Bearer {self.tts_api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "tts-1",
                "input": text,
                "voice": "alloy"
            }
            response = requests.post(
                self.tts_api_base_url,
                headers=headers,
                json=data
            )
            if response.status_code == 200:
                return response.content
            else:
                st.error(f"TTS Error: {response.status_code} - {response.text}")
                return None
        except Exception as e:
            st.error(f"Error in text-to-speech: {str(e)}")
            return None

def main():
    st.title("AI Voice Market Analyzer")
    st.write("Upload a WAV file to analyze market-related queries via voice.")

    uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])
    if uploaded_file is not None:
        audio_data = uploaded_file.read()
        st.audio(audio_data, format='audio/wav')
        assistant = VoiceAssistant()
        transcript = assistant.transcribe_audio(audio_data)
        st.write(f"**Transcription:** {transcript}")
        response = assistant.get_llm_response(transcript)
        st.write(f"**AI Response:** {response}")
        tts_audio = assistant.text_to_speech(response)
        if tts_audio:
            st.audio(tts_audio, format='audio/wav')

if __name__ == "__main__":
    main()