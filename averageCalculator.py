
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        self.result = Label(text="0", halign="right", valign="bottom", size_hint=(1, 0.4), font_size=32)
        layout = GridLayout(cols=4)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '=', '+'
        ]
        for button in buttons:
            button_object = Button(text=button, pos_hint={'center_x': 0.5, 'center_y': 0.5})
            button_object.bind(on_press=self.on_button_press)
            layout.add_widget(button_object)
        equals_button = Button(text="=")
        equals_button.bind(on_press=self.on_solution)
        layout.add_widget(equals_button)
        clear_button = Button(text="C")
        clear_button.bind(on_press=self.clear)
        layout.add_widget(clear_button)
        layout.add_widget(self.result)
        return layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if current == "0":
            new_text = button_text
        else:
            new_text = current + button_text

        self.result.text = new_text

    def on_solution(self, instance):
        text = self.result.text
        # İşlem sırasında son operatörü kullanıp kullanmadığımızı kontrol edin
        if text and text[-1] in self.operators:
            return

        try:
            solution = str(eval(self.result.text))
            self.result.text = solution
        except Exception:
            self.result.text = "Error"

    def clear(self, instance):
        self.result.text = "0"

if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
