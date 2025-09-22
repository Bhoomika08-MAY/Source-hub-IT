# Source-hub-IT 🎓  
**AI Quiz Evaluator** — A Streamlit-powered app for automated grading and feedback.

## 🚀 Overview
This app allows educators and reviewers to upload quiz responses in CSV format and instantly evaluate student performance. It checks for required columns, validates answers, and displays intuitive feedback — all in a clean, interactive UI.

## ✨ Features
- 📁 CSV upload with structure validation
- ✅ Auto grading based on correct answers
- 📊 Score display and feedback
- 🧠 Probability-based feedback (optional)
- 🏆 Certificate generation (coming soon)
- 🔄 Multi-student support for batch evaluation

## 🎬 Demo

Check out how the AI Quiz Evaluator works:

📁 See [`assets/demo1.mp4`](assets/demo1.mp4) for a full walkthrough of the app in action.

> The demo shows how to upload a CSV, evaluate student answers, and view graded results with feedback.



## 🛠️ Tech Stack
- Python 3.11+
- Streamlit
- pandas

## 📂 File Structure
AI-QUIZ-EVALUATOR/
├── .gitignore              # Git exclusions (e.g., venv, __pycache__, CSVs)
├── app.py                 # Streamlit UI and main app logic
├── evaluator.py           # Core grading logic (score calculation, feedback)
├── graded_quiz.csv        # Output file with evaluated results
├── quiz_data.csv          # Input file with raw quiz questions and answers
├── README.md              # Project overview and usage instructions
├── requirements.txt       # Python dependencies for setup
