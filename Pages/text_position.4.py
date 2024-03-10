import flet as ft

def main(page: ft.Page):
    page.title = "Szövegigazítás4"
    page.theme_mode = ft.ThemeMode.DARK
    page.add(
        ft.Text(value= "Szöveg igazízás gyakorlása Szöveg balra középen."))
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    page.update()

ft.app(target = main)
