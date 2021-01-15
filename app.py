from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello():
  if request.method == "GET":
    return render_template('index.html')
  if request.method == "POST":
    print(request.form)
    d = request.form.to_dict(flat=True) or {}
    return d

if __name__ == '__main__':
    app.run()
