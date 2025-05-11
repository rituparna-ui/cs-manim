from manim import *


class RituStack(VMobject):
    def __init__(self, size=5, **kwargs):
        super().__init__(**kwargs)
        self.size = size
        self.stack = []
        self.stack_objects = VGroup()

    def push(self, value):
        self.stack.append(value),

        rect = (
            Rectangle(
                height=0.5,
                width=1,
            )
            .add(Text(str(value)).scale(0.5))
            .next_to(
                self.stackgram,
                UP,
                buff=0.5,
            )
        )
        self.stack_objects.add(rect),

        rect_animation = rect.animate.next_to(
            self.stack_objects[-1],
            DOWN,
        )

        if len(self.stack) == 1:
            rect_animation = rect.animate.align_to(
                self.stackgram,
                DOWN,
            )

        return Succession(
            Create(rect),
            rect_animation,
        )
