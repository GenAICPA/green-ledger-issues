import re
import os

def get_cluster(q_num):
    """Returns the cluster name for a given question number."""
    if 1 <= q_num <= 10:
        return "Ledger Foundations & Accounting Parallels"
    elif 11 <= q_num <= 15:
        return "Fidelity, Event Theory, Auditability"
    elif 16 <= q_num <= 20:
        return "Assets, Liabilities & Metrics in ESG"
    elif 21 <= q_num <= 30:
        return "Subledgers, Process Models, and Supply Chain"
    elif 31 <= q_num <= 40:
        return "Standards, Data Flows & Confidentiality"
    elif 41 <= q_num <= 51:
        return "Controls, Anti-Greenwashing & Technology Links"
    return ""

def parse_text(text):
    """Parses the text to extract questions and answers."""
    questions_data = {}

    # Extract ChatGPT responses section
    chatgpt_responses_text_match = re.search(r'Responses from ChatGPT\n(.*?)\nResponses from ChatGPT', text, re.DOTALL)
    if not chatgpt_responses_text_match:
        chatgpt_responses_text_match = re.search(r'Responses from ChatGPT\n(.*)', text, re.DOTALL)

    chatgpt_responses_text = chatgpt_responses_text_match.group(1)

    # Extract concise answers section first
    concise_answers_text_match = re.search(r'Section I – Concise Answers\n(.*?)\nSection 2: Detailed Answers', chatgpt_responses_text, re.DOTALL)
    concise_answers_text = concise_answers_text_match.group(1)

    # Split concise answers
    concise_parts = re.split(r'(?:^|\n)Q(\d{1,2})\. ', concise_answers_text.strip())[1:]

    for i in range(0, len(concise_parts), 2):
        q_num = int(concise_parts[i])
        content = concise_parts[i+1]

        lines = content.split('\n')
        question_text = lines[0].strip()
        concise_answer = '\n'.join(lines[1:]).strip()

        questions_data[q_num] = {
            "question": question_text,
            "concise_answer": concise_answer
        }

    # Extract detailed answers section
    detailed_answers_text_match = re.search(r'Section 2: Detailed Answers\n(.*?)(?=\nBrief commentary on the AI experience|\Z)', chatgpt_responses_text, re.DOTALL)
    detailed_answers_text = detailed_answers_text_match.group(1)

    # Remove introduction from detailed answers
    detailed_answers_text = re.sub(r'Introduction:.*?\n\n', '', detailed_answers_text, 1, re.DOTALL)

    # Split detailed answers into question/answer blocks
    detailed_parts = re.split(r'\n(\d{1,2})\. ', detailed_answers_text.strip())[1:]

    for i in range(0, len(detailed_parts), 2):
        q_num = int(detailed_parts[i])
        content = detailed_parts[i+1]

        lines = content.split('\n')
        detailed_question = lines[0].strip()
        detailed_answer = '\n'.join(lines[1:]).strip()

        if q_num in questions_data:
            if questions_data[q_num]['question'] != detailed_question:
                print(f"Warning: Question text mismatch for Q{q_num}. Using question from concise answer.")
            questions_data[q_num]["detailed_answer"] = detailed_answer

    return questions_data

def main():
    """Main function to run the script."""
    with open('source_documents/extracted_text.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    questions = parse_text(text)

    for q_num, data in questions.items():
        cluster = get_cluster(q_num)

        front_matter = f"""---
status: draft
cluster: "{cluster}"
---
"""

        content = f"""
# Q{q_num}: {data['question']}

## Short Answer

{data.get('concise_answer', 'Not available.')}

## Detailed Answer

{data.get('detailed_answer', 'Not available.')}

## References

*Coming soon...*

## Cross-references

*Coming soon...*
"""

        file_path = f"docs/questions/Q{q_num}.md"
        with open(file_path, "w", encoding='utf-8') as f:
            f.write(front_matter.strip() + '\n\n' + content.strip())
        print(f"Populated {file_path}")

if __name__ == "__main__":
    main()
