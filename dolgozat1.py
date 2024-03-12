import flet as ft

def main(page: ft.Page):
    page.title = "Dolgozat"
    

    page.add(
        ft.Text(value= "Hello" + "                                                                                                                                                                                                                                                                                               " + "world")
    ) #tudom,hogy nem így kell igazítani de nem tudok más megoldást

    page.add(
        ft.Row(
            [
                ft.Container(
                    content=ft.Text("A"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE,
                    width=1230,
                    height = 200,
                    expand = True,
                ),
            ]
        )
    )

    page.add(
        ft.Row(
            [
                ft.Container(
                    margin = 10,
                    padding= 10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.YELLOW,
                    width=200,
                    height = 200,
                ),

                ft.Container(
                    margin = 10,
                    padding=20,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE,
                    width=200,
                    height = 200,
                ),
                ft.Container(
                    margin = 10,
                    padding=20,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.GREEN,
                    width=200,
                    height = 200,
                ),
                ft.Container(
                    margin = 10,
                    padding=20,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLACK,
                    width=200,
                    height = 200,
                ),
                ft.Container(
                    margin = 10,
                    padding=20,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.RED,
                    width=200,
                    height = 200,
                ),
            ],
        )
    )


    page.update()

ft.app(target = main)
    
