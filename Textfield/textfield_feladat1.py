import flet as ft

def main(page: ft.Page):
    def button_clicked(e):
        t.value = f"Textboxes values are:  '{tb1.value}'."
        page.update()

    t = ft.Text()
    tb1 = ft.TextField(label="Kérlek add meg a teljes neved: ")

    page.add(tb1, t)
    page.update()




if __name__=='__main__':
    ft.app(target=main)
