from colorsys import hsv_to_rgb
import random
from tkinter import LEFT, Frame, Button, Canvas, Tk
import time

def color_to_hex(r, g, b):
    return '#' + hex(r * 256 * 256 + g * 256 + b).replace('0x', '').zfill(6)

def color_clip(num):
    if num < 0: return 0
    return int(num) if num < 255 else 255

CANVAS_HEIGHT =  1750
CANVAS_WIDTH = int(1.5 * CANVAS_HEIGHT)

SCALE = 2

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

        self.graph_area = Canvas(master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.graph_area.pack()

        # Creating background
        self.graph_area.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, fill='#000000')

        # Draw coords?
        self.draw_coords()

        # Calculate
        self.calculate = Button(frame, text='Hello', command=self.render)
        self.calculate.pack(side=LEFT)

        # Constants
        self.x, self.y = 10, 10
        self.iterations = 2000
        # Working vars (add z to self for future visualizations?


    def draw_coords(self):
        lx1, lx2 = self.coords_to_pixel(-2 * SCALE, 0)
        lx3, lx4 = self.coords_to_pixel(1 * SCALE, 0)
        self.graph_area.create_line(lx1, lx2, lx3, lx4,  fill="#ffffff")

        ly1, ly2 = self.coords_to_pixel(0, 1 * SCALE)
        ly3, ly4 = self.coords_to_pixel(0, -1 * SCALE)
        self.graph_area.create_line(ly1, ly2, ly3, ly4, fill="#ffffff")

    def pixel_to_coords(self, px, py):
        ax = px / CANVAS_WIDTH
        ay = py / CANVAS_HEIGHT

        ax = (ax * 3 - 2)*SCALE
        ay = (ay * 2 - 1)*SCALE
        return (ax, ay)

    def coords_to_pixel(self, cx, cy):
        cx = (cx/SCALE + 2) / 3
        cy = (cy/SCALE + 1) / 2

        return (cx * CANVAS_WIDTH, cy * CANVAS_HEIGHT)


    def render(self):
        print("help!")
        start_time = time.thread_time()
        for x in range(self.graph_area.winfo_width()):
            for y in range(self.graph_area.winfo_height()):
                self.draw_pixel(x=x, y=y)
        end_time = time.thread_time()
        print("Done in " + str(end_time - start_time) + " secs")
        self.draw_coords()



    def pixel_color(self, x, y):
        ax, ay = self.pixel_to_coords(x, y)

        rf, gf, bf = (0, 0, 0)
        c = complex(ax, ay)
        z = c
        for _i in range(self.iterations):
            if abs(z) > 2:
                rf, gf, bf = hsv_to_rgb((_i % 255 / 255) ** 0.5, 1.0, 1.0)
                break
            z = z ** 2 + c
            
        col = color_to_hex(color_clip(rf * 256),color_clip(gf * 256), color_clip(bf * 256))

        return col

#         c = complex(x, y)
# -        z = complex(0, 0)
# -        i = 0
# -        while i < self.iterations:
# -            if (z.imag ** 2 + z.real ** 2) < (2 ** 2):
# -                z = z ** 2 + c
# -                i += 1
# -            else:
# -                return False
# -        return True

    def draw_pixel(self, x, y): # draws pixels in reverse order
            self.graph_area.create_rectangle(x, self.graph_area.winfo_height() - y, x, self.graph_area.winfo_height() - y, outline=self.pixel_color(x, y), fill=self.pixel_color(x, y))

root = Tk()
app = Mandlebrot(root)
root.mainloop()
root.destroy()

# Cool! I should multi-thread this! If only I could use SIMD in python (is there a way??)
# I definitely need to do this in C++ next.

