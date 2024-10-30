from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu
from rouge_score import rouge_scorer
import json

# Function to compute BLEU score with smoothing
def bleu_score(generated, reference):
    reference = [reference.split()]  # Tokenize reference answer
    generated = generated.split()  # Tokenize generated answer
    # Use smoothing function to handle 0 n-gram overlaps
    smoothing = SmoothingFunction().method1
    return sentence_bleu(reference, generated, smoothing_function=smoothing)

# Function to compute ROUGE score
def rouge_score(generated, reference):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    return scorer.score(reference, generated)

# Function to evaluate generated answers
def evaluate_generated_answers(train_data, test_data):
    total_bleu = 0
    total_rouge1 = 0
    total_rougeL = 0
    num_entries = len(test_data)
    
    # Evaluate each generated answer in the test set
    for generated_entry, reference_entry in zip(train_data, test_data):
        generated_answer = generated_entry['exemplar_answer']
        reference_answer = reference_entry['answer']
        
        # Calculate BLEU score with smoothing
        bleu = bleu_score(generated_answer, reference_answer)
        total_bleu += bleu

        # Calculate ROUGE score
        rouge = rouge_score(generated_answer, reference_answer)
        total_rouge1 += rouge['rouge1'].fmeasure
        total_rougeL += rouge['rougeL'].fmeasure

        # Print individual scores for reference
        print(f"Question {reference_entry['question_id']} - BLEU: {bleu}, ROUGE-1: {rouge['rouge1'].fmeasure}, ROUGE-L: {rouge['rougeL'].fmeasure}")
    
    # Calculate average scores
    avg_bleu = total_bleu / num_entries
    avg_rouge1 = total_rouge1 / num_entries
    avg_rougeL = total_rougeL / num_entries

    # Print overall averages
    print(f"Average BLEU Score: {avg_bleu}")
    print(f"Average ROUGE-1 Score: {avg_rouge1}")
    print(f"Average ROUGE-L Score: {avg_rougeL}")

# Main function to handle split and evaluation
def main():
    # Load the generated answers
    with open('../data/exemplar_answers.json', 'r', encoding='utf-8') as f:
        generated_answers = json.load(f)

    # Load the original dataset to get reference answers
    with open('../data/cura-llm-training-data.json', 'r', encoding='utf-8') as f:
        reference_data = json.load(f)

    # Split 80% for training, 20% for testing
    split_idx = int(0.8 * len(reference_data))
    training_data = reference_data[:split_idx]
    test_data = reference_data[split_idx:]

    print(f"Evaluating {len(test_data)} questions in the test set.")
    
    # Evaluate the model on the test data
    evaluate_generated_answers(training_data, test_data)

if __name__ == "__main__":
    main()
