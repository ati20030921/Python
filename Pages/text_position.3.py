import flet as ft

def main(page: ft.Page):
    page.title = "Szövegigazítás3"
    page.add(
    ft.Text(value= "Szöveg igazízás gyakorlása Szöveg jobbra fent.",text_align="TOP",color="GREY_100"))
    page.horizontal_alignment = ft.CrossAxisAlignment.END
    page.bgcolor = ft.colors.TEAL
    
    page.update()

ft.app(target=main)
