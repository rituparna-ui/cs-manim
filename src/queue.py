from manim import *


class RituQueue(VMobject):
    def __init__(self, size=5, **kwargs):
        super().__init__(**kwargs)
        self.size = size
        self.queue = []
        self.queue_objects = []

        self.quegram = (
            Polygram(
                [[0, 0, 0], [0, size / 2, 0]],
                [[1, 0, 0], [1, size / 2, 0]],
            )
            .set_stroke(RED)
            .set_z_index(1)
        ).move_to(ORIGIN)
        self.add(self.quegram)

    def enqueue(self, value):
        if len(self.queue) == self.size:
            rect = (
                Rectangle(height=0.5, width=1)
                .add(Text(str(value)).scale(0.5))
                .next_to(self.quegram, DOWN)
            )
            return (
                Write(rect),
                Blink(
                    rect,
                    time_off=0.1,
                    time_on=0.1,
                    hide_at_end=True,
                    blinks=10,
                ),
            )

        rect = (
            Rectangle(height=0.5, width=1)
            .add(Text(str(value)).scale(0.5))
            .next_to(self.quegram, DOWN)
        )
        self.queue.append(value)
        self.queue_objects.append(rect)

        rect_add_anim = (
            rect.animate.next_to(
                self.quegram,
                UP,
            ).align_to(
                self.quegram,
                UP,
            )
            if len(self.queue) == 1
            else rect.animate.next_to(
                self.queue_objects[-2],
                DOWN,
                buff=0,
            )
        )

        return (
            Write(rect),
            rect_add_anim,
        )

    def dequeue(self):
        if not self.queue:
            return None

        popped = self.queue_objects.pop(0)
        self.queue.pop(0)
        return {
            "anim": Succession(
                popped.animate.next_to(self.quegram, RIGHT)
                .align_to(self.quegram, DOWN)
                .set_stroke(RED),
                AnimationGroup(
                    *[
                        queue_object.animate.shift(UP * 0.5)
                        for queue_object in self.queue_objects
                    ],
                ),
                FadeOut(popped),
            ),
            "box": popped,
        }

    # (
    #     AnimationGroup(
    #         AnimationGroup(
    #             *[
    #                 queue_object.animate.shift(UP * 0.5)
    #                 for queue_object in self.queue_objects
    #             ],
    #         ),
    #         popped.animate.set_opacity(0),
    #         lag_ratio=1,
    #     ),
    # )
