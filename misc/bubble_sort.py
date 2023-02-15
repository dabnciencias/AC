from manim import *
import numpy as np
from typing_extensions import runtime
from lib.rect_list import RectList
from lib.transform import SwapAligned


class RectListScene(Scene):
    def construct(self):
        self.rectlist = RectList(np.random.rand(55))
        self.play(Create(self.rectlist.get_rects()))
        self.wait()

        rect1 = self.rectlist.get_rect(0)
        rect2 = self.rectlist.get_rect(5)

        self.rectlist.swap(0, 5)
        self.play(SwapAligned(rect1, rect2, path_arc=0, aligned_edge=DOWN))
        self.wait()


class BubbleSort(Scene):
    def __init__(self, swap_time=0.1, size=20, **kwargs):
        super().__init__(**kwargs)
        self.swap_time = swap_time
        self.size = size

    def construct(self):
        title = Text("Bubble sort")
        title.move_to(2*UP)
        self.rectlist = RectList(np.random.rand(self.size))

        self.play(Write(title))
        self.play(Create(self.rectlist.get_rects()))
        self.wait()

        swapped = True
        while swapped:
            swapped = False
            for i in range(1, self.rectlist.size):
                if self.rectlist.get_value(i-1) > self.rectlist.get_value(i):
                    self.swap(i-1, i)
                    swapped = True

    def swap(self, i, j, animate=True):
        rect1 = self.rectlist.get_rect(i)
        rect2 = self.rectlist.get_rect(j)
        self.rectlist.swap(i, j)
        self.play(SwapAligned(rect1, rect2, path_arc=0,
                              aligned_edge=DOWN), runtime=self.swap_time)
