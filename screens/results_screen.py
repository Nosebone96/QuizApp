import flet as ft

class ResultsScreen:
    def __init__(self, score, total_questions, users, restart_callback):
        self.users = users
        self.score = score
        self.total_questions = total_questions
        self.restart_callback = restart_callback
        self.percentage = (score / total_questions) * 100
        self.top_score = None
        n = len(self.users)
        for i in range(n):
            min_ind = i
            for j in range(i + 1, n):
                if self.users[j][1] < self.users[min_ind][1]:
                    min_ind = j
            self.users[i], self.users[min_ind] = self.users[min_ind], self.users[i]
        print(self.users)
        self.users.reverse()
        self.users_rows = []
        for i in range(n):
            self.users_rows.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(f'{self.users[i][0]}')),
                    ft.DataCell(ft.Text(f'{self.users[i][1]}'))
                ]
            ))


    def build(self):
        
        if self.percentage >= 80:
            message = "¡Excelente trabajo!"
            color = ft.colors.GREEN
        elif self.percentage >= 60:
            message = "¡Buen trabajo!"
            color = ft.colors.BLUE
        else:
            message = "Sigue intentando"
            color = ft.colors.ORANGE
        
        self.top_score = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text('Usuario')),
                ft.DataColumn(ft.Text('Puntaje'), numeric=True)
            ],
            rows=self.users_rows
        )
            
        return ft.View(
            route="/results",
            controls=[
                ft.Column(
                    [
                        ft.Container(
                            content=ft.Text(
                                "Resultados",
                                size=28,
                                weight=ft.FontWeight.BOLD,
                            ),
                            margin=ft.margin.only(top=80, bottom=20),
                        ),
                        ft.Container(
                            content=ft.Text(
                                message,
                                size=22,
                                color=color,
                                weight=ft.FontWeight.BOLD,
                            ),
                            margin=ft.margin.only(bottom=30),
                        ),
                        ft.Container(
                            content=ft.Text(
                                f"Tu puntuación: {self.score} de {self.total_questions}",
                                size=20,
                            ),
                            margin=ft.margin.only(bottom=20),
                        ),
                        ft.Container(
                            content=ft.ProgressBar(
                                width=300,
                                value=self.score / self.total_questions,
                                color=color,
                                bgcolor=ft.colors.GREY_300,
                            ),
                            margin=ft.margin.only(bottom=40),
                        ),
                        ft.Container(
                            content=ft.Text(
                                f"{self.percentage:.0f}%",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                color=color,
                            ),
                            margin=ft.margin.only(bottom=50),
                        ),
                        ft.Container(
                            content=ft.ElevatedButton(
                                "Jugar de nuevo",
                                width=200,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=10),
                                    color={
                                        ft.ControlState.DEFAULT: ft.colors.WHITE,
                                    },
                                    bgcolor={
                                        ft.ControlState.DEFAULT: ft.colors.BLUE,
                                    },
                                ),
                                on_click=lambda _: self.restart_callback(),
                            ),
                            alignment=ft.alignment.center,
                        ),
                        ft.Column(
                            controls=[self.top_score],
                            scroll=ft.ScrollMode.ALWAYS,  
                            height=300, 
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    scroll= ft.ScrollMode.ALWAYS
                )
            ],
        )

