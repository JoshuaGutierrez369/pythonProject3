from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextFieldRect
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import NumericProperty

midterm_mult = 15
finals_mult = 15
MIDTERM = 0
FINALS = 0

project_mult = 30
performance_mult = 20
PROJECT = 0
PERFORMANCE = 0

exercises_mult = 20
EXERCISES = 0



class ProjectApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        self.title = "AGTACalc: CPEN21 Grade Calculator"
        Builder.load_file("helpers.kv")
        return RootWidget()

    def show_alert_dialog1(self):
        close_button = MDFlatButton(text="Yes",
                                    on_press=self.confirm1)
        more_button = MDFlatButton(text="Cancel",
                                   on_press=self.close_dialog)
        self.dialog = MDDialog(title="        Confirmation",
                               text="Are the provided data final?",
                               size_hint=(0.7, 0.3), elevation=0,
                               buttons=[close_button, more_button])
        self.dialog.open()

    def confirm1(self, obj):
        global midterm_mult, finals_mult, MIDTERM, FINALS
        if self.root.get_screen('assessments').ids.midterm_written.text:
            mw = float(self.root.get_screen('assessments').ids.midterm_written.text)
        else:
            mw = 0
        if self.root.get_screen('assessments').ids.midterm_practical.text:
            mh = float(self.root.get_screen('assessments').ids.midterm_practical.text)
        else:
            mh = 0
        if self.root.get_screen('assessments').ids.final_written.text:
            fw = float(self.root.get_screen('assessments').ids.final_written.text)
        else:
            fw = 0
        if self.root.get_screen('assessments').ids.final_practical.text:
            fh = float(self.root.get_screen('assessments').ids.final_practical.text)
        else:
            fh = 0
        if self.root.get_screen('assessments').ids.midterm_written_multiplier.text:
            mwm = int(self.root.get_screen('assessments').ids.midterm_written_multiplier.text)
        else:
            mwm = 6
        if self.root.get_screen('assessments').ids.midterm_practical_multiplier.text:
            mhm = int(self.root.get_screen('assessments').ids.midterm_practical_multiplier.text)
        else:
            mhm = 9
        if self.root.get_screen('assessments').ids.final_written_multiplier.text:
            fwm = int(self.root.get_screen('assessments').ids.final_written_multiplier.text)
        else:
            fwm = 6
        if self.root.get_screen('assessments').ids.final_practical_multiplier.text:
            fhm = int(self.root.get_screen('assessments').ids.final_practical_multiplier.text)
        else:
            fhm = 9

        midterm_mult = round((mwm + mhm), 2)
        finals_mult = round((fwm + fhm), 2)

        midterm_written = mw * mwm / 100
        midterm_practical = mh * mhm / 100
        final_written = fw * fwm / 100
        final_practical = fh * fhm / 100

        MIDTERM = midterm_written + midterm_practical
        FINALS = final_written + final_practical

        self.dialog.dismiss()

        return midterm_mult, finals_mult, MIDTERM, FINALS

    def callback1(self):
        self.root.current = 'performance'

    def show_alert_dialog2(self):
        close_button = MDFlatButton(text="Yes",
                                    on_press=self.confirm2)
        more_button = MDFlatButton(text="Cancel",
                                   on_press=self.close_dialog)
        self.dialog = MDDialog(title="        Confirmation",
                               text="Are the provided data final?",
                               size_hint=(0.7, 0.3), elevation=0,
                               buttons=[close_button, more_button])
        self.dialog.open()

    def confirm2(self, obj):
        global performance_mult, PERFORMANCE, PROJECT, project_mult
        if self.root.get_screen('performance').ids.days.text:
            total = int(self.root.get_screen('performance').ids.days.text)
        else:
            total = 30
        if self.root.get_screen('performance').ids.late.text:
            late = int(self.root.get_screen('performance').ids.late.text)
        else:
            late = 0
        if self.root.get_screen('performance').ids.absent.text:
            absent = int(self.root.get_screen('performance').ids.absent.text)
        else:
            absent = total
        if self.root.get_screen('performance').ids.attendance_multiplier.text:
            am = int(self.root.get_screen('performance').ids.attendance_multiplier.text)
        else:
            am = 5

        ATTENDANCE = am * (total - absent - late / 2) / total

        if self.root.get_screen('performance').ids.professor.text:
            professor = float(self.root.get_screen('performance').ids.professor.text)
        else:
            professor = 0
        if self.root.get_screen('performance').ids.student.text:
            student = float(self.root.get_screen('performance').ids.student.text)
        else:
            student = 0
        if self.root.get_screen('performance').ids.materials.text:
            materials = float(self.root.get_screen('performance').ids.materials.text)
        else:
            materials = 0
        if self.root.get_screen('performance').ids.participation_multiplier.text:
            pm = int(self.root.get_screen('performance').ids.participation_multiplier.text)
        else:
            pm = 15

        PARTICIPATION = pm * (professor + student + materials) / 300

        performance_mult = am + pm
        PERFORMANCE = ATTENDANCE + PARTICIPATION

        if self.root.get_screen('performance').ids.capsule.text:
            capsule = float(self.root.get_screen('performance').ids.capsule.text)
        else:
            capsule = 0
        if self.root.get_screen('performance').ids.proposal.text:
            proposal = float(self.root.get_screen('performance').ids.proposal.text)
        else:
            proposal = 0
        if self.root.get_screen('performance').ids.final.text:
            final = float(self.root.get_screen('performance').ids.final.text)
        else:
            final = 0
        if self.root.get_screen('performance').ids.project_multiplier.text:
            project_mult = int(self.root.get_screen('performance').ids.project_multiplier.text)
        else:
            project_mult = 30
        PROJECT = project_mult * (capsule + proposal + final) / 300

        self.dialog.dismiss()

    def callback2(self):
        self.root.current = 'reports'

    def show_alert_dialog3(self):
        close_button = MDFlatButton(text="Yes",
                                    on_press=self.confirm3)
        more_button = MDFlatButton(text="Cancel",
                                   on_press=self.close_dialog)
        self.dialog = MDDialog(title="        Confirmation",
                               text="Are the provided data final?",
                               size_hint=(0.7, 0.3), elevation=0,
                               buttons=[close_button, more_button])
        self.dialog.open()

    def confirm3(self, obj):
        global EXERCISES, exercises_mult
        if self.root.get_screen('reports').ids.ex1.text:
            ex1 = float(self.root.get_screen('reports').ids.ex1.text)
        else:
            ex1 = 0
        if self.root.get_screen('reports').ids.ex2.text:
            ex2 = float(self.root.get_screen('reports').ids.ex2.text)
        else:
            ex2 = 0
        if self.root.get_screen('reports').ids.ex3.text:
            ex3 = float(self.root.get_screen('reports').ids.ex3.text)
        else:
            ex3 = 0
        if self.root.get_screen('reports').ids.ex4.text:
            ex4 = float(self.root.get_screen('reports').ids.ex4.text)
        else:
            ex4 = 0
        if self.root.get_screen('reports').ids.ex5.text:
            ex5 = float(self.root.get_screen('reports').ids.ex5.text)
        else:
            ex5 = 0
        if self.root.get_screen('reports').ids.ex6.text:
            ex6 = float(self.root.get_screen('reports').ids.ex6.text)
        else:
            ex6 = 0
        if self.root.get_screen('reports').ids.ex7.text:
            ex7 = float(self.root.get_screen('reports').ids.ex7.text)
        else:
            ex7 = 0
        if self.root.get_screen('reports').ids.ex8.text:
            ex8 = float(self.root.get_screen('reports').ids.ex8.text)
        else:
            ex8 = 0
        if self.root.get_screen('reports').ids.ex9.text:
            ex9 = float(self.root.get_screen('reports').ids.ex9.text)
        else:
            ex9 = 0
        if self.root.get_screen('reports').ids.ex10.text:
            ex10 = float(self.root.get_screen('reports').ids.ex10.text)
        else:
            ex10 = 0
        if self.root.get_screen('reports').ids.ex11.text:
            ex11 = float(self.root.get_screen('reports').ids.ex11.text)
        else:
            ex11 = 0
        if self.root.get_screen('reports').ids.ex12.text:
            ex12 = float(self.root.get_screen('reports').ids.ex12.text)
        else:
            ex12 = 0
        if self.root.get_screen('reports').ids.ex13.text:
            ex13 = float(self.root.get_screen('reports').ids.ex13.text)
        else:
            ex13 = 0
        if self.root.get_screen('reports').ids.ex14.text:
            ex14 = float(self.root.get_screen('reports').ids.ex14.text)
        else:
            ex14 = 0
        if self.root.get_screen('reports').ids.exercises_multiplier.text:
            exercises_mult = int(self.root.get_screen('reports').ids.exercises_multiplier.text)
        else:
            exercises_mult = 20

        exercises_sum = ex1 + ex2 + ex3 + ex4 + ex5 + ex6 + ex7 + ex8 + ex9 + ex10 + ex11 + ex12 + ex13 + ex14
        EXERCISES = exercises_mult * exercises_sum / 1400

        self.dialog.dismiss()

    def callback3(self):
        self.root.current = 'results'

    def callback4(self):
        self.root.current = 'assessments'

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def clear_inputs(self):
        self.root.get_screen('assessments').ids.midterm_written.text = ''
        self.root.get_screen('assessments').ids.midterm_practical.text = ''
        self.root.get_screen('assessments').ids.final_written.text = ''
        self.root.get_screen('assessments').ids.final_practical.text = ''
        self.root.get_screen('assessments').ids.midterm_written_multiplier.text = ''
        self.root.get_screen('assessments').ids.midterm_practical_multiplier.text = ''
        self.root.get_screen('assessments').ids.final_written_multiplier.text = ''
        self.root.get_screen('assessments').ids.final_practical_multiplier.text = ''

        self.root.get_screen('performance').ids.days.text = ''
        self.root.get_screen('performance').ids.late.text = ''
        self.root.get_screen('performance').ids.absent.text = ''
        self.root.get_screen('performance').ids.attendance_multiplier.text = ''
        self.root.get_screen('performance').ids.professor.text = ''
        self.root.get_screen('performance').ids.student.text = ''
        self.root.get_screen('performance').ids.materials.text = ''
        self.root.get_screen('performance').ids.participation_multiplier.text = ''
        self.root.get_screen('performance').ids.capsule.text = ''
        self.root.get_screen('performance').ids.proposal.text = ''
        self.root.get_screen('performance').ids.final.text = ''
        self.root.get_screen('performance').ids.project_multiplier.text = ''

        self.root.get_screen('reports').ids.ex1.text = ''
        self.root.get_screen('reports').ids.ex2.text = ''
        self.root.get_screen('reports').ids.ex3.text = ''
        self.root.get_screen('reports').ids.ex4.text = ''
        self.root.get_screen('reports').ids.ex5.text = ''
        self.root.get_screen('reports').ids.ex6.text = ''
        self.root.get_screen('reports').ids.ex7.text = ''
        self.root.get_screen('reports').ids.ex8.text = ''
        self.root.get_screen('reports').ids.ex9.text = ''
        self.root.get_screen('reports').ids.ex10.text = ''
        self.root.get_screen('reports').ids.ex11.text = ''
        self.root.get_screen('reports').ids.ex12.text = ''
        self.root.get_screen('reports').ids.ex13.text = ''
        self.root.get_screen('reports').ids.ex14.text = ''
        self.root.get_screen('reports').ids.exercises_multiplier.text = ''


class SummaryScreen(Screen):
    if midterm_mult:
        pass
    else:
        midterm_mult = NumericProperty(15)
    if finals_mult:
        pass
    else:
        finals_mult = NumericProperty(15)
    if MIDTERM:
        pass
    else:
        MIDTERM = NumericProperty(0)
    if FINALS:
        pass
    else:
        FINALS = NumericProperty(0)

    if project_mult:
        pass
    else:
        project_mult = NumericProperty(30)
    if performance_mult:
        pass
    else:
        performance_mult = NumericProperty(20)
    if PROJECT:
        pass
    else:
        PROJECT = NumericProperty(0)
    if PERFORMANCE:
        pass
    else:
        PERFORMANCE = NumericProperty(0)

    if exercises_mult:
        pass
    else:
        exercises_mult = NumericProperty(20)
    if EXERCISES:
        pass
    else:
        EXERCISES = NumericProperty(0)

    def load_screen(self):
        layout = AnchorLayout()
        self.grade = MDTextFieldRect(size_hint=(0.25, 0.04),
                                     pos_hint={"x": 0.625, "y": 0.2425},

                                     font_size='20sp',
                                     foreground_color=(0.12, 0.58, 0.95, 1))
        self.transmutation = MDTextFieldRect(size_hint=(0.25, 0.04),
                                             pos_hint={"x": 0.625, "y": 0.16},
                                             font_size='20sp',
                                             foreground_color=(0.12, 0.58, 0.95, 1))

        final_grade = round((MIDTERM + FINALS + PERFORMANCE + PROJECT + EXERCISES), 3)
        self.grade.text = f"  {final_grade}"
        self.add_widget(self.grade)

        if final_grade >= 290 / 3:
            self.transmutation.text = "  1.00"
        elif 290 / 3 > final_grade >= 280 / 3:
            self.transmutation.text = "  1.25"
        elif 280 / 3 > final_grade >= 90:
            self.transmutation.text = "  1.50"
        elif 90 > final_grade >= 260 / 3:
            self.transmutation.text = "  1.75"
        elif 260 / 3 > final_grade >= 250 / 3:
            self.transmutation.text = "  2.00"
        elif 250 / 3 > final_grade >= 80:
            self.transmutation.text = "  2.25"
        elif 80 > final_grade >= 230 / 3:
            self.transmutation.text = "  2.50"
        elif 230 / 3 > final_grade >= 220 / 3:
            self.transmutation.text = "  2.75"
        elif 220 / 3 > final_grade >= 70:
            self.transmutation.text = "  3.00"
        elif 70 > final_grade:
            self.transmutation.text = "  5.00"
        self.add_widget(self.transmutation)
        return layout

    def load_table(self):
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.61, "center_x": 0.5},
            size_hint=(0.90, 0.45),
            column_data=[
                ("Criteria", dp(27)),
                ("Max %", dp(15)),
                ("Overall %", dp(15)),
            ],
            row_data=[("Midterm Exams", round(midterm_mult, 2), round(MIDTERM, 2)),
                      ("Final Exams", round(finals_mult, 2), round(FINALS, 2)),
                      ("Class Performance", round(performance_mult, 2), round(PERFORMANCE, 2)),
                      ("Project", round(project_mult, 2), round(PROJECT, 2)),
                      ("Exercises", round(exercises_mult, 2), round(EXERCISES, 2))]
        )
        self.add_widget(self.data_tables)
        return layout

    def on_enter(self):
        self.load_screen()
        self.load_table()


class RootWidget(ScreenManager):
    pass


class ExamScreen(Screen):
    pass


class AttendanceScreen(Screen):
    pass


class ReportsScreen(Screen):
    pass


if __name__ == "__main__":
    ProjectApp().run()
