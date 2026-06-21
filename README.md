# 🎓 Career Advisor Chatbot using Gemini API

## 📌 Project Overview

The Career Advisor Chatbot is a multi-turn conversational AI application built using Google's Gemini API, LangChain, and Streamlit.

The chatbot acts as a professional career advisor and provides guidance on:

* Career Planning
* AI/ML Learning Roadmaps
* Resume Improvement Suggestions
* Interview Preparation
* Skill Development Recommendations

The application supports conversation memory, allowing it to remember previous interactions and provide context-aware responses.

---

## 🚀 Features

### Multi-Turn Conversation

* Maintains conversation history using LangChain memory.
* Provides context-aware responses.

### Career Guidance

* Suggests career paths based on user interests and goals.
* Provides structured and professional advice.

### AI/ML Roadmaps

* Generates personalized learning roadmaps for AI, Machine Learning, Data Science, and related domains.

### Resume Suggestions

* Offers recommendations to improve resumes and job applications.

### Interview Preparation

* Helps users prepare for technical and behavioral interviews.

### Streamlit User Interface

* Interactive chat-style interface.
* Real-time response rendering.
* Conversation history display.
* Loading indicator for better user experience.

### Secure API Key Management

* Gemini API key stored using environment variables.
* Prevents exposure of sensitive credentials.

### Logging and Error Handling

* Logs application activities and errors.
* Implements exception handling for improved reliability.

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Frameworks & Libraries

* Streamlit
* LangChain
* LangChain Google GenAI
* Python Dotenv

### AI Model

* Google Gemini 2.5 Flash Lite

---

## 📂 Project Structure

career_chatbot/

├── app.py

├── chains.py

├── chatbot.py

├── llm.py

├── logger.py

├── memory.py

├── prompt.py

├── requirements.txt

├── README.md

├── .env

└── chatbot.log

---

## ⚙️ Installation

### Clone Repository

git clone <repository-url>

cd career_chatbot

### Create Virtual Environment

python -m venv .venv

### Activate Virtual Environment

Windows:

.venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

---

## 🔑 Environment Variables

Create a `.env` file in the project root directory.

Example:

gemini_key=YOUR_GEMINI_API_KEY

---

## ▶️ Running the Application

Start the Streamlit application:

streamlit run app.py

The application will open automatically in your browser.

---

## 💬 Example Queries

* How can I become an AI Engineer?
* Create a Data Scientist roadmap.
* Review my resume skills.
* How should I prepare for technical interviews?
* What skills should a fresher learn in 2026?

---

## 🧠 Architecture

User

↓

Streamlit UI

↓

Chatbot Layer

↓

LangChain Chain

↓

Prompt Template

↓

Gemini API

↓

Response Generation

↓

Memory Update

↓

UI Rendering

---

## 📈 Future Improvements

* Resume Upload and Analysis
* PDF Report Generation
* Retrieval-Augmented Generation (RAG)
* User Authentication
* Cloud Deployment
* Career Recommendation Dashboard

