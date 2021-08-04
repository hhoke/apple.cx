from manim import *

class Apple():
    def __init__(self, scene):
        self.scene = scene
        self.apple = Circle(color=GREEN, radius=1)
        self.apple.set_fill(GREEN, opacity=0.4)
        core_color = "#18453B"
        self.core = Square(color=BLACK, side_length=0.5).set_fill(core_color, opacity=1)
        self.g = Group().add(self.apple, self.core)
        self.cuts = []
        self.labels = []
        
    def create_apple(self):
        self.scene.add(self.apple)
        self.scene.wait()

        for cut, label in zip(self.cuts[:-1],self.labels[:-1]):
            self.scene.play(Create(cut), run_time=1)
            self.scene.add(label)
            self.scene.wait()

        self.scene.play(Create(self.cuts[-1]), FadeIn(self.core), run_time=1)
        self.scene.add(self.labels[-1])

        self.scene.wait()

class AsymApple(Apple):
    def __init__(self, scene):
        super().__init__(scene)
        self.define_cuts()
        self.define_and_place_labels()

    def define_cuts(self):
        self.cuts.append(Line(self.core.get_corner(RIGHT+DOWN)+DOWN,
            self.core.get_corner(RIGHT+UP)+UP, color=BLACK))
        self.cuts.append(Line(self.core.get_corner(RIGHT+UP),
            self.core.get_corner(LEFT+UP)+LEFT, color=BLACK))
        self.cuts.append(Line(self.core.get_corner(LEFT+UP),
            self.core.get_corner(LEFT+DOWN)+DOWN, color=BLACK))
        self.cuts.append(Line(self.core.get_corner(LEFT+DOWN),
            self.core.get_corner(RIGHT+DOWN), color=BLACK))

        self.g.add(*self.cuts)

    def define_and_place_labels(self):
        self.labels.append(Integer(1).scale(0.5))
        self.labels[0].next_to(self.core.get_edge_center(RIGHT))
        self.labels.append(Integer(2).scale(0.5))
        self.labels[1].next_to(self.core.get_corner(UP+LEFT), UP)
        self.labels.append(Integer(3).scale(0.5))
        self.labels[2].next_to(self.core.get_corner(DOWN+LEFT), LEFT)
        self.labels.append(Integer(4).scale(0.5))
        self.labels[3].next_to(self.core.get_edge_center(DOWN), DOWN)

        self.g.add(*self.labels)

class DoubleGeminiApple(Apple):
    def __init__(self, scene):
        super().__init__(scene)
        self.define_cuts()
        self.define_and_place_labels()

    def define_cuts(self):
        self.cuts.append(Line(self.core.get_corner(RIGHT+DOWN)+DOWN,
            self.core.get_corner(RIGHT+UP)+UP, color=BLACK))
        self.cuts.append(Line(self.core.get_corner(LEFT+UP)+UP,
            self.core.get_corner(LEFT+DOWN)+DOWN, color=BLACK))
        self.cuts.append(Line(self.core.get_corner(RIGHT+UP),
            self.core.get_corner(LEFT+UP), color=BLACK))
        self.cuts.append(Line(self.core.get_corner(LEFT+DOWN),
            self.core.get_corner(RIGHT+DOWN), color=BLACK))

        self.g.add(*self.cuts)

    def define_and_place_labels(self):
        self.labels.append(Integer(1).scale(0.5))
        self.labels[0].next_to(self.core.get_edge_center(RIGHT))
        self.labels.append(Integer(2).scale(0.5))
        self.labels[1].next_to(self.core.get_corner(LEFT), LEFT)
        self.labels.append(Integer(3).scale(0.5))
        self.labels[2].next_to(self.core.get_corner(UP), UP)
        self.labels.append(Integer(4).scale(0.5))
        self.labels[3].next_to(self.core.get_edge_center(DOWN), DOWN)

        self.g.add(*self.labels)

class CanineApple(Apple):
    def __init__(self, scene):
        super().__init__(scene)
        self.define_cuts()
        self.define_and_place_labels()

    def define_cuts(self):
        self.cuts.append(Line(self.core.get_corner(RIGHT+DOWN)+DOWN,
            self.core.get_corner(RIGHT+UP)+UP, color=BLACK))
        self.cuts.append(Line(self.core.get_corner(RIGHT+UP),
            self.core.get_corner(LEFT+UP)+LEFT, color=BLACK))
        self.cuts.append(Line(self.core.get_corner(RIGHT+DOWN),
            self.core.get_corner(LEFT+DOWN)+LEFT, color=BLACK))
        self.cuts.append(Line(self.core.get_corner(LEFT+UP),
            self.core.get_corner(LEFT+DOWN), color=BLACK))

        self.g.add(*self.cuts)

    def define_and_place_labels(self):
        self.labels.append(Integer(1).scale(0.5))
        self.labels[0].next_to(self.core.get_edge_center(RIGHT))
        self.labels.append(Integer(2).scale(0.5))
        self.labels[1].next_to(self.core.get_corner(UP+LEFT), UP)
        self.labels.append(Integer(3).scale(0.5))
        self.labels[2].next_to(self.core.get_corner(DOWN+LEFT), DOWN)
        self.labels.append(Integer(4).scale(0.5))
        self.labels[3].next_to(self.core.get_edge_center(LEFT), LEFT)

        self.g.add(*self.labels)

class AppleCuts(Scene):
    def construct(self):
        title = Text(r"Cutting an Apple with a Square Core")
        self.play(
            Write(title),
        )
        self.play(title.animate.to_edge(DOWN))

        #asym
        asym_apple = AsymApple(self)
        asym_apple.create_apple()
        self.play(ApplyMethod(asym_apple.g.shift, LEFT*3))

        self.wait()

        # double gemini sym
        double_gemini_apple = DoubleGeminiApple(self)
        double_gemini_apple.create_apple()
        self.play(ApplyMethod(double_gemini_apple.g.shift, RIGHT*3))
        self.wait()

        # canine sym
        canine_sym_apple = CanineApple(self)
        canine_sym_apple.create_apple()
        self.wait()
