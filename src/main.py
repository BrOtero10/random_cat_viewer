import flet as ft


def main(page: ft.Page):
    page.title = "Random Cat Viewer"
    page.window_width = 1200
    page.window_height = 900

    page.floating_action_button = ft.Row(
        controls=[
            ft.FloatingActionButton(
                icon=ft.Icons.COPY,
            ),
            ft.FloatingActionButton(
                icon=ft.Icons.REFRESH,
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    
    page.add(
        ft.SafeArea(
            ft.Container(
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
