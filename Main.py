import tkinter as tk
import tkinter.ttk as ttk
import unicodedata as unicode

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Unicode Viewer")
        self.geometry("800x600")
        self.config(borderwidth=-1, bd=-1, border=0)

    def debug_info(self):
        print("#====================\\")
        print("| Screen Height:\t | "+str(self.winfo_screenheight()))
        print("| Screen Width:\t\t | "+str(self.winfo_screenwidth()))
        print("| Screen Depth:\t\t | "+str(self.winfo_screendepth()))
        print("| Screen Cells:\t\t | "+str(self.winfo_screencells()))
        print("| Screen Visual:\t | "+str(self.winfo_screenvisual()))
        print("| Window Name: \t\t | "+str(self.winfo_name()))
        print("| Window Is mapped:\t | "+str(self.winfo_ismapped()))
        print("| Window Viewable: \t | "+str(self.winfo_viewable()))
        print("| Window Visual ID:\t | "+str(self.winfo_visualid()))
        print("| Window Cells: \t | "+str(self.winfo_cells()))
        print("| Window Depth:\t\t | "+str(self.winfo_depth()))
        print("| Window ID:\t\t | "+str(self.winfo_id()))
        print("| Window Exits:\t\t | "+str(self.winfo_exists()))
        print("| Window Geometry:\t | "+str(self.winfo_geometry()))
        print("| Window Height:\t\t | "+str(self.winfo_height()))
        print("| Window Width:\t\t | "+str(self.winfo_width()))
        print("| Window X:\t\t\t | "+str(self.winfo_x()))
        print("| Window Y:\t\t\t | "+str(self.winfo_y()))
        print("| vRoot Height:\t\t | "+str(self.winfo_vrootheight()))
        print("| vRoot Width:\t\t | "+str(self.winfo_vrootwidth()))
        print("| vRoot X:\t\t\t | "+str(self.winfo_vrootx()))
        print("| vRoot Y:\t\t\t | "+str(self.winfo_vrooty()))
        print("| Root X:\t\t\t | "+str(self.winfo_rootx()))
        print("| Root Y:\t\t\t | "+str(self.winfo_rooty()))
        print("| Req. Height:\t\t | "+str(self.winfo_reqheight()))
        print("| Req. Width:\t\t | "+str(self.winfo_reqwidth()))
        print("| Manager:\t\t\t | "+str(self.winfo_manager()))
        print("| Color Map Full:\t | "+str(self.winfo_colormapfull()))
        print("| Class:\t\t\t | "+str(self.winfo_class()))
        print("| Pointer Pos: \t\t | "+str(self.winfo_pointerxy()))
        print("| PC Info: \t\t\t | "+str(self.winfo_server()))
        print("| Children:\t\t\t | "+str(self.winfo_children()))
        print("#====================/")


class MainCanvas(tk.Canvas):
    def __init__(self, master):
        """
        Custom Canvas.
        :param master:
        """
        super().__init__(master, bd=0, borderwidth=0, highlightthickness=0)
        self.config(background="Orange")

    def winfo_background(self):
        """
        Information about the background color.
        :return str:
        """

        return self.cget("background")


class CharInfo:
    def __init__(self, master, root):
        """
        Init of CharInfo. Initializes the character viewer.
        :param master:
        :param root:
        """

        # Sets master and root classes
        self.master = master
        self.root = root

        # Reading size of the Canvas.
        height = master.winfo_height()
        width = master.winfo_width()
        mid_x = width / 2
        mid_y = height / 2

        self.c_procent = 40

        # Debug.
        print((mid_x, mid_y), (width, height), height/20, mid_y-(40*height/768))

        # -Creating the info's-
        #  Character
        self.char_id = master.create_text(mid_x, mid_y-(40*height/768), text="!", font=("helvetica", int(self.c_procent*height/100)), fill="white")
        self.char_id_pos = (mid_x, mid_y-(40*height/768))

        # Name
        self.name_id = master.create_text(mid_x, (height-40), text=unicode.name('!').capitalize(), font=("helvetica", 15), fill="white")
        self.name_id_pos = (mid_x, height-40)

        # Number Index
        self.ord_id = master.create_text(5, 5, text="DEC: "+str(ord('!')), font=("helvetica", 15), fill="white", anchor=tk.NW)
        self.ord_id_pos = (5, 5)

        # -End of the info's-

        # Printing name ID position for debug.
        print(self.name_id_pos)

        # Sets start value for char index.
        self.index = 33

        master.bind("<Key>", self.key_event)

    def copy(self):
        print("Clipoard!")
        self.master.clipboard_clear()
        self.master.clipboard_append(chr(self.index))

    def key_event(self, event):
        """
        Key event handler. If a key was pressedm this method will been executed.
        :param event:
        :return:
        """
        if event.keysym == "Left":
            self.prev(event)
        if event.keysym == "Right":
            self.next(event)
        if event.keysym == "End":
            self.end(event)
        if event.keysym == "Home":
            self.home(event)
        if event.keysym == "Up":
            self.prev_turbo(event)
        if event.keysym == "Down":
            self.next_turbo(event)
        if event.keysym == "Prior":
            self.prev_page(event)
        if event.keysym == "Next":
            self.next_page(event)
        if event.keysym == "F11":
            # Fullscreen toggle.
            if bool((self.root.attributes("-fullscreen"))) == True:
                self.root.wm_attributes("-fullscreen", False)
            elif bool((self.root.attributes("-fullscreen"))) == False:
                self.root.wm_attributes("-fullscreen", True)
        if event.keysym == "c":
            self.copy()

    def next(self, event):
        """
        Go to the next character index
        :param event:
        :return:
        """
        if self.index < 65535:
            self.index += 1
        self.refresh()

    def prev(self, event):
        """
        Go to the previous character index.
        :param event:
        :return:
        """
        if 32 < self.index:
            self.index -= 1
        self.refresh()

    def end(self, event):
        """
        Go to the end of the index
        :param event:
        :return:
        """

        self.index = 65535
        self.refresh()

    def home(self, event):
        """
        Go to the begin of the index
        :param event:
        :return:
        """

        self.index = 32
        self.refresh()

    def next_turbo(self, event):
        if self.index < 65526:
            self.index += 10
        self.refresh()

    def prev_turbo(self, event):
        if 41 < self.index:
            self.index -= 10
        self.refresh()

    def next_page(self, event):
        if self.index < 65436:
            self.index += 100
        self.refresh()

    def prev_page(self, event):
        if 131 < self.index:
            self.index -= 100
        self.refresh()

    def resize(self, event):
        """
        Resizing all Canvas ID's
        :param event:
        :return:
        """

        # Recalculating the size and the middle of the Canvas
        height = self.master.winfo_height()
        width = self.master.winfo_width()
        mid_x = width / 2
        mid_y = height / 2

        # New pos for char_id (char_id_pos)
        pos2 = (mid_x, mid_y-(40*height/768))

        # Character Config
        self.master.move(self.char_id, -self.char_id_pos[0], -self.char_id_pos[1])
        self.master.move(self.char_id, pos2[0], pos2[1])
        self.master.itemconfig(self.char_id, font=("helvetica", int(self.c_procent*height/100)))
        self.char_id_pos = pos2

        # Char Name Config
        self.master.move(self.name_id, -self.name_id_pos[0], -self.name_id_pos[1])
        self.master.move(self.name_id, mid_x, height-40)
        self.name_id_pos = (mid_x, height-40)

        # Updates the Canvas, so also the window.
        self.master.update()

    def refresh(self):
        """
        Refresh all Canvas ID's
        :return:
        """

        # Character refresh with new.
        self.master.itemconfig(self.char_id, text=chr(self.index))

        # Name refresh with new.
        try:
            self.master.itemconfig(self.name_id, text=unicode.name(chr(self.index)).capitalize())
        except ValueError:
            self.master.itemconfig(self.name_id, text="<No Name>")

        # Index refresh with new.
        self.master.itemconfig(self.ord_id, text="DEC: "+str(self.index))

        # Updates Canvas
        self.master.update()
        self.master.update_idletasks()

        # Updates Window
        self.root.update()


# Starts here
if __name__ == "__main__":
    # Create custom Window
    Window = MainWindow()
    Window.debug_info() # Window debug info (only information in Console.

    # Create custom Canvas
    Canvas = MainCanvas(Window)
    Canvas.pack(expand=True, fill="both") # Places the Canvas on the window.
    Canvas.focus_set()

    # Updating window
    Window.update()

    # Initializing (Starts) charater and information about it. (Tkinter Window)
    c_info = CharInfo(Canvas, Window)

    # Binds a event for resizing the window. (Official for any config change)
    Window.bind_all("<Configure>", c_info.resize)

    # Using this, so that the window not closes. If the code is in the end of this file.
    Window.mainloop()