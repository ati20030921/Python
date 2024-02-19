import flet as ft

def main(page: ft.Page):
    page.title ="Petőfi Sándor : Azokon A Szép Kék Hegyeken Túl"
    page.bgcolor=ft.colors.AMBER_100

    page.add(
        ft.Text(value = """Azokon A Szép Kék Hegyeken Túl""", size=25,color="black")
    )
    page.padding = ft.padding.symmetric(vertical=200)

    page.add(
        ft.Text(value = """2024-02-12""",size=20)
    )

    page.padding = ft.padding.symmetric(vertical=200)
    
    page.add(
        ft.Text(value = """Azokon a szép kék hegyeken túl
    Fogsz te élni, kedvesem, ezentúl,
    Ott fogsz élni boldog férjed mellett,
    Kit boldoggá egyedűl szived tett;
    Napkeletről messzebb napkeletre""", color="red",size="25")
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = ft.padding.only(left=50, top=100)

    page.add(
    ft.Text(value = """Vers folytatása >>>""",size=20,text_align=ft.TextAlign.RIGHT,color="black",width=500)
    )
    url='https://szerelmes-versek.info/azokon-szep-kek-hegyeken-tul-petofi-sandor.vers',
    

    page.add(
    ft.Text(value = """Boldog szerelem Petőfi Sándor szerelmes verse Szólj hozzá""",color="black",size=24)
    )

    page.padding = ft.padding.only(left=50, top=100)



    page.update()

if __name__=='__main__':
    ft.app(target=main)
