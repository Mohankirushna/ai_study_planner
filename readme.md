# 🧠 AI Study Planner
Your personal AI-powered academic companion built with Flask, HTML/CSS/JavaScript, and Gemini API. The app helps students study smarter with intelligent features like plan generation, productivity tracking, AI chat, quizzes, and more — all in one place.

## 🚀 Features
Feature	Description
📚 Study Plan Generator	AI-generated daily plans tailored to your subjects and time availability.
💬 Chat with AI	Ask academic questions or get study suggestions using Gemini API.
🧠 Quiz Me	Test yourself on uploaded or AI-generated topics to enhance recall.
📅 Study Calendar	Visualize and track study plans using a built-in calendar interface.
📊 Productivity Tracker	Monitor your daily focus, time spent, and task completion rates.
⏲️ Pomodoro Timer	Boost concentration with a built-in Pomodoro technique timer.
📁 Upload Material	Upload PDFs, notes, or textbooks to personalize your AI experience.

## 🎯 Objective
The app aims to:
Help students optimize time and retain information.
Deliver personalized, engaging, and adaptive study experiences.
Blend productivity techniques (Pomodoro, calendar scheduling) with AI assistance.

## 🛠️ Tech Stack
Layer	Technologies
Frontend	HTML5, CSS3, JavaScript
Backend	Python, Flask
AI Engine	Gemini API (Google Generative AI)
Styling	Custom CSS, Bootstrap (optional)
Scheduling	JavaScript FullCalendar / Custom Modules
Deployment	Flask Development Server

## 📁 Project Structure
```
ai_study_planner/
│
├── static/
│   ├── css/                  # Stylesheets
│   ├── js/                   # Client-side logic
│   └── assets/               # Icons, fonts, images
│
├── templates/
│   ├── index.html            # Home page
│   ├── planner.html          # Study plan UI
│   ├── chat.html             # AI chat interface
│   ├── quiz.html             # Quiz interface
│   ├── calendar.html         # Calendar view
│   ├── pomodoro.html         # Pomodoro timer page
│   └── upload.html           # Upload interface
│
├── app.py                   # Flask app + routes + Gemini logic
├── requirements.txt         # Dependencies
├── .env                     # Gemini API Key (keep secret!)
└── README.md
```


## 🧪 How to Use
📝 Enter subjects + time → Get AI-generated study plan
💬 Chat with the Gemini-powered assistant for help
📁 Upload materials (PDFs, notes) to tailor AI responses
🧠 Quiz yourself using uploaded or AI-suggested questions
⏱️ Use Pomodoro timer to stay productive
📊 Track productivity metrics
📅 View schedule in study calendar

## 🔧 Setup Instructions
1. Clone the Repository
git clone https://github.com/Mohankirushna/ai_study_planner.git
cd ai_study_planner
2. Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3.Set Up API Key
Create a .env file in the root directory with your Gemini key:
GEMINI_API_KEY=your_actual_gemini_api_key_here
4.Run the App
python app.py

## 🧠 Powered By
Gemini Pro API (Google Generative AI)
Flask
JavaScript FullCalendar 
HTML, CSS, JS

## 🚀 Future Enhancements
 Daily email reminders for study plans
 Sync with Google Calendar
 User profiles with history
 Data analytics for long-term productivity
 Mobile PWA support


## 📝 License
Licensed under the MIT License
