from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ConverterApp(App):
    def build(self):
        # Create a grid layout with one column
        layout = GridLayout(cols=1, padding=20, spacing=20)

        # Title label
        title = Label(text="Conversion System", font_size=20, bold=True, size_hint_y=None, height=50)
        layout.add_widget(title)

        # Input label
        input_label = Label(text="Enter Number:", font_size=16, bold=True, size_hint_y=None, height=50)
        layout.add_widget(input_label)

        # Input field for the number
        self.number_input = TextInput(font_size=16, multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.number_input)

        # Convert button
        convert_button = Button(text="Convert", font_size=18, size_hint_y=None, height=50)
        convert_button.bind(on_press=self.convert)
        layout.add_widget(convert_button)

        # Output labels
        self.binary_label = Label(text="Binary:", font_size=16, bold=True, size_hint_y=None, height=50)
        layout.add_widget(self.binary_label)

        self.decimal_label = Label(text="Decimal:", font_size=16, bold=True, size_hint_y=None, height=50)
        layout.add_widget(self.decimal_label)

        self.hexadecimal_label = Label(text="Hexadecimal:", font_size=16, bold=True, size_hint_y=None, height=50)
        layout.add_widget(self.hexadecimal_label)

        self.octal_label = Label(text="Octal:", font_size=16, bold=True, size_hint_y=None, height=50)
        layout.add_widget(self.octal_label)

        return layout

    def convert(self, instance):
        try:
            # Get the number from the input field
            num = int(self.number_input.text)
            
            # Update the output labels with conversions
            self.binary_label.text = f"Binary: {bin(num)[2:]}"
            self.decimal_label.text = f"Decimal: {num}"
            self.hexadecimal_label.text = f"Hexadecimal: {hex(num)[2:].upper()}"
            self.octal_label.text = f"Octal: {oct(num)[2:]}"
        except ValueError:
            # Handle invalid input
            self.binary_label.text = "Binary: Invalid Input"
            self.decimal_label.text = "Decimal: Invalid Input"
            self.hexadecimal_label.text = "Hexadecimal: Invalid Input"
            self.octal_label.text = "Octal: Invalid Input"

if __name__ == "__main__":
    ConverterApp().run()

