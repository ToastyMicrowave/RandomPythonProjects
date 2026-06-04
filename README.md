# Random Python Projects

A personal collection of small Python projects, games, bots, and web apps — mostly built while learning.

All projects were tested on **Python 3.13 (macOS)** and currently run. ✅ = verified working; notes call out anything you need to supply (a `.env`, a display, etc.).

## Projects

| Project | What it is | Status |
| --- | --- | --- |
| [Amazon Price checker](Amazon%20Price%20checker/) | Scrapes an Amazon product page and emails you when the price drops. | ⚠️ Runs, but fragile — needs `.env` (`EMAIL`/`PASSWORD`); depends on Amazon not serving a CAPTCHA. |
| [Flash Card app](Flash%20Card%20app/) | Tkinter flashcard app for learning French vocabulary. | ✅ Works (GUI). |
| [Flask](Flask/) | A small Flask web app with custom decorators. | ✅ Works — `flask --app app run`. |
| [Higher Lower](Higher%20Lower/) | The "Higher or Lower" guessing game (web version). | ✅ Works — `flask --app server:server run`. |
| [ISS overhead notifier](ISS%20overhead%20notifier/) | Emails you when the ISS passes overhead at night. | ✅ Works — needs `.env` (`EMAIL`/`PASSWORD`) to send mail. |
| [Pomodoro Project](Pomodoro%20Project/) | Tkinter Pomodoro timer. | ✅ Works (GUI). |
| [Selenium](Selenium/) | Auto-clicker for the Cookie Clicker game. | ✅ Works — opens Firefox; Selenium Manager handles the driver automatically. |
| [Snake game](Snake%20game/) | Classic Snake, built with turtle graphics. | ✅ Works (GUI). |
| [The Pong game](The%20Pong%20game/) | Classic Pong, built with turtle graphics. | ✅ Works (GUI). |
| [Websites](Websites/) | Static/Flask website experiments (CV site, personal site). | ✅ Works (static HTML; `CV website/main.py` prints sample markup). |
| [quizzler app](quizzler%20app/) | True/False trivia quiz pulling live questions from the Open Trivia DB API. | ✅ Works (GUI + live API). |

> **Reddit Bot** lives in its own separate git repository inside this folder and is intentionally ignored here.

## Standalone scripts

Single-file scripts live in [scripts/](scripts/):

| Script | What it does | Status |
| --- | --- | --- |
| [Hangman.py](scripts/Hangman.py) | Command-line Hangman game (words in `scripts/words.txt`). | ✅ Works (CLI). |
| [Electronic Config calc.py](scripts/Electronic%20Config%20calc.py) | Calculates the electron configuration for a given atomic number. | ✅ Works (CLI). |

## Running a project

```bash
cd "<project folder>"
python3 -m venv .venv          # create a virtual environment (ignored by git)
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt   # if the project has one
python main.py                 # GUI/CLI apps
```

For the Flask web apps, start them with Flask instead of `python main.py`:

```bash
flask --app app run            # Flask/
flask --app server:server run  # Higher Lower/
```

Projects that talk to email/APIs (Amazon Price checker, ISS overhead notifier) need a `.env` file — copy the project's `.env.example` and fill in your own values. Use a Gmail **App Password**, not your normal password.

## Notes

- Secrets (API keys, tokens) belong in a `.env` file, which is git-ignored. Never commit them.
- Virtual environments (`.venv/`), caches, and driver binaries (`geckodriver`, `*.exe`) are git-ignored — recreate/download them locally as needed.
- GUI apps (Tkinter/turtle) need a desktop session to display their window.
