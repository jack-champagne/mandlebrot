from tkinter import LEFT, Frame, Button, Canvas, Tk
import time
import math

def color_to_hex(r, g, b):
    return '#' + hex(r * 256 * 256 + g * 256 + b).replace('0x', '').zfill(6)


class Mandlebrot:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame,
            text="Exit",
            fg="red",
            command=frame.quit
        )
        self.button.pack(side=LEFT)

        self.graph_area = Canvas(master, width=1800, height=900)
        self.graph_area.pack()

        # Creating background
        self.graph_area.create_rectangle(0, 0, self.graph_area.winfo_screenwidth(), self.graph_area.winfo_screenheight(), fill='#000000')

        # Draw coords?


        # Calculate
        self.calculate = Button(frame, text='Hello', command=self.render)
        self.calculate.pack(side=LEFT)

        # Constants
        self.x, self.y = 10, 10
        self.iterations = 1000
        # Working vars (add z to self for future visualizations?

    def render(self):
        print("help!")
        start_time = time.thread_time()
        for x in range(self.graph_area.winfo_screenwidth()):
            for y in range(self.graph_area.winfo_screenheight()):
                self.draw_pixel(x=x, y=y)
        end_time = time.thread_time()
        print("Done in " + str(end_time - start_time) + " secs")

    def pixel_color(self, x, y):
        ax = x / self.graph_area.winfo_screenwidth()
        ay = y / self.graph_area.winfo_screenheight()
        col = color_to_hex(math.floor((math.sin(50 * math.pi * ax) + 1) * 255/2), math.floor((math.sin(50 * math.pi * ay) + 1) * 255/2), 10)

        return col

    def draw_pixel(self, x, y):
            self.graph_area.create_rectangle(x, y, x + 1, y + 1, outline=self.pixel_color(x, y), fill=self.pixel_color(x, y))


root = Tk()
app = Mandlebrot(root)
root.mainloop()
root.destroy()

# Cool! I should multi-thread this! If only I could use SIMD in python (is there a way??)
# I definitely need to do this in C++ next.
