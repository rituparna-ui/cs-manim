from manim import *
from src.queue import RituQueue


class RituScene(Scene):
    def construct(self):
        rq = RituQueue()
        self.play(Create(rq))

        for anim in rq.enqueue(5):
            self.play(anim)

        for anim in rq.enqueue(6):
            self.play(anim)

        for anim in rq.enqueue(2):
            self.play(anim)

        for anim in rq.enqueue(1):
            self.play(anim)

        for anim in rq.enqueue(3):
            self.play(anim)

        for anim in rq.enqueue(4):
            self.play(anim)

        self.play(rq.dequeue()["anim"])

        deq = rq.dequeue()
        self.play(deq["anim"])

        lastpop = deq["box"]
        lastpop.to_corner(UL)
        self.play(FadeIn(lastpop))

        # quegram = (
        #     Polygram(
        #         [[0, 0, 0], [0, 3, 0]],
        #         [[1, 0, 0], [1, 3, 0]],
        #     )
        #     .set_stroke(RED)
        #     .set_z_index(1)
        # ).move_to(ORIGIN)
        # self.add(quegram)

        # queue = []
        # rects = []
        # rect = (
        #     Rectangle(height=0.5, width=1)
        #     .add(Text("1").scale(0.5))
        #     .next_to(quegram, DOWN)
        # )
        # rects.append(rect)
        # queue.append(1)
        # self.play(Create(rect))

        # self.play(rect.animate.next_to(quegram, UP).align_to(quegram, UP))

        # queue.append(2)
        # rect = (
        #     Rectangle(height=0.5, width=1)
        #     .add(Text("2").scale(0.5))
        #     .next_to(quegram, DOWN)
        # )
        # rects.append(rect)
        # self.play(Create(rect))
        # self.play(rect.animate.next_to(rects[-2], DOWN, buff=0))

        # queue.append(3)
        # rect = (
        #     Rectangle(height=0.5, width=1)
        #     .add(Text("3").scale(0.5))
        #     .next_to(quegram, DOWN)
        # )
        # rects.append(rect)
        # self.play(Create(rect))
        # self.play(rect.animate.next_to(rects[-2], DOWN, buff=0))

        # queue.append(4)
        # rect = (
        #     Rectangle(height=0.5, width=1)
        #     .add(Text("4").scale(0.5))
        #     .next_to(quegram, DOWN)
        # )
        # rects.append(rect)
        # self.play(Create(rect))
        # self.play(rect.animate.next_to(rects[-2], DOWN, buff=0))

        # queue.append(5)
        # rect = (
        #     Rectangle(height=0.5, width=1)
        #     .add(Text("5").scale(0.5))
        #     .next_to(quegram, DOWN)
        # )
        # rects.append(rect)
        # self.play(Create(rect))
        # self.play(rect.animate.next_to(rects[-2], DOWN, buff=0))

        # # # popped = rects.pop(0)
        # # # self.play(
        # # #     popped.animate.next_to(quegram, RIGHT)
        # # #     .align_to(quegram, DOWN)
        # # #     .set_stroke(RED),
        # # #     run_time=2,
        # # # )
        # # # queue.pop(0)
        # # # self.play(*[rect.animate.shift(UP * 0.5) for rect in rects])

        # popped = rects.pop(0)
        # queue.pop(0)
        # self.play(
        #     *[rect.animate.shift(UP * 0.5) for rect in rects],
        #     popped.animate.next_to(quegram, RIGHT)
        #     .align_to(quegram, DOWN)
        #     .set_stroke(RED),
        # )

        # self.wait(2)


class ChangingRectangleSides(Scene):
    def construct(self):
        # 1. Create a Rectangle
        rect = Rectangle(
            width=4, height=3, fill_color=BLUE, fill_opacity=0.5, stroke_width=2
        ).rotate(PI / 2)
        self.add(rect)
        self.wait(1)

        # 2. Define Colors
        colors = {
            "top": RED,
            "bottom": GREEN,
            "left": YELLOW,
            "right": MAROON,
        }

        # 3. Get the Points
        points = rect.get_points()

        # 4. Modify the Points (Example: Change the top side to RED)
        top_side_points = [points[0], points[1]]  # Top side is between points 0 and 1

        # Create a new VMobject to represent the top side
        line = VMobject()
        line.set_points(top_side_points)
        line.set_color(colors["top"])
        self.play(rect.animate.add(line), run_time=2)  # Animate the change
        self.wait(1)

        # Repeat for other sides as needed.
