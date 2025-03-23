import flet as ft
import random
import time as tm
import threading as thr

class GameScreen:
    def __init__(self, questions, question_number, total_questions, answer_callback, page):
        self.page = page
        self.question = questions
        self.question_number = question_number
        self.total_questions = total_questions
        self.answer_callback = answer_callback
        self.timer_text = ft.Text("", size=20, color=ft.colors.RED)
        self.hilo = thr.Thread(target=self.start_timer)
        self.hilo.start()
        print(self.question)
        print(self.question_number)
        print('______________________________')

    def start_timer(self):
        try:
            for i in range(10, 0, -1):
                tm.sleep(1)
                self.timer_text.value = f'{i}'
                if i >= 7:
                    self.timer_text.color = ft.colors.GREEN
                elif i <= 5 and i >3:
                    self.timer_text.color = ft.colors.ORANGE
                else:
                    self.timer_text.color = ft.colors.RED
                self.timer_text.update()
            self.timer_text.value = 'tiempo agotado'
            self.timer_text.update()
            tm.sleep(0.4)
            print('el hilo detiene')
            self.handle_answer(False)
        except AssertionError:
            pass


    def build(self):
        # Shuffle the options
        options = self.question["options"].copy()
        random.shuffle(options)

        option_buttons = []
        for option in options:
            is_correct = option == self.question["correct_answer"]

            # Crear un manejador de clics que llama a la función de respuesta
            def create_click_handler(is_correct):
                return lambda _: self.handle_answer(is_correct)

            option_buttons.append(
                ft.Container(
                    content=ft.ElevatedButton(
                        option,
                        width=300,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=8),
                        ),
                        on_click=create_click_handler(is_correct),
                    ),
                    margin=ft.margin.only(bottom=10),
                )
            )

        self.view_game = ft.View(
            route="/game",
            controls=[
                ft.Column(
                    [
                        ft.Container(
                            content=ft.Text(
                                f"Pregunta {self.question_number} de {self.total_questions}",
                                size=16,
                                color=ft.colors.BLUE_GREY,
                            ),
                            margin=ft.margin.only(top=40, bottom=20),
                        ),
                        ft.Container(
                            content=ft.Text(
                                self.question["text"],
                                size=22,
                                weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            margin=ft.margin.only(bottom=40),
                            padding=ft.padding.all(20),
                        ),
                        self.timer_text,
                        ft.Column(
                            option_buttons,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            ],
        )
        return self.view_game
    def handle_answer(self, is_correct):
        self.view_game.update()
        if is_correct:
            self.view_game.bgcolor = ft.colors.GREEN_400  
        else:
            self.view_game.bgcolor = ft.colors.RED_400
        self.view_game.update()
        tm.sleep(0.5)
        self.answer_callback(is_correct)