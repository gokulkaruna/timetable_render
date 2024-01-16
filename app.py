from flask import Flask, render_template, request, send_from_directory
import src.generator as gen
import src.export_to_pdf as exp
from flask_cors import CORS

app = Flask(__name__, static_folder='output')
CORS(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def get_formdata():
    flag = True
    teacher_courses = []
    sections = []
    abb = {}

    sec = request.form["sections"].split("\n")
    teach_cour = request.form["teacher_course"].split("\n")

    sections = [[i.strip()] for i in sec]

    for i in teach_cour:
        if len(i.split("-")) == 3:
            teacher, course, abrv = i.split("-")
            teacher_courses.append([teacher.strip(), course.strip()])
            abb[course] = [abrv, teacher]
        else:
            flag = False
            print("hello")
            # return render_template('error.html')
        
    abb["Short Break"] = ["Short Break", "-"]
    abb["Lunch Break"] = ["Lunch Break", "-"]
    abb["None"] = [" ---", "-"]
    x = gen.generate_timetable(sections,teacher_courses)
    exp.export_pdf(x, sections, abb)
    if flag:
        return render_template('timetable.html', sections=sections, teacher_course=teacher_courses)
    else:
        return render_template('error.html')

@app.route('/download')
def download_file():
    return send_from_directory(app.static_folder, 'timetable.pdf',as_attachment=True)
    
if __name__ == '__main__':
    app.run(debug=True)
