from manim import *

class Strain_Transformation(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors= True
        )

    def construct(self):
        matrix = [[5/4,0], [0, 1]]
        
        strain_formula = (
            MathTex(r"Strain = \frac{Increament (\Delta L)}{Original Length (L)}")
            .to_edge(UL)
            .add_background_rectangle()
        )

        matrix_tex = (
            MathTex("Transformation Vector = \\begin{bmatrix} 5 & 0 \\\ 0 & 1 \\end{bmatrix}")
            .to_edge(UL)
            .add_background_rectangle()
        )

        # unit_square = self.get_unit_square()
        unit_square = Rectangle(width=4.0, height=1.0, grid_xstep=4, grid_ystep=1, color=PURE_RED, fill_color=PURE_RED, fill_opacity=0.4).shift(UP * 0.5 + RIGHT * 2)
        # vect = self.get_vector([1, -2], color=PURPLE_B)
        
        # self.play(FadeIn(vect))
        
        self.wait(10)
        self.play(FadeIn(unit_square))
        self.wait(6)
        # unit_square.stretch(5/4, 0)
        arrow = Arrow(start=LEFT, end=RIGHT).next_to(unit_square, RIGHT)
        self.play(FadeIn(arrow))
        self.wait(6)
        kamsutra = unit_square.copy().stretch(5/4, 0)
        self.play(FadeIn(kamsutra.shift(RIGHT*0.5), run_time=2), FadeIn(arrow.shift(RIGHT), run_time=2))
        self.play(FadeOut(arrow))
        self.play(FadeIn(strain_formula))
        self.wait(10)
        
        self.play(FadeOut(strain_formula))
        self.wait()
        self.play(FadeOut(kamsutra))
        self.wait(5)
        #### traditional way of looking at strain.
        ### now let's take a more mathematical approach where strain would be modelled using a matrix. which will wrap and stretch the space.
        
        self.play(FadeIn(matrix_tex))
        self.wait(2)
        # self.play(FadeTransform(circ1, ellipse, strech = True))
        # self.add_transformable_mobject(vect, unit_square, rect1, circ1)
        # self.add_background_mobject(matrix_tex)
        # self.apply_matrix(matrix)
        # self.play(FadeTransform(circ1, circ1.copy().apply_matrix(matrix), stretch = True))
        kamsutra2 = unit_square.copy()
        self.play(ApplyMatrix(matrix, NumberPlane()), ApplyMatrix(matrix, kamsutra2))
        self.wait(10)
        