from manim import *

class Intro(Scene):
	def construct(self):

		text = Tex("From [Grothendieck],",
             "I have also learned not to take glory in the difficulty of a proof:",
             "difficulty means we have not understood.")
		text2 = Tex("The idea is to be able to paint a landscape in which the proof is obvious.") 
		text3 = Tex("-Pierre Deligne")

		text[0].set_color(RED)
		text[1].set_color(YELLOW)
		text[2].set_color(BLUE)
		text2.set_color(TEAL)
		text3.set_color(ORANGE)

		text.shift(2*UP)
		text3.next_to(text2,DOWN)
		# text4.next_to(text3,DOWN*2)
		# text5.next_to(text4,DOWN)
		text.scale(1.1)
		text2.scale(1.1)
		text3.scale(1)

		self.play(Write(text))
		self.wait(3)
		self.play(Write(text2))
		self.wait(4)
		self.play(Write(text3))
		self.wait(3)


class background(Scene):
    def construct(self):
        text = Tex("In this video we shall be answering two fundamental questions in Stress Strain Theory:").next_to(ORIGIN,UP)
        
        text2 = MarkupText(
            f'Why are <span underline="double" underline_color="green">principal components of stress</span> <span fgcolor="{YELLOW}">related with Eigenvectors? </span>',
            font_size=34
        ).next_to(text,DOWN)
        
        text3 = MarkupText(
            f"How does <span underline='double' underline_color='green'>transformations work</span> <span fgcolor='{YELLOW}'> and derive formula of Mohr's circle visually</span>?",
            font_size=34
        ).next_to(text2,DOWN)
        
        self.play(Write(text),run_time=3.0)
        self.wait(3)
        self.play(Write(text2),run_time=3.0)
        self.wait(4)
        self.play(Write(text3),run_time=3.0)
        self.wait(3)



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

        unit_square = self.get_unit_square()
        unit_square = Rectangle(width=4.0, height=1.0, grid_xstep=4, grid_ystep=1, color=PURE_RED, fill_color=PURE_RED, fill_opacity=0.4).shift(UP * 0.5 + RIGHT * 2)
        # vect = self.get_vector([1, -2], color=PURPLE_B)
        
        # self.play(FadeIn(vect))
        
        Matrix([("\sigma_{xx}", "\sigma_{xy}", "\sigma_{xz}"),
                ("\sigma_{yx}", "\sigma_{yy}", "\sigma_{yz}"),
                ("\sigma_{xx}", "\sigma_{zy}", "\sigma_{zz}")]),
        self.wait(10)
        self.play(FadeIn(unit_square))
        self.wait(6)
        # unit_square.stretch(5/4, 0)
        arrow = Arrow(start=LEFT, end=RIGHT).next_to(unit_square, RIGHT)
        self.play(FadeIn(arrow))
        self.wait(6)
        kat = unit_square.copy().stretch(5/4, 0)
        self.play(FadeIn(kat.shift(RIGHT*0.5), run_time=2), FadeIn(arrow.shift(RIGHT), run_time=2))
        self.play(FadeOut(arrow))
        self.play(FadeIn(strain_formula))
        self.wait(10)
        
        self.play(FadeOut(strain_formula))
        self.wait()
        self.play(FadeOut(kat))
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
        kat2 = unit_square.copy()
        self.play(ApplyMatrix(matrix, NumberPlane()), ApplyMatrix(matrix, kat2))
        self.wait(10)



class Strain_Transformation(Scene):
    # def __init__(self):
    #     LinearTransformationScene.__init__(
    #         self,
    #         show_coordinates=False,
    #         leave_ghost_vectors=True,
    #         show_basis_vectors= False
    #     )

    def construct(self):
        matrix = [[5/4,0], [0, 1]]

        title = Tex(r"Transformation of Strain").scale(1.5)
        subtitle = Tex(r"Let us see how transformation of strain works").scale(0.8)
        VGroup(title, subtitle).arrange(DOWN*0.5)

        self.play(
            Write(title),
        )
        self.wait()
        self.play(
            FadeIn(subtitle, shift = DOWN*0.5)
        )
        self.wait()
        self.play(
            FadeOut(subtitle)
        )
        transform_title = Tex("Consider a box.")
        transform_title.to_corner(UP+LEFT)
        self.play(
            Transform(title, transform_title),
        )
        self.wait()
        strain_formula = (
            MathTex(r"Strain = \frac{\textrm{Increment} (\Delta L)}{\textrm{Original Length} (L)}")
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
        
        # self.wait(10)
        self.play(FadeIn(unit_square))
        self.wait(2)

        grid = NumberPlane()
        grid_title = Tex("We shall apply some force on this box.", font_size=50)
        grid_title.move_to(transform_title).shift(RIGHT*3)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeIn(grid_title, shift=UP),
            Create(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        # self.wait(6)
        # unit_square.stretch(5/4, 0))
        arrow = Arrow(start=LEFT, end=RIGHT*1.25).next_to(unit_square, RIGHT).shift(RIGHT*(-0.25))
        texForce = Tex("$F_0$").next_to(arrow, UP*0.7)
        # self.wait(6)
        unit_square_extended = unit_square.copy().stretch(5/4, 0)
        self.play(GrowArrow(arrow), arrow.animate.shift(RIGHT*1), texForce.animate.shift(RIGHT*1), unit_square.animate.stretch(1.25, 0).move_to(RIGHT*2.5 + UP*0.5))
        self.wait(2)
        self.play(FadeOut(arrow), FadeOut(texForce))
        self.wait()
        self.play(FadeOut(grid_title))
        self.play(Write(strain_formula))
        self.wait(2)
        line1 = Line(0, 4).set_color(ORANGE)
        line2 = Line(4, 5).set_color(RED)
        b1 = Brace(line1)
        b2 = Brace(line2).shift(DOWN*4)
        b1_tex = b1.get_text("$L_0$").set_color(ORANGE)
        b2_tex = b2.get_text("$\Delta L$").set_color(RED)
        self.play(GrowFromCenter(b1), GrowFromCenter(b2), Write(b1_tex), Write(b2_tex))
        self.wait(3)
        self.play(FadeOut(unit_square), FadeOut(grid), FadeOut(b1), FadeOut(b2), FadeOut(b1_tex), FadeOut(b2_tex))
        self.wait()
        strain_center = strain_formula.copy().move_to(0)
        self.play(Transform(strain_formula, strain_center))
        self.wait(3)
        # self.wait(10)
        title = Tex("This is the traditional way of looking at Strain.").scale(0.8).shift(UP*2)
        self.play(Write(title))
        self.play(FadeOut(strain_formula))
        title_ = Tex("But there's a better way of doing it.")
        self.play(Write(title_))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(title_))


        #### traditional way of looking at strain.
        ### now let's take a more mathematical approach where strain would be modelled using a matrix. which will wrap and stretch the space.
        unit_square = Rectangle(width=4.0, height=1.0, grid_xstep=4, grid_ystep=1, color=PURE_RED, fill_color=PURE_RED, fill_opacity=0.4).shift(UP * 0.5 + RIGHT * 2)
        self.play(FadeIn(unit_square), Create(grid))
        self.wait()
        self.play(FadeIn(matrix_tex))
        self.wait(2)
        # self.play(FadeTransform(circ1, ellipse, strech = True))
        # self.add_transformable_mobject(vect, unit_square, rect1, circ1)
        # self.add_background_mobject(matrix_tex)
        # self.apply_matrix(matrix)
        # self.play(FadeTransform(circ1, circ1.copy().apply_matrix(matrix), stretch = True))

        grid_og = NumberPlane()
        kat2 = unit_square.copy()
        self.play(ApplyMatrix(matrix, grid_og), ApplyMatrix(matrix, unit_square))
        self.wait(10)

class Matrix(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors=True,
        )

    def construct(self):

        matrix = [[2, 1], [1, 2]]
        matrix_tex = (
            MathTex("A = \\begin{bmatrix} 2 & 1 \\\ 1 & 2 \\end{bmatrix}")
            .to_edge(UL)
            .add_background_rectangle()
        )

        unit_square = self.get_unit_square()
        # text = always_redraw(
        #     lambda: Tex("Det(A)").set(width=0.7).move_to(unit_square.get_center())
        # )

        vect = self.get_vector([1, -2], color=PURPLE_B)

        rect1 = Rectangle(
            height=2, width=1, stroke_color=BLUE_A, fill_color=BLUE_D, fill_opacity=0.6
        ).shift(UP * 2 + LEFT * 2)

        circ1 = Circle(
            radius=1, stroke_color=BLUE_A, fill_color=BLUE_D, fill_opacity=0.6
        ).shift(DOWN * 2 + RIGHT * 1)
        
        self.wait()
        self.play(FadeIn(circ1))
        self.wait(2)
        self.play(FadeIn(rect1))
        self.wait(2)
        self.play(FadeIn(vect))
        self.wait(2)
        self.play(FadeIn(unit_square))
        self.wait(2)
        self.play(FadeIn(matrix_tex))
        self.wait(10)
        # self.play(FadeTransform(circ1, ellipse, strech = True))
        # self.add_transformable_mobject(vect, unit_square, rect1, circ1)
        # self.add_background_mobject(matrix_tex)
        # self.apply_matrix(matrix)
        # self.play(FadeTransform(circ1, circ1.copy().apply_matrix(matrix), stretch = True))
        self.play(ApplyMatrix(matrix, circ1), ApplyMatrix(matrix, NumberPlane()), ApplyMatrix(matrix,rect1), ApplyMatrix(matrix,vect), ApplyMatrix(matrix, unit_square))
        self.wait(10)

        