from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        
        self.button1 = Button(text="Click Me!", font_size=24, on_press=self.on_button_click)
        self.button2 = Button(text="Exit", font_size=24, on_press=self.stop_app)

        layout.add_widget(self.button1)
        layout.add_widget(self.button2)

        return layout

    def on_button_click(self, instance):
        instance.text = "You Clicked Me!"

    def stop_app(self, instance):
        App.get_running_app().stop()

if __name__ == "__main__":
    MyApp().run()
