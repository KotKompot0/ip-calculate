from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            [".", "0", "C"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        ip_to_binary_button = Button(
            text="Перевести ip в 2 СС", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        ip_to_binary_button.bind(on_press=self.ip_to_binary)
        main_layout.add_widget(ip_to_binary_button)

        ip_back_button = Button(
            text="Перевести ip в 10 СС", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        ip_back_button.bind(on_press=self.ip_back)
        main_layout.add_widget(ip_back_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Очистка виджета с решением
            self.solution.text = ""
        else:
            new_text = current + button_text
            self.solution.text = new_text
        self.last_button = button_text

    def ip_to_binary(self, instance):
        ip_test = self.solution.text
        if ip_test:
            try:
                ip_config = []
                ip_test = ip_test.split(".")
                if len(ip_test) != 4:
                    self.solution.text = "IP не корректный"
                    return

                def ip_convert(ip):
                    i = 0
                    act = 7
                    binary = ''

                    while i < 8:
                        if ip >= 2**act:
                            binary += '1'
                            ip = ip - 2**act
                        else:
                            binary += '0'
                        i += 1
                        act -= 1
                    ip_config.append(binary)

                for x in ip_test:
                    ip_convert(int(x))
                self.solution.text = '.'.join(ip_config)

            except:
                self.solution.text = "IP не корректный"
                return

    def ip_back(self, instance):
        binary = self.solution.text
        if binary:
            try:
                ip_decod = []
                binary = binary.split(".")
                if len(binary) != 4:
                    self.solution.text = "IP не корректный"
                    return

                def ip_convert(ipb):
                    i = 0
                    act = 7
                    encodip = 0
                    while i < 8:
                        if ipb[i] == '1':
                            encodip = encodip + 2**act
                        i += 1
                        act -= 1
                    ip_decod.append(encodip)

                for x in binary:
                    ip_convert(list(x))
                self.solution.text = '.'.join(str(e) for e in ip_decod)
            except:
                self.solution.text = "IP не корректный"
                return


if __name__ == '__main__':
    app = MainApp()
    app.run()
