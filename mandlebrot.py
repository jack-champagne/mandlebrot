from tkinter import *
import time
import math


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

        self.graph_area = Canvas(master, width=750, height=500)
        self.graph_area.pack()

        # Creating background
        self.graph_area.create_rectangle(0, 0, 750, 500, fill='#002200')

        # Draw coords?

        # Calculate
        self.calculate = Button(frame, text='Hello', command=self.render)
        self.calculate.pack(side=LEFT)

        # Constants
        self.x, self.y = 10, 10
        self.iterations = 1000
        # Working vars (add z to self for future visualizations?)

        # Test
        self.draw_pixel(x=100, y=100, color=True)
        self.draw_pixel(x=102, y=102, color=False)
        print(self.pixel_color(x=2, y=-1))

    def render(self):
        start_time = time.thread_time()
        for x in range(750):
            for y in range(500):
                # Do world space and pixel space conversion
                f_x = x / 200 - 2.25
                f_y = y / 200 - 1.25
                self.draw_pixel(x=x, y=y, color=self.pixel_color(f_x, f_y))
        end_time = time.thread_time()
        print("Done in " + str(end_time - start_time) + " secs")

    def pixel_color(self, x, y):
        c = complex(x, y)
        z = complex(0, 0)
        i = 0
        while i < self.iterations:
            if (z.imag ** 2 + z.real ** 2) < (2 ** 2):
                z = z ** 2 + c
                i += 1
            else:
                return False
        return True

    def draw_pixel(self, x, y, color):
        if color:
            self.graph_area.create_rectangle(x, y, x + 1, y + 1, outline='white')
        else:
            self.graph_area.create_rectangle(x, y, x + 1, y + 1, outline='black')


root = Tk()
app = Mandlebrot(root)
root.mainloop()
root.destroy()

# Cool! I should multi-thread this! If only I could use SIMD in python (is there a way??)
# I definitely need to do this in C++ next.
