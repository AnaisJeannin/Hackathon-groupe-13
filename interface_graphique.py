import flet as ft

squares = [ft.TextField(i) for i in range(9)] #création du widget

def reset(board):
    for i, square in zip(board, squares):
        square.value = i
    

def main(page : ft.Page):
    page.title = "Taquin"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    page.update()

    entete = ft.Row([ft.TextField("taquin")])

    # cases = ft.GridView([ ft.TextField(1), ft.TextField(2), ft.TextField(3), ft.TextField(4), ft.TextField(5),
    #     ft.TextField(6), ft.TextField(7), ft.TextField(8), ft.TextField(0)], runs_count = 3, 
    #     spacing = 3, run_spacing = 3)

    cases_1 = ft.Row([ft.TextField(1, fill_color = (146, 162, 239), max_length = 1, keyboard_type = int), 
                      ft.TextField(2, fill_color = (146, 162, 239), max_length = 1, keyboard_type = int), 
                      ft.TextField(3, fill_color = (146, 162, 239), max_length = 1, keyboard_type = int)])
    
    cases_2 = ft.Row([ft.TextField(4, fill_color = (146, 162, 239), max_length = 1, keyboard_type = int), 
                      ft.TextField(5, fill_color = (146, 162, 239), max_length = 1, keyboard_type = int), 
                      ft.TextField(6, fill_color = (146, 162, 239), max_length = 1, keyboard_type = int)])
    
    cases_3 = ft.Row([ft.TextField(7, fill_color = (146, 162, 239), max_length = 1, keyboard_type = int), 
                      ft.TextField(8, fill_color = (146, 162, 239), max_length = 1, keyboard_type = int), 
                      ft.TextField(0, fill_color = (239, 183, 146), max_length = 1, keyboard_type = int)])
    
    bas =  ft.Row([ft.IconButton(icon = ft.Icons.MENU), ft.IconButton(icon = ft.Icons.REFRESH),
            ft.IconButton(icon = ft.Icons.REPLY), ft.IconButton(icon = ft.Icons.MORE_VERT)])
    
    page.add(ft.Column([entete, cases_1, cases_2, cases_3, bas,]))

ft.app(main)