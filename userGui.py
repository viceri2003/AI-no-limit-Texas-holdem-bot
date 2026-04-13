import tkinter as tk
import pokerEnvironment
from pokerEnvironment import heads_up_poker

game = heads_up_poker("User", "Bot")
root = tk.Tk()
root.title("Poker")
root.geometry("300x300")

root.mainloop()



