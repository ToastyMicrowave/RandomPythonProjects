import flask, random

server = flask.Flask(__name__)

RAND_NUM = random.randrange(10)

def rand_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def html_converter(func):
    def wrapper(*args, **kwargs):
        data = func(**kwargs).split(";")
        text = data[0]
        img = data[1]
        return f"<h1 style='color:{rand_color()}'>{text}</h1><br><img src={img}>"
    wrapper.__name__ = func.__name__
    return wrapper

@server.route("/")
@html_converter
def home():
    return "Guess a number between 0 to 9;https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"

@server.route("/<int:num>")
@html_converter
def guess(num):
    if num > RAND_NUM:
        return "Too high, try again!;https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
    elif num < RAND_NUM:
        return "Too low, try again!;https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
    else:
        return "You found me!;https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"