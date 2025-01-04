# first_project
Project name: Quiz application
Language: Python

Quiz Game Program

This Python-based Quiz Game program allows users to test their knowledge by answering multiple-choice questions. The questions are loaded from an external text file, and the player's scores are recorded for future reference.

---
Key Features

1. Randomized Questions:
The program shuffles the questions each time it is run, ensuring a unique experience every time.

2. Customizable Questions:
Questions are stored in a questions.txt file. Users can add or modify questions by editing this file.

3. Leaderboard:
The program maintains a record of player scores in a score.txt file, which can be viewed at the end of the quiz.

4. User-Friendly Design:
Simple command-line interface with clear instructions and options for answering questions.

5. Error Handling:
Handles missing or incorrectly formatted files gracefully, displaying error messages where appropriate.
---
Project Structure

📁 QuizGame
 ├── quiz_app.py        # Main Python script for the quiz game
 ├── questions.txt     # File containing quiz questions and answers
 ├── score.txt         # File storing player scores

---

How to Use

1. Setup Files
Ensure the questions.txt file exists in the same directory as project.py. The file should be formatted as follows:

Question 1;Option A;Option B;Option C;Option D;Correct Answer
Question 2;Option A;Option B;Option C;Option D;Correct Answer

Example:

What is the capital of France?;Paris;London;Berlin;Madrid;A
Which planet is known as the Red Planet?;Earth;Mars;Venus;Jupiter;B

2. Run the Program

Open a terminal or IDE.
Navigate to the directory where project.py is located.
Run the program using:
python project.py



3. Play the Quiz

Follow the instructions displayed in the terminal.
Enter the correct option (A, B, C, or D) for each question.


4. View Scores
After completing the quiz, choose to view the leaderboard to see previously recorded scores.


---

How to Add Questions

Open the questions.txt file.
Add new questions in the format:
Question;Option A;Option B;Option C;Option D;Correct Answer
Save the file and re-run the program.

---

Requirements

Python 3.x

Text editor (for editing questions.txt)

---

Future Enhancements

1. Add support for different difficulty levels.

2. Allow users to select the number of questions they want to attempt.

3. Build a GUI version of the quiz for enhanced user experience.
   
4. Implement timed quizzes for added challenge.

---


