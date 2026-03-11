from Flask import Flask
app = Flask(_name_)
@app.route('/')
def home():
  return "merhaba , benemirhan!"

