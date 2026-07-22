# components/markdown_utils.py

import re
import streamlit as st


def render_markdown_with_images(content, image_map, image_width=900):
    """
    Render markdown text, replacing [FIGURE_n] placeholders with centered st.image calls.

    Parameters
    ----------
    content : str
        Markdown text containing placeholders like [FIGURE_1].
    image_map : dict
        Maps placeholder strings (e.g. "[FIGURE_1]") to image file paths.
    image_width : int
        Width in pixels to display each figure.
    """
    pattern = "(" + "|".join(re.escape(key) for key in image_map) + ")"
    pieces = re.split(pattern, content)

    for piece in pieces:
        if piece in image_map:
            _, col_mid, _ = st.columns([0.5, 10, 0.5])
            with col_mid:
                st.image(image_map[piece], width=image_width)
        elif piece.strip():
            st.markdown(piece)

def load_quiz(path):
    """Load a quiz from a markdown file."""

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Get rid of the title
    text = re.sub(r"^#.*?\n+", "", text, flags=re.DOTALL)

    # Split into question blocks
    blocks = re.split(r"\n---\n", text)

    questions = []

    for block in blocks:
        block = block.strip()

        if not block:
            continue

        lines = block.splitlines()

        question = None
        options = []
        correct = None
        success = ""

        i = 0
        while i < len(lines):

            line = lines[i].strip()

            if line.startswith("Question:"):
                question = line.replace("Question:", "", 1).strip()

            elif line == "Options:":
                i += 1
                while i < len(lines) and lines[i].startswith("- "):
                    options.append(lines[i][2:].strip())
                    i += 1
                continue

            elif line.startswith("Correct:"):
                correct = line.replace("Correct:", "", 1).strip()

            elif line == "Success:":
                success = "\n".join(lines[i + 1:]).strip()
                break

            i += 1

        questions.append(
            {
                "question": question,
                "options": options,
                "correct": correct,
                "success": success,
            }
        )

    return questions

def display_quiz(path, quiz_id):
    quiz = load_quiz(path)

    for i, q in enumerate(quiz):

        answer = st.radio(
            q["question"],
            q["options"],
            index=None,
            key=f"{quiz_id}_radio_{i}"
        )

        if answer is None:
            continue

        if answer == q["correct"]:
            st.success(q["success"] + " ✅")
        else:
            st.error("Incorrect, try again! ❌")