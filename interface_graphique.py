import flet as ft

"""code qui affiche le taquin terminé"""

#création des widgets
squares = [ft.TextField(i, fill_color = (146, 162, 239), max_length = 1) for i in range(9)] 
ligne_1 = [ft.TextField(i, fill_color = (146, 162, 239), max_length = 1) for i in range(1,4)]
ligne_2 = [ft.TextField(i, fill_color = (146, 162, 239), max_length = 1) for i in range(4,7)]
ligne_3 = [ft.TextField(7, fill_color = (146, 162, 239), max_length = 1), 
           ft.TextField(8, fill_color = (146, 162, 239), max_length = 1), 
           ft.TextField(0, fill_color = (146, 162, 239), max_length = 1),]

def reset(board):
    for i, square in zip(board, squares):
        square.value = i
    

def main(page : ft.Page):
    page.title = "Taquin"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    page.update()

    entete = ft.Row([ft.TextField("taquin", fill_color = (146, 162, 239))])

    cases_1 = ft.Row(ligne_1)
    cases_2 = ft.Row(ligne_2)
    cases_3 = ft.Row(ligne_3)
    
    bas =  ft.Row([ft.IconButton(icon = ft.Icons.MENU), ft.IconButton(icon = ft.Icons.REFRESH),
            ft.IconButton(icon = ft.Icons.REPLY), ft.IconButton(icon = ft.Icons.MORE_VERT)])
    
    page.add(ft.Column([entete, cases_1, cases_2, cases_3, bas,]))

ft.app(main)