## here we can define what are linear transformations and how are they related with eigen-vectors
from re import L
from manim import *
import random

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

class LinearTransformation_Transpose(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors= True
        )

    def construct(self):
        matrix = [[0, 1], [1, 0]]

        matrix_tex = (
            MathTex("A = \\begin{bmatrix} 0 & 1 \\\ 1 & 0 \\end{bmatrix}")
            .to_edge(UL)
            .add_background_rectangle()
        )

        unit_square = self.get_unit_square()

        vect = self.get_vector([1, -2], color=PURPLE_B)
        
        self.play(FadeIn(vect))
        self.wait()
        self.play(FadeIn(unit_square))
        self.wait()
        self.play(FadeIn(matrix_tex))
        self.wait(4)
        self.play(ApplyMatrix(matrix, NumberPlane()), ApplyMatrix(matrix,vect), ApplyMatrix(matrix, unit_square))
        self.wait(5)


### then we chall define change of basis vectors

class effect_on_matrix_multiplication(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors= True
        )

    def construct(self):
        
        matrix = [[0, 1], [1, 0]]
        matrix_tex = (
            MathTex("A = \\begin{bmatrix} 0 & 1 \\\ 1 & 0 \\end{bmatrix}")
            .to_edge(UL)
            .add_background_rectangle()
        )
        unit_square = self.get_unit_square()
        vect = self.get_vector([1, -2], color=PURPLE_B)
        
        self.play(FadeIn(vect))
        self.play(FadeIn(unit_square))
        self.play(FadeIn(matrix_tex))
        self.wait(4)
        self.play(ApplyMatrix(matrix, NumberPlane()), ApplyMatrix(matrix,vect), ApplyMatrix(matrix, unit_square))
        self.wait(1)
        
        matrix2 = [[2, 1], [1, 2]]
        self.play(FadeOut(matrix_tex))
        self.wait(1)
        unit_square = self.get_unit_square()
        matrix_tex2 = (
            MathTex("B = \\begin{bmatrix} 2 & 1 \\\ 1 & 2 \\end{bmatrix}")
            .to_edge(UL)
            .add_background_rectangle()
        )
        vect2 = self.get_vector([-2, 1], color=PURPLE_B)
        
        self.play(FadeIn(matrix_tex2))
        self.wait(4)
        self.play(ApplyMatrix(matrix2, NumberPlane()), ApplyMatrix(matrix2,vect2), ApplyMatrix(matrix2, unit_square))
        self.wait(5)
        self.play(FadeOut(matrix_tex2))
        
        vect = self.get_vector([1, -2], color=PURE_GREEN)
        self.play(FadeIn(vect))
        final_vect = self.get_vector([-3, 0], color=PURE_RED)
        self.play(FadeIn(final_vect))
        self.wait(5)
        
        ### now let's multiply two matrix
        
        ## code to multiply matrix here...
        
        ### let's seee what happend when we perform transformation using the matrix that we got on multiplication
        
class effect_on_matrix_multiplication_part3(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors= True
        )

    def construct(self):       
        matrix2 = [[1, 2], [2, 1]]

        unit_square = self.get_unit_square()

        matrix_tex2 = (
            MathTex("B = \\begin{bmatrix} 1 & 2 \\\ 2 & 1 \\end{bmatrix}")
            .to_edge(UL)
            .add_background_rectangle()
        )
        vect2 = self.get_vector([1, -2], color=PURPLE_B)
        self.play(FadeIn(matrix_tex2))
        self.play(ApplyMatrix(matrix2, NumberPlane()), ApplyMatrix(matrix2,vect2), ApplyMatrix(matrix2, unit_square))
        self.wait(2)
        # vect = self.get_vector([1, -2], color=PURE_GREEN)
        # self.play(FadeIn(vect))
        final_vect = self.get_vector([-3, 0], color=PURE_RED)
        self.play(FadeIn(final_vect))
        self.wait(7)
        

        
        
        
    
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
        
        ### and now I want to find out what will be the effect of this transformation martrix if
        ### viewed form some other frame of reference
        
        rf_vector = [[3/5,2/5], [2/5,3/5]] # this is the refrence vector
        
        # matrix_tex = (
        #     MathTex("")
        #     .to_edge(UL)
        #     .add_background_rectangle()
        # )
        
        x_vect = self.get_vector([3, 2], color=GREEN)
        y_vect = self.get_vector([2, 3], color=RED)
        
        matrix_tex = (
            MathTex("Let \ the \ transformation \ matrix \ be \ T = \\begin{bmatrix} 2 & 1 \\\ 1 & 2 \\end{bmatrix}")
            .to_edge(UL)
            .add_background_rectangle()
        )
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
        self.play(Write(matrix_tex), running_time=3)
        self.wait(7)
        self.play(FadeOut(matrix_tex))
        self.play(Write(matrix_tex_r), running_time=3)
        self.play(Write(matrix_tex_right), running_time=3)
        self.wait(7)
        self.play(FadeOut(matrix_tex_right))
        self.wait(1)
        self.play(Write(matrix_tex_right_r), running_time=3)
        self.wait(1)
        self.wait(4)
        
        self.play(FadeIn(x_vect))
        self.wait(2)
        self.play(FadeIn(y_vect))
        self.wait(6)
        
        ### Since now we want to see the transformation from the view of the reference frame
        ### first let' assume that we are in the new refernce frame 
        ### so inoder to traverse back to old refernce from new refernce frame we need to multiply with 
        ## the inverse of the transformation matrix
        
        # inverse_matrix = [[2, -1], [-1, 2]]
        
        inverse_rf_vector = [[3/5, -2/5], [-2/5, 3/5]]
        
        matrix_tex_r = (
            MathTex("T = \\begin{bmatrix} 2 & 1 \\\ 1 & 2 \\end{bmatrix}")
            .to_edge(UL)
            .add_background_rectangle()
        )
        
        matrix_tex_r_inverse = (
            MathTex("R^{-1} = \\begin{bmatrix} 3/5 & -2/5 \\\ -2/5 & 3/5 \\end{bmatrix}")
            .to_edge(UR)
            .add_background_rectangle()
        )
        
        self.play(FadeIn(matrix_tex_r_inverse))
        self.wait(10)
        x_vect_c = x_vect.copy()
        y_vect_c = y_vect.copy()
        N = NumberPlane()
        self.play(ApplyMatrix(inverse_rf_vector, N ), ApplyMatrix(inverse_rf_vector, x_vect_c ), ApplyMatrix(inverse_rf_vector, y_vect_c))
        self.wait(10)
        # self.play(FadeOut(NumberPlane()))
        self.wait(2)
        self.play(ApplyMatrix(matrix, N), ApplyMatrix(inverse_rf_vector, x_vect_c), ApplyMatrix(inverse_rf_vector, x_vect_c))
        self.wait(3)
        self.play(ApplyMatrix(rf_vector, N), ApplyMatrix(rf_vector, x_vect_c), ApplyMatrix(rf_vector, x_vect_c))
        self.wait(2)
        

class Interval_between_straina_and_linear_algebra(Scene):
    def construct(self):
        text = Tex("Writing this Mathematically:").scale(0.8).next_to(ORIGIN, UP)
        self.play(Write(text), run_time=3.0)
        self.wait(2)
        matrix_text = MathTex("R^{-1}TR = \\begin{bmatrix} 3/5 & -2/5 \\\ -2/5 & 3/5 \\end{bmatrix} \\begin{bmatrix} 2 & 1 \\\ 1 & 2 \\end{bmatrix} \\begin{bmatrix} 3 & 2 \\\ 2 & 3 \\end{bmatrix}").scale(0.8).next_to(text, DOWN)
        self.play(Write(matrix_text), run_time = 3.0)
        
        


        
        
      
         
        