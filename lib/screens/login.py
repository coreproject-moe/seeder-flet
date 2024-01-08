import flet as ft

class LoginScreen(ft.GridView):
    def __init__(self, *args, **kwargs):
        super(LoginScreen, self).__init__(*args, **kwargs)
        # Tokens
        self.doodstream_token = ""
        # grid config
        self.expand = 1
        self.spacing = 10
        self.runs_count = 2
        self.padding = 0
        # create view
        self.__create_view__()

    def __create_form__(self) -> ft.Container:
        return ft.Container(
            padding=50,
            content=ft.Column([
                ft.Container(
                    content=ft.Column([
                        ft.Text(value="Paste your API token", font_family="Kokoro-Bold", size=25, color=ft.colors.WHITE),
                        ft.Text(value="for seamless integration", font_family="Kokoro-Medium", size=15)
                    ], spacing=0)
                ),
                ft.Column([
                    ft.Container(
                        content=ft.Column([
                            ft.Text(value="DoodStream", font_family="Kokoro-Medium", size=16),
                            ft.TextField(
                                label="DoodStream Token",
                                border_color=ft.colors.BLUE_700,
                                border_width=2,
                                label_style=ft.TextStyle(size=15),
                                focused_border_color=ft.colors.BLUE_500,
                                border_radius=10,
                                text_size=15,
                                height=50,
                                prefix_icon=ft.icons.ABC,
                            ),
                            ft.Text(value="Insert your unique API token here to unlock the full potential of Streamsb's video services", font_family="Kokoro", size=12)
                        ], spacing=2)
                    )
                ])
            ], spacing=50)
        )
    
    def __create_fish__(self) -> ft.Container:
        return ft.Container(
            padding=0,
            image_src="images/fish-gradient.png",
            image_fit=ft.ImageFit.FIT_HEIGHT,
        )

    def __create_view__(self):
        form = self.__create_form__()
        fish = self.__create_fish__()

        for control in [form, fish]:
            self.controls.append(control)