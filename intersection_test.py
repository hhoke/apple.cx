from manim import *

def make_apple():
        apple = Circle(color=GREEN, radius=1)
        apple.set_fill(GREEN, opacity=0.4)
        core_color = "#18453B"
        core = Square(color=BLACK, side_length=0.5).set_fill(core_color, opacity=1)
        return apple, core

class IntersectionScene(Scene,GetIntersections):
    def construct(self):
        title = Text(r"Cutting an Apple with a Square Core")
        self.play(
            Write(title),
        )
        self.play(title.animate.to_edge(DOWN))

        #asym
        apple, core = make_apple()

        core_top_right = core.get_critical_point(RIGHT+UP)
        core_bottom_right = core.get_critical_point(RIGHT+DOWN)
        core_bottom_left = core.get_critical_point(LEFT+DOWN)
        core_top_left = core.get_critical_point(LEFT+UP)

        first_cut = Line(core_top_right+UP, core_bottom_right+DOWN, color=BLACK)
        second_cut = Line(core_top_right, core_top_right+LEFT*2, color=BLACK)
        third_cut = Line(core_top_left, core_top_left+DOWN*2, color=BLACK)
        fourth_cut = Line(core_bottom_left, core_bottom_right, color=BLACK)

        first_label = Integer(1).scale(0.5)
        first_label.next_to(core.get_edge_center(RIGHT))
        second_label = Integer(2).scale(0.5)
        second_label.next_to(core.get_corner(UP+LEFT), UP)
        third_label = Integer(3).scale(0.5)
        third_label.next_to(core.get_corner(DOWN+LEFT), LEFT)
        fourth_label = Integer(4).scale(0.5)
        fourth_label.next_to(core.get_edge_center(DOWN), DOWN)

        self.add(apple)
        self.wait()

        self.play(Create(first_cut), run_time=1)
        self.add(first_label)
        self.wait()

        self.play(Create(second_cut), run_time=1)
        self.add(second_label)
        self.wait()

        self.play(Create(third_cut), run_time=1)
        self.add(third_label)
        self.wait()

        self.play(Create(fourth_cut), run_time=1)
        self.add(fourth_label)
        self.wait(0.25)
        self.add(core)

        self.wait()

        g = Group() 

        g.add(apple, core, first_label, first_cut, second_label, second_cut,
                third_label, third_cut, fourth_label, fourth_cut)

        self.play(ApplyMethod(g.shift, LEFT*3))

        self.wait()

        # may the good lord forgive me for this pasta
        # double gemini sym
        apple2, core2 = make_apple()

        core2_top_right = core2.get_critical_point(RIGHT+UP)
        core2_bottom_right = core2.get_critical_point(RIGHT+DOWN)
        core2_bottom_left = core2.get_critical_point(LEFT+DOWN)
        core2_top_left = core2.get_critical_point(LEFT+UP)

        first_cut2 = Line(core2_top_right+UP, core2_bottom_right+DOWN, color=BLACK)
        second_cut2 = Line(core2_top_left+UP, core2_bottom_left+DOWN, color=BLACK)
        third_cut2 = Line(core2_top_left, core2_top_right, color=BLACK)
        fourth_cut2 = Line(core2_bottom_left, core2_bottom_right, color=BLACK)

        first_label2 = Integer(1).scale(0.5)
        first_label2.next_to(core2.get_edge_center(RIGHT))
        second_label2 = Integer(2).scale(0.5)
        second_label2.next_to(core2.get_edge_center(LEFT), LEFT)
        third_label2 = Integer(3).scale(0.5)
        third_label2.next_to(core2.get_edge_center(UP), UP)
        fourth_label2 = Integer(4).scale(0.5)
        fourth_label2.next_to(core2.get_edge_center(DOWN), DOWN)

        self.add(apple2)
        self.wait()

        self.play(Create(first_cut2), run_time=1)
        self.add(first_label2)
        self.wait()

        self.play(Create(second_cut2), run_time=1)
        self.add(second_label2)
        self.wait()

        self.play(Create(third_cut2), run_time=1)
        self.add(third_label2)
        self.wait()

        self.play(Create(fourth_cut2), run_time=1)
        self.add(fourth_label2)
        self.wait(0.25)
        self.add(core2)

        self.wait()

        g = Group() 

        g.add(apple2, core2, first_label2, first_cut2, second_label2, second_cut2,
                third_label2, third_cut2, fourth_label2, fourth_cut2)

        self.play(ApplyMethod(g.shift, RIGHT*3))

        self.wait()

        # canine sym
        apple3, core3 = make_apple()

        core3_top_right = core3.get_critical_point(RIGHT+UP)
        core3_bottom_right = core3.get_critical_point(RIGHT+DOWN)
        core3_bottom_left = core3.get_critical_point(LEFT+DOWN)
        core3_top_left = core3.get_critical_point(LEFT+UP)

        first_cut3 = Line(core3_top_right+UP, core3_bottom_right+DOWN, color=BLACK)
        second_cut3 = Line(core3_top_right, core3_top_left+LEFT, color=BLACK)
        third_cut3 = Line(core3_bottom_right, core3_bottom_left+LEFT, color=BLACK)
        fourth_cut3 = Line(core3_bottom_left, core3_top_left, color=BLACK)

        first_label3 = Integer(1).scale(0.5)
        first_label3.next_to(core3.get_edge_center(RIGHT))
        second_label3 = Integer(2).scale(0.5)
        second_label3.next_to(core3.get_corner(UP+LEFT), UP)
        third_label3 = Integer(3).scale(0.5)
        third_label3.next_to(core3.get_corner(DOWN+LEFT), DOWN)
        fourth_label3 = Integer(4).scale(0.5)
        fourth_label3.next_to(core3.get_edge_center(LEFT), LEFT)

        self.add(apple3)
        self.wait()

        self.play(Create(first_cut3), run_time=1)
        self.add(first_label3)
        self.wait()

        self.play(Create(second_cut3), run_time=1)
        self.add(second_label3)
        self.wait()

        self.play(Create(third_cut3), run_time=1)
        self.add(third_label3)
        self.wait()

        self.play(Create(fourth_cut3), run_time=1)
        self.add(fourth_label3)
        self.wait(0.25)
        self.add(core3)

        self.wait()

        g = Group() 

        g.add(apple3, core3, first_label3, first_cut3, second_label3, second_cut3,
                third_label3, third_cut3, fourth_label3, fourth_cut3)


        self.wait()
