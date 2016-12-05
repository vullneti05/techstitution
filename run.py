from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html')
  elif request.method == 'POST':
    error = ""
    field1 = request.form['field1']
    field2 = request.form['field2']
    if len(field1) < 6 or len(field2) < 6:
      error = "Filan, te lutem shkruaj me shume se 6 karaktere."
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5555)
