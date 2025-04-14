# Save this code in a file with .py extension (e.g., "birthday_larissa.py")
# Make sure you have Python installed on your computer
# Open command prompt/terminal in the folder containing this file
# Run the command: python birthday_larissa.py

import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

def create_birthday_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Happy Birthday Larissa ❤️")
    root.geometry("800x600")
    root.configure(bg="#FFD1DC")  # Light pink background

    # Header Frame
    header_frame = tk.Frame(root, bg="#FF69B4")  # Hot pink
    header_frame.pack(fill="x")

    # Title Label
    title_label = tk.Label(
        header_frame,
        text="Happy Birthday My Love 💖",
        font=("Helvetica", 24, "bold"),
        bg="#FF69B4",
        fg="white",
        pady=20
    )
    title_label.pack()

    # Main Content Frame
    content_frame = tk.Frame(root, bg="#FFD1DC", padx=20, pady=20)
    content_frame.pack(expand=True, fill="both")

    # Animated Heart
    def animate_heart():
        heart_label.config(text="💖")
        root.after(500, lambda: heart_label.config(text="❤️"))
        root.after(1000, animate_heart)

    heart_label = tk.Label(
        content_frame,
        text="❤️",
        font=("Arial", 48),
        bg="#FFD1DC"
    )
    heart_label.pack(pady=10)
    animate_heart()

    # Love Message
    message_label = tk.Label(
        content_frame,
        text="Though we may be apart in distance,\nwe're always connected at heart.\nHappy Birthday, my beautiful Larissa!",
        font=("Georgia", 16),
        bg="#FFD1DC",
        fg="#8B008B",
        pady=20
    )
    message_label.pack()

    # Virtual Hug Button
    def send_hug():
        messagebox.showinfo("Virtual Hug", "🤗 Sending you the biggest virtual hug!\nWish I could be there with you today!")

    hug_button = tk.Button(
        content_frame,
        text="🤗 Send Virtual Hug",
        font=("Arial", 14),
        bg="#FF1493",
        fg="white",
        command=send_hug
    )
    hug_button.pack(pady=10)

    # Love Letter Button
    def show_love_letter():
        letter_window = tk.Toplevel(root)
        letter_window.title("My Love Letter to You ❤️")
        letter_window.geometry("500x400")
        letter_window.configure(bg="#FFF0F5")

        letter_text = """my dear larissa


there isn’t a second that passes where I don’t find myself thinking of you baby. ur everywhere, when i daydream, in the sky when the sun sets, in the way the wind brushes against my hair ur always a thought in my mind
being apart from you is annoying. It doesn’t feel good. my days are full of things, school, gym, noise, rusty barking, but none of it matters the same way it does when i see you. i always miss your laugh. i miss the way your eyes soften when you look at me like I’m the only one in the world.
sometimes I close my eyes and try to picture you standing in front of me. I’d give anything to hold you right now, even just for a minute. I want to be near you, to trace your face with my fingertips, to feel your heartbeat against mine. The distance may be great, but my love for you is greater still. It stretches across cities, across skies, across time.
i don’t know when I’ll see you again but i need you to know that I’m waiting for you. ill keep waiting. ill always wait, because you’re worth every mile, every lonely night, every missed moment.
and when that day finally comes, when I can hold you again I swear I’ll never let go.
"""

        letter_label = tk.Label(
            letter_window,
            text=letter_text,
            font=("Comic Sans MS", 12),
            bg="#FFF0F5",
            fg="#8B008B",
            justify="left",
            wraplength=400
        )
        letter_label.pack(pady=20)

    letter_button = tk.Button(
        content_frame,
        text="💌 Read Love Letter",
        font=("Arial", 14),
        bg="#BA55D3",
        fg="white",
        command=show_love_letter
    )
    letter_button.pack(pady=10)

    # Play Special Song
    def play_song():
        webbrowser.open("https://www.youtube.com/watch?v=y1cBhJLNNXU")  # Replace with your special song URL

    song_button = tk.Button(
        content_frame,
        text="🎵 Play Our Song",
        font=("Arial", 14),
        bg="#BA55D3",
        fg="white",
        command=play_song
    )
    song_button.pack(pady=10)

    # Footer
    footer_label = tk.Label(
        content_frame,
        text="Made with endless love for my Larissa ❤️",
        font=("Comic Sans MS", 12),
        bg="#FFD1DC",
        fg="#8B0000"
    )
    footer_label.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_birthday_gui()

# To run this program:
# 1. Save this file as "birthday_larissa.py"
# 2. Make sure Python is installed on your computer
# 3. Open command prompt/terminal
# 4. Navigate to the folder containing this file
# 5. Type: python birthday_larissa.py
# 6. Press Enter

