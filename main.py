import flet as ft
from lib.views import LoginView, UploadView
from lib.components.appbar import custom_appbar

def main(page: ft.Page):
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    # configure custom fonts
    page.fonts = {
        "Kokoro": "fonts/Kokoro/Regular.ttf",
        "Kokoro-Medium": "fonts/Kokoro/Medium.ttf",
        "Kokoro-Bold": "fonts/Kokoro/Bold.ttf",
    }
    page.theme = ft.Theme(
        font_family="Kokoro",
        color_scheme=ft.ColorScheme(
            tertiary_container="#1E2036"
        )
    )
    page.update()

    # views
    def route_change(route):
        page.views.clear()
        # page.views.append(
        #     ft.View(
        #         "/",
        #         [
        #             custom_appbar(),
        #             LoginView(page)
        #         ],
        #         bgcolor="#03020c",
        #         padding=0,
        #     )
        # )
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [
                        custom_appbar(
                            automatically_imply_leading=False,
                            leading=ft.IconButton(
                                icon=ft.icons.ARROW_BACK,
                                icon_size=30,
                                scale=0.75,
                                # event
                                on_click=lambda _: page.go("/"),
                            ),
                        ),
                        UploadView(page)
                    ],
                    bgcolor="#03020c",
                    padding=0,
                )
            )
        page.update()
    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    
ft.app(target=main, assets_dir="assets/")