import sys
import os
import pytest
import openai

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import generate_exemplars as ge

# Set your OpenAI API key here or ensure it's set in your environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

if not openai.api_key:
    raise ValueError("OpenAI API key not found. Please set it as an environment variable.")


# @pytest.mark.timeout(10)  # Add a timeout of 10 seconds for the test
def test_generate_exemplar_answer():
    task_content = "Sample task content"
    question = "Sample question"
    rubric = "Sample rubric"
    
    # Call the function and assert the result is not None
    answer = ge.generate_exemplar_answer(task_content, question, rubric)
    
    assert answer is not None
    assert isinstance(answer, str)
    assert len(answer) > 0  # Ensure that the answer is not an empty string
