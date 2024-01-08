import flet as ft
from lib.views.login import LoginView

def main(page: ft.Page):
    page.window_frameless = True
    # configure custom fonts
    page.fonts = {
        "Kokoro": "fonts/Kokoro/Regular.ttf",
        "Kokoro-Medium": "fonts/Kokoro/Medium.ttf",
        "Kokoro-Bold": "fonts/Kokoro/Bold.ttf",
    }
    page.theme = ft.Theme(font_family="Kokoro")

    # views
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(
                        title=ft.Image(src="/icons/logo.png", height=25),
                        center_title=True,
                        bgcolor = "#03020c",
                    ),
                    LoginView()
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