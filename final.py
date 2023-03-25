from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField, MDTextFieldRect
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout


class ExamScreen(Screen):
    pass


class AssignmentScreen(Screen):
    pass


class ProjectScreen(Screen):
    pass


class SummaryScreen(Screen):
    def load_screen(self):
        layout = AnchorLayout()
        self.grade = MDTextFieldRect(size_hint=(0.23, 0.06),
                                     pos_hint={"x": 0.625, "y": 0.2425},
                                     font_size=20,
                                     foreground_color=(0.12, 0.58, 0.95, 1))
        self.transmutation = MDTextFieldRect(size_hint=(0.2, 0.06),
                                             pos_hint={"x": 0.625, "y": 0.16},
                                             font_size=20,
                                             foreground_color=(0.12, 0.58, 0.95, 1))

        FINAL_GRADE = round(((MIDTERM_EXAM + EXERCISES + ASSIGNMENTS + PROJECT) * 0.75 + FINAL_EXAM * 0.25), 2)
        self.grade.text = f"  {FINAL_GRADE}"
        self.add_widget(self.grade)

        if FINAL_GRADE >= 290 / 3:
            self.transmutation.text = "  1.00"
        elif 290 / 3 > FINAL_GRADE >= 280 / 3:
            self.transmutation.text = "  1.25"
        elif 280 / 3 > FINAL_GRADE >= 90:
            self.transmutation.text = "  1.50"
        elif 90 > FINAL_GRADE >= 260 / 3:
            self.transmutation.text = "  1.75"
        elif 260 / 3 > FINAL_GRADE >= 250 / 3:
            self.transmutation.text = "  2.00"
        elif 250 / 3 > FINAL_GRADE >= 80:
            self.transmutation.text = "  2.25"
        elif 80 > FINAL_GRADE >= 230 / 3:
            self.transmutation.text = "  2.50"
        elif 230 / 3 > FINAL_GRADE >= 220 / 3:
            self.transmutation.text = "  2.75"
        elif 220 / 3 > FINAL_GRADE >= 70:
            self.transmutation.text = "  3.00"
        elif 70 > FINAL_GRADE:
            self.transmutation.text = "  5.00"
        self.add_widget(self.transmutation)
        return layout

    def load_table(self):
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.62, "center_x": 0.5},
            size_hint=(0.9, 0.536),
            use_pagination=True,
            rows_num=4,
            pagination_menu_height='60dp',
            column_data=[
                ("Criteria", dp(27)),
                ("Max %", dp(15)),
                ("Rating %", dp(15)),
                ("Overall %", dp(15)),
            ],
            row_data=[("Midterm Exam", f"{mem}", f"{MIDTERM_EXAM}", f"{round(MIDTERM_EXAM * 0.75, 2)}"),
                      ("Exercises", f"{exm}", f"{EXERCISES}", f"{round(EXERCISES * 0.75, 2)}"),
                      ("Assignments", f"{am}", f"{ASSIGNMENTS}", f"{round(ASSIGNMENTS * 0.75, 2)}"),
                      ("Project", f"{pjm}", f"{PROJECT}", f"{round(PROJECT * 0.75, 2)}"),
                      ("Final Exam", f"{fem}", f"{FINAL_EXAM}", f"{round(FINAL_EXAM * 0.25, 2)}")]
        )
        self.add_widget(self.data_tables)
        return layout

    def on_enter(self):
        self.load_screen()
        self.load_table()


class RootWidget(ScreenManager):
    pass


class ProjectApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        self.title = "CPEN21A Grade Calculator"
        Builder.load_file("helpers.kv")
        Window.size = (350, 600)
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
        global mem, MIDTERM_EXAM, fem, FINAL_EXAM
        mw = int(self.root.get_screen('assessments').ids.midterm_written.text)
        mh = int(self.root.get_screen('assessments').ids.midterm_handson.text)
        fw = int(self.root.get_screen('assessments').ids.final_written.text)
        fh = int(self.root.get_screen('assessments').ids.final_handson.text)
        mwm = int(self.root.get_screen('assessments').ids.midterm_written_multiplier.text)
        mhm = int(self.root.get_screen('assessments').ids.midterm_handson_multiplier.text)
        mem = round((mwm + mhm), 2)
        fwm = int(self.root.get_screen('assessments').ids.final_written_multiplier.text) / 0.25
        fhm = int(self.root.get_screen('assessments').ids.final_handson_multiplier.text) / 0.25
        fem = round((fwm + fhm), 2)
        Midterm_Written = mw * mwm / 100
        Midterm_Handson = mh * mhm / 100
        Final_Written = fw * fwm / 100
        Final_Handson = fh * fhm / 100

        MIDTERM_EXAM = round((Midterm_Written + Midterm_Handson), 2)
        FINAL_EXAM = round((Final_Written + Final_Handson), 2)
        self.dialog.dismiss()

    def callback1(self):
        self.root.current = 'laboratory'

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
        global am, ASSIGNMENTS
        MCO1 = int(self.root.get_screen('laboratory').ids.mco1.text)
        MCO2 = int(self.root.get_screen('laboratory').ids.mco2.text)
        MCO3 = int(self.root.get_screen('laboratory').ids.mco3.text)
        MCO4 = int(self.root.get_screen('laboratory').ids.mco4.text)
        MCO5 = int(self.root.get_screen('laboratory').ids.mco5.text)
        MCO6 = int(self.root.get_screen('laboratory').ids.mco6.text)
        MCO7 = int(self.root.get_screen('laboratory').ids.mco7.text)
        am = round(int(self.root.get_screen('laboratory').ids.assignment_multiplier.text), 2)

        ASSIGNMENTS = round(am * (MCO1 + MCO2 + MCO3 + MCO4 + MCO5 + MCO6 + MCO7) / 700, 2)
        self.dialog.dismiss()

    def callback2(self):
        self.root.current = 'performance'

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
        global EXERCISES, exm, PROJECT, pjm
        EX1 = int(self.root.get_screen('performance').ids.ex1.text)
        EX2 = int(self.root.get_screen('performance').ids.ex2.text)
        EX3 = int(self.root.get_screen('performance').ids.ex3.text)
        EX4 = int(self.root.get_screen('performance').ids.ex4.text)
        EX5 = int(self.root.get_screen('performance').ids.ex5.text)
        EX6 = int(self.root.get_screen('performance').ids.ex6.text)
        exm = round(int(self.root.get_screen('performance').ids.exercises_multiplier.text), 2)

        CAPSULE = int(self.root.get_screen('performance').ids.capsule.text)
        PROPOSAL = int(self.root.get_screen('performance').ids.proposal.text)
        FINAL = int(self.root.get_screen('performance').ids.final.text)
        pjm = round(int(self.root.get_screen('performance').ids.project_multiplier.text), 2)

        EXERCISES = round(exm * (EX1 + EX2 + EX3 + EX4 + EX5 + EX6) / 600, 2)
        PROJECT = round(pjm * (CAPSULE + PROPOSAL + FINAL) / 300, 2)

        self.dialog.dismiss()

    def callback3(self):
        self.root.current = 'results'

    def callback4(self):
        self.root.current = 'assessments'

    def clear_text_fields(self, *args):
        text_fields = self.root.get_all_md_textfields()
        for text_field in text_fields:
            text_field.text = ""

    def close_dialog(self, obj):
        self.dialog.dismiss()


class MDTextFieldHelper:
    @staticmethod
    def get_all_fields(widget=None, results=None):
        if widget is None:
            widget = MDApp.get_running_app().root
        if results is None:
            results = []

        if isinstance(widget, MDTextField):
            results.append(widget)

        for child in widget.children:
            MDTextFieldHelper.get_all_fields(child, results)
        return results


if __name__ == "__main__":
    ProjectApp().run()
