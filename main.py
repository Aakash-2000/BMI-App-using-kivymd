from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton, MDRoundFlatIconButton
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.screen import Screen
from kivymd.font_definitions import theme_font_styles
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog

global name
global height
global weight

tool_bar = """
BoxLayout:
    orientation: 'vertical'
    
    MDToolbar:
        title: 'BMI Calculator'
        left_action_items:[["calculator",lambda x:app.nothing()]]
        elevation:5
          
    Widget:


"""
name = """
MDTextField:
    pos_hint:{'center_x':0.5,'center_y':0.8}
    hint_text:"Name"
    size_hint_x:None
    width:300 
"""
height = """
MDTextField:
    hint_text:"Height"
    helper_text:"in meters"
    helper_text_mode:"on_focus"
    pos_hint:{'center_x':0.5,'center_y':0.6}
    size_hint_x:None
    width:300 
"""
weight = """
MDTextField:
    hint_text:"Weight"
    helper_text:"in kilograms"
    helper_text_mode:"on_focus"
    pos_hint:{'center_x':0.5,'center_y':0.7}
    size_hint_x:None
    width:300 

"""


class BMI(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Dark"
        screen = Screen()

        self.tool_kit = Builder.load_string(tool_bar)
        self.name_input = Builder.load_string(name)
        self.weight_input = Builder.load_string(weight)
        self.height_input = Builder.load_string(height)
        button = MDRectangleFlatButton(text="Calculate", pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                       on_release=self.result)
        screen.add_widget(self.tool_kit)
        screen.add_widget(self.name_input)
        screen.add_widget(self.weight_input)
        screen.add_widget(self.height_input)
        screen.add_widget(button)

        return screen

    def result(self, obj):
        if (self.name_input.text != "" and self.height_input.text != "" and self.weight_input.text != ""):
            bmi = float(self.weight_input.text) / (float(self.height_input.text) * float(self.height_input.text))
            if 25.0 <= bmi <= 30.0:
                report = "Overweight"
            elif bmi > 30.0:
                report = "Obese"
            elif bmi < 18.5:
                report = "Underweight"
            else:
                report = "Healthy"

            self.dialog = MDDialog(title="BMI Report", text=self.name_input.text + " ,your BMI is " + str(
                round(bmi, 2)) + " and you are in " + report + " category",
                                   size_hint=(0.8, 1),
                                   buttons=[MDRoundFlatIconButton(icon="close", text="close", on_release=self.close)])
            self.dialog.open()
        else:
            self.dialog = MDDialog(title="Error", text="Enter the details", size_hint=(0.8, 1),
                                   buttons=[MDRoundFlatIconButton(icon="close", text="close", on_release=self.close)])
            self.dialog.open()

    def close(self, obj):

        self.dialog.dismiss()

    def nothing(self):
        print("Nothing")


BMI().run()