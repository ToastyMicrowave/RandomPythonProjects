# Random Python Projects

Some small Python projects I've built over the years including games, a few bots,
some web apps, and one-off scripts.

Everything runs on Python 3.13 (developed on macOS). GUI apps use Tkinter or turtle and
need a desktop session. Anything that sends email or hits an API needs its own `.env`
(copy the project's `.env.example`).

## Projects

| Project | What it is |
| --- | --- |
| [ISS overhead notifier](ISS%20overhead%20notifier/) | Emails me when the ISS is passing overhead at night. Runs on a schedule via GitHub Actions — no server needed. See its [DEPLOY.md](ISS%20overhead%20notifier/DEPLOY.md). |
| [Flash Card app](Flash%20Card%20app/) | Tkinter flashcards for learning French vocabulary. |
| [Flask](Flask/) | A small Flask app, mostly an excuse to play with custom decorators. |
| [Higher Lower](Higher%20Lower/) | The "Higher or Lower" guessing game, web version. |
| [Pomodoro Project](Pomodoro%20Project/) | A Tkinter Pomodoro timer. |
| [Selenium](Selenium/) | An auto-clicker for Cookie Clicker. |
| [Snake game](Snake%20game/) | Classic Snake in turtle graphics. |
| [The Pong game](The%20Pong%20game/) | Classic Pong in turtle graphics. |
| [Websites](Websites/) | Static and Flask website experiments (a CV site and a personal site). |
| [quizzler app](quizzler%20app/) | True/false trivia quiz pulling live questions from the Open Trivia DB API. |

## Standalone scripts

Single-file scripts live in [scripts/](scripts/):

- [Hangman.py](scripts/Hangman.py) — command-line Hangman (word list in `scripts/words.txt`).
- [Electronic Config calc.py](scripts/Electronic%20Config%20calc.py) — works out the electron configuration for a given atomic number.

## Running a project

```bash
cd "<project folder>"
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt    # if the project has one
python main.py
```

The Flask apps start through Flask rather than `python main.py`:

```bash
flask --app app run                # Flask/
flask --app server:server run      # Higher Lower/
```

The ISS notifier isn't really a "run it on your laptop" app — it's wired up to run on a
schedule via GitHub Actions (each run does one check and exits). Its
[DEPLOY.md](ISS%20overhead%20notifier/DEPLOY.md) covers the secrets to set; you can still
run `python main.py` locally for a one-off check.

## Notes

- Secrets live in a git-ignored `.env`. Copy `.env.example`, fill it in, and never commit
  the real thing. For Gmail, use an [App Password](https://myaccount.google.com/apppasswords),
  not your account password.
- Virtualenvs (`.venv/`), caches, and driver binaries are git-ignored — recreate them locally.
- GUI apps (Tkinter/turtle) need a desktop to draw their window.
</content>
</invoke>
