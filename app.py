import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load the transformer model once
model = SentenceTransformer('all-MiniLM-L6-v2')

# Grading logic
def grade_quiz(df):
    def compute_similarity(row):
        score = util.cos_sim(model.encode(row['correct_answer']), model.encode(row['student_answer'])).item()
        return round(score, 2)

    def assign_grade(score):
        if score >= 0.85:
            return 'Correct'
        elif score >= 0.6:
            return 'Partially Correct'
        else:
            return 'Incorrect'

    def give_feedback(grade):
        return {
            'Correct': '✅ Well done!',
            'Partially Correct': '⚠️ Close, but needs improvement.',
            'Incorrect': '❌ Try again.'
        }[grade]

    df['similarity_score'] = df.apply(compute_similarity, axis=1)
    df['grade'] = df['similarity_score'].apply(assign_grade)
    df['feedback'] = df['grade'].apply(give_feedback)
    return df

# Streamlit UI setup
st.set_page_config(page_title="AI Quiz Evaluator", page_icon="🧠", layout="centered")
st.title("🧠 AI Quiz Evaluator")
st.markdown("Upload your quiz CSV file to get instant grading based on semantic similarity.")

# File uploader
uploaded_file = st.file_uploader("📤 Upload `quiz_data.csv`", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 Original Quiz Data")
    st.dataframe(df)

    # Check required columns
    required_cols = ['question', 'correct_answer', 'student_answer']
    if all(col in df.columns for col in required_cols):
        graded_df = grade_quiz(df)

        st.subheader("✅ Graded Results")
        st.dataframe(graded_df)

        # 🎓 Certificate logic
        average_score = graded_df['similarity_score'].mean()

        if average_score >= 0.85:
            st.success("🎉 Congratulations! You’ve earned a certificate of excellence.")
            st.markdown(f"""
            ---
            ### 🏆 Certificate of Excellence
            This certifies that **you** have successfully completed the quiz with an outstanding performance.

            **Average Score:** {round(average_score, 2)}  
            **Grade:** Excellent  
            **Date:** {pd.Timestamp.now().date()}

            _Keep up the great work!_
            ---
            """)
        else:
            st.info(f"Your average score is {round(average_score, 2)}. Keep practicing to earn a certificate!")

        # 📥 Download button
        csv = graded_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Graded Results",
            data=csv,
            file_name="graded_quiz.csv",
            mime="text/csv"
        )
    else:
        st.error("❌ CSV must contain 'question', 'correct_answer', and 'student_answer' columns.")
else:
    st.info("👆 Upload a CSV file to begin.")