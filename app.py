from Flask import Flask
app = Flask(_name_)
@app.route('/')
def home():
  return "merhaba , guys!"


@app.route ('/about')
def about():
  return "hakkımda"

