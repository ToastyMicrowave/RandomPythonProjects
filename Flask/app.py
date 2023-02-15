from flask import Flask, render_template

app = Flask(__name__)

def make_bold(html):
   def wrapper():
         return f'<b>{html()}</b>'
   return wrapper

def make_underlined(html):
   def wrapper():
         return f'<u>{html()}</u>'
   return wrapper

def make_emphasis(html):
   def wrapper():
         return f'<em>{html()}</em>'
   return wrapper

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/byelol")
@make_bold
@make_emphasis
@make_underlined
def bye():
   return "Bye!"

if __name__ == "__main__":
    app.run(debug=True)
    
