from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='templates')
task =["test"]

@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add/<task_name>')
def add(task_name):
    task.append(task_name)

    return jsonify(task)

@app.route('/remove/<task_name>')
def remove(task_name):
    removed_task= task.pop(task.index(task_name))

    return jsonify(removed_task)

if __name__ == '__main__':
    app.run()