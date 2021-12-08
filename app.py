from flask import Flask, request, render_template
from db_functions import get_groups
from db_functions import get_timetable_by_group
from db_functions import get_teachers

app = Flask(__name__)


@app.route('/')
def get_timetable_group():
    timetable = [[f"({i}, {j})" for j in range(1, 9)] for i in range(1, 7)]
    groups = get_groups()
    return render_template(
        'timetable_gr.html',
        groups=groups,
        timetable=timetable,
    )


@app.route('/choice-group', methods=['POST'])
def get_timetable_for_group():
    group = request.form['group']
    timetable = get_timetable_by_group(group)


@app.route('/temp')
def hello_world():  # put application's code here
    return render_template(
        'add_subjects.html',
        groups=get_groups(),
        # нужно пробросить список учителей
        teachers=get_teachers(),
    )


@app.route('/add_course', methods=['POST'])
def function():
    print(request.form['group'], request.form['title'], request.form['type-stream'])
    return render_template(
        'add_subjects.html',
        groups=get_groups()
    )


if __name__ == '__main__':
    app.run()
