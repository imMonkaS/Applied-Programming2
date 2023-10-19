from tkinter import *
from PIL import Image, ImageTk
from functools import partial


class Game:
    def __init__(self):
        self.__field_size = 3
        self.__root = Tk()
        self.turn = 1

    def field_size(self):
        return self.__field_size

    def set_field_size(self, field_size):
        self.__field_size = field_size

    def start(self):
        self.__root.title("Tic-Tac-Toe")
        self.__root.geometry("800x600")
        self.__root.minsize(800, 600)
        self.__root.configure(bg="#222020")
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
                             command=self.__root.quit)
        quit_button.pack(fill='x', pady=20)

        parent.pack(expand=True)

        self.__root.mainloop()

    def settings_menu(self):
        pass

    def check_for_winner(self, field):
        for i in range(self.__field_size):
            flag = True
            for j in range(self.__field_size):
                if field[i][j] == 1:
                    flag = False

    def set_on_field(self, xo_button: Button, field: list, i: int, j: int):
        # if field[i][j][0] == 2:
        if self.turn % 2 == 0:  # zero's turn
            field[i][j] = 0
            xo_button['text'] = '0'
        else:
            field[i][j] = 1
            xo_button['text'] = 'X'

        self.turn += 1

        xo_button.config(state='disabled')

    def play_game(self):
        self.reset()

        turn = 1
        play_field = []

        for i in range(self.__field_size):
            play_field.append([])
            for j in range(self.__field_size):
                play_field[i].append([2])
                xo_button = Button(width=5, height=2)
                xo_button['command']=partial(self.set_on_field, xo_button, play_field, i, j)
                # xo_button['command'] = partial(self.set_on_field, xo_button, play_field, turn, i, j)
                xo_button.grid(row=i, column=j)

        print(play_field)

    def reset(self):
        if len(self.__root.winfo_children()) != 0:
            for child in self.__root.winfo_children():
                child.destroy()


def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
