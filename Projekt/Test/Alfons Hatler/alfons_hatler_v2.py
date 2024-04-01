import tkinter as tk
import random
from PIL import Image, ImageTk
import os
import time


class TitleScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Titelbildschirm")

        self.title_label = tk.Label(master, text="Sind Sie Alfons Hatler oder nicht?", font=("Helvetica", 16))
        self.title_label.pack(pady=20)

        self.find_out_button = tk.Button(master, text="Finde es heraus", command=self.show_test_screen)
        self.find_out_button.pack(pady=10)

        self.quit_button = tk.Button(master, text="Beenden", command=self.quit)
        self.quit_button.pack(pady=10)

    def show_test_screen(self):
        self.master.destroy()  # Schließe den Titelbildschirm
        test_screen = TestScreen()

    def quit(self):
        self.master.destroy()


class TestScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Testbildschirm")

        self.start_test_button = tk.Button(self.root, text="Test starten", command=self.start_test)
        self.start_test_button.pack(pady=20)

        self.root.mainloop()

    def start_test(self):
        self.root.destroy()  # Schließe den Testbildschirm
        test_timer_screen = TestTimerScreen()


class TestTimerScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Test Timer")

        self.timer_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.timer_label.pack(pady=20)

        self.timer_countdown()

        self.root.mainloop()

    def timer_countdown(self):
        for i in range(5, 0, -1):
            self.timer_label.config(text=f"Timer: {i}")
            self.root.update()
            time.sleep(1)
        self.show_random_image()

    def show_random_image(self):
        self.root.destroy()  # Schließe den Timerbildschirm
        random_image_screen = RandomImageScreen()

class RandomImageScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Zufälliges Bild")

        # Pfad zum Ordner mit den Bildern
        data_folder = "Data"
        # Bildpfade aus dem Data-Ordner
        self.image_paths = [os.path.join(data_folder, filename) for filename in os.listdir(data_folder) if filename.endswith(('.png', '.jpg'))]

        self.show_random_image()

        self.back_to_menu_button = tk.Button(self.root, text="Zurück zum Hauptmenü", command=self.back_to_menu)
        self.back_to_menu_button.pack(pady=20)

        self.root.mainloop()

    def show_random_image(self):
        random_image_path = random.choice(self.image_paths)
        self.image = Image.open(random_image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self.root, image=self.photo)
        self.image_label.pack()

    def back_to_menu(self):
        self.root.destroy()  # Schließe den Bildschirm für das zufällige Bild
        title_screen = TitleScreen(tk.Tk())

    # Titelbildschirm anzeigen
    title_screen = TitleScreen(tk.Tk())

