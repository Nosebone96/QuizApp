import flet as ft

class HomeScreen:
    def __init__(self, start_game_callback):
        self.start_game_callback = start_game_callback
        self.name_textf = None  
        self.button_start = None  

    def build(self):
        # Crear el TextField
        self.name_textf = ft.TextField(
            hint_text='Digita tu nombre',
            label='Nombre',
            on_change=self.on_name_change  
        )

        
        self.button_start = ft.ElevatedButton(
            "Iniciar Juego",
            width=200,
            height=50,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                color={
                    ft.ControlState.DEFAULT: ft.colors.WHITE,
                },
                bgcolor={
                    ft.ControlState.DEFAULT: ft.colors.BLUE,
                },
            ),
            on_click=lambda _: self.start_game_callback(self.nombre),
            disabled=True 
        )

        
        self.home_view = ft.View(
            route="/",
            controls=[
                ft.Column(
                    [
                        ft.Container(
                            content=ft.Text(
                                "Juego de Preguntas y Respuestas",
                                size=28,
                                weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            margin=ft.margin.only(top=70, bottom=40),
                        ),
                        self.name_textf,
                        ft.Container(
                            content=ft.Image(
                                src=f"assets/nobitches.jpg",
                                width=250,
                                height=250,
                            ),
                            alignment=ft.alignment.center,
                            margin=ft.margin.only(bottom=10),
                        ),
                        ft.Container(
                            content=self.button_start,
                            alignment=ft.alignment.center,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            ],
        )
        return self.home_view

    def on_name_change(self, e):
        
        self.button_start.disabled = not bool(self.name_textf.value.strip())
        self.nombre = self.name_textf.value
        print(self.name_textf.value)
        self.home_view.update() 
