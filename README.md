# Random Python Projects

A personal collection of small Python projects, games, bots, and web apps — mostly built while learning.

## Projects

| Project | What it is |
| --- | --- |
| [Amazon Price checker](Amazon%20Price%20checker/) | Scrapes an Amazon product page and alerts when the price drops. |
| [Flash Card app](Flash%20Card%20app/) | Tkinter flashcard app for learning French vocabulary. |
| [Flask](Flask/) | A small Flask web app. |
| [Higher Lower](Higher%20Lower/) | The "Higher or Lower" guessing game (server version). |
| [ISS overhead notifier](ISS%20overhead%20notifier/) | Emails you when the ISS passes overhead during the night. |
| [Pomodoro Project](Pomodoro%20Project/) | Tkinter Pomodoro timer. |
| [Selenium](Selenium/) | Selenium automation experiments. |
| [Snake game](Snake%20game/) | Classic Snake, built with turtle graphics. |
| [The Pong game](The%20Pong%20game/) | Classic Pong, built with turtle graphics. |
| [Websites](Websites/) | Static/Flask website experiments (CV site, personal site). |
| [quizzler app](quizzler%20app/) | Quiz app that pulls trivia questions from an API. |

> **Reddit Bot** lives in its own separate git repository inside this folder and is intentionally ignored here.

## Standalone scripts

Single-file scripts live in [scripts/](scripts/):

| Script | What it does |
| --- | --- |
| [Hangman.py](scripts/Hangman.py) | Command-line Hangman game (words in `scripts/words.txt`). |
| [Electronic Config calc.py](scripts/Electronic%20Config%20calc.py) | Calculates the electron configuration for a given atomic number. |
| [old.py](scripts/old.py) | Old Selenium scratch script, kept for reference. |

## Running a project

Most projects are self-contained. A typical workflow:

```bash
cd "<project folder>"
python -m venv .venv          # create a virtual environment (ignored by git)
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt   # if the project has one
python main.py
```

## Notes

- Secrets (API keys, tokens) belong in a `.env` file, which is git-ignored. Never commit them.
- Virtual environments (`.venv/`), caches, and driver binaries (`geckodriver`, `*.exe`) are git-ignored — recreate/download them locally as needed.
