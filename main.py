import flet as ft
from screens.home_screen import HomeScreen
from screens.game_screen import GameScreen
from screens.results_screen import ResultsScreen
from data.questions import get_questions

class QuizApp:
    def __init__(self):
        self.current_score = 0
        self.questions = get_questions()
        self.current_question_index = 0
        self.answered_questions = []
        self.page = None
        self.users = []
        self.user_index = 0


    def main(self, page: ft.Page):
        self.page = page
        
        page.title = "Juego de Preguntas y Respuestas"
        page.theme_mode = ft.ThemeMode.LIGHT
        page.padding = 20
        page.window.width = 400
        page.window.resizable = False
        page.scroll = ft.ScrollMode.ALWAYS

        def route_change(e):
            route = page.route
            print(f'cambia ruta {route}')
            page.views.clear()
            
            if route == "/":
                print('pasa home')
                page.views.append(
                    HomeScreen(start_game).build()
                )
            elif route == "/game":
                print('pasa por juego')
                
                page.views.append(
                    GameScreen(
                        self.questions[self.current_question_index],
                        self.current_question_index + 1,
                        len(self.questions),
                        answer_question,
                        page
                    ).build()
                )
            elif route == "/results":
                page.views.append(
                    ResultsScreen(
                        self.current_score,
                        len(self.questions),
                        self.users,
                        restart_game
                    ).build()
                )
            
            page.update()

        def view_pop(e):
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

        def start_game(nombre):
            print('inicia juego')
            self.current_score = 0
            self.current_question_index = 0
            self.answered_questions = []
            self.users.append([nombre, 0])
            print(self.users)
            page.go("/game")

        def answer_question(is_correct):
            if is_correct:
                self.current_score += 1
            
            self.answered_questions.append({
                "question": self.questions[self.current_question_index],
                "correct": is_correct
            })
            
            self.current_question_index += 1
            
            if self.current_question_index < len(self.questions):
                print(self.current_score)
                print(self.current_question_index)
                print('siguiente pregunta')
                page.go('/')
                page.go('/game')
            else:
                self.users[self.user_index][1] = self.current_score
                self.user_index += 1
                page.go("/results")

        def restart_game():
            page.go("/")

        page.on_route_change = route_change
        page.on_view_pop = view_pop
        
        page.go("/")

def main():
    app = QuizApp()
    ft.app(target=app.main)

if __name__ == "__main__":
    main()