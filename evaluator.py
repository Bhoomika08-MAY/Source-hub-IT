import pandas as pd

df = pd.DataFrame({
    'question': ['What is the capital of France?'],
    'correct_answer': ['Paris'],
    'student_answer': ['Paris'],
    'similarity_score': [1.0]
})

df.to_csv('graded_quiz.csv', index=False)
print("✅ File created.")