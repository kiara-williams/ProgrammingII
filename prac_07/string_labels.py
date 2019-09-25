from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.string_labels = ["string1", "string2", "string3"]

    def build(self):
        self.title = "String Labels"
        self.root = Builder.load_file('string_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.string_labels:
            temp_label = Label(text=name)
            self.root.ids.string_label.add_widget(temp_label)


DynamicLabelsApp().run()
