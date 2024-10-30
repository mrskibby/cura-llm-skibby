import openai
import json
import os

# Set your OpenAI API key here or ensure it's set in your environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

if not openai.api_key:
    raise ValueError("OpenAI API key not found. Please set it as an environment variable.")

# Function to generate exemplar answers
def generate_exemplar_answer(task_content, question, rubric):
    print("Sending request to OpenAI API...")  # Log this
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates exemplar answers based on task content and rubrics."},
            {"role": "user", "content": f"Task Content: {task_content}\nQuestion: {question}\nRubric: {rubric}\nPlease generate an exemplar answer."}
        ],
        max_tokens=500
    )
    print("Received response from OpenAI API...")  # Log this
    return response['choices'][0]['message']['content']

# Load and process the training data
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Main function to generate answers and save results
def main():
    # Load the training data
    data = load_data('data/cura-llm-training-data.json')

    results = []
    
    # Generate exemplar answers for each entry
    for entry in data:
        task_content = entry['task_content']
        question = entry['question']
        rubric = entry['rubric']
        
        # Generate the answer using the OpenAI API
        exemplar_answer = generate_exemplar_answer(task_content, question, rubric)
        
        # Print for reference
        print(f"Exemplar Answer for Question: {question}")
        print(exemplar_answer)
        print("-" * 50)
        
        # Store the result for saving later
        results.append({
            "question_id": entry['question_id'],
            "exemplar_answer": exemplar_answer
        })
    
    # Save the results to a JSON file
    with open('data/exemplar_answers.json', 'w') as outfile:
        json.dump(results, outfile, indent=4)

if __name__ == "__main__":
    main()
