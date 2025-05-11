from manim import *
from src.stack import RituStack


class RituScene(Scene):
    def construct(self):
        size = 6
        stackgram = (
            Polygram(
                [[0, size * 0.5, 0], [0, 0, 0]],
                [[0, 0, 0], [1, 0, 0]],
                [[1, 0, 0], [1, size * 0.5, 0]],
            )
            .set_stroke(RED)
            .set_z_index(1)
        ).move_to(ORIGIN)
        self.add(stackgram)

        rects = []

        rects.append(
            Rectangle(
                width=1,
                height=0.5,
                fill_color=BLUE,
                fill_opacity=0.5,
                stroke_width=2,
                stroke_color=WHITE,
            )
            .add(Text("1").scale(0.5))
            .next_to(stackgram, UP)
        )

        self.play(Write(rects[0]))
        self.play(rects[0].animate.align_to(stackgram, DOWN))

        rects.append(
            Rectangle(
                width=1,
                height=0.5,
                fill_color=BLUE,
                fill_opacity=0.5,
                stroke_width=2,
                stroke_color=WHITE,
            )
            .add(Text("4").scale(0.5))
            .next_to(stackgram, UP)
        )

        self.play(Write(rects[-1]))
        self.play(
            rects[-1].animate.align_to(rects[-2], UP).next_to(rects[-2], UP, buff=0),
        )

        rects.append(
            Rectangle(
                width=1,
                height=0.5,
                fill_color=BLUE,
                fill_opacity=0.5,
                stroke_width=2,
                stroke_color=WHITE,
            )
            .add(Text("2").scale(0.5))
            .next_to(stackgram, UP)
        )

        self.play(Write(rects[-1]))
        self.play(
            rects[-1]
            .animate.align_to(
                rects[-2],
                UP,
            )
            .next_to(
                rects[-2],
                UP,
                buff=0,
            ),
        )

        rects.append(
            Rectangle(
                width=1,
                height=0.5,
                fill_color=BLUE,
                fill_opacity=0.5,
                stroke_width=2,
                stroke_color=WHITE,
            )
            .add(Text("2").scale(0.5))
            .next_to(stackgram, UP)
        )

        self.play(Write(rects[-1]))
        self.play(
            rects[-1]
            .animate.align_to(
                rects[-2],
                UP,
            )
            .next_to(
                rects[-2],
                UP,
                buff=0,
            ),
        )
