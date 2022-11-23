from manim import *

class Interval_between_straina_and_linear_algebra(Scene):
	def construct(self):

		text = Tex("Having seen how to relate matrix multiplication with transformation let's now use this idea for changing the reference frame.").scale(0.6)
		text2 = Tex("The idea is to be able to paint a landscape in which the proof is obvious.").scale(0.6)
		text3 = Tex("-Pierre Deligne").scale(0.6)

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

		self.play(Write(text), run_time=6.0)
		self.wait(3)
		self.play(Write(text2), run_time=3.0)
		self.wait(4)
		self.play(Write(text3), run_time=3.0)
		self.wait(3)


class background(Scene):
    def construct(self):
        text = Tex("In this video we shall be answering a fundamental questions in Stress Strain Theory:").next_to(ORIGIN,UP).scale(0.6)
        
        # text2 = MarkupText(
        #     f'Why are <span underline="double" underline_color="green">principal components of stress</span> <span fgcolor="{YELLOW}">related with Eigenvectors? </span>',
        #     font_size=34
        # ).next_to(text,DOWN).scale(0.6)
        
        text3 = MarkupText(
            f"How does stress and strain <span underline='double' underline_color='green'>transformations work?</span>",
            font_size=34
        ).next_to(text,DOWN).scale(0.6)
        
        text4 = MarkupText(f"<span fgcolor='{YELLOW}'> And I shall derive formula of stress and strain transformation visually.</span>",
            font_size=34
        ).next_to(text3,DOWN).scale(0.6)
        
        self.play(Write(text),run_time=3.0)
        self.wait(3)
        # self.play(Write(text2),run_time=3.0)
        # self.wait(4)
        self.play(Write(text3),run_time=4.0)
        self.play(Write(text4),run_time=4.0)

        self.wait(5)
        animations = [
            FadeOut(text),
            # FadeOut(text2),
            FadeOut(text3),
            FadeOut(text4)      
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))
        
class Strain(Scene):
    def construct(self):
        title=MathTex(r"\mathbb{S}\mathbb{T}\mathbb{R}\mathbb{A}\mathbb{I}\mathbb{N}}",color=PINK).scale(2)
        self.play(Write(title),run_time=3.0)
        self.wait(1)
        self.play(Unwrite(title),run_time=2.0)

class MathPro(Scene):
    def construct(self):
        title=MathTex(r"\mathbb{T}\mathbb{R}\mathbb{A}\mathbb{N}\mathbb{S}\mathbb{F}\mathbb{O}\mathbb{R}\mathbb{M}\mathbb{A}\mathbb{T}\mathbb{I}\mathbb{O}\mathbb{N}\ \mathbb{E}\mathbb{Q}\mathbb{U}\mathbb{A}\mathbb{T}\mathbb{I}\mathbb{O}\mathbb{N}",color=PINK).scale(1.5)
        self.play(Write(title),run_time=3.0)
        self.wait(4)
        self.play(Unwrite(title),run_time=2.0)
        
class Deformation(LinearTransformationScene):
    def construct(self):
        rect = Rectangle(height=2, width=4)
        rect.move_to(0)
        vector_array = np.array([[1], [2]])
        matrix = [[1, 1], [0, 1]]

        text = Tex("Deformation or strain")
        text.to_edge(UP)

        self.play(Write(text))

        self.add_transformable_mobject(rect)

        # self.apply_matrix(matrix)

        self.wait(3)


class DeformationThreeD(ThreeDScene):
    	def construct(self):
            axes = ThreeDAxes()
            prism1 = Prism(dimensions = [4,2,2])
            axes.add(axes.get_axis_labels())

            title = Tex("Strain, in three dimensions.").scale(0.7)
            title.add_background_rectangle()
            title.to_edge(UP)

            matrixzx = [[1, 0, 1], [0, 1, 0], [0, 0, 1]]

            vecxxp1 = Vector([1,0,0])
            vecxyp1 = Vector([0,1,0])
            vecxzp1 = Vector([0,0,1])
            vecyxp1 = Vector([1,0,0])
            vecyyp1 = Vector([0,1,0])
            vecyzp1 = Vector([0,0,1])
            veczxp1 = Vector([1,0,0])
            veczyp1 = Vector([0,1,0])
            veczzp1 = Vector([0,0,1])
            vecxxp1.shift(RIGHT)
            vecxyp1.shift(RIGHT)
            vecxzp1.shift(RIGHT)
            vecyxp1.shift(UP)
            vecyyp1.shift(UP)
            vecyzp1.shift(UP)
            veczxp1.shift(OUT)
            veczyp1.shift(OUT)
            veczzp1.shift(OUT)
            vecxxp1.set_color(RED)
            vecxyp1.set_color(YELLOW)
            vecxzp1.set_color(GREEN)
            vecyxp1.set_color(RED)
            vecyyp1.set_color(YELLOW)
            vecyzp1.set_color(GREEN)
            veczxp1.set_color(RED)
            veczyp1.set_color(YELLOW)
            veczzp1.set_color(GREEN)

            vecxxn1 = Vector([-1,0,0])
            vecxyn1 = Vector([0,-1,0])
            vecxzn1 = Vector([0,0,-1])
            vecyxn1 = Vector([-1,0,0])
            vecyyn1 = Vector([0,-1,0])
            vecyzn1 = Vector([0,0,-1])
            veczxn1 = Vector([-1,0,0])
            veczyn1 = Vector([0,-1,0])
            veczzn1 = Vector([0,0,-1])
            vecxxn1.shift(LEFT)
            vecxyn1.shift(LEFT)
            vecxzn1.shift(LEFT)
            vecyxn1.shift(DOWN)
            vecyyn1.shift(DOWN)
            vecyzn1.shift(DOWN)
            veczxn1.shift(IN)
            veczyn1.shift(IN)
            veczzn1.shift(IN)
            vecxxn1.set_color(RED)
            vecxyn1.set_color(YELLOW)
            vecxzn1.set_color(GREEN)
            vecyxn1.set_color(RED)
            vecyyn1.set_color(YELLOW)
            vecyzn1.set_color(GREEN)
            veczxn1.set_color(RED)
            veczyn1.set_color(YELLOW)
            veczzn1.set_color(GREEN)

            vecxxp2 = Vector([1,0,0])
            vecxyp2 = Vector([0,1,0])
            vecxzp2 = Vector([0,0,1])
            vecyxp2 = Vector([1,0,0])
            vecyyp2 = Vector([0,1,0])
            vecyzp2 = Vector([0,0,1])
            veczxp2 = Vector([1,0,0])
            veczyp2 = Vector([0,1,0])
            veczzp2 = Vector([0,0,1])
            vecxxp2.shift(RIGHT*2)
            vecxyp2.shift(RIGHT+UP)
            vecxzp2.shift(RIGHT+OUT)
            vecyxp2.shift(UP+RIGHT)
            vecyyp2.shift(UP*2)
            vecyzp2.shift(UP+OUT)
            veczxp2.shift(OUT+RIGHT)
            veczyp2.shift(OUT+UP)
            veczzp2.shift(OUT*2)
            vecxxp2.set_color(RED)
            vecxyp2.set_color(YELLOW)
            vecxzp2.set_color(GREEN)
            vecyxp2.set_color(RED)
            vecyyp2.set_color(YELLOW)
            vecyzp2.set_color(GREEN)
            veczxp2.set_color(RED)
            veczyp2.set_color(YELLOW)
            veczzp2.set_color(GREEN)

            vecxxn2 = Vector([-1,0,0])
            vecxyn2 = Vector([0,-1,0])
            vecxzn2 = Vector([0,0,-1])
            vecyxn2 = Vector([-1,0,0])
            vecyyn2 = Vector([0,-1,0])
            vecyzn2 = Vector([0,0,-1])
            veczxn2 = Vector([-1,0,0])
            veczyn2 = Vector([0,-1,0])
            veczzn2 = Vector([0,0,-1])
            vecxxn2.shift(LEFT*2)
            vecxyn2.shift(LEFT+DOWN)
            vecxzn2.shift(LEFT+IN)
            vecyxn2.shift(DOWN+LEFT)
            vecyyn2.shift(DOWN*2)
            vecyzn2.shift(DOWN+IN)
            veczxn2.shift(IN+LEFT)
            veczyn2.shift(IN+DOWN)
            veczzn2.shift(IN*2)
            vecxxn2.set_color(RED)
            vecxyn2.set_color(YELLOW)
            vecxzn2.set_color(GREEN)
            vecyxn2.set_color(RED)
            vecyyn2.set_color(YELLOW)
            vecyzn2.set_color(GREEN)
            veczxn2.set_color(RED)
            veczyn2.set_color(YELLOW)
            veczzn2.set_color(GREEN)


            rvecxxp1 = Vector([-1,0,0])
            rvecxyp1 = Vector([0,-1,0])
            rvecxzp1 = Vector([0,0,-1])
            rvecyxp1 = Vector([-1,0,0])
            rvecyyp1 = Vector([0,-1,0])
            rvecyzp1 = Vector([0,0,-1])
            rveczxp1 = Vector([-1,0,0])
            rveczyp1 = Vector([0,-1,0])
            rveczzp1 = Vector([0,0,-1])
            rvecxxp1.shift(RIGHT*2)
            rvecxyp1.shift(RIGHT)
            rvecxzp1.shift(RIGHT)
            rvecyxp1.shift(UP)
            rvecyyp1.shift(UP*2)
            rvecyzp1.shift(UP)
            rveczxp1.shift(OUT)
            rveczyp1.shift(OUT)
            rveczzp1.shift(OUT*2)
            rvecxxp1.set_color(RED)
            rvecxyp1.set_color(YELLOW)
            rvecxzp1.set_color(GREEN)
            rvecyxp1.set_color(RED)
            rvecyyp1.set_color(YELLOW)
            rvecyzp1.set_color(GREEN)
            rveczxp1.set_color(RED)
            rveczyp1.set_color(YELLOW)
            rveczzp1.set_color(GREEN)

            rvecxxn1 = Vector([1,0,0])
            rvecxyn1 = Vector([0,1,0])
            rvecxzn1 = Vector([0,0,1])
            rvecyxn1 = Vector([1,0,0])
            rvecyyn1 = Vector([0,1,0])
            rvecyzn1 = Vector([0,0,1])
            rveczxn1 = Vector([1,0,0])
            rveczyn1 = Vector([0,1,0])
            rveczzn1 = Vector([0,0,1])
            rvecxxn1.shift(LEFT*2)
            rvecxyn1.shift(LEFT)
            rvecxzn1.shift(LEFT)
            rvecyxn1.shift(DOWN)
            rvecyyn1.shift(DOWN*2)
            rvecyzn1.shift(DOWN)
            rveczxn1.shift(IN)
            rveczyn1.shift(IN)
            rveczzn1.shift(IN*2)
            rvecxxn1.set_color(RED)
            rvecxyn1.set_color(YELLOW)
            rvecxzn1.set_color(GREEN)
            rvecyxn1.set_color(RED)
            rvecyyn1.set_color(YELLOW)
            rvecyzn1.set_color(GREEN)
            rveczxn1.set_color(RED)
            rveczyn1.set_color(YELLOW)
            rveczzn1.set_color(GREEN)

            rvecxxp2 = Vector([-1,0,0])
            rvecxyp2 = Vector([0,-1,0])
            rvecxzp2 = Vector([0,0,-1])
            rvecyxp2 = Vector([-1,0,0])
            rvecyyp2 = Vector([0,-1,0])
            rvecyzp2 = Vector([0,0,-1])
            rveczxp2 = Vector([-1,0,0])
            rveczyp2 = Vector([0,-1,0])
            rveczzp2 = Vector([0,0,-1])
            rvecxxp2.shift(RIGHT*3)
            rvecxyp2.shift(RIGHT+UP)
            rvecxzp2.shift(RIGHT+OUT)
            rvecyxp2.shift(UP+RIGHT)
            rvecyyp2.shift(UP*3)
            rvecyzp2.shift(UP+OUT)
            rveczxp2.shift(OUT+RIGHT)
            rveczyp2.shift(OUT+UP)
            rveczzp2.shift(OUT*3)
            rvecxxp2.set_color(RED)
            rvecxyp2.set_color(YELLOW)
            rvecxzp2.set_color(GREEN)
            rvecyxp2.set_color(RED)
            rvecyyp2.set_color(YELLOW)
            rvecyzp2.set_color(GREEN)
            rveczxp2.set_color(RED)
            rveczyp2.set_color(YELLOW)
            rveczzp2.set_color(GREEN)

            rvecxxn2 = Vector([1,0,0])
            rvecxyn2 = Vector([0,1,0])
            rvecxzn2 = Vector([0,0,1])
            rvecyxn2 = Vector([1,0,0])
            rvecyyn2 = Vector([0,1,0])
            rvecyzn2 = Vector([0,0,1])
            rveczxn2 = Vector([1,0,0])
            rveczyn2 = Vector([0,1,0])
            rveczzn2 = Vector([0,0,1])
            rvecxxn2.shift(LEFT*3)
            rvecxyn2.shift(LEFT+DOWN)
            rvecxzn2.shift(LEFT+IN)
            rvecyxn2.shift(DOWN+LEFT)
            rvecyyn2.shift(DOWN*3)
            rvecyzn2.shift(DOWN+IN)
            rveczxn2.shift(IN+LEFT)
            rveczyn2.shift(IN+DOWN)
            rveczzn2.shift(IN*3)
            rvecxxn2.set_color(RED)
            rvecxyn2.set_color(YELLOW)
            rvecxzn2.set_color(GREEN)
            rvecyxn2.set_color(RED)
            rvecyyn2.set_color(YELLOW)
            rvecyzn2.set_color(GREEN)
            rveczxn2.set_color(RED)
            rveczyn2.set_color(YELLOW)
            rveczzn2.set_color(GREEN)

            vaxis_1 = Vector([1,0,0], color = YELLOW)
            vaxis_2 = Vector([0,1,0], color = YELLOW)
            vaxis_3 = Vector([0,0,1], color = YELLOW)

            v = [vaxis_1, vaxis_2, vaxis_3]
            
            # text = Tex("Visualizing Deformation of a solid cube in 3D space")
            # text.to_edge(UP)
            # text.scale(1.5)
            # self.play(Write(text))
            # self.wait()
            # self.remove(text)


            self.set_camera_orientation(phi=75 * DEGREES,theta= 210*DEGREES)
            self.begin_ambient_camera_rotation(rate=0.2)

            self.add(axes)
            self.add_fixed_in_frame_mobjects(title)
            self.play(Write(prism1))
            # self.add(vecxx,vecxy,vecxz,vecyx,vecyy,vecyz,veczx,veczy,veczz)
            def numberToBase(n, b):
                if n == 0:
                    return 0
                digits = 0
                while n:
                    digits = digits*10 + (int(n % b))
                    n //= b
                return digits
            c = 0
            self.wait(3)
            for dir in [OUT, -UP, -2*LEFT]:
                for _ in v:
                    rot = -LEFT
                    st = ""
                    i = (numberToBase(c, 3))
                    base = f"{i:02}"
                    print(base)
                    dict = {'0':'x', '1':'y', '2':'z'}
                    st = st+  (dict[base[0]])
                    st = st+ (dict[base[1]])
                    
                    self.play(
                        Create(_.copy().shift(dir*1)), 
                        Write((Tex(f"$\epsilon_\u007b{st}\u007d$").scale(1).next_to(_.copy().shift(dir*1)).rotate(PI/2, axis = rot*1))),
                        run_time = 0.7
                        )
                    c += 1

            self.wait(3)

            self.play(
                ApplyMethod(prism1.apply_matrix, matrixzx),
                ReplacementTransform(veczxp1,veczxp2),
                ReplacementTransform(veczxn1,veczxn2), 
                run_time=2
            )
            self.remove(veczxp2,veczxn2)
            self.wait(5)

