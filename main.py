import flet as ft
from lib.screens.login import LoginScreen

def main(page: ft.Page):
    page.window_frameless = True
    page.bgcolor = "#03020c"
    page.padding = 0
    # configure custom fonts
    page.fonts = {
        "Kokoro": "fonts/Kokoro/Regular.ttf",
        "Kokoro-Medium": "fonts/Kokoro/Medium.ttf",
        "Kokoro-Bold": "fonts/Kokoro/Bold.ttf",
    }

    page.appbar = ft.AppBar(
        title=ft.Image(src="/icons/logo.png", height=25),
        center_title=True,
        bgcolor = "#03020c",
    )
    
    page.add(LoginScreen())
    page.update()

ft.app(target=main, assets_dir="assets/")