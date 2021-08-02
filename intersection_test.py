from manim import *
import numpy as np


def Range(in_val,end_val,step=1):
    return list(np.arange(in_val,end_val+step,step))

class GetIntersections:
    """
    update of woElteoremadebeethoven's work.
    """
    def get_coord_from_proportion(self,vmob,proportion):
        return vmob.point_from_proportion(proportion)

    def get_points_from_curve(self, vmob, dx=0.005):
        coords = []
        for point in Range(0, 1, dx):
            dot = Dot(self.get_coord_from_proportion(vmob,point))
            coords.append(dot.get_center())
        return coords

    def get_intersections_between_two_vmobs(self, vmob1, vmob2,
                                            tolerance=0.05,
                                            radius_error=0.2,
                                            use_average=True,
                                            use_first_vmob_reference=False):
        coords_1 = self.get_points_from_curve(vmob1)
        coords_2 = self.get_points_from_curve(vmob2)
        intersections = []
        for coord_1 in coords_1:
            for coord_2 in coords_2:
                distance_between_points = np.linalg.norm(coord_1 - coord_2)
                if use_average:
                    coord_3 = (coord_2 - coord_1) / 2
                    average_point = coord_1 + coord_3
                else:
                    if use_first_vmob_reference:
                        average_point = coord_1
                    else:
                        average_point = coord_2
                if len(intersections) > 0 and distance_between_points < tolerance:
                    last_intersection=intersections[-1]
                    distance_between_previus_point = np.linalg.norm(average_point - last_intersection)
                    if distance_between_previus_point > radius_error:
                        intersections.append(average_point)
                if len(intersections) == 0 and distance_between_points < tolerance:
                    intersections.append(average_point)
        return intersections

# do I really need to use this?
def snap_to(mobject_one,direction_one,mobject_two,direction_two):
    if isinstance(mobject_one, Mobject):
        point = mobject_one.get_critical_point(direction_one)
    else:
        point = mobject_one

    if isinstance(mobject_two, Mobject):
        point = mobject_two.get_critical_point(direction_two)
    else:
        point = mobject_two

    for dim in range(mobject_one.dim):
        if direction[dim] != 0:
            mobject_one.set_coord(point[dim], dim, direction)
    return self

class IntersectionScene(Scene,GetIntersections):
    def construct(self):
        title = Text(r"Cutting an Apple with a Square Core")
        self.play(
            Write(title),
        )
        self.play(title.animate.to_edge(DOWN))

        apple = Circle(color=GREEN,radius=1)
        apple.set_fill(GREEN, opacity=0.4)
        core_color = "#18453B"
        square = Square(color=core_color,side_length=0.5).set_fill(core_color, opacity=1)
        vert_rect= Rectangle(color=BLACK,height=2,width=1)
        square_right_center = square.get_critical_point(RIGHT)
        vert_rect.align_to(square_right_center,LEFT)

        first_label = Integer(1).scale(0.25)
        first_label.next_to(square.get_corner(UP+RIGHT))
        first_cut = Line()

        intersections = self.get_intersections_between_two_vmobs(apple, vert_rect)
        for point in intersections:
            self.add(Dot(radius=0.05, color=YELLOW).move_to(point))

        self.add(apple, square, vert_rect, first_label)
        self.play(Create(square))
        self.wait()
