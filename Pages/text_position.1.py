import flet as ft

def main(page: ft.Page):
    page.title = "Szövegigazítás1"
    page.theme_mode = ft.ThemeMode.DARK
    page.add(
    ft.Text(value= "Szöveg igazízás gyakorlása. Szöveg alul, középen."))
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding= ft.padding.only(top=600)



    page.update()

ft.app(target=main)
