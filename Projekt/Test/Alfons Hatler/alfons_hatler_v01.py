import tkinter as tk
import random
from PIL import Image, ImageTk
import os


class RandomImageApp:
    def __init__(self, master, image_paths):
        self.master = master
        self.image_paths = image_paths

        self.master.title("Zufälliges Bild anzeigen")
        self.master.attributes('-fullscreen', True)  # Vollbildmodus aktivieren

        self.image_label = tk.Label(master)
        self.image_label.pack(fill=tk.BOTH, expand=True)

        self.show_random_image_button = tk.Button(master, text="Zufälliges Bild anzeigen",
                                                  command=self.show_random_image)
        self.show_random_image_button.pack()

    def show_random_image(self):
        random_image_path = random.choice(self.image_paths)
        image = Image.open(random_image_path)
        photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo


# Pfad zum Ordner mit den Bildern
data_folder = "Data"
# Bildpfade aus dem Data-Ordner
image_paths = [os.path.join(data_folder, filename) for filename in os.listdir(data_folder) if
               filename.endswith(('.png', '.jpg'))]

root = tk.Tk()
app = RandomImageApp(root, image_paths)
root.mainloop()
