from tkinter import *
from PIL import Image, ImageTk


class Game:
    def __init__(self):
        self.__field_size = 3
        self.__root = Tk()

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

    def play_game(self):
        self.reset()
        play_field = []
        xo_button = Button()

        for i in range(self.__field_size):
            play_field.append([])
            for _ in range(self.__field_size):
                play_field[i].append(

                )


    def reset(self):
        if len(self.__root.winfo_children()) != 0:
            for child in self.__root.winfo_children():
                child.destroy()


def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()