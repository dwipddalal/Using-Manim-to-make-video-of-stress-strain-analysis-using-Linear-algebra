class ThankScene(Scene):
	def construct(self):
		thanks = Tex("This video was made using Manim library, ")
		thanks2 = Tex("made by")
		thanks3 = Tex("Grant Sanderson youtuber of ", "3Blue","1Brown", ".")

		# thanks3[1].set_color(BLUE)
		# thanks3[2].set_color("#964b00")

		thanks.next_to(thanks2, UP)
		thanks3.next_to(thanks2, DOWN)

		self.play(Write(thanks))
		self.play(Write(thanks2))
		self.play(Write(thanks3))
		self.wait(2)