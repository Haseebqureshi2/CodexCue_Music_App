import pygame
import os
from tkinter import Tk, Button, Label, filedialog

# Initialize pygame mixer
pygame.mixer.init()

# Music Player Class
class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Music Player")
        self.root.geometry("400x300")

        # Initialize variables
        self.playing_state = False
        self.current_song = ""

        # Song label
        self.song_label = Label(self.root, text="No song selected", font=("Helvetica", 12))
        self.song_label.pack(pady=20)

        # Buttons
        self.play_button = Button(self.root, text="Play", width=10, command=self.play_song)
        self.play_button.pack(pady=10)

        self.pause_button = Button(self.root, text="Pause", width=10, command=self.pause_song)
        self.pause_button.pack(pady=10)

        self.resume_button = Button(self.root, text="Resume", width=10, command=self.resume_song)
        self.resume_button.pack(pady=10)

        self.stop_button = Button(self.root, text="Stop", width=10, command=self.stop_song)
        self.stop_button.pack(pady=10)

        self.select_button = Button(self.root, text="Select Song", width=10, command=self.load_song)
        self.select_button.pack(pady=10)

    # Load song from file
    def load_song(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            self.current_song = file_path
            self.song_label.config(text=f"Loaded: {os.path.basename(file_path)}")

    # Play selected song
    def play_song(self):
        if self.current_song:
            pygame.mixer.music.load(self.current_song)
            pygame.mixer.music.play()
            self.playing_state = True

    # Pause song
    def pause_song(self):
        if self.playing_state:
            pygame.mixer.music.pause()

    # Resume song
    def resume_song(self):
        if self.playing_state:
            pygame.mixer.music.unpause()

    # Stop song
    def stop_song(self):
        if self.playing_state:
            pygame.mixer.music.stop()
            self.playing_state = False

# Initialize the application
if __name__ == "__main__":
    root = Tk()
    app = MusicPlayer(root)
    root.mainloop()
