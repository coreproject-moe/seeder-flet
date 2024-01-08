import flet as ft
from lib.screens.login import LoginScreen

def main(page: ft.Page):
    page.window_frameless = True
    page.bgcolor = "#03020c"

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.UPLOAD),
        leading_width=40,
        title=ft.Image(src="/icons/logo.png", height=25),
        center_title=True,
        bgcolor = "#03020c",
    )
    
    page.add(LoginScreen())
    page.update()

ft.app(target=main, assets_dir="assets/")