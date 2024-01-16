import fpdf

def export_pdf(all_classes_timetable_array, sections, abreviations):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    timing = ["08:00 - 09:00", "09:00 - 10:00", "10:00 - 10:30", "10:30 - 11:30", "11:30 - 12:30", "12:30 - 13:15", "13:15 - 14:15", "14:15 - 15:15"]
    dummy = ["Course", "Abbreviation", "Faculty"]
    sec = sections
    legend = []
    for _i in list(abreviations.keys()):
        legend.append([_i, abreviations[_i][0], abreviations[_i][1]])


    pdf = fpdf.FPDF(format='a4')    

    for time_table in range(len(sections)):
        pdf.add_page()
        pdf.set_font("Arial", 'B', size = 25)

        pdf.ln()
        pdf.ln()
        main_title = "PES University"
        pdf.write(5, main_title)
        pdf.ln()
        pdf.ln()
        pdf.ln()
        pdf.ln()
        


        # Set desired "resolution" of printed grid
        rows_per_page = 6
        cols_per_page = 9

        # Calculate dimensions of print-able area
        print_h = pdf.h - pdf.t_margin - pdf.b_margin
        print_w = pdf.w - pdf.l_margin - pdf.r_margin
        # Actual size of grid cells on the page is available space divided by desired resolution, in each dimension
        c_h = (print_h / rows_per_page) - 30
        c_w = (print_w / cols_per_page)
        
        pdf.set_font("Arial", 'B', size = 10)
        title = 'Timetable for : ' + sec[time_table][0]
        pdf.write(5, title)
        pdf.ln()
        pdf.ln()
        pdf.ln()
        pdf.ln()
        pdf.ln()
        
        pdf.set_draw_color(255, 0, 0)
        pdf.set_line_width(1)
        pdf.rect(0, 0, pdf.w, pdf.h, "D")

        pdf.set_draw_color(0, 0, 0)
        pdf.set_line_width(0.2)
        pdf.rect(0.5, 0.5, pdf.w - 0.5, pdf.h - 0.5, "D")
        for i in range(rows_per_page):
            x = 0
            for j in range(cols_per_page):
                if i == 0 and j >= 1:
                    pdf.set_font("Arial", 'B', size = 8)
                    s = timing[j - 1]
                    pdf.cell(c_w, c_h, s, border=1, ln=0, align="C")
                elif j == 0 and i == 0:
                    pdf.set_font("Arial", 'B', size = 10)
                    s = "Days\\Time"
                    pdf.cell(c_w, c_h, s, border=1, ln=0, align="C")
                elif j == 0 and i >= 1 :
                    pdf.set_font("Arial", 'B', size = 8)
                    s = days[i-1]
                    pdf.cell(c_w, c_h, s, border=1, ln=0, align="C")
                else:
                    pdf.set_font("Arial", size=7)
                    s = abreviations[str(all_classes_timetable_array[time_table][i-1][x]).split(':')[0]][0]
                    x+=1
                    pdf.cell(c_w, c_h, s, border=1, ln=0, align="C")
            pdf.ln()

        pdf.ln()
        pdf.ln()

        rows = len(sections) + 1
        cols = 3
        # Calculate dimensions of print-able area
        print_h = pdf.h - pdf.t_margin - pdf.b_margin
        print_w = pdf.w - pdf.l_margin - pdf.r_margin
        # Actual size of grid cells on the page is available space divided by desired resolution, in each dimension
        c_h = (print_h / rows) - 40
        c_w = (print_w / cols)
        
        pdf.set_draw_color(255, 0, 0)
        pdf.set_line_width(1)
        pdf.rect(0, 0, pdf.w, pdf.h, "D")

        pdf.set_draw_color(0, 0, 0)
        pdf.set_line_width(0.2)
        pdf.rect(0.5, 0.5, pdf.w - 0.5, pdf.h - 0.5, "D")
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j >=0:
                    pdf.set_font("Arial", 'B', size = 10)
                    s = dummy[j]
                    pdf.cell(c_w, c_h, s, border=1, ln=0, align="C")
                else:
                    pdf.set_font("Arial", size=7)
                    s = legend[i-1][j]
                    x+=1
                    pdf.cell(c_w, c_h, s, border=1, ln=0, align="C")
            pdf.ln()


    pdf.output("./output/timetable.pdf")
