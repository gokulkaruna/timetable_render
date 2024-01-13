from flask import Flask, render_template, request, send_file, send_from_directory
import src.generator as gen
import src.export_to_pdf as exp

import os 
print(os.getcwd())
app = Flask(__name__, static_folder='output')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def get_formdata():
    if request.method == "POST":

        print(request.form)
        print(request.form["sections"])
        print(type(request.form["sections"]))
        print(request.form["teacher_course"])

        teacher_courses = []
        sections = []
        abb = {}

        sec = request.form["sections"].split("\n")
        teach_cour = request.form["teacher_course"].split("\n")

        sections = [[i.strip()] for i in sec]

        for i in teach_cour:
            teacher, course, abrv = i.split("-")
            teacher_courses.append([teacher.strip(), course.strip()])
            abb[course] = [abrv, teacher]

        print(sections)
        print(teacher_courses)
        abb["Short Break"] = ["Short Break", "-"]
        abb["Lunch Break"] = ["Lunch Break", "-"]
        abb["None"] = [" ---", "-"]
        x = gen.generate_timetable(sections,teacher_courses)
        print(x)
        exp.export_pdf(x, sections, abb)



    return render_template('timetable.html', sections=sections, teacher_course=teacher_courses)

@app.route('/download')
def download_file():
    path = '/test.pdf'
    return send_from_directory(app.static_folder, 'timetable.pdf')
    
if __name__ == '__main__':
    app.run(debug=True)
