# LLM Exemplar Answer Generation and Evaluation

This project generates exemplar answers using OpenAI's GPT-4o mini model and evaluates them using BLEU and ROUGE scores.

## Project Overview

1. **`generate_exemplars.py`**: This script generates exemplar answers based on the provided dataset.
2. **`evaluate_exemplars.py`**: This script evaluates the generated answers using BLEU (with smoothing) and ROUGE scores.
3. **GitHub Actions**: The entire process (generation and evaluation) is automated using GitHub Actions.

## Setup Instructions

### 1. Clone the Repository

bash
git clone https://github.com/mrskibby/cura-llm-skibby.git

cd cura-llm-exemplar


### 2. Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Set Your OpenAI API Key

You need an OpenAI API key to generate exemplar answers.

    Set your API key as an environment variable:

    On Mac/Linux:
        export OPENAI_API_KEY="your_api_key"

    On Windows:
        set OPENAI_API_KEY="your_api_key"

### 5. Generate Exemplar Answers

python src/generate_exemplars.py

### 6. Evaluating Answers on Unseen Data

The evaluation process uses a train/test split to evaluate the model on unseen data:

Train/Test Split: The dataset is split into 80% for training and 20% for testing. The exemplar answers are generated using the training set, and the evaluation is performed on the unseen test set.

Evaluation Metrics:

BLEU (with smoothing): Evaluates n-gram overlap between the generated and reference answers.
ROUGE: Measures word-level overlap and evaluates the precision, recall, and F1 score of generated answers against the reference answers.

To evaluate the answers:

python src/evaluate_exemplars.py

This script will:

- Perform the train/test split.
- Generate evaluation metrics for BLEU and ROUGE on the unseen test data.
- Output the results for each test question and the overall average scores.

### 7. Running the Workflow with GitHub Actions
The workflow is set to run automatically on every push or pull request to the main branch. It will:

    1. Generate exemplar answers.
    2. Evaluate them using BLEU and ROUGE scores.
    3. Output the results in the GitHub Actions workflow.

### 8. Project Structure

cura-llm-exemplar/
├── src/
│   ├── generate_exemplars.py  # Script to generate exemplar answers
│   ├── evaluate_exemplars.py  # Script to evaluate the generated answers
├── tests/
│   └── test_generate_exemplars.py  # Unit tests for generation logic
├── data/
│   ├── cura-llm-training-data.json  # Provided dataset
│   └── exemplar_answers.json  # Generated answers saved here
├── .github/
│   └── workflows/
│       └── main.yml  # GitHub Actions workflow for automation
├── requirements.txt  # Python dependencies
└── README.md  # Project documentation

### 9. How to commit Changes

git add .
git commit -m "Update workflow and README"
git push origin main


