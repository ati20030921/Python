import flet as ft

def main(page: ft.Page):
    page.title = "Szövegigazítás5"

    page.add(
    ft.Text(value = "Szöveg igazízás gyakorlása Szöveg alapértelmezett és padding."))
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = ft.padding.only(top=100,left=150)

    page.update()

ft.app(target =  main)
