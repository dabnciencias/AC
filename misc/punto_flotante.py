from manim import * #Nota: Esta animación se programó usando Manim Community v0.17.2

NARANJA = '#FF7700'
VERDE = '#1FFF00'
AZUL = '#0087FF'
ROJO = '#FF0000'
AMARILLO = '#FFFF00'
MAGENTA = '#FF00FF'

class ClockwiseTransform(Transform):
    def __init__(
        self,
        mobject: Mobject,
        target_mobject: Mobject,
        path_arc: float = -np.pi,
        **kwargs,
    ) -> None:
        super().__init__(mobject, target_mobject, path_arc=path_arc, **kwargs)


class CounterclockwiseTransform(Transform):
    def __init__(
        self,
        mobject: Mobject,
        target_mobject: Mobject,
        path_arc: float = np.pi,
        **kwargs,
    ) -> None:
        super().__init__(mobject, target_mobject, path_arc=path_arc, **kwargs)

#Nota: las dos clases anteriores se basaron en las de https://github.com/animathica/alganim/blob/main/1/PEyBO_E4.py del mismo nombre, que fueron contribuidas por Juan Pablo Gamucero Arana.

class PuntoFlotante(Scene):
    def construct (self):
        expresión = VGroup(Tex("significando", color=AZUL),
                            MathTex("598"),
                            Tex("exponente", color=ROJO),
                            MathTex("-2"),
                            Tex("base", color=AMARILLO),
                            MathTex("10")).arrange(DOWN).scale(1.75)
        expresión[1].shift(0.25*UP)
        expresión[3].shift(0.25*UP)
        expresión[5].shift(0.25*UP)
        expresión.shift(4*LEFT)

        exp1 = MathTex("-2").scale(1.75).move_to(expresión[3].get_center())
        exp2 = MathTex("-1").scale(1.75).move_to(expresión[3].get_center())
        exp3 = MathTex("0").scale(1.75).move_to(expresión[3].get_center())
        exp4 = MathTex("-3").scale(1.75).move_to(expresión[3].get_center())

        flecha = MathTex("\\rightarrow").scale(1.75)

        número = VGroup(Tex("número", color=MAGENTA),
                         VGroup(MathTex("5"),
                                 MathTex("9"),
                                 MathTex("8")).arrange(RIGHT, buff=0.05)).arrange(DOWN).scale(1.75).shift(4*RIGHT)
        número[1][1:].shift(0.2*RIGHT)

        punto_flotante = VGroup(MathTex(".", color=NARANJA).scale(1.75),
                                MathTex("\\uparrow", color=NARANJA),
                                Tex("punto ``flotante''", color=NARANJA).scale(1.25)).arrange(DOWN)
        punto_flotante.shift(3.875*RIGHT+1.55*DOWN)

        self.add(expresión, flecha, número, punto_flotante)
        self.wait(0.75)

        self.play(Transform(expresión[3],exp2),
                  CounterclockwiseTransform(punto_flotante,punto_flotante.copy().shift(0.45*RIGHT)),
                  número[1][1].animate.shift(0.2*LEFT))
        self.wait(0.75)

        self.play(Transform(expresión[3],exp3),
                  CounterclockwiseTransform(punto_flotante,punto_flotante.copy().shift(0.45*RIGHT)),
                  número[1][2].animate.shift(0.2*LEFT))
        self.wait(0.75)

        self.play(Transform(expresión[3],exp2),
                  ClockwiseTransform(punto_flotante,punto_flotante.copy().shift(0.45*LEFT)),
                  número[1][2].animate.shift(0.2*RIGHT))
        self.wait(0.75)

        self.play(Transform(expresión[3],exp1),
                  ClockwiseTransform(punto_flotante,punto_flotante.copy().shift(0.45*LEFT)),
                  número[1][1].animate.shift(0.2*RIGHT))
        self.wait(0.75)

        self.play(Transform(expresión[3],exp4),
                  ClockwiseTransform(punto_flotante,punto_flotante.copy().shift(0.45*LEFT)),
                  número[1][0].animate.shift(0.2*RIGHT))
        self.wait(0.75)

        self.play(Transform(expresión[3],exp1),
                  CounterclockwiseTransform(punto_flotante,punto_flotante.copy().shift(0.45*RIGHT)),
                  número[1][0].animate.shift(0.2*LEFT))
