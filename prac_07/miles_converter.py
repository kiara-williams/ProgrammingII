from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

KMS = 1.6


class MileConverterApp(App):
    def build(self):
        Window.size = (400, 200)
        self.title = "Mile to Kilometre Converter"
        self.root = Builder.load_file('miles_converter.kv')
        return self.root

    def convert_miles(self, value):
        try:
            result = float(value) * KMS
        except ValueError:
            result = 0
        self.root.ids.output_label.text = "{:.2f}".format(result)

    def increment_miles(self, increment):
        if self.root.ids.input_miles.text == '':
            increment += 0
        else:
            increment += float(self.root.ids.input_miles.text)
        self.root.ids.input_miles.text = "{:.2f}".format(increment)


MileConverterApp().run()
