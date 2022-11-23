## here we can define what are linear transformations and how are they related with eigen-vectors
from re import L
from manim import *
import random


class Strain_Transformation(Scene):
    def construct(self):

        # # unit_square = self.get_unit_square()
        # unit_square = Rectangle(width=4.0, height=1.0, grid_xstep=4, grid_ystep=1, color=PURE_RED, fill_color=PURE_RED, fill_opacity=0.4).shift(UP * 0.5 + RIGHT * 2)
        # # vect = self.get_vector([1, -2], color=PURPLE_B)
        
        # # self.play(FadeIn(vect))
        
        # # self.wait(10)
        # self.play(FadeIn(unit_square))
        # self.wait(2)

        grid = NumberPlane()
        # grid_title = Tex("We shall apply some force on this box.", font_size=50)
        # grid_title.move_to(transform_title).shift(RIGHT*3)

        # self.add(grid, grid_title)  # Make sure title is on top of grid
        # self.play(
        #     FadeOut(title),
        #     FadeIn(grid_title, shift=UP),
        #     Create(grid, run_time=3, lag_ratio=0.1),
        # )
        # self.wait()

        # # self.wait(6)
        # # unit_square.stretch(5/4, 0))
        # arrow = Arrow(start=LEFT, end=RIGHT*1.25).next_to(unit_square, RIGHT).shift(RIGHT*(-0.25))
        # texForce = Tex("$F_0$").next_to(arrow, UP*0.7)
        # # self.wait(6)
        # unit_square_extended = unit_square.copy().stretch(5/4, 0)
        # self.play(GrowArrow(arrow), arrow.animate.shift(RIGHT*1), texForce.animate.shift(RIGHT*1), unit_square.animate.stretch(1.25, 0).move_to(RIGHT*2.5 + UP*0.5))
        # self.wait(2)
        # self.play(FadeOut(arrow), FadeOut(texForce))
        # self.wait()
        # self.play(FadeOut(grid_title))
        # self.play(Write(strain_formula))
        # self.wait(2)
        # line1 = Line(0, 4).set_color(ORANGE)
        # line2 = Line(4, 5).set_color(RED)
        # b1 = Brace(line1)
        # b2 = Brace(line2).shift(DOWN*4)
        # b1_tex = b1.get_text("$L_0$").set_color(ORANGE)
        # b2_tex = b2.get_text("$\Delta L$").set_color(RED)
        # self.play(GrowFromCenter(b1), GrowFromCenter(b2), Write(b1_tex), Write(b2_tex))
        # self.wait(3)
        # self.play(FadeOut(unit_square), FadeOut(grid), FadeOut(b1), FadeOut(b2), FadeOut(b1_tex), FadeOut(b2_tex))
        # self.wait()
        # strain_center = strain_formula.copy().move_to(0)
        # self.play(Transform(strain_formula, strain_center))
        # self.wait(3)
        # # self.wait(10)
        # title = Tex("This is the traditional way of looking at Strain.").scale(0.8).shift(UP*2)
        # self.play(Write(title))
        # self.play(FadeOut(strain_formula))
        # title_ = Tex("But there's a better way of doing it.")
        # self.play(Write(title_))
        # self.wait(3)
        # self.play(FadeOut(title), FadeOut(title_))


        # #### traditional way of looking at strain.
        # ### now let's take a more mathematical approach where strain would be modelled using a matrix. which will wrap and stretch the space.
        unit_square = Rectangle(width=5.0, height=2.0, grid_xstep=4, grid_ystep=1, color=PURE_RED, fill_color=PURE_RED, fill_opacity=0.4).shift(UP * 0.5 + RIGHT * 2)
        self.play(FadeIn(unit_square), Create(grid))
        # self.wait()
        # self.play(FadeIn(matrix_tex))
        # self.wait(2)
        # self.play(FadeTransform(circ1, ellipse, strech = True))
        # self.add_transformable_mobject(vect, unit_square, rect1, circ1)
        # self.add_background_mobject(matrix_tex)
        # self.apply_matrix(matrix)
        # self.play(FadeTransform(circ1, circ1.copy().apply_matrix(matrix), stretch = True))

        # grid_og = NumberPlane()
        # kamsutra2 = unit_square.copy()
        # self.play(ApplyMatrix(matrix, grid_og), ApplyMatrix(matrix, unit_square))
        # self.wait(10)
        


class change_of_Basis(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors= True
        )
        
    def construct(self):
        matrix = [[2, 1], [1, 2]] # transfomation matrix
        
        unit_square = Rectangle(width=5.0, height=2.0, grid_xstep=4, grid_ystep=1, color=PURE_RED, fill_color=PURE_RED, fill_opacity=0.4).shift(UP + RIGHT * 2.5)
        self.play(FadeIn(unit_square))
        
        rf_vector = [[3/5,2/5], [2/5,3/5]] # this is the refrence vector
        
        # matrix_tex = (
        #     MathTex("")
        #     .to_edge(UL)
        #     .add_background_rectangle()
        # )
        
        x_vect = self.get_vector([3, 2], color=GREEN)
        y_vect = self.get_vector([2, 3], color=RED)
        
        rotation_tex = (
            MathTex()
        )
        
        # matrix_tex = (
        #     MathTex("The \ \ transformation \ matrix \ be \ T = \\begin{bmatrix} 2 & 1 \\\ 1 & 2 \\end{bmatrix}")
        #     .to_edge(UL)
        #     .add_background_rectangle()
        # )
        matrix_tex_r = (
            MathTex("T = \\begin{bmatrix} 2 & 1 \\\ 1 & 2 \\end{bmatrix}")
            .to_edge(UL)
            .add_background_rectangle()
        )
        
        matrix_tex_right = (
            MathTex("Let \ the \ reference \ co-ordinate \ system \ be \ R = \\begin{bmatrix} 3 & 2 \\\ 2 & 3 \\end{bmatrix}")
            .to_edge(DR)
            .add_background_rectangle()
        )
        
        matrix_tex_right_r = (
            MathTex("R = \\begin{bmatrix} 3 & 2 \\\ 2 & 3 \\end{bmatrix}")
            .to_edge(DR)
            .add_background_rectangle()
        )
        
        # unit_square = self.get_unit_square()
        # vect = self.get_vector([1, -2], color=PURPLE_B)
        
        # self.play(FadeIn(vect))
        # self.play(FadeIn(unit_square))
        # self.play(FadeIn(matrix_tex))
        # self.wait(7)
        # self.play(FadeOut(matrix_tex))
        # self.play(FadeIn(matrix_tex_r))
        # self.play(FadeIn(matrix_tex_right))
        # self.wait(7)
        # self.play(FadeOut(matrix_tex_right))
        # self.wait(1)
        # self.play(FadeIn(matrix_tex_right_r))
        # self.wait(1)
        # self.wait(4)
        
        # self.play(FadeIn(x_vect))
        # self.wait(2)
        # self.play(FadeIn(y_vect))
        # self.wait(2)
        
        # ### Since now we want to see the transformation from the view of the reference frame
        # ### first let' assume that we are in the new refernce frame 
        # ### so inoder to traverse back to old refernce from new refernce frame we need to multiply with 
        # ## the inverse of the transformation matrix
        
        # # inverse_matrix = [[2, -1], [-1, 2]]
        
        # inverse_rf_vector = [[3/5, -2/5], [-2/5, 3/5]]
        
        # matrix_tex_r = (
        #     MathTex("T = \\begin{bmatrix} 2 & 1 \\\ 1 & 2 \\end{bmatrix}")
        #     .to_edge(UL)
        #     .add_background_rectangle()
        # )
        
        # matrix_tex_r_inverse = (
        #     MathTex("R^{-1} = \\begin{bmatrix} 3/5 & -2/5 \\\ -2/5 & 3/5 \\end{bmatrix}")
        #     .to_edge(UR)
        #     .add_background_rectangle()
        # )
        
        # self.play(FadeIn(matrix_tex_r_inverse))
        # self.wait(2)
        # x_vect_c = x_vect.copy()
        # y_vect_c = y_vect.copy()
        # N = NumberPlane()
        # self.play(ApplyMatrix(inverse_rf_vector, N ), ApplyMatrix(inverse_rf_vector, x_vect_c ), ApplyMatrix(inverse_rf_vector, y_vect_c))
        # self.wait(10)
        # # self.play(FadeOut(NumberPlane()))
        # self.wait(2)
        # self.play(ApplyMatrix(matrix, N), ApplyMatrix(inverse_rf_vector, x_vect_c), ApplyMatrix(inverse_rf_vector, x_vect_c))
        # self.wait(2)
        # self.play(ApplyMatrix(rf_vector, N), ApplyMatrix(rf_vector, x_vect_c), ApplyMatrix(rf_vector, x_vect_c))
        # self.wait(2)
        

class Interval_between_straina_and_linear_algebra(Scene):
    def construct(self):
        text = Tex("Writing this Mathematically:").scale(0.8).next_to(ORIGIN, UP)
        self.play(Write(text), run_time=3.0)
        self.wait(2)
        matrix_text = MathTex("R^{-1}TR = \\begin{bmatrix} 3/5 & -2/5 \\\ -2/5 & 3/5 \\end{bmatrix} \\begin{bmatrix} 2 & 1 \\\ 1 & 2 \\end{bmatrix} \\begin{bmatrix} 3 & 2 \\\ 2 & 3 \\end{bmatrix}").scale(0.8).next_to(text, DOWN)
        self.play(Write(matrix_text), run_time = 3.0)
        
class forumla(Scene):
    def construct(self):
        text_1 = MathTex(r"So \ for \ arbitary \ angle \ \theta \ rotation \  we \ have:").scale(0.8).next_to(ORIGIN, 10*UP)
        self.play(Write(text_1), run_time=3.0)
        self.wait(2)
        text = MathTex("S = R^{-1}TR").scale(1.2).next_to(text_1, DOWN)
        self.play(Write(text), run_time = 3.0)
        self.wait()
        text2 = MathTex(r"\left[\begin{array}{ll} S_{11}^{\prime} & S_{12}^{\prime} \\ S_{21}^{\prime} & S_{22}^{\prime} \end{array}\right]=\left[\begin{array}{cc} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{array}\right]\left[\begin{array}{ll} S_{11} & S_{12} \\ S_{21} & S_{22} \end{array}\right]\left[\begin{array}{cc} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{array}\right]").scale(0.8).next_to(text, DOWN)
        self.play(Write(text2), run_time=8.0)
        self.wait()
        text4 = Tex(" which on simplification gives:").scale(0.8).next_to(text2, DOWN)
        text3 = MathTex(r"\begin{aligned} &S_{11}^{\prime}=S_{11} \cos ^2 \theta+S_{22} \sin ^2 \theta+s_{12} \sin 2 \theta \\ &S_{22}^{\prime}=S_{11} \sin ^2 \theta+S_{22} \cos ^2 \theta+s_{12} \sin 2 \theta \\ &S_{12}^{\prime}=\left(S_{22}-S_{11}\right) \sin \theta \cos \theta+S_{12} \cos 2 \theta \end{aligned}").scale(0.8).next_to(text4, DOWN)
        self.play(Write(text3), run_time=8.0)
        self.wait(5)
        self.play(FadeOut(text_1))
        self.wait()
        self.play(FadeOut(text))
        self.wait()
        self.play(FadeOut(text2))
        self.wait(2)
        self.play(FadeOut(text4))
        self.wait()
        self.play(FadeOut(text3))
        self.wait(2)
        

class substitute_value_stress(Scene):
    def construct(self):
        text = Tex("On substituting the components of stress tensors we get").next_to(ORIGIN, 10*UP).scale(0.7)
        self.play(Write(text), run_time=3.0)
        self.wait()
        text2 = MathTex(r"\left\{\begin{aligned} \sigma_{x^{\prime}} &=\frac{\sigma_x+\sigma_y}{2}+\frac{\sigma_x-\sigma_y}{2} \cos 2 \theta+\tau_{x y} \sin 2 \theta \\ \sigma_{y^{\prime}} &=\frac{\sigma_x+\sigma_y}{2}-\frac{\sigma_x-\sigma_y}{2} \cos 2 \theta-\tau_{x y} \sin 2 \theta \\ &=\sigma_x+\sigma_y-\sigma_{x^{\prime}} \\ \tau_{x^{\prime} y^{\prime}} &=-\frac{\sigma_x-\sigma_y}{2} \sin 2 \theta+\tau_{x y} \cos 2 \theta \end{aligned}\right.")
        self.play(Write(text2), run_time=8.0)
        self.play(FadeOut(text))
        self.wait()
        self.play(FadeOut(text2))
        self.wait(2)
        

class substitute_value_strain(Scene):
    def construct(self):
        text = Tex("And similarly on substituting the components of strain tensors we get").next_to(ORIGIN, 10*UP).scale(0.7)
        self.play(Write(text), run_time=3.0)
        self.wait()
        text2 = MathTex(r"\begin{aligned} &\varepsilon_{x^{\prime}}=\frac{\varepsilon_x+\varepsilon_y}{2}+\frac{\varepsilon_x-\varepsilon_y}{2} \cos 2 \theta+\frac{\gamma_{x y}}{2} \sin 2 \theta \\ &\varepsilon_{y^{\prime}}=\frac{\varepsilon_x+\varepsilon_y}{2}-\frac{\varepsilon_x-\varepsilon_y}{2} \cos 2 \theta-\frac{\gamma_{x y}}{2} \sin 2 \theta \\ &\frac{\gamma_{x^{\prime} y^{\prime}}}{2}=-\left(\frac{\varepsilon_x-\varepsilon_y}{2}\right) \sin 2 \theta+\frac{\gamma_{x y}}{2} \cos 2 \theta \end{aligned}").next_to(text, DOWN)
        self.play(Write(text2), run_time=8.0)
        self.play(FadeOut(text))
        self.wait()
        self.play(FadeOut(text2))
        self.wait(2)
        
        
      
         
        