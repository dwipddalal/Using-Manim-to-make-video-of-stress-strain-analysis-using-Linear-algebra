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
        kamsutra2 = unit_square.copy()
        self.play(ApplyMatrix(matrix, grid_og), ApplyMatrix(matrix, unit_square))
        self.wait(10)
        


class manim_mobject_matrix_2d(Scene):
    def construct(self):
        size = 0.5
        lines = VGroup(

            Tex("Kernel Matrix", color=BLUE),
            
            Matrix([("0", "1"),
                    ("1", "0")]),
            
            Matrix([("2", "1"),
                    ("1", "2")]),

            

            Tex("*", color=BLUE),
            Tex("=", color=BLUE),
            Tex(".", color=BLUE),
            Tex("(", color=BLUE),
            Tex(")", color=BLUE),
            Tex("+", color=BLUE),

            Matrix([("2", "-", "0"),
                    ("-45", "485", "-123"),
                    ("0", "-56", "0")]),

            Tex("241", color=BLUE)

        )


        op = VGroup(
            Tex("0"),
            Tex("-20"),
            Tex("0"),
            Tex("-45"),
            Tex("485"),
            Tex("-123"),
            Tex("0"),
            Tex("-56"),
            Tex("0")
        )

        t1_1 = lines[0]
        kernel_matrix = lines[1]
        image_matrix = lines[2]
        multi = lines[3]
        equal = lines[4]
        m_mul = lines[5]
        b_open = lines[6]
        b_close = lines[7]
        plus = lines[8]
        mm = lines[9]
        sum_oppp = lines[-1]
        t1_1.shift(UL * 3)

        kernel_matrix.shift(UP)
        self.play(Write(kernel_matrix))
        self.play(ApplyMethod(kernel_matrix.shift, LEFT*5))
        multi.next_to(kernel_matrix)
        image_matrix.next_to(multi)
        equal.next_to(image_matrix)
        self.play(Write(multi))
        self.play(Write(image_matrix))
        self.play(Write(equal))
        mm.next_to(equal)


        final_mat = VGroup(*mm)
        final_mat1 = VGroup(*final_mat[0])

        for i in final_mat[1:]:
            self.play(Write(i))

        kk = VGroup(*kernel_matrix)
        k1 = VGroup(*kk[0])
        ii = VGroup(*image_matrix)
        i1 = VGroup(*ii[0])

        runtime = 0.1
        flag = True

        for i, j, final_mm, o1 in zip(k1.copy(), i1.copy(), final_mat1.copy(), op):
            i2 = i.copy()
            j2 = j.copy()
            f2 = final_mm.copy()
            m_mul1 = m_mul.copy()
            b_o1 = b_open.copy()
            b_c1 = b_close.copy()
            eq1 = equal.copy()

            b_o1.shift(DOWN*2)
            b_o1.shift(LEFT * 3)
            i2.set_color(RED)
            self.play(Write(b_o1), )
            self.play(ApplyMethod(i2.next_to, b_o1), )

            m_mul1.next_to(i2)
            self.play(Write(m_mul1), )
            j2.set_color(RED)
            self.play(ApplyMethod(j2.next_to, m_mul1), )
            b_c1.next_to(j2)
            self.play(Write(b_c1), )
            eq1.next_to(b_c1)
            self.play(Write(eq1), )
            o1.next_to(eq1)
            self.play(Write(o1),)

            self.play(FadeOut(b_o1), FadeOut(i2), FadeOut(m_mul1), FadeOut(j2),
                      FadeOut(b_c1), FadeOut(eq1), Transform(o1, f2))

        self.play(FadeOut(equal), FadeOut(image_matrix), FadeOut(multi), FadeOut(kernel_matrix))
        summ = Tex("$\sum$", color=BLUE)
        summ.shift(UP)
        summ.shift(LEFT*3)

        self.play(Write(summ))
        self.play(FadeOut(op), ApplyMethod(mm.next_to, summ))

        ii = VGroup(*mm)
        m1 = VGroup(*ii[0])
        len_mm = len(m1)
        count = 0
        flag = True
        for i in m1.copy():
            count = count + 1
            i1 = i.copy()
            ss = sum_oppp.copy()
            if flag:
                p1 = plus.copy()
                i1.set_color(RED)
                self.play(ApplyMethod(i1.shift, DOWN*4), )
                self.play(ApplyMethod(i1.shift, LEFT * 5), )
                p1.next_to(i1)
                self.play(Write(p1), )
                flag = False
            else:
                p1 = p1.copy()
                i1.set_color(RED)
                self.play(ApplyMethod(i1.next_to, p1), )
                if count >= len_mm:
                    equal.next_to(i1)
                    self.play(Write(equal), )
                    ss.next_to(equal)
                    self.play(Write(ss), )
                    equal.set_color(YELLOW)
                    self.play(ApplyMethod(equal.next_to, mm), )
                    ss.set_color(YELLOW)
                    self.play(ApplyMethod(ss.next_to, equal), )

                else:
                    p1.next_to(i1)
                    self.play(Write(p1), )
        self.wait(2)
        self.clear()
        self.wait(2)
        
import numpy as np

class matrixTest(Scene):
	
	def construct(self):
		A = np.array([[0, 1], [1, 0]])
		B = np.array([[2, 1], [1, 2]])
		C = np.dot(A, B)
		
		stuff = VGroup(Matrix(A), Matrix(B), Matrix(C))
		matrixA = stuff[0]
		matrixB = stuff[1]
		matrixC = stuff[2]
		matrixA.height = 2.5
		matrixB.height = 2.5
		matrixA.color = PURPLE
		matrixB.color = RED
		Dot = Tex(".", color=WHITE, font_size = 200)
		Equals = Tex("=", color=WHITE, font_size = 100)
		bOpen = Tex("[", color=WHITE, font_size = 100)
		bClose = Tex("]", color=WHITE, font_size=100)
		bOpen1 = Tex("[", color=WHITE, font_size=200)
		bClose1 = Tex("]", color=WHITE, font_size=200)
		
		
		self.play(Write(matrixA))
		self.play(matrixA.animate.scale(1).to_corner(UP+LEFT*2))
		
		Dot.next_to(matrixA, RIGHT)
		self.play(Write(Dot))
		
		self.play(Write(matrixB))
		self.play(matrixB.animate.scale(1).next_to(Dot, RIGHT))
		
		Equals.next_to(matrixB, RIGHT)
		self.play(Write(Equals))
		
		matrixC.next_to(Equals)
		C_elements = VGroup(*matrixC)
		for i in C_elements[1:]:
			i.height = 2.5
			self.play(Write(i))
		C_elements = VGroup(*C_elements[0])
		A_rows = matrixA.get_rows()
		A = VGroup(A_rows[0], A_rows[0], A_rows[1], A_rows[1])
		B_columns = matrixB.get_columns()
		B = VGroup(B_columns[0], B_columns[1], B_columns[0], B_columns[1])
		
		for r, c, ans in zip(A.copy(), B.copy(), C_elements.copy()):
			_bOpen = bOpen.copy()
			_bClose = bClose.copy()
			_bOpen1 = bOpen1.copy()
			_bClose1 = bClose1.copy()
			_Dot = Dot.copy()
			_r = r.copy()
			_c = c.copy()
			_bOpen.next_to(matrixA, DOWN*3)
			self.play(Write(_bOpen))
			self.play(_r.set_color(BLUE).animate.next_to(_bOpen))
			_bClose.next_to(_r, RIGHT)
			self.play(Write(_bClose))
			_Dot.next_to(_bClose, RIGHT)
			self.play(Write(_Dot))
			_bOpen1.next_to(_Dot, RIGHT)
			self.play(Write(_bOpen1))
			self.play(_c.set_color(YELLOW).animate.next_to(_bOpen1))
			_bClose1.next_to(_c, RIGHT)
			self.play(Write(_bClose1))
			g = VGroup(_bOpen, _r, _bClose, _Dot, _bOpen1, _c, _bClose1)
			ans.font_size = 60
			ans.set_color(PURE_GREEN)
			self.play(Transform(g, ans))
			
		self.wait()
		# self.play(Write(Text("Code in the desciption", font_size=80)))
		self.wait()
		self.play(Write(Tex("Similarly, for the next two numbers...")))
		self.play(Write(Tex("$2$").shift(RIGHT*3.2+UP*1.75).scale(1.4).set_color(PURE_GREEN)), Write(Tex("$1$").shift(RIGHT*4.5+UP*1.75).scale(1.4).set_color(PURE_GREEN)))
		self.wait()

		



class manim_mobject_matrix_001a(Scene):
    def construct(self):
        size = 0.5
        lines = VGroup(

            Tex("Kernel Matrix", color=BLUE),
            Matrix([("\epsilon_{xx}", "\epsilon_{xy}", "\epsilon_{xz}"),
                    ("\epsilon_{yx}", "\epsilon_{yy}", "\epsilon_{yz}"),
                    ("\epsilon_{xx}", "\epsilon_{zy}", "\epsilon_{zz}")]),

            Matrix([("\sigma_{xx}", "\sigma_{xy}", "\sigma_{xz}"),
                        ("\sigma_{yx}", "\sigma_{yy}", "\sigma_{yz}"),
                        ("\sigma_{xx}", "\sigma_{zy}", "\sigma_{zz}")]),

            Tex("*", color=BLUE),
            Tex("=", color=BLUE),
            Tex(".", color=BLUE),
            Tex("(", color=BLUE),
            Tex(")", color=BLUE),
            Tex("+", color=BLUE),

            Matrix([("2", "-", "0"),
                    ("-45", "485", "-123"),
                    ("0", "-56", "0")]),

            Tex("241", color=BLUE)

        )


        op = VGroup(
            Tex("0"),
            Tex("-20"),
            Tex("0"),
            Tex("-45"),
            Tex("485"),
            Tex("-123"),
            Tex("0"),
            Tex("-56"),
            Tex("0")
        )

        t1_1 = lines[0]
        kernel_matrix = lines[1]
        image_matrix = lines[2]
        multi = lines[3]
        equal = lines[4]
        m_mul = lines[5]
        b_open = lines[6]
        b_close = lines[7]
        plus = lines[8]
        mm = lines[9]
        sum_oppp = lines[-1]
        t1_1.shift(UL * 3)

        kernel_matrix.shift(UP)
        image_matrix.shift(UP)

        
        self.play(Write(kernel_matrix))
        t_1 = Tex("This is the Strain Tensor", color=BLUE).next_to(kernel_matrix, DOWN)
        t_2 = Tex("This is the Stress Tensor", color=BLUE).next_to(kernel_matrix, DOWN)
        self.play(Write(t_1))
        self.wait(10)
        self.play(Transform(kernel_matrix, image_matrix))
        self.wait(3)
        self.play(Transform(t_1, t_2))
        self.wait(10)


class LineAndAngle(Scene):
    def construct(self):
        grid = NumberPlane()
        self.play(Create(grid))
        line = Line(RIGHT*4 + DOWN*3 + 2*UP + 2*RIGHT, RIGHT*1 + DOWN*2 + 2*UP + 2*RIGHT)
        line_x = Line(LEFT* 0, RIGHT *1)
        line = line.scale(5)
        unit_square = Rectangle(width=4.0, height=1.0, grid_xstep=4, grid_ystep=1, color=PURE_RED, fill_color=PURE_RED, fill_opacity=0.4).shift(UP * 0.5 + RIGHT * 2)
        line.set_color(RED)
        point = Dot(UP*1, color=RED).scale(2)
        arrow = Arrow(UP*1, LEFT*3 + UP*2)
        angle = Angle(line_x, line, quadrant=(1,1))
        text_theta = Tex("$\\theta$", color=RED).next_to(angle, RIGHT)

        arrow_2 = Arrow(UP*1, RIGHT*1 + UP*4).shift(LEFT*0.30 + DOWN*0.18)
        text_x1 = Tex("$V_{parallel}$", color=RED).next_to(arrow, LEFT).scale(0.8)
        text_x2 = Tex("$V_{normal}$", color=RED).next_to(arrow_2, RIGHT).scale(0.8)
        point.move_to(arrow.get_start())

        line.scale(5)
        self.play(Write(unit_square))
        self.wait(10)
        self.play(Write(line))
        self.play(Write(angle), Write(text_theta))
        self.play(Write(point))
        self.wait(10)
        self.play(GrowArrow(arrow))
        self.play(GrowArrow(arrow_2))
        self.play(Write(text_x1), Write(text_x2))
        self.wait(20)
        self.wait(2)
        self.wait(2)



