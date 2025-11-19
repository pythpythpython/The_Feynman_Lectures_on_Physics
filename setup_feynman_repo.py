import os
from pathlib import Path
import nbformat as nbf

# -------------- helpers --------------

def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def create_gitkeep(path: Path):
    ensure_dir(path)
    keep = path / ".gitkeep"
    if not keep.exists():
        keep.write_text("")

def new_notebook(cells, path: Path):
    ensure_dir(path.parent)
    if path.exists():
        return  # don't overwrite if already there
    nb = nbf.v4.new_notebook()
    nb.cells = cells
    path.write_text(nbf.writes(nb), encoding="utf-8")

def md(text: str):
    return nbf.v4.new_markdown_cell(text)

def code(text: str = ""):
    return nbf.v4.new_code_cell(text)


# -------------- templates for notebooks --------------

def chapter_reading_notes_template(title: str):
    return [
        md(f"# {title} – Reading Notes\n"),
        md("## Overview\n\n_Summarize the main ideas in your own words._"),
        md("## Key Definitions\n\n- \n- "),
        md("## Key Equations\n\nWrite them with LaTeX, e.g. `$F = ma$`.\n"),
        md("## Derivations\n\nWalk through important derivations step by step.\n"),
        md("## Confusions / Questions\n\nWrite anything that feels unclear here.")
    ]

def chapter_examples_code_template(title: str):
    return [
        md(f"# {title} – Examples and Code Experiments\n"),
        md("Use this notebook for extra examples, numerical checks, and visualizations."),
        code("# import common tools\nimport numpy as np\nimport matplotlib.pyplot as plt\n%matplotlib inline"),
    ]

def chapter_exercises_in_progress_template(title: str):
    return [
        md(f"# {title} – Exercises (In Progress)\n"),
        md("Use this for rough work. It can be messy."),
        md("## Problem 1 (rough)\n"),
        md("## Problem 2 (rough)\n"),
    ]

def chapter_exercises_solutions_template(title: str):
    return [
        md(f"# {title} – Exercises (Clean Solutions)\n"),
        md("Write polished, final solutions here."),
        md("## Problem 1 – Solution\n"),
        md("## Problem 2 – Solution\n"),
    ]

def chapter_ai_qa_template(title: str):
    return [
        md(f"# {title} – AI Q&A Log\n"),
        md("Use this to paste in questions you asked and the answers you want to keep.\n"),
        md("## Q1 – [date]\n\n**Question:**\n\n...\n\n**Answer (summary or paste):**\n\n..."),
    ]

def chapter_flashcards_template(title: str):
    return [
        md(f"# {title} – Flashcards\n"),
        md("This notebook provides flippable flashcards using `ipywidgets`.\n"),
        code(
            "import random\n"
            "from dataclasses import dataclass\n"
            "from IPython.display import display, Markdown\n"
            "import ipywidgets as widgets\n"
        ),
        code(
            "@dataclass\n"
            "class Card:\n"
            "    front: str\n"
            "    back: str\n\n"
            "cards = [\n"
            "    Card(front=r'State Newton\\'s second law.', back=r'$\\\\vec F = m\\\\vec a$'),\n"
            "    # Add more cards here\n"
            "]"
        ),
        code(
            "current_index = 0\n"
            "showing_front = True\n\n"
            "front_button = widgets.Button(description='Show Front', button_style='primary')\n"
            "back_button = widgets.Button(description='Show Back')\n"
            "next_button = widgets.Button(description='Next Card')\n\n"
            "output = widgets.Output()\n\n"
            "def show_front(idx):\n"
            "    with output:\n"
            "        output.clear_output()\n"
            "        display(Markdown('**Front**:\\n\\n' + cards[idx].front))\n\n"
            "def show_back(idx):\n"
            "    with output:\n"
            "        output.clear_output()\n"
            "        display(Markdown('**Back**:\\n\\n' + cards[idx].back))\n\n"
            "def on_front_click(b):\n"
            "    global showing_front\n"
            "    showing_front = True\n"
            "    show_front(current_index)\n\n"
            "def on_back_click(b):\n"
            "    global showing_front\n"
            "    showing_front = False\n"
            "    show_back(current_index)\n\n"
            "def on_next_click(b):\n"
            "    global current_index, showing_front\n"
            "    current_index = random.randrange(len(cards))\n"
            "    showing_front = True\n"
            "    show_front(current_index)\n\n"
            "front_button.on_click(on_front_click)\n"
            "back_button.on_click(on_back_click)\n"
            "next_button.on_click(on_next_click)\n\n"
            "display(widgets.HBox([front_button, back_button, next_button]))\n"
            "display(output)\n\n"
            "# Show first card initially\n"
            "show_front(current_index)\n"
        ),
    ]

def ai_qa_simple_template(title: str):
    return [
        md(f"# {title} – AI Q&A Log\n"),
        md("## Q1 – [date]\n\n**Question:**\n\n...\n\n**Answer (summary or paste):**\n\n..."),
    ]

def simple_reading_notes_template(title: str):
    return [
        md(f"# {title} – Notes\n"),
        md("Use this notebook to summarize and annotate the material."),
    ]

def simple_flashcards_template(title: str):
    # same as chapter_flashcards_template, but title generic
    cells = chapter_flashcards_template(title)
    cells[0].source = f"# {title} – Flashcards\n"
    return cells

# -------------- main structure creation --------------

ROOT = Path(".")

# Basic definitions of chapter names you can extend later
vol1_chapters = {
    "ch01-atoms-in-motion": "Volume 1, Chapter 1 – Atoms in Motion",
    "ch02-basic-physics": "Volume 1, Chapter 2 – Basic Physics",
    # add more as you go
}

vol2_chapters = {
    "ch01-electromagnetism": "Volume 2, Chapter 1 – Electromagnetism",
    # add more as needed
}

vol3_chapters = {
    "ch01-quantum-behavior": "Volume 3, Chapter 1 – Quantum Behavior",
    # add more as needed
}

def create_volume_structure(volume_dir: Path, chapter_dict: dict):
    ensure_dir(volume_dir)
    # Templates folder
    templates_dir = volume_dir / "templates"
    ensure_dir(templates_dir)

    # Example template notebooks (optional)
    new_notebook(
        chapter_reading_notes_template("Chapter – TEMPLATE"),
        templates_dir / "chapter-notes-template.ipynb",
    )
    new_notebook(
        chapter_flashcards_template("Chapter – TEMPLATE"),
        templates_dir / "flashcards-template.ipynb",
    )

    chapters_dir = volume_dir / "chapters"
    ensure_dir(chapters_dir)

    for ch_slug, title in chapter_dict.items():
        ch_dir = chapters_dir / ch_slug
        ensure_dir(ch_dir)

        new_notebook(chapter_reading_notes_template(title), ch_dir / "01-reading-notes.ipynb")
        new_notebook(chapter_examples_code_template(title), ch_dir / "02-examples-and-code.ipynb")
        new_notebook(chapter_exercises_in_progress_template(title), ch_dir / "03-exercises-in-progress.ipynb")
        new_notebook(chapter_exercises_solutions_template(title), ch_dir / "04-exercises-solutions.ipynb")
        new_notebook(chapter_ai_qa_template(title), ch_dir / "05-ai-qa-log.ipynb")
        new_notebook(chapter_flashcards_template(title), ch_dir / "06-flashcards.ipynb")

        create_gitkeep(ch_dir)


def create_cornell_structure():
    base = ROOT / "cornell-messenger-lectures"
    ensure_dir(base)

    lectures = {
        "lecture01-law-of-gravitation": "Messenger Lecture 1 – The Law of Gravitation",
        "lecture02-symmetry-in-physical-law": "Messenger Lecture 2 – Symmetry in Physical Law",
        "lecture03-the-great-conservation-principles": "Messenger Lecture 3 – The Great Conservation Principles",
        "lecture04-the-quantum-mechanical-view-of-nature": "Messenger Lecture 4 – The Quantum Mechanical View of Nature",
        "lecture05-the-distinction-of-past-and-future": "Messenger Lecture 5 – The Distinction of Past and Future",
        "lecture06-probability-and-uncertainty": "Messenger Lecture 6 – Probability and Uncertainty",
        "lecture07-seeking-new-laws": "Messenger Lecture 7 – Seeking New Laws",
    }

    for slug, title in lectures.items():
        lec_dir = base / slug
        ensure_dir(lec_dir)

        new_notebook(simple_reading_notes_template(title), lec_dir / "01-listening-notes.ipynb")
        new_notebook(chapter_examples_code_template(title), lec_dir / "02-examples-and-code.ipynb")
        new_notebook(ai_qa_simple_template(title), lec_dir / "03-ai-qa-log.ipynb")
        new_notebook(simple_flashcards_template(title), lec_dir / "04-flashcards.ipynb")

        create_gitkeep(lec_dir)


def create_audio_tapes_structure():
    base = ROOT / "flp-audio-recordings"
    ensure_dir(base)

    # You can add more or rename as you discover the exact list
    lectures = {
        "lecture01-atoms-in-motion-1961-09-26": "Audio Lecture 1 – Atoms in Motion (1961-09-26)",
        "lecture02-basic-physics-1961-09-29": "Audio Lecture 2 – Basic Physics (1961-09-29)",
    }

    for slug, title in lectures.items():
        lec_dir = base / slug
        ensure_dir(lec_dir)

        new_notebook(simple_reading_notes_template(title), lec_dir / "01-listening-notes.ipynb")
        new_notebook(ai_qa_simple_template(title), lec_dir / "02-ai-qa-log.ipynb")
        new_notebook(simple_flashcards_template(title), lec_dir / "03-flashcards.ipynb")

        create_gitkeep(lec_dir)


def create_feynman_notes_structure():
    base = ROOT / "feynman-lecture-notes"
    ensure_dir(base)

    by_topic = base / "by-topic"
    ensure_dir(by_topic)

    topics = {
        "mechanics": "Feynman Notes – Mechanics",
        "electromagnetism": "Feynman Notes – Electromagnetism",
        "quantum-mechanics": "Feynman Notes – Quantum Mechanics",
    }

    for slug, title in topics.items():
        tdir = by_topic / slug
        ensure_dir(tdir)
        new_notebook(simple_reading_notes_template(title), tdir / "01-reading-notes.ipynb")
        new_notebook(simple_reading_notes_template(title + " – Crosslinks"), tdir / "02-crosslinks-to-flp.ipynb")
        create_gitkeep(tdir)

    pedagogy = base / "pedagogy"
    ensure_dir(pedagogy)
    new_notebook(simple_reading_notes_template("Feynman – Teaching Philosophy"), pedagogy / "01-teaching-philosophy-notes.ipynb")
    new_notebook(ai_qa_simple_template("Feynman – Teaching Philosophy"), pedagogy / "02-ai-qa-log.ipynb")
    create_gitkeep(pedagogy)


def create_handouts_structure():
    base = ROOT / "original-course-handouts"
    ensure_dir(base)

    for year in ["year1", "year2"]:
        for week in ["week01", "week02"]:
            wdir = base / year / week
            ensure_dir(wdir)

            title = f"Handouts – {year}, {week}"
            new_notebook(simple_reading_notes_template(title), wdir / "01-handout-notes.ipynb")
            new_notebook(chapter_exercises_in_progress_template(title), wdir / "02-problems-in-progress.ipynb")
            new_notebook(chapter_exercises_solutions_template(title), wdir / "03-problems-solutions.ipynb")
            new_notebook(ai_qa_simple_template(title), wdir / "04-ai-qa-log.ipynb")

            create_gitkeep(wdir)


def create_tips_on_physics_structure():
    base = ROOT / "exercises-tips-on-physics"
    ensure_dir(base)

    chapters = {
        "chapter01": "Tips on Physics – Chapter 1",
        "chapter02": "Tips on Physics – Chapter 2",
    }

    for slug, title in chapters.items():
        cdir = base / slug
        ensure_dir(cdir)

        new_notebook(simple_reading_notes_template(title), cdir / "01-reading-notes.ipynb")
        new_notebook(chapter_exercises_in_progress_template(title), cdir / "02-exercises-in-progress.ipynb")
        new_notebook(chapter_exercises_solutions_template(title), cdir / "03-exercises-solutions.ipynb")
        new_notebook(ai_qa_simple_template(title), cdir / "04-ai-qa-log.ipynb")
        new_notebook(simple_flashcards_template(title), cdir / "05-flashcards.ipynb")

        create_gitkeep(cdir)


def create_info_resources_structure():
    base = ROOT / "info-resources"
    ensure_dir(base)

    preface_dir = base / "preface-and-introduction"
    ensure_dir(preface_dir)
    new_notebook(simple_reading_notes_template("Preface and Introduction"), preface_dir / "01-reading-notes.ipynb")
    new_notebook(ai_qa_simple_template("Preface and Introduction"), preface_dir / "02-ai-qa-log.ipynb")
    create_gitkeep(preface_dir)

    history_dir = base / "site-history-and-notes"
    ensure_dir(history_dir)
    new_notebook(simple_reading_notes_template("FLP Site History and Notes"), history_dir / "01-reading-notes.ipynb")
    new_notebook(simple_reading_notes_template("Reflections"), history_dir / "02-reflections.ipynb")
    create_gitkeep(history_dir)


def create_photos_structure():
    base = ROOT / "flp-lecture-photos"
    ensure_dir(base)
    new_notebook(simple_reading_notes_template("Lecture Photos – Notes"), base / "01-photo-notes.ipynb")
    create_gitkeep(base)


def create_learning_tools_structure():
    base = ROOT / "learning-tools"
    flash_dir = base / "flashcards"
    sr_dir = base / "spaced-repetition"

    ensure_dir(flash_dir)
    ensure_dir(sr_dir)

    # Flashcards global template
    new_notebook(simple_flashcards_template("Global Flashcards Template"), flash_dir / "flashcards-template.ipynb")

    # Spaced repetition helper
    cells = [
        md("# Spaced Repetition Helper\n"),
        md("This notebook manages a simple spaced-repetition schedule in a CSV file."),
        code(
            "import pandas as pd\n"
            "from datetime import date, timedelta\n\n"
            "csv_path = 'spaced_cards.csv'\n"
            "try:\n"
            "    df = pd.read_csv(csv_path, parse_dates=['next_review'])\n"
            "except FileNotFoundError:\n"
            "    df = pd.DataFrame(columns=['id', 'question', 'answer', 'interval_days', 'next_review'])\n"
            "    df.to_csv(csv_path, index=False)\n"
            "df.head()"
        ),
        code(
            "def add_card(question, answer, interval_days=1):\n"
            "    global df\n"
            "    today = date.today()\n"
            "    next_review = today + timedelta(days=interval_days)\n"
            "    new = {\n"
            "        'id': len(df),\n"
            "        'question': question,\n"
            "        'answer': answer,\n"
            "        'interval_days': interval_days,\n"
            "        'next_review': next_review,\n"
            "    }\n"
            "    df = pd.concat([df, pd.DataFrame([new])], ignore_index=True)\n"
            "    df.to_csv(csv_path, index=False)\n"
            "\n"
            "# Example:\n"
            "# add_card(\"State Newton's 2nd law.\", r\"$\\\\vec F = m\\\\vec a$\")"
        ),
        code(
            "today = date.today()\n"
            "due = df[df['next_review'] <= pd.to_datetime(today)]\n"
            "due[['id', 'question', 'answer']]"
        ),
        code(
            "def mark_reviewed(card_id, rating):\n"
            "    '''rating: 0 = hard, 1 = okay, 2 = easy'''\n"
            "    global df\n"
            "    row = df.loc[df['id'] == card_id].iloc[0]\n"
            "    if rating == 0:\n"
            "        new_interval = 1\n"
            "    elif rating == 1:\n"
            "        new_interval = max(1, int(row['interval_days'] * 1.5))\n"
            "    else:\n"
            "        new_interval = max(2, int(row['interval_days'] * 2.5))\n\n"
            "    df.loc[df['id'] == card_id, 'interval_days'] = new_interval\n"
            "    df.loc[df['id'] == card_id, 'next_review'] = date.today() + timedelta(days=new_interval)\n"
            "    df.to_csv(csv_path, index=False)\n"
            "\n"
            "# Example usage after testing yourself:\n"
            "# mark_reviewed(card_id=0, rating=2)"
        ),
    ]
    new_notebook(cells, sr_dir / "spaced-repetition-helper.ipynb")

    create_gitkeep(flash_dir)
    create_gitkeep(sr_dir)


def main():
    # Volume structures
    create_volume_structure(ROOT / "volume-1-mechanics-radiation-heat", vol1_chapters)
    create_volume_structure(ROOT / "volume-2-electromagnetism", vol2_chapters)
    create_volume_structure(ROOT / "volume-3-quantum-mechanics", vol3_chapters)

    # Other sections
    create_cornell_structure()
    create_audio_tapes_structure()
    create_feynman_notes_structure()
    create_handouts_structure()
    create_tips_on_physics_structure()
    create_info_resources_structure()
    create_photos_structure()
    create_learning_tools_structure()

    print("Feynman repo structure and notebooks created/updated.")


if __name__ == "__main__":
    main()
