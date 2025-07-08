import flet as ft
import pyperclip
from typing import Optional
from api import CatImage, get_random_cat_image

def main(page: ft.Page):
    page.title = "Random Cat Viewer"
    page.window.maximized = True
    page.bgcolor = "#003265"

    image_history: list[CatImage] = []

    history_dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("Histórico de Imagens", text_align="center"),
        content=ft.Text("Nenhuma imagem no histórico"),
        alignment=ft.alignment.center,
        actions=[
            ft.TextButton("Fechar", on_click=lambda e: page.close(history_dlg)),
        ],
        on_dismiss=lambda e: print("Fechou")
    )

    def show_history(e=None):
        history_dlg.content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.GestureDetector(
                        content=ft.Container(
                            content=ft.Image(src=img["url"], width=100, height=100),
                            border_radius=10,
                            padding=5,
                            bgcolor=ft.Colors.GREY_100,
                            width=200
                        ),
                        on_tap=lambda e, url=img["url"]: show_big_image(e, url)
                    )
                    for img in image_history
                ],
                scroll=ft.ScrollMode.AUTO
            ),
            alignment=ft.alignment.top_center,
            width=400,
            height=600
        )
        page.update()
        page.open(history_dlg)

    def show_big_image(e, url: str):
        preview_dialog = ft.AlertDialog(
            modal=True,
            content=ft.Image(src=url, width=600),
            actions=[
                ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.Icons.COPY, on_click=lambda e: pyperclip.copy(url)),
                        ft.Container(expand=True),
                        ft.TextButton("Voltar", on_click=lambda e: page.open(history_dlg)),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            ],
        )
        page.update()
        page.open(preview_dialog)

    def copy_cat_image_src(e=None):
        nonlocal cat_image
        pyperclip.copy(cat_image.src)

    def update_cat_image(e=None):
        nonlocal cat_image
        cat_data = get_random_cat_image()
            
        if cat_data is None:
            cat_data = {
                "id": "n/a",
                "url": "https://via.placeholder.com/400x300?text=Imagem+Indisponível",
                "width": 400,
                "height": 300
            }
        else:
            image_history.append(cat_data)

        cat_image.src = cat_data["url"]
        cat_image.width = cat_data["width"]
        cat_image.height = cat_data["height"]

        page.update()

    initial_cat_data: Optional[CatImage] = get_random_cat_image()
    if initial_cat_data is None:
        initial_cat_data = {
            "id": "n/a",
            "url": "https://via.placeholder.com/400x300?text=Imagem+Indisponível",
            "width": 400,
            "height": 300
        }
    else:
        image_history.append(initial_cat_data)
    
    cat_image = ft.Image(
        src=initial_cat_data["url"],
        width=initial_cat_data["width"],
        height=initial_cat_data["height"],
        fit=ft.ImageFit.CONTAIN
    )

    page.floating_action_button = ft.Row(
        controls=[
            ft.FloatingActionButton(
                icon=ft.Icons.HISTORY,
                width=100,
                on_click=show_history
            ),
            ft.FloatingActionButton(
                icon=ft.Icons.COPY,
                width=100,
                on_click=copy_cat_image_src
            ),
            ft.FloatingActionButton(
                icon=ft.Icons.CACHED,
                width=100,
                on_click=update_cat_image
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(
        ft.Stack(
            [
                ft.Image(
                    src="/nyan_cat.gif",
                    fit=ft.ImageFit.COVER, # Cobrir toda a área disponível
                    expand=True, # Expande a imagem para preencher o ft.Stack
                    width=page.window.width,
                    height=page.window.height,
                    opacity=0.4,
                ),
                ft.Column(
                    [
                        ft.SafeArea(
                            ft.Container(
                                content=cat_image,
                                alignment=ft.alignment.center,
                                expand=True
                            ),
                            expand=True,
                        ),
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
                
            ],
            expand=True, # Expande o ft.Stack para preencher página inteira
        )
        
    )

ft.app(target=main, assets_dir="assets")