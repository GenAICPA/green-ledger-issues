import os
import re

def standardize_question_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the question label (e.g., "Q1") and the title from headings like "# Q1: Title" or "# Question 1: Title"
        # This regex is more robust to handle variations in the heading format.
        title_match = re.search(r'^#\s*(?:Q|Question)\s*(\d+):\s*(.*)', content, re.IGNORECASE | re.MULTILINE)

        # If the first pattern doesn't match, try a simpler one for files that might not have the "Q##:" prefix.
        if not title_match:
            title_match = re.search(r'^#\s*(.*)', content, re.MULTILINE)
            if not title_match:
                print(f"Warning: Could not find a suitable title in {filepath}. Skipping.")
                return
            title = title_match.group(1).strip()
            # Extract question number from filename if not in title
            q_num_match = re.search(r'Q(\d+)\.md', filepath)
            if not q_num_match:
                print(f"Warning: Could not determine question number for {filepath}. Skipping.")
                return
            question_label = f"Q{q_num_match.group(1)}"
        else:
            question_label = f"Q{title_match.group(1)}"
            title = title_match.group(2).strip()

        # Remove the old title line from the content
        content_after_title_removal = content[:title_match.start()] + content[title_match.end():]

        # Remove any existing YAML frontmatter block (--- ... ---)
        # This ensures we don't duplicate frontmatter.
        body = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content_after_title_removal, flags=re.DOTALL).strip()

        # Create the new, standardized frontmatter
        new_frontmatter = f"""---
sidebar_label: '{question_label}'
title: '{title}'
---

"""

        # Assemble the new file content with a clean H1 heading
        new_content = new_frontmatter + f"# {title}\\n\\n" + body

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully processed {filepath}")

    except Exception as e:
        print(f"Error processing {filepath}: {e}")

# Process files from Q4.md to Q10.md
for i in range(4, 11):
    filename = f"docs/questions/Q{i}.md"
    if os.path.exists(filename):
        standardize_question_file(filename)
    else:
        print(f"File not found: {filename}")

print("\\nStandardization complete for Q4-Q10.")
