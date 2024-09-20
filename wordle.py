import tkinter as tk
from tkinter import messagebox
import random

five_letter_words = [
    "apple", "bread", "chair", "dance", "eagle", "flame", "grass", "house", "ideal", "joker",
    "alarm", "brave", "candy", "dream", "earth", "flair", "globe", "heart", "index", "jolly",
    "knack", "laser", "mango", "night", "ocean", "peace", "queen", "robot", "stone", "tiger",
    "usual", "vigor", "waltz", "zebra", "actor", "beach", "cloud", "dough", "enter", "frank",
    "glove", "haste", "input", "jumpy", "kites", "latch", "mirth", "novel", "olive", "piano",
    "quilt", "radio", "sheep", "trophy", "under", "valid", "whale", "yacht", "zesty", "apple",
    "brick", "climb", "daisy", "eagle", "frost", "grape", "hobby", "ivory", "jewel", "knife",
    "light", "mirth", "needy", "olive", "pearl", "quash", "racer", "scale", "train", "upset",
    "vigor", "waste", "xenon", "yearn", "zesty", "agent", "blush", "candy", "dread", "eerie",
    "flute", "gleam", "heart", "icicle", "jumpy", "knock", "leafy", "march", "noble", "opine",
    "pinky", "quilt", "react", "sheen", "trick", "unity", "vapid", "wacky", "xylem", "yield",
    "zesty", "aider", "baker", "caddy", "dance", "eagle", "fable", "gleef", "hover", "index",
    "jaded", "kiosk", "laser", "mango", "nerdy", "olive", "plumb", "query", "river", "sassy",
    "table", "unite", "value", "waver", "xenon", "yield", "zippy", "altar", "brisk", "charm",
    "douse", "eject", "froth", "glint", "hasty", "input", "joint", "knack", "light", "moist",
    "nudge", "ocean", "punch", "quilt", "roast", "sneak", "tramp", "usual", "vowel", "wound",
    "xenon", "youth", "zebra", "abbey", "bloom", "cider", "dandy", "elbow", "fresh", "glide",
    "hitch", "ivory", "jolly", "knoll", "laser", "meaty", "nerve", "oasis", "plaza", "quake",
    "ratio", "savor", "tango", "urban", "vocal", "wryly", "yacht", "zesty", "alien", "baker",
    "candy", "dough", "eagle", "frown", "globe", "haste", "irony", "jolly", "karma", "laser",
    "mango", "noble", "olive", "plumb", "quiet", "rocky", "shout", "tiger", "unity", "vivid",
    "waste", "xenon", "yield", "zippy", "amber", "bingo", "cider", "ducky", "eager", "fluff",
    "gorge", "honey", "indie", "joker", "kites", "lapse", "mirth", "nerdy", "ocean", "plaza",
    "quilt", "raspy", "sneak", "tread", "ultra", "vivid", "wryly", "xerox", "yacht", "zesty",
    "alarm", "brisk", "crush", "daisy", "enter", "fable", "glory", "harsh", "ivory", "jolly",
    "knack", "lemon", "mango", "needy", "olive", "pearl", "quark", "racer", "stark", "tiger",
    "ugly", "vapor", "whale", "xenon", "yacht", "zesty", "arcus", "bride", "cider", "deity",
    "equid", "frizz", "glove", "heart", "irony", "jewel", "knock", "lapse", "march", "novel",
    "orate", "plume", "quest", "rover", "scoop", "trust", "ultra", "verge", "wacky", "xylem",
    "youth", "zippy", "abyss", "bliss", "crate", "douse", "earth", "flare", "gloom", "hasty",
    "ideal", "jolly", "knife", "laser", "meaty", "nerve", "oasis", "plaza", "quilt", "racer",
    "shine", "tryst", "upend", "vowel", "wider", "xenon", "yield", "zesty", "alert", "bloat",
    "curve", "dance", "eagle", "frown", "glint", "hitch", "index", "jumpy", "knack", "lemon",
    "moist", "nifty", "olive", "plumb", "quirk", "reset", "scorn", "trend", "upend", "vapid",
    "whirl", "xenon", "yield", "zesty", "aroma", "baker", "cleat", "dandy", "every", "fable",
    "grace", "haste", "irony", "jolly", "knock", "lunar", "mango", "nerve", "ocean", "plaza",
    "quiet", "racer", "scale", "tiger", "ultra", "vigor", "whale", "xylem", "yacht", "zippy",
    "alien", "brisk", "clash", "drama", "eject", "flair", "gloom", "honey", "indie", "joker",
    "karma", "lapse", "mirth", "nerdy", "oasis", "plumb", "quirk", "razor", "scoff", "tread",
    "unzip", "vivid", "wryly", "xenon", "yield", "zesty", "agile", "brave", "charm", "debut",
    "elude", "frost", "gleam", "hasty", "index", "jumpy", "knock", "lance", "meaty", "noble",
    "olive", "plume", "quest", "rapid", "sheep", "tango", "uncle", "vapor", "waltz", "xylem",
    "youth", "zesty", "apple", "beard", "chair", "dance", "eagle", "fable", "grape", "hatch",
    "inbox", "jewel", "knife", "laser", "mango", "nifty", "olive", "plumb", "quirk", "relay",
    "scoop", "tiger", "usual", "vigor", "whale", "xenon", "yield", "zesty", "altar", "brisk",
    "creek", "douse", "eject", "fluff", "glide", "harsh", "indie", "jolly", "karma", "lemon",
    "moist", "nerve", "olive", "plaza", "quilt", "racer", "scale", "tread", "urban", "vapid",
    "waver", "xenon", "yacht", "zesty", "actor", "beach", "cloud", "dough", "enter", "frank",
    "glove", "haste", "input", "jumpy", "kites", "latch", "mirth", "novel", "olive", "piano",
    "quilt", "radio", "sheep", "trophy", "under", "valid", "whale", "yacht", "zebra", "abbey",
    "bloom", "cider", "dandy", "elbow", "fresh", "glide", "hitch", "ivory", "jolly", "knoll",
    "laser", "meaty", "nerve", "oasis", "plaza", "quake", "ratio", "savor", "tango", "urban",
    "vocal", "wryly", "yacht", "zesty", "aider", "baker", "caddy", "dance", "eagle", "fable",
    "gleef", "hover", "index", "jaded", "kiosk", "laser", "mango", "nerdy", "olive", "plumb",
    "query", "river", "sassy", "table", "unite", "value", "waver", "xenon", "yield", "zippy",
    "alarm", "brisk", "crush", "daisy", "enter", "fable", "glory", "harsh", "ivory", "jolly",
    "knack", "lemon", "mango", "needy", "olive", "pearl", "quark", "racer", "stark", "tiger",
    "ugly", "vapor", "whale", "xenon", "yacht", "zesty", "arcus", "bride", "cider", "deity",
    "equid", "frizz", "glove", "heart", "irony", "jewel", "knock", "lapse", "march", "novel",
    "orate", "plume", "quest", "rover", "scoop", "trust", "ultra", "verge", "wacky", "xylem",
    "youth", "zippy", "abyss", "bliss", "crate", "douse", "earth", "flare", "gloom", "hasty",
    "ideal", "jolly", "knife", "laser", "meaty", "nerve", "oasis", "plaza", "quilt", "racer",
    "shine", "tryst", "upend", "vowel", "wider", "xenon", "yield", "zesty", "alert", "bloat",
    "curve", "dance", "eagle", "frown", "glint", "hitch", "index", "jumpy", "knack", "lemon",
    "moist", "nifty", "olive", "plumb", "quirk", "reset", "scorn", "trend", "upend", "vapid",
    "whirl", "xenon", "yield", "zesty", "aroma", "baker", "cleat", "dandy", "every", "fable",
    "grace", "haste", "irony", "jolly", "knock", "lunar", "mango", "nerve", "ocean", "plaza",
    "quiet", "racer", "scale", "tiger", "ultra", "vigor", "whale", "xylem", "yacht", "zippy"
]


o_word = random.choice(five_letter_words)

root = tk.Tk()
root.title("Wordle Game")
root.geometry("400x600")

# Dark theme colors
bg_color = "#2e2e2e"
fg_color = "#ffffff"
entry_bg_color = "#3e3e3e"
entry_fg_color = "#00ff00"
button_bg_color = "#4e4e4e"
button_fg_color = "#ffffff"

# Set dark theme
root.configure(bg=bg_color)

guess_try = 1
max_tries = 6
word_length = 5

entries = []

def on_key_release(event, i, j):
    widget = event.widget
    if widget.get():
        if j < word_length - 1:
            entries[i][j + 1].focus_set()
        elif i < max_tries - 1:
            entries[i + 1][0].focus_set()

for i in range(max_tries):
    row_entries = []
    for j in range(word_length):
        entry = tk.Entry(root, font=("Helvetica", 28), width=2, justify="center", 
                         bg=entry_bg_color, fg=entry_fg_color)
        entry.grid(row=i, column=j, padx=5, pady=10)
        entry.bind("<KeyRelease>", lambda event, i=i, j=j: on_key_release(event, i, j))
        row_entries.append(entry)
    entries.append(row_entries)

feedback_label = tk.Label(root, text="", font=("Helvetica", 18), bg=bg_color, fg=fg_color)
feedback_label.grid(row=max_tries + 1, column=0, pady=20, columnspan=word_length)

def check_word():
    global guess_try

    if guess_try > max_tries:
        messagebox.showinfo("Game Over", f"The correct word was: {o_word}")
        return

    guess_word = ''.join([entries[guess_try - 1][i].get() for i in range(word_length)])

    if len(guess_word) != word_length:
        messagebox.showwarning("Invalid", "Please enter all 5 letters.")
        return

    counter = ['x'] * word_length
    
    for i in range(word_length):
        if guess_word[i] == o_word[i]:
            counter[i] = guess_word[i]
        elif guess_word[i] in o_word:
            counter[i] = f"{guess_word[i]}*"

    feedback = ' '.join(counter)
    
    if counter == ['x'] * word_length:
        feedback_label.config(text="Sorry, no letters are correct.", fg="red")
    else:
        feedback_label.config(text=f"Feedback: {feedback} ('*' means correct letter, wrong position)", fg="blue")

    for entry in entries[guess_try - 1]:
        entry.config(state="disabled")

    if guess_word == o_word:
        messagebox.showinfo("Congratulations", f"You guessed the word '{o_word}' in {guess_try} tries!")
        root.quit()
    elif guess_try == max_tries:
        messagebox.showinfo("Game Over", f"You've used all your tries. The word was '{o_word}'.")
        root.quit()
    else:
        guess_try += 1

submit_button = tk.Button(root, text="Submit", font=("Helvetica", 16), command=check_word,
                          bg=button_bg_color, fg=button_fg_color)
submit_button.grid(row=max_tries + 2, column=0, pady=20, columnspan=word_length)

root.mainloop()