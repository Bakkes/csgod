import tkinter as tk

main_window = tk.Tk()
main_window_widgets = {
    "hello": tk.Button(main_window, text="Hello", command=quit)
}

def setup_main_window():
    for widget in main_window_widgets.values():
        widget.pack()

def main():
    main_window.mainloop()

if __name__ == '__main__':
    main()