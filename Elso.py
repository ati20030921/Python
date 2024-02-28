import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Text(value='A nevem: Daroczi Attila')
    )
    page.add(
        ft.Text(value='Éhezők Viadala')
    )
    page.add(
        ft.Text(value='Olaszország')
    )

    page.update();

ft.app(target=main)
