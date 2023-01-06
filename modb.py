from manim import *

VECTOR_LABEL_SCALE_FACTOR = 1
FRAME_X_RADIUS = 1
FRAME_Y_RADIUS = 1
FRAME_WIDTH  =1 
FRAME_HEIGHT = 1
X_COLOR = RED
Y_COLOR = RED

# class Intro(Scene):
# 	def construct(self):

# 		text = Tex("From [Grothendieck],",
#              "I have also learned not to take glory in the difficulty of a proof:",
#              "difficulty means we have not understood.")
# 		text2 = Tex("The idea is to be able to paint a landscape in which the proof is obvious.") 
# 		text3 = Tex("-Pierre Deligne")

# 		text[0].set_color(RED)
# 		text[1].set_color(YELLOW)
# 		text[2].set_color(BLUE)
# 		text2.set_color(TEAL)
# 		text3.set_color(ORANGE)

# 		text.shift(2*UP)
# 		text3.next_to(text2,DOWN)
# 		# text4.next_to(text3,DOWN*2)
# 		# text5.next_to(text4,DOWN)
# 		text.scale(1.1)
# 		text2.scale(1.1)
# 		text3.scale(1)

# 		self.play(Write(text))
# 		self.wait(3)
# 		self.play(Write(text2))
# 		self.wait(4)
# 		self.play(Write(text3))
# 		self.wait(3)




# class MatrixExamples(Scene):
#     def construct(self):
#         m0 = Matrix([[2, "\pi"], [-1, 1]])
#         m1 = Matrix([[2, 0, 4], [-1, 1, 5]],
#             v_buff=1.3,
#             h_buff=0.8,
#             bracket_h_buff=SMALL_BUFF,
#             bracket_v_buff=SMALL_BUFF,
#             left_bracket="\{",
#             right_bracket="\}")
#         m1.add(SurroundingRectangle(m1.get_columns()[1]))
#         m2 = Matrix([[2, 1], [-1, 3]],
#             element_alignment_corner=UL,
#             left_bracket="(",
#             right_bracket=")")
#         m3 = Matrix([[2, 1], [-1, 3]],
#             left_bracket="\\langle",
#             right_bracket="\\rangle")
#         m4 = Matrix([[2, 1], [-1, 3]],
#         ).set_column_colors(RED, GREEN)
#         m5 = Matrix([[2, 1], [-1, 3]],
#         ).set_row_colors(RED, GREEN)
#         g = Group(
#             m0,m1,m2,m3,m4,m5
#         ).arrange_in_grid(buff=2)
#         self.add(g)


class VelocityGradientTensor(Scene):
    def construct(self):
        matrix = Matrix(
            [
                [r"$\frac{\partial u}{\partial x}$", r"$\frac{\partial u}{\partial y}$", r"$\frac{\partial u}{\partial z}$"], 
                [r"$\frac{\partial v}{\partial x}$", r"$\frac{\partial v}{\partial y}$", r"$\frac{\partial v}{\partial z}$"],
                [r"$\frac{\partial w}{\partial x}$", r"$\frac{\partial w}{\partial y}$", r"$\frac{\partial w}{\partial z}$"],
            ], v_buff=1.5)

        text1 = Tex("Velocity gradient tensor")
        textL = Tex("\\underline{\\underline{L}}", " \\equiv ")
        textDiv = Tex("(",
            "\\nabla \\textbf{v}",
            ")^T =")
        textLT = Tex("(\\underline{\\underline{L}})^T \\equiv ")
        textDivT = Tex("",
            "\\nabla \\textbf{v} ",
            "=")
        textJ = Tex("=(\\nabla \\underline{\\underline{J}})^T")
        
        textJT = Tex("= \\underline{\\underline{J}}")
        

        
        matrixT = Matrix(
           [[r"$\frac{\partial u}{\partial x}$", r"$\frac{\partial u}{\partial y}$", r"$\frac{\partial u}{\partial z}$"], 
            [r"$\frac{\partial v}{\partial x}$", r"$\frac{\partial v}{\partial y}$", r"$\frac{\partial v}{\partial z}$"],
            [r"$\frac{\partial w}{\partial x}$", r"$\frac{\partial w}{\partial y}$", r"$\frac{\partial w}{\partial z}$"]
            ], v_buff=1.5)

        text1.set_color(RED)
        textL[0].set_color(RED)
        textDiv[1].set_color(RED)
        textDivT[0].set_color(RED)
        matrix[1].set_color(RED)
        matrix[2].set_color(RED)
        matrixT[1].set_color(RED)
        matrixT[2].set_color(RED)


        text1.to_edge(UP)
        textDiv.next_to(matrix, LEFT)
        textDivT.next_to(matrixT, LEFT)
        textL.next_to(textDiv, LEFT)
        textLT.next_to(textDivT, LEFT)
        textJ.next_to(matrix, RIGHT)
        textJT.next_to(matrixT, RIGHT)

        textM1 = Tex(r"$\frac{\partial u}{\partial x}$")

        
        self.play(Write(textDivT))
        self.play(Write(matrixT))
        self.wait(5)

        self.play(Write(textJT))
        self.wait(2)

        self.play(ReplacementTransform(textDivT,textDiv), 
            ReplacementTransform(matrixT[0][1],matrix[0][3]),
            ReplacementTransform(matrixT[0][2],matrix[0][6]),
            ReplacementTransform(matrixT[0][5],matrix[0][7]),
            ReplacementTransform(matrixT[0][7],matrix[0][5]),
            ReplacementTransform(matrixT[0][6],matrix[0][2]),
            ReplacementTransform(matrixT[0][3],matrix[0][1]), 
            ReplacementTransform(textJT,textJ))
        self.wait()
        self.play(Write(textL))
        self.wait()

        self.play(Write(text1))
        self.wait(2)

        self.remove(matrix[0][3],matrix[0][6],matrix[0][7],matrix[0][5],matrix[0][2],matrix[0][1])

        self.play(FadeOut(text1), FadeOut(textDiv), FadeOut(textL), FadeOut(matrixT), FadeOut(textJ), ReplacementTransform(matrix[0][0], textM1))
        self.wait(3)
        self.play(ApplyMethod(textM1.to_corner, UL))

# class FluidElement(LinearTransformationScene):
    CONFIG = {
        "include_background_plane": False,
        "include_foreground_plane": False,
        "foreground_plane_kwargs": {
            "x_radius": FRAME_WIDTH,
            "y_radius": FRAME_HEIGHT,
            "secondary_line_ratio": 0
        },
        "background_plane_kwargs": {
            "color": GREY,
            "secondary_color": DARK_GREY,
            "axes_color": GREY,
            "stroke_width": 2,
        },
        "show_coordinates": False,
        "show_basis_vectors": False,
        "basis_vector_stroke_width": 6,
        "i_hat_color": X_COLOR,
        "j_hat_color": Y_COLOR,
        "leave_ghost_vectors": False,
        }

#     def formulas(self):
#         text1 = Tex("\\textbf{v}(\\textbf{x}+d\\textbf{x}) = ",
#             "\\textbf{v}(\\textbf{x}) + ", 
#             "\\pdv{\\textbf{v}(\\textbf{x})}{x}",
#             "dx + ",
#             "\\pdv{\\textbf{v}(\\textbf{x})}{y}", 
#             "dy + ",
#             "\\pdv{\\textbf{v}(\\textbf{x})}{z}",
#             "dz")

#         text1[2].set_color(RED)
#         text1[4].set_color(RED)
#         text1[6].set_color(RED)

#         text2 = Tex("\\textbf{v}(\\textbf{x}+d\\textbf{x}) = \\textbf{v}(\\textbf{x}) + d\\textbf{x} \\cdot",
#             "\\nabla \\textbf{v}(\\textbf{x}) ")

#         text2[1].set_color(RED)

#         text1.shift(2*DOWN)
#         text2.next_to(text1, DOWN)
#         text2.shift(2.4*LEFT)

#         self.play(Write(text1))
#         self.wait(7)
#         self.play(Write(text2))
		
# class Deformation(LinearTransformationScene):
#     CONFIG = {
#         "include_background_plane": False,
#         "include_foreground_plane": False,
#         "foreground_plane_kwargs": {
#             "x_radius": FRAME_WIDTH,
#             "y_radius": FRAME_HEIGHT,
#             "secondary_line_ratio": 0
#         },
#         "background_plane_kwargs": {
#             "color": GREY,
#             "secondary_color": DARK_GREY,
#             "axes_color": GREY,
#             "stroke_width": 2,
#         },
#         "show_coordinates": False,
#         "show_basis_vectors": False,
#         "basis_vector_stroke_width": 6,
#         "i_hat_color": X_COLOR,
#         "j_hat_color": Y_COLOR,
#         "leave_ghost_vectors": False,
#         }
#     def construct(self):
#         rect = Rectangle(height=2, width=4)
#         rect.move_to(0)
#         vector_array = np.array([[1], [2]])
#         matrix = [[1, 1], [0, 1]]

#         text = Tex("Deformation or strain")
#         text.to_edge(UP)

#         self.play(Write(text))

#         self.add_transformable_mobject(rect)

#         # self.apply_matrix(matrix)

#         self.wait(3)


# class DeformationThreeD(ThreeDScene):
#     	def construct(self):
#             axes = ThreeDAxes()
#             prism1 = Prism(dimensions = [4,2,2])
#             axes.add(axes.get_axis_labels())

#             title = Tex("Deformation or strain")
#             title.add_background_rectangle()
#             title.to_edge(UP)

#             matrixxx = [[2, 0, 0], [0, 1, 0], [0, 0, 1]]
#             matrixxy = [[1, 0, 0], [1, 1, 0], [0, 0, 1]]
#             matrixxz = [[1, 0, 0], [0, 1, 0], [1, 0, 1]]

#             matrixyy = [[1, 0, 0], [0, 2, 0], [0, 0, 1]]
#             matrixyx = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
#             matrixyz = [[1, 0, 0], [0, 1, 0], [0, 1, 1]]

#             matrixzz = [[1, 0, 0], [0, 1, 0], [0, 0, 2]]
#             matrixzx = [[1, 0, 1], [0, 1, 0], [0, 0, 1]]
#             matrixzy = [[1, 0, 0], [0, 1, 1], [0, 0, 1]]


#             rmatrixxx = [[1/2, 0, 0], [0, 1, 0], [0, 0, 1]]
#             rmatrixxy = [[1, 0, 0], [-1, 1, 0], [0, 0, 1]]
#             rmatrixxz = [[1, 0, 0], [0, 1, 0], [-1, 0, 1]]

#             rmatrixyy = [[1, 0, 0], [0, 1/2, 0], [0, 0, 1]]
#             rmatrixyx = [[1, -1, 0], [0, 1, 0], [0, 0, 1]]
#             rmatrixyz = [[1, 0, 0], [0, 1, 0], [0, -1, 1]]

#             rmatrixzz = [[1, 0, 0], [0, 1, 0], [0, 0, 1/2]]
#             rmatrixzx = [[1, 0, -1], [0, 1, 0], [0, 0, 1]]
#             rmatrixzy = [[1, 0, 0], [0, 1, -1], [0, 0, 1]]

            
#             vecxxp1 = Vector([1,0,0])
#             vecxyp1 = Vector([0,1,0])
#             vecxzp1 = Vector([0,0,1])
#             vecyxp1 = Vector([1,0,0])
#             vecyyp1 = Vector([0,1,0])
#             vecyzp1 = Vector([0,0,1])
#             veczxp1 = Vector([1,0,0])
#             veczyp1 = Vector([0,1,0])
#             veczzp1 = Vector([0,0,1])
#             vecxxp1.shift(RIGHT)
#             vecxyp1.shift(RIGHT)
#             vecxzp1.shift(RIGHT)
#             vecyxp1.shift(UP)
#             vecyyp1.shift(UP)
#             vecyzp1.shift(UP)
#             veczxp1.shift(OUT)
#             veczyp1.shift(OUT)
#             veczzp1.shift(OUT)
#             vecxxp1.set_color(RED)
#             vecxyp1.set_color(YELLOW)
#             vecxzp1.set_color(GREEN)
#             vecyxp1.set_color(RED)
#             vecyyp1.set_color(YELLOW)
#             vecyzp1.set_color(GREEN)
#             veczxp1.set_color(RED)
#             veczyp1.set_color(YELLOW)
#             veczzp1.set_color(GREEN)

#             vecxxn1 = Vector([-1,0,0])
#             vecxyn1 = Vector([0,-1,0])
#             vecxzn1 = Vector([0,0,-1])
#             vecyxn1 = Vector([-1,0,0])
#             vecyyn1 = Vector([0,-1,0])
#             vecyzn1 = Vector([0,0,-1])
#             veczxn1 = Vector([-1,0,0])
#             veczyn1 = Vector([0,-1,0])
#             veczzn1 = Vector([0,0,-1])
#             vecxxn1.shift(LEFT)
#             vecxyn1.shift(LEFT)
#             vecxzn1.shift(LEFT)
#             vecyxn1.shift(DOWN)
#             vecyyn1.shift(DOWN)
#             vecyzn1.shift(DOWN)
#             veczxn1.shift(IN)
#             veczyn1.shift(IN)
#             veczzn1.shift(IN)
#             vecxxn1.set_color(RED)
#             vecxyn1.set_color(YELLOW)
#             vecxzn1.set_color(GREEN)
#             vecyxn1.set_color(RED)
#             vecyyn1.set_color(YELLOW)
#             vecyzn1.set_color(GREEN)
#             veczxn1.set_color(RED)
#             veczyn1.set_color(YELLOW)
#             veczzn1.set_color(GREEN)

#             vecxxp2 = Vector([1,0,0])
#             vecxyp2 = Vector([0,1,0])
#             vecxzp2 = Vector([0,0,1])
#             vecyxp2 = Vector([1,0,0])
#             vecyyp2 = Vector([0,1,0])
#             vecyzp2 = Vector([0,0,1])
#             veczxp2 = Vector([1,0,0])
#             veczyp2 = Vector([0,1,0])
#             veczzp2 = Vector([0,0,1])
#             vecxxp2.shift(RIGHT*2)
#             vecxyp2.shift(RIGHT+UP)
#             vecxzp2.shift(RIGHT+OUT)
#             vecyxp2.shift(UP+RIGHT)
#             vecyyp2.shift(UP*2)
#             vecyzp2.shift(UP+OUT)
#             veczxp2.shift(OUT+RIGHT)
#             veczyp2.shift(OUT+UP)
#             veczzp2.shift(OUT*2)
#             vecxxp2.set_color(RED)
#             vecxyp2.set_color(YELLOW)
#             vecxzp2.set_color(GREEN)
#             vecyxp2.set_color(RED)
#             vecyyp2.set_color(YELLOW)
#             vecyzp2.set_color(GREEN)
#             veczxp2.set_color(RED)
#             veczyp2.set_color(YELLOW)
#             veczzp2.set_color(GREEN)

#             vecxxn2 = Vector([-1,0,0])
#             vecxyn2 = Vector([0,-1,0])
#             vecxzn2 = Vector([0,0,-1])
#             vecyxn2 = Vector([-1,0,0])
#             vecyyn2 = Vector([0,-1,0])
#             vecyzn2 = Vector([0,0,-1])
#             veczxn2 = Vector([-1,0,0])
#             veczyn2 = Vector([0,-1,0])
#             veczzn2 = Vector([0,0,-1])
#             vecxxn2.shift(LEFT*2)
#             vecxyn2.shift(LEFT+DOWN)
#             vecxzn2.shift(LEFT+IN)
#             vecyxn2.shift(DOWN+LEFT)
#             vecyyn2.shift(DOWN*2)
#             vecyzn2.shift(DOWN+IN)
#             veczxn2.shift(IN+LEFT)
#             veczyn2.shift(IN+DOWN)
#             veczzn2.shift(IN*2)
#             vecxxn2.set_color(RED)
#             vecxyn2.set_color(YELLOW)
#             vecxzn2.set_color(GREEN)
#             vecyxn2.set_color(RED)
#             vecyyn2.set_color(YELLOW)
#             vecyzn2.set_color(GREEN)
#             veczxn2.set_color(RED)
#             veczyn2.set_color(YELLOW)
#             veczzn2.set_color(GREEN)




#             rvecxxp1 = Vector([-1,0,0])
#             rvecxyp1 = Vector([0,-1,0])
#             rvecxzp1 = Vector([0,0,-1])
#             rvecyxp1 = Vector([-1,0,0])
#             rvecyyp1 = Vector([0,-1,0])
#             rvecyzp1 = Vector([0,0,-1])
#             rveczxp1 = Vector([-1,0,0])
#             rveczyp1 = Vector([0,-1,0])
#             rveczzp1 = Vector([0,0,-1])
#             rvecxxp1.shift(RIGHT*2)
#             rvecxyp1.shift(RIGHT)
#             rvecxzp1.shift(RIGHT)
#             rvecyxp1.shift(UP)
#             rvecyyp1.shift(UP*2)
#             rvecyzp1.shift(UP)
#             rveczxp1.shift(OUT)
#             rveczyp1.shift(OUT)
#             rveczzp1.shift(OUT*2)
#             rvecxxp1.set_color(RED)
#             rvecxyp1.set_color(YELLOW)
#             rvecxzp1.set_color(GREEN)
#             rvecyxp1.set_color(RED)
#             rvecyyp1.set_color(YELLOW)
#             rvecyzp1.set_color(GREEN)
#             rveczxp1.set_color(RED)
#             rveczyp1.set_color(YELLOW)
#             rveczzp1.set_color(GREEN)

#             rvecxxn1 = Vector([1,0,0])
#             rvecxyn1 = Vector([0,1,0])
#             rvecxzn1 = Vector([0,0,1])
#             rvecyxn1 = Vector([1,0,0])
#             rvecyyn1 = Vector([0,1,0])
#             rvecyzn1 = Vector([0,0,1])
#             rveczxn1 = Vector([1,0,0])
#             rveczyn1 = Vector([0,1,0])
#             rveczzn1 = Vector([0,0,1])
#             rvecxxn1.shift(LEFT*2)
#             rvecxyn1.shift(LEFT)
#             rvecxzn1.shift(LEFT)
#             rvecyxn1.shift(DOWN)
#             rvecyyn1.shift(DOWN*2)
#             rvecyzn1.shift(DOWN)
#             rveczxn1.shift(IN)
#             rveczyn1.shift(IN)
#             rveczzn1.shift(IN*2)
#             rvecxxn1.set_color(RED)
#             rvecxyn1.set_color(YELLOW)
#             rvecxzn1.set_color(GREEN)
#             rvecyxn1.set_color(RED)
#             rvecyyn1.set_color(YELLOW)
#             rvecyzn1.set_color(GREEN)
#             rveczxn1.set_color(RED)
#             rveczyn1.set_color(YELLOW)
#             rveczzn1.set_color(GREEN)

#             rvecxxp2 = Vector([-1,0,0])
#             rvecxyp2 = Vector([0,-1,0])
#             rvecxzp2 = Vector([0,0,-1])
#             rvecyxp2 = Vector([-1,0,0])
#             rvecyyp2 = Vector([0,-1,0])
#             rvecyzp2 = Vector([0,0,-1])
#             rveczxp2 = Vector([-1,0,0])
#             rveczyp2 = Vector([0,-1,0])
#             rveczzp2 = Vector([0,0,-1])
#             rvecxxp2.shift(RIGHT*3)
#             rvecxyp2.shift(RIGHT+UP)
#             rvecxzp2.shift(RIGHT+OUT)
#             rvecyxp2.shift(UP+RIGHT)
#             rvecyyp2.shift(UP*3)
#             rvecyzp2.shift(UP+OUT)
#             rveczxp2.shift(OUT+RIGHT)
#             rveczyp2.shift(OUT+UP)
#             rveczzp2.shift(OUT*3)
#             rvecxxp2.set_color(RED)
#             rvecxyp2.set_color(YELLOW)
#             rvecxzp2.set_color(GREEN)
#             rvecyxp2.set_color(RED)
#             rvecyyp2.set_color(YELLOW)
#             rvecyzp2.set_color(GREEN)
#             rveczxp2.set_color(RED)
#             rveczyp2.set_color(YELLOW)
#             rveczzp2.set_color(GREEN)

#             rvecxxn2 = Vector([1,0,0])
#             rvecxyn2 = Vector([0,1,0])
#             rvecxzn2 = Vector([0,0,1])
#             rvecyxn2 = Vector([1,0,0])
#             rvecyyn2 = Vector([0,1,0])
#             rvecyzn2 = Vector([0,0,1])
#             rveczxn2 = Vector([1,0,0])
#             rveczyn2 = Vector([0,1,0])
#             rveczzn2 = Vector([0,0,1])
#             rvecxxn2.shift(LEFT*3)
#             rvecxyn2.shift(LEFT+DOWN)
#             rvecxzn2.shift(LEFT+IN)
#             rvecyxn2.shift(DOWN+LEFT)
#             rvecyyn2.shift(DOWN*3)
#             rvecyzn2.shift(DOWN+IN)
#             rveczxn2.shift(IN+LEFT)
#             rveczyn2.shift(IN+DOWN)
#             rveczzn2.shift(IN*3)
#             rvecxxn2.set_color(RED)
#             rvecxyn2.set_color(YELLOW)
#             rvecxzn2.set_color(GREEN)
#             rvecyxn2.set_color(RED)
#             rvecyyn2.set_color(YELLOW)
#             rvecyzn2.set_color(GREEN)
#             rveczxn2.set_color(RED)
#             rveczyn2.set_color(YELLOW)
#             rveczzn2.set_color(GREEN)


#             text = Tex("Visualizing Deformation of a solid cube in 3D space")
#             text.to_edge(UP)
#             text.scale(1.5)
#             self.play(Write(text))
#             self.wait()
#             self.remove(text)


#             self.set_camera_orientation(phi=75 * DEGREES,theta= 210*DEGREES)
#             self.begin_ambient_camera_rotation(rate=0.2)

#             self.add(axes)
#             self.add_fixed_in_frame_mobjects(title)
#             self.add(prism1)
#             # self.add(vecxx,vecxy,vecxz,vecyx,vecyy,vecyz,veczx,veczy,veczz)
#             self.wait(3)

#             self.play(
#                 ApplyMethod(prism1.apply_matrix, matrixzx),
#                 ReplacementTransform(veczxp1,veczxp2),
#                 ReplacementTransform(veczxn1,veczxn2), 
#                 run_time=2
#             )
#             self.remove(veczxp2,veczxn2)
#             self.wait(4)

# class Axes3DExample(ThreeDScene):
#     def construct(self):
#         axes = ThreeDAxes()

#         x_label = axes.get_x_axis_label(Tex("x"))
#         y_label = axes.get_y_axis_label(Tex("y")).shift(UP * 1.8)

#         # 3D variant of the Dot() object
#         dot = Dot3D()

#         # zoom out so we see the axes
#         self.set_camera_orientation(zoom=0.5)

#         self.play(FadeIn(axes), FadeIn(dot), FadeIn(x_label), FadeIn(y_label))

#         self.wait(0.5)

#         # animate the move of the camera to properly see the axes
#         self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom=1, run_time=1.5)

#         # built-in updater which begins camera rotation
#         self.begin_ambient_camera_rotation(rate=0.15)

#         # one dot for each direction
#         upDot = dot.copy().set_color(RED)
#         rightDot = dot.copy().set_color(BLUE)
#         outDot = dot.copy().set_color(GREEN)

#         self.wait(1)

#         self.play(
#             upDot.animate.shift(UP),
#             rightDot.animate.shift(RIGHT),
#             outDot.animate.shift(OUT),
#         )   

#         self.wait(2)


# # code to show 3d graph with gird lines
# class Graph3DExample(ThreeDScene):
#     def construct(self):
#         axes = ThreeDAxes()
#         axes.set_opacity(0.5)
#         axes.set_color(GRAY)
#         axes.set_stroke(width=1)
#         axes.set_z_axis_label(Tex("z"))
#         axes.set_y_axis_label(Tex("y"))
#         axes.set_x_axis_label(Tex("x"))
#         self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
#         self.add(axes)
#         self.wait(1)
#         self.begin_ambient_camera_rotation(rate=0.15)
#         self.wait(1)
#         self.play(
#             axes.animate.set_opacity(1),
#             axes.animate.set_stroke(width=2),
#         )
#         self.wait(1)
#         self.play(
#             axes.animate.set_opacity(0.5),
#             axes.animate.set_stroke(width=1),
#         )
#         self.wait(1)
#         self.play(
#             axes.animate.set_opacity(1),
#             axes.animate.set_stroke(width=2),
#         )
#         self.wait(1)
#         self.play(
#             axes.animate.set_opacity(0.5),
#             axes.animate.set_stroke(width=1),
#         )
#         self.wait(1)
#         self.play(
#             axes.animate.set_opacity(1),
#             axes.animate.set_stroke(width=2),
#         )
#         self.wait(1)
#         self.play(
#             axes.animate.set_opacity(0.5),
#             axes.animate.set_stroke(width=1),
#         )
#         self.wait(1)
#         self.play(
#             axes.animate.set_opacity(1),
#             axes.animate.set_stroke(width=2),
#         )
#         self.wait(1)
#         self.play(
#             axes.animate.set_opacity(0.5),
#             axes.animate.set_stroke(width=1),
#         )
#         self.wait(1)
#         self.play(
#             axes.animate.set_opacity(1),
#             axes.animate.set_stroke(width=2),
#         )
#         self.wait(1)
#         self.play(
#             axes.animate.set_opacity(0.5),
#             axes.animate.set_stroke(width=1),
#         )
#         self.wait(1)
#         self.play(
#             axes.animate.set_opacity(1),
#             axes.animate.set_stroke(width=2),
#         )
#         self.wait(1)
#         self.play(
#             axes.animate.set_opacity(0.5),
#             axes.animate.set_stroke(width=1),
#         )
#         self.wait



# class ThankScene(Scene):
# 	def construct(self):
# 		thanks = Tex("This video was made using Manim library, ")
# 		thanks2 = Tex("made by")
# 		thanks3 = Tex("Grant Sanderson youtuber of ", "3Blue","1Brown", ".")

# 		# thanks3[1].set_color(BLUE)
# 		# thanks3[2].set_color("#964b00")

# 		thanks.next_to(thanks2, UP)
# 		thanks3.next_to(thanks2, DOWN)

# 		self.play(Write(thanks))
# 		self.play(Write(thanks2))
# 		self.play(Write(thanks3))
# 		self.wait(2)