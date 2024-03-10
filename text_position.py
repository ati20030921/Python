import flet as ft

def main(page: ft.Page):
    page.title = "text_position.py"

    page.add(
    ft.Text(value = "Dreamcatcher(드림캐쳐) 'BONVOYAGE' MV"))
    page.horizontal_alignment = ft.CrossAxisAlignment.END

    page.update()

ft.app(target =  main)


import flet as ft

def main(page: ft.Page):
    page.title = "text_position.py"

    page.add(
    ft.Text(value = "Dreamcatcher(드림캐쳐) 'Odd Eye' MV"))
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.update()

ft.app(target =  main)

import flet as ft

def main(page: ft.Page):
    page.title = "text_position.py"

    page.add(
    ft.Text(value = "[Special Clip] Dreamcatcher(드림캐쳐) 'SAHARA' 자체 제작 MV"))
    page.horizontal_alignment = ft.CrossAxisAlignment.START

    page.update()

ft.app(target =  main)
