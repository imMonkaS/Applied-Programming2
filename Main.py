"""
Технологии: Python.

Инструменты: PyCharm, draw.io, Notepad++.

Лабораторная работа № 2. C++: STL. Python: Оконные приложения.

1) Выполнить задание на Python на тему оконного приложения (предложив свой вариант или по вариантам из файла).
Предварительно спроектировать макет в сервисе draw.io. Реализовать приложение предпочтительно на Tkinter
(https://docs.python.org/3/library/tkinter.html).

Возможна реализация на C++ и QT Widgets по согласованию с преподавателем.

2) Дополнительное задание для претендующих на оценку от 40 баллов: выполнить задание на тему STL
(предложив свой вариант или по вариантам из файла).

3) Подготовить отчёт о выполненной лабораторной работе. Подготовиться по вопросам к защите.

Вариант 2
Написать игру крестики-нолики для двух игроков. Использовать в программе основное меню.
Предусмотреть в игре изменение размера поля.

"""


from tkinter import *
from PIL import Image, ImageTk
from functools import partial


class Game:
    def __init__(self):
        self.__field_size = 3
        self.__root = Tk()
        self.turn = 1

    # this method is not written by me, but it is weird that Tkinter does not have it as a built-in method
    def center_main_window_at_start(self):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        self.__root.update_idletasks()
        width = self.__root.winfo_width()
        frm_width = self.__root.winfo_rootx() - self.__root.winfo_x()
        win_width = width + 2 * frm_width
        height = self.__root.winfo_height()
        titlebar_height = self.__root.winfo_rooty() - self.__root.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.__root.winfo_screenwidth() // 2 - win_width // 2
        y = self.__root.winfo_screenheight() // 2 - win_height // 2
        self.__root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.__root.deiconify()

    def field_size(self):
        return self.__field_size

    def set_field_size(self, field_size):
        self.__field_size = field_size

    def start(self):
        self.__root.title("Tic-Tac-Toe")
        self.__root.geometry("800x600")
        self.__root.minsize(800, 600)
        self.__root.configure(bg="#222020")

        self.center_main_window_at_start()

        # self.__root.eval('tk::PlaceWindow . center')

        # self.__root.resizable(False, False)

        self.main_menu()

    def main_menu(self):
        self.reset()

        text_label = Label(self.__root, text="Tic-Tac-Toe", bg="#222020", fg="#d9d9d9", font=("Arial", 40))
        text_label.pack(fill='x', side='top', pady=50)

        image = ImageTk.PhotoImage(Image.open("tic_tac_toe.png").resize((170, 140), Image.LANCZOS))
        image_label = Label(self.__root, bg="#222020", image=image, borderwidth=0, highlightthickness=0)
        image_label.pack(side='top')

        parent = Frame(self.__root, bg="#222020")

        play_button = Button(parent, text="Play", bg="#d9d9d9", font=('Maharlika', 18), width=12, height=1,
                             command=self.play_game)
        play_button.pack(fill='x', pady=20)

        settings_button = Button(parent, text="Settings", bg="#d9d9d9", font=('Maharlika', 18), width=12, height=1,
                                 command=self.settings_menu)
        settings_button.pack(fill='x')

        quit_button = Button(parent, text="Quit", bg="#d9d9d9", font=('Maharlika', 18), width=12, height=1,
                             command=self.__root.destroy)
        quit_button.pack(fill='x', pady=20)

        parent.pack(expand=True)

        self.__root.mainloop()

    def settings_menu(self):
        self.reset()

        text_label = Label(self.__root, text="Change field size", bg="#222020", fg="#d9d9d9", font=("Arial", 40))
        text_label.pack(fill='x', side='top', pady=50)

        parent = Frame(self.__root, bg="#222020")

        new_size = IntVar()

        field_size_scale = Scale(parent, orient='horizontal', length=5, from_=3, to=8, variable=new_size)
        field_size_scale.set(self.__field_size)
        field_size_scale.pack(fill='x', pady=20)

        def back_to_menu():
            self.__field_size = new_size.get()
            print(self.__field_size)
            self.main_menu()

        back_to_main_menu_button = Button(parent, text="Save and return to main menu", bg="#d9d9d9", font=('Maharlika', 18), width=30, height=1,
                             command=back_to_menu)
        back_to_main_menu_button.pack(fill='x', pady=20)

        parent.pack(expand=True)

    # player_symbol:
    # 1 if checking for X
    # 0 if checking for 0
    def player_won(self, field, player_symbol):
        for i in range(self.__field_size):
            flag = True
            for j in range(self.__field_size):
                if field[i][j] != player_symbol:
                    flag = False
            if flag:
                return [(i, j) for j in range(self.__field_size)]

        for i in range(self.__field_size):
            flag = True
            for j in range(self.__field_size):
                if field[j][i] != player_symbol:
                    flag = False
            if flag:
                return [(j, i) for j in range(self.__field_size)]

        main_diagonal_flag = True
        for i in range(self.__field_size):
            for j in range(self.__field_size):
                if field[i][j] != player_symbol and i == j:
                    main_diagonal_flag = False
        if main_diagonal_flag:
            return [(i, i) for i in range(self.__field_size)]

        off_diagonal_flag = True
        for i in range(self.__field_size):
            if field[i][-i-1] != player_symbol:
                off_diagonal_flag = False
        if off_diagonal_flag:
            return [(i, abs(i - self.__field_size + 1)) for i in range(self.__field_size)]

        return None

    def xo_button_click(self, xo_button: Button, turn_text: Label, field: list, i: int, j: int):

        if self.turn % 2 == 0:  # zero's turn
            field[i][j] = 0
            turn_text['text'] = "Current Turn: X"
            xo_button['text'] = '0'
        else:
            field[i][j] = 1
            turn_text['text'] = "Current Turn: 0"
            xo_button['text'] = 'X'

        x_win_coeffs = self.player_won(field, 1)
        o_win_coeffs = self.player_won(field, 0)
        # check if X won
        if x_win_coeffs is not None:
            for button in self.__root.winfo_children()[1].winfo_children():
                button.config(state='disabled')
                button['bg'] = '#222020'
                button.config(highlightbackground='#222020')
                button.config(highlightthickness='3')
                button.config(bd='0')
                if button['text'] == '':
                    button.config(text='#')

                for coeffs in x_win_coeffs:
                    if button.grid_info()['row'] == coeffs[0] and button.grid_info()['column'] == coeffs[1]:
                        button['bg'] = '#7de849'

            self.__root.winfo_children()[0].destroy()

            back_to_menu_button = Button(self.__root, width=20, height=2, text='X won\nBack to menu', font='15',
                                         command=self.main_menu)
            back_to_menu_button.grid(row=0, column=0, sticky=N, pady=30)

        # check if 0 won
        elif o_win_coeffs is not None:
            for button in self.__root.winfo_children()[1].winfo_children():
                button.config(state='disabled')
                button['bg'] = '#222020'
                button.config(highlightbackground='#222020')
                button.config(highlightthickness='3')
                button.config(bd='0')
                if button['text'] == '':
                    button.config(text='#')

                for coeffs in o_win_coeffs:
                    if button.grid_info()['row'] == coeffs[0] and button.grid_info()['column'] == coeffs[1]:
                        button['bg'] = '#7de849'

            self.__root.winfo_children()[0].destroy()

            back_to_menu_button = Button(self.__root, width=20, height=2, text='0 won\n Back to menu', font='15',
                                         command=self.main_menu)
            back_to_menu_button.grid(row=0, column=0, sticky=N, pady=30)

        elif self.turn == self.__field_size**2:
            xo_button['bg'] = '#222020'
            xo_button.config(highlightbackground='#222020')
            xo_button.config(highlightthickness='3')
            xo_button.config(bd='0')
            xo_button.config(state='disabled')

            self.__root.winfo_children()[0].destroy()

            back_to_menu_button = Button(self.__root, width=20, height=2, text='Nobody won\nBack to menu', font='15',
                                         command=self.main_menu)
            back_to_menu_button.grid(row=0, column=0, sticky=N, pady=30)

        else:
            self.turn += 1

            xo_button['bg'] = '#222020'
            xo_button.config(highlightbackground='#222020')
            xo_button.config(highlightthickness='3')
            xo_button.config(bd='0')
            xo_button.config(state='disabled')

    def play_game(self):
        self.reset()
        self.turn = 1

        current_turn_text_label = Label(self.__root, text="Current Turn: X", bg="#222020", fg="#d9d9d9",
                                        font=("Arial", 40))
        current_turn_text_label.grid(row=0, column=0, sticky=N, pady=30)

        play_field = []
        field_frame = Frame(self.__root, bg='#222020')

        for i in range(self.__field_size):
            play_field.append([])
            for j in range(self.__field_size):
                play_field[i].append([])
                xo_button = Button(field_frame, width=5, height=2, disabledforeground='red', font='50')
                xo_button['command'] = partial(self.xo_button_click,
                                               xo_button,
                                               current_turn_text_label,
                                               play_field,
                                               i, j)
                xo_button.grid(row=i, column=j)

        field_frame.grid(row=0, column=0)
        field_frame.grid_rowconfigure(0, weight=1)
        field_frame.grid_columnconfigure(0, weight=1)
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

    def reset(self):
        if len(self.__root.winfo_children()) != 0:
            for child in self.__root.winfo_children():
                child.destroy()


def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
