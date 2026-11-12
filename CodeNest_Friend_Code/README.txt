CODENEST – AI-DRIVEN CODE GENERATION LAB
Short practical-exam programs

CONTENTS
1. Exp1b_Code_Generation_Test_Cases.py
2. Exp2_GAN_Style_Code_Classification.py
3. Exp4_Code_Completion.py
4. Exp5_Pseudocode_to_Python.py
5. Exp6_Code_Quality_Evaluation.py

SETUP (simple commands)

STEP 1 – Install Ollama
Download and install Ollama from:
https://ollama.com/download

Open Ollama and keep it running.

STEP 2 – Download the AI model
Open Terminal / Command Prompt and run:
ollama pull qwen2.5-coder:3b

Check that it is installed:
ollama list

STEP 3 – Install Python packages
For Experiments 1b, 4 and 5:
pip install ollama

For Experiment 2:
pip install ollama scikit-learn

Experiment 6 uses only Python's built-in ast module. No package installation is needed.

RUN A PROGRAM
Open the folder in Terminal / Command Prompt and run, for example:
python Exp1b_Code_Generation_Test_Cases.py

Replace the filename with the experiment you want to run.

IMPORTANT NOTES
- Ollama must be installed and running before running Experiments 1b, 2, 4 and 5.
- The qwen2.5-coder:3b model is downloaded once; you do not need to download it for every experiment.
- Experiment 2 is a simplified GAN-style demonstration: it uses an AI code generator and a Logistic Regression classifier, not a full traditional GAN.
- Experiment 6 demonstrates syntax checking and test-based scoring. Its static-analysis and type-checking lines are illustrative messages, not actual tool executions.
- In Experiment 6, the stray word "Syntax" from the forwarded code has been removed because it causes a syntax error.
- AI-generated code and output can vary between runs.
