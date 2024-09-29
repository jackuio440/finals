# Facial Recognition Login System with Voice and Gesture Control

This project implements a facial recognition login system, combined with voice and gesture controls to provide a hands-free and intuitive user experience. The system uses a variety of Python libraries to achieve these functionalities.

## Features

### 1. Facial Recognition Login
The program allows users to log in via facial recognition. Upon first use, the program creates a facial model of the user using a webcam, which is stored and used for future logins.

- **Library Used**: `OpenCV`
- **Process**: 
  - Captures images of the user's face through the webcam.
  - Creates a model based on the images for facial recognition.
  - Compares the user's face with the stored model each time the program is opened to authenticate and log in the user.

### 2. Voice Control
Users can execute basic commands by using their voice. The system supports the following commands:

- **Commands**:
  - `新聞` – Fetches and reads out news headlines gathered via web scraping.
  - `英文新聞` – Fetches news headlines and reads out their English translations.
  - `音樂` – Plays music from a pre-existing library.
  - `直播` – Opens a live broadcast of YouTube news.
  - `嗨` – Greets the user and announces the current time.
  - `結束` – Ends the recognition session.
  
- **Libraries Used**:
  - `SpeechRecognition`
  - `PyAudio`
  - `gTTS` (Google Text-to-Speech)

### 3. Gesture Control
Users can perform basic operations by making specific hand gestures in front of the webcam. The gesture commands mirror the voice control commands.

- **Gestures**:
  - `1` – Fetches and reads out news headlines.
  - `2` – Fetches and reads out news translated into English.
  - `3` – Plays music from the library.
  - `4` – Opens a live broadcast of YouTube news.
  - `5` – Greets the user and announces the current time.
  - `ok` – Ends the recognition session.

- **Libraries Used**:
  - `MediaPipe`
  - `OpenCV` 

### 4. News Reporting & Live News Streaming
News reporting and live streaming can be triggered via voice or gesture commands.

- **News Reporting**: 
  - The program uses web scraping (via `BeautifulSoup`) to fetch news headlines from the PTT news page. 
  - Headlines and URLs are randomly selected and stored in a text file. The content is read aloud using the `pyttsx3` text-to-speech engine.
  
- **Live News Streaming**:
  - The program opens a web browser and directly streams live news broadcasts from YouTube.

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/facial-recognition-voice-gesture-control.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the program:
   ```bash
   python main.py
   ```

## Dependencies

- `OpenCV` – For facial and gesture recognition.
- `SpeechRecognition`, `PyAudio`, `gTTS` – For voice recognition and text-to-speech functionality.
- `MediaPipe` – For gesture recognition.
- `BeautifulSoup` – For web scraping news headlines.
- `pyttsx3` – For text-to-speech conversion.

## Usage

Once the program is running, users can log in through facial recognition and interact with the system using voice commands or hand gestures.

--- 

This README provides an overview of the project's key features, installation instructions, and usage guidelines.
