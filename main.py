from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import StringProperty


class IconButton(Button):
    icon = StringProperty("Faraona.jpg")

# you can alos just put this in your KV file
from kivy.lang import Builder
Builder.load_string("""
<IconButton>:
    canvas:
        Rectangle:
            source:self.icon
            pos: self.pos
            size: self.size
""")


class TestApp(App):
    def build(self):
        return IconButton()


if __name__ in ("__main__", "android"):
    TestApp().run()