# AI-ML: Study Pattern Analyzer

*Author:* [jainam jain]  
*Project Title:* Study Pattern Analyzer

### ⬥ Overview of the Project:
This application predicts a student's performance category based on their daily habits, specifically *study hours, sleep duration, and level of distractions. It utilizes a **Decision Tree Classifier* model trained on sample behavioral data to provide personalized feedback and suggestions for improvement.

### ⬥ Features:
* *Behavioral Prediction:* Uses a Decision Tree algorithm to categorize performance into "Good," "Average," or "Poor."
* *Real-time Analysis:* Takes direct user input for daily metrics to provide an instant academic outlook.
* *Personalized Suggestions:* Evaluates specific input thresholds to offer actionable advice (e.g., increasing study time or reducing distractions).
* *Error Handling:* Utilizes integer casting to ensure user inputs are processed correctly for the ML model.

### ⬥ Technologies/Tools Used:
* *Programming Language*
    * *Python 3.x:* Used to implement the logic, handle user inputs, and manage data structures.
* *Libraries*
    * *Scikit-learn:* Used to implement the DecisionTreeClassifier for the AI-based performance prediction.
* *Runtime Environment*
    * *Google Colab / Jupyter Notebook:* Executes the code blocks and displays the interactive terminal interface.

### ⬥ Steps to Install & Run the Project:
*Instructions for Testing:*

1.  Open *Google Colab* or *VS Code* with the Python extension installed.
2.  Ensure you have the required library installed by running:
    pip install scikit-learn
3.  Copy the code into a .py file or a notebook cell.
4.  *How to Run the Program:*
    * Click the *Play/Run* button in your IDE or Colab cell.
    * Follow the on-screen prompts in the terminal/output window.

### ⬥ Expected Program Flow:
* System initializes the sample dataset (Study hours, sleep, distractions) and trains the *Decision Tree* model.
* User enters their *Name*.
* User enters *Study Hours*.
* User enters *Sleep Hours*.
* User enters *Distractions* (on a scale).

*Program Displays:*
* A performance prediction: *"Looks like you will do good,"* *"Maybe average performance,"* or *"Performance might be low."*
* Specific suggestions based on the user's habits (e.g., "sleep a bit more").
* <img width="1920" height="1080" alt="Screenshot (65)" src="https://github.com/user-attachments/assets/a362b934-df1b-45d0-92f8-7fd7b5e8e24f" />
<img width="1920" height="1080" alt="Screenshot (67)" src="https://github.com/user-attachments/assets/9abf885e-e53b-4c04-83fe-ccfa075e3dd4" />


