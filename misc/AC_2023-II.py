from manim import *

NARANJA = '#FF7700'
VERDE = '#1FFF00'
AZUL = '#0087FF'
ROJO = '#FF0000'

class Curso(Scene):
    def construct (self):
        curso = Tex("AC", color = NARANJA).scale(5).move_to(UP)
        curso[0][1].set_color(VERDE)
        semestre = Tex("2023-II").scale(5).move_to(DOWN)
        semestre[0][0:4].set_color(AZUL)
        semestre[0][5:7].set_color(ROJO)
        self.play(Write(curso), run_time=2)
        self.play(Write(semestre), run_time=2)
        self.wait()
        self.play(FadeOut(curso, semestre))
