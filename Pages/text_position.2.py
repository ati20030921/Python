import flet as ft

def main(page:ft.Page):
    page.title = "Szövegigazítás2"
    page.bgcolor = "ORANGE"
    page.add(
    ft.Text(value= "Szöveg igazízás gyakorlása Szöveg középen."))
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    page.update()

ft.app(target=main)
