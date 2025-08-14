import os
import re

def main():
    """
    Reads all question markdown files, concatenates them into a single
    'all-in-one.md' file for a consolidated view.
    """
    questions_dir = 'docs/questions'
    output_file = 'docs/all-in-one.md'

    # Get all question files and sort them numerically
    try:
        files = os.listdir(questions_dir)
    except FileNotFoundError:
        print(f"Error: Directory not found at {questions_dir}")
        print("Please ensure you are running this script from the repository root.")
        return

    question_files = sorted(
        [f for f in files if f.startswith('Q') and f.endswith('.md')],
        key=lambda f: int(re.search(r'Q(\d+)', f).group(1))
    )

    if not question_files:
        print(f"No question files found in {questions_dir}")
        return

    all_content = []

    # Add a header for the all-in-one page
    all_content.append("# All-in-One: All Green Ledger Questions")
    all_content.append("\nThis page contains all 51 questions and their answers in a single document for a continuous reading experience.")

    for filename in question_files:
        filepath = os.path.join(questions_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Remove front matter for a cleaner consolidated view
            content = re.sub(r'---\n.*?\n---\n*', '', content, flags=re.DOTALL)
            all_content.append('\n---\n\n' + content.strip()) # Add a horizontal rule separator

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(all_content))

    print(f"Successfully generated {output_file} with {len(question_files)} questions.")

if __name__ == "__main__":
    main()
