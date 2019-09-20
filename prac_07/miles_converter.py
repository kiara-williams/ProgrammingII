from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MileConverterApp(App):
    def build(self):
        Window.size = (400, 400)
        self.title = "Mile to Kilometre Converter"
        self.root = Builder.load_file('miles_converter.kv')
        return self.root

    def convert_miles(self, value):
        result = value * 1.6
        self.root.ids.output_label.text = "{:.2f}".format(result)

    def increment_miles(self, increment):
        increment += float(self.root.ids.input_miles.text)
        self.root.ids.input_miles.text = "{:.2f}".format(increment)


MileConverterApp().run()
