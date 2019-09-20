from kivy.app import App
from kivy.lang import Builder


class MileConverterApp(App):
    def build(self):
        self.title = "Mile to Kilometre Converter"
        self.root = Builder.load_file('miles_converter.kv')
        return self.root

    def convert_miles(self, value):
        result = value * 1.6
        self.root.ids.output_label.text = "{:.2f}".format(result)

    def add_one_value(self, value):
        value += 1
        self.root.ids.input_miles.text = "{:.2f}".format(value)

    def subtract_one_value(self, value):
        value -= 1
        self.root.ids.input_miles.text = "{:.2f}".format(value)


MileConverterApp().run()
