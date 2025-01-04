#importing the relevant modules
import os
import random

#Function to load questions from the questions.txt file
def question_file(file_path):
  questions = []
  if os.path.exists("/content/questions.txt"):
    with open("/content/questions.txt", "r") as file:
      for line in file:
        parts = line.strip().split(",")
        if len(parts) == 6:
          question = {"question": parts[0], "options": parts[1:5], "answer": parts[5].strip()}
          questions.append(question)
        else:
          print("Error: File not found")
      return questions
  return questions

#Function to record  user score in the score.txt file
def record_score(name, score, total, file_path):
  with open("/content/scores.txt", "a") as file:
    file.write(f"{name},{score}/{total}\n")


#function to display the leaderboard
def leaderboard(file_path):
  if os.path.exists("/content/scores.txt"):
    with open("/content/scores.txt", "r") as file:
      scores = [line.strip() for line in file]
      print("\nLeaderboard: ")
      for score in scores:
        print(score)
  else:
    print("No scores available.")

#main quiz function code.
def run_quiz():
  print("Welcome to the Quiz Game!")
  print("Rules: ")
  print("- Each question has 4 options.")
  print("- Enter the option (A, B, C, D) as your answer.")
  input("Press Enter to start the quiz...")

 #loading questions here
  questions = question_file("/content/questions.txt")
  if not questions:
    print("No questions available. Please check the questions.txt file")
    return
  questions = random.sample(questions, min(5, len(questions)))
  random.shuffle(questions)
  name = input("Enter your name: ")
  score = 0

#loop for the quiz
  for i, q in enumerate(questions):
    print(f"\nQuestion {i + 1}: {q['question']}")
    for j, option in enumerate(q['options'], start= 1):
        print(f"{chr(64 + j)}. {option}")

    user_answer = input("Your Answer: ").strip().upper()
    correct_answer = q['answer']

    if user_answer == correct_answer.upper():
      print("Correct!")
      score += 1
    else:
        print(f"Wrong! The correct answer is: {correct_answer}")

#showing final score here and recording it
  print(f"\nQuiz Complete! Your Score: {score}/{len(questions)}")
  record_score(name, score, len(questions), "/content/scores.txt")
  print("Your score has been recorded in score.txt file")

#option to view leaderboard
  view_leaderboard = input("Do you want to see the leaderboard? (yes/no): ").strip().lower()
  if view_leaderboard == "yes":
      leaderboard("/content/scores.txt")
  else:
      print("Thank you for playing!")

#run the quiz
if __name__ == "__main__":
  run_quiz()

