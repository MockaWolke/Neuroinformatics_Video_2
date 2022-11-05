from manim import *
import numpy as np

config.verbosity = "WARNING"

class Matrix_B(VectorScene):
    def construct(self):
        plane = self.add_plane(background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.3
            },animate=False).add_coordinates()
        beta = Variable(1, r"\beta").shift(UP*3,LEFT*3)

        formula = MathTex(r"""B_{\beta} \cdot a = \begin{bmatrix} \beta & 0 \\ 0 & \beta\end{bmatrix} \cdot a""").shift(RIGHT * 3,UP*3)
        self.play(Write(formula))
        self.wait(2) 
        self.play(Write(beta)) 

        v1= self.add_vector([1,0],color = YELLOW)

        l1 = self.label_vector(vector=v1,label=MathTex(r"a"))
        c1 = v1.coordinate_label()
        self.add(c1,l1)
        self.wait(1)
        self.remove(c1,l1)

        v2 = Vector([5,0],color = GREEN)
        self.play(Transform(v1,v2),beta.tracker.animate.set_value(5),run_time = 6)

        l2 = self.label_vector(vector=v2,label=MathTex(r"B_5 \cdot a"))

        c2 = v2.coordinate_label()
        self.play(FadeIn(c2))
        self.wait(1)
        self.remove(l2,v1,c2)

        v3 = Vector([-3,0],color = BLUE)
        self.play(Transform(v2,v3),beta.tracker.animate.set_value(-3),run_time = 6)
        l3 = self.label_vector(vector=v3,label=MathTex(r"B_{-3} \cdot a"))
        c3 = v3.coordinate_label()
        self.play(FadeIn(c3))
        self.wait(1)
        self.remove(l3,v2,c3)
        self.wait(2)
        


class Matrix_A(VectorScene):

    def construct(self):
        plane = self.add_plane(background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.3
            },x_range = [-1.5,1.5],y_range = [-1.5,1.5] ,animate=False).add_coordinates()
        alpha = Variable(0, r"\alpha").shift(LEFT * 6)

        formula = MathTex(r"""A_{\alpha} \cdot a = \begin{bmatrix} cos(\alpha) & -sin(\alpha) \\ sin(\alpha) & cos(\alpha)\end{bmatrix} \cdot a""").shift(UP * 3)
        self.play(Write(formula))

        vector1 = self.add_vector([1,0],color = YELLOW)
        vector2 = Vector([1,0],color=GREEN)

        self.wait(2)
   
        pi = Tex(r"$\cdot\pi$",font_size = 80).next_to(alpha, RIGHT).shift(LEFT *.1) 
        l1 = self.label_vector(vector=vector1,label=MathTex(r"a"))
        c1 = vector1.coordinate_label()
        self.add(c1)
        self.wait(1)
        self.remove(c1)

        self.add(alpha,pi)
        self.play(Transform(vector1,vector2))
        self.add(vector2)
        self.remove(l1,vector1)
        label = self.label_vector(vector=vector2,label=MathTex(r"\hat{a}"))


        label.add_updater(lambda d: d.move_to([vector2.get_end()[0]*1.2,vector2.get_end()[1]*1.2,vector2.get_end()[2]]))
   

        self.wait(1)        
        self.play(Rotating(vector2,radians=2 * PI,about_point= ORIGIN),alpha.tracker.animate.set_value(2),run_time = 6)
        self.wait(2)

        
class Task_B(VectorScene):
    def construct(self):
        plane = self.add_plane(background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.3
            },animate=False).add_coordinates()

        circle = Circle(radius=1)

        self.add(circle)

        v1,v2,v3,l1,l2,l3 = self.start_situation()


        self.wait(2)
        alpha = Variable(.25, r"\alpha").shift(LEFT * 6, UP * 3)
        pi = Tex(r"$\cdot\pi$",font_size = 80).next_to(alpha, RIGHT).shift(LEFT *.1) 

        self.remove(l1,l2,l3)

        l1, l2, l3 = self.create_head_tracer(v1, v2, v3)
   
        degree = 0.25        

        # noch nicht rotiert

        formula = MathTex(r"""\hat{a} = \begin{bmatrix} cos(\frac{\pi}{4} ) & -sin(\frac{\pi}{4} ) \\ sin(\frac{\pi}{4} ) & cos(\frac{\pi}{4} )\end{bmatrix} \cdot a""").shift(UP * 3,RIGHT*3).scale(.8)
        self.play(Write(formula))
        self.play(Write(alpha),Write(pi))

        formula2 = MathTex(r"""\hat{a} = \begin{bmatrix} 0 & -1 \\ 1 & 0\end{bmatrix} \cdot a""").move_to(formula)
        self.play(Transform(formula,formula2))
        self.remove(formula)
        self.wait(2)
        alpha.tracker.set_value(0)
        self.play(Write(alpha))



        self.wait(1)        
        self.play(Rotating(v1,radians=degree* PI,about_point= ORIGIN),
        Rotating(v2,radians=degree* PI,about_point= ORIGIN),
        Rotating(v3,radians=degree* PI,about_point= ORIGIN),
        alpha.tracker.animate.set_value(degree),run_time = 6)
        self.wait(2)

        beta_TEX = MathTex(r"\beta\,=\,\sqrt{2}").shift(UP*3,LEFT*3).move_to(alpha).shift(DOWN*1.5)
        self.play(Write(beta_TEX))

        formula3 = MathTex(r"""\hat{a} = \begin{bmatrix} \sqrt{2} &  \\ 0 & \sqrt{2}\end{bmatrix} \cdot \begin{bmatrix} 0 & -1 \\ 1 & 0\end{bmatrix} \cdot a""").move_to(formula2).shift(RIGHT*0.3)
        self.play(Transform(formula2,formula3))
        self.add(formula3)
        self.remove(formula2)
        self.wait(2)

        formula4 = MathTex(r"""\hat{a} = \begin{bmatrix} 0 & -\sqrt{2}  \\ \sqrt{2} & 0\end{bmatrix} \cdot a""").move_to(formula3)
        self.play(Transform(formula3,formula4))
        self.remove(formula4)
        self.wait(2)

        beta = Variable(1, r"\beta").move_to(beta_TEX)
        self.play(FadeOut(beta_TEX,l1,l2,l3),Write(beta))
        self.wait(2)

        sv1,sv2,sv3 = map(lambda x: stretch_vector(x,np.sqrt(2)),[v1,v2,v3])

        circle2 = Circle(radius=np.sqrt(2))

        self.play(Transform(v1,sv1),
                Transform(v2,sv2),
                Transform(v3,sv3),
                Transform(circle,circle2),
                beta.tracker.animate.set_value(np.sqrt(2)),
                 run_time = 4)

        self.wait(2)


    


    def start_situation(self):
        v1 = self.add_vector([1,0],color = YELLOW)
        l1 = self.label_vector(vector=v1,label=MathTex(r"a"))
        c1 = v1.coordinate_label()
        self.add(c1)
        self.wait(1)
        self.remove(c1)
        v2 = self.add_vector([0,1],color = GREEN)
        l2 = self.label_vector(vector=v2,label=MathTex(r"b"))
        c2 = v2.coordinate_label()
        self.add(c2)
        self.wait(1)
        self.remove(c2)
        v3 = self.add_vector([.5,np.sqrt(3)*.5],color = BLUE)
        l3 = self.label_vector(vector=v3,label=MathTex(r"v"))
        c3 = v3.coordinate_label()
        self.add(c3)
        self.wait(1)
        self.remove(c3)
        return v1,v2,v3,l1,l2,l3


    def create_head_tracer(self, v1, v2, v3):
        l1 = self.label_vector(vector=v1,label=MathTex(r"\hat{a}"))
        l2 = self.label_vector(vector=v2,label=MathTex(r"\hat{b}"))
        l3 = self.label_vector(vector=v3,label=MathTex(r"\hat{v}"))

        self.play(l1.animate.move_to([v1.get_end()[0]*1.2,v1.get_end()[1]*1.2,v1.get_end()[2]]),
        l2.animate.move_to([v2.get_end()[0]*1.2,v2.get_end()[1]*1.2,v2.get_end()[2]]),
        l3.animate.move_to([v3.get_end()[0]*1.2,v3.get_end()[1]*1.2,v3.get_end()[2]]))


        l1.add_updater(lambda d: d.move_to([v1.get_end()[0]*1.2,v1.get_end()[1]*1.2,v1.get_end()[2]]))
        l2.add_updater(lambda d: d.move_to([v2.get_end()[0]*1.2,v2.get_end()[1]*1.2,v2.get_end()[2]]))
        l3.add_updater(lambda d: d.move_to([v3.get_end()[0]*1.2,v3.get_end()[1]*1.2,v3.get_end()[2]]))
        return l1,l2,l3


def stretch_vector(vector,factor):

    new_vector = Vector([i*factor for i in vector.get_end()[:2]],color = vector.get_color())
    return new_vector

class Matrix_A_and_B(VectorScene):

    def construct(self):
        plane = self.add_plane(background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.3
            },animate=False).add_coordinates()
        alpha = Variable(0, r"\alpha").shift(LEFT * 6, UP * 3)

        v1, v2, v3, l1,l2,l3 = self.start_situation()

        self.wait(2)
   
        pi = Tex(r"$\cdot\pi$",font_size = 80).next_to(alpha, RIGHT).shift(LEFT *.1) 
        self.play(Write(alpha),Write(pi))

        self.remove(l1,l2,l3)

        l1, l2, l3 = self.create_head_tracer(v1, v2, v3)
   
        

        self.wait(1)        
        self.play(Rotating(v1,radians=2 * PI,about_point= ORIGIN),
        Rotating(v2,radians=2 * PI,about_point= ORIGIN),
        Rotating(v3,radians=2 * PI,about_point= ORIGIN),
        alpha.tracker.animate.set_value(2),run_time = 6)
        self.wait(2)

        beta = Variable(1, r"\beta").move_to(alpha)
        self.play(TransformMatchingShapes(alpha,beta),FadeOut(pi))
        self.remove(alpha,pi)
        self.add(beta)

        
        factor1 = 2.5
        sv1,sv2,sv3 = map(lambda x: self.stretch_vector(x,factor1), [v1,v2,v3])

        
        self.play(Transform(v1,sv1),
                Transform(v2,sv2),
                Transform(v3,sv3),
                beta.tracker.animate.set_value(factor1),run_time = 6)

        self.remove(v1,v2,v3,l1,l2,l3)
        v1,v2,v3 = sv1,sv2,sv3
        factor2 = -1.7
        sv1,sv2,sv3 = map(lambda x: self.stretch_vector(x,factor2/factor1), [v1,v2,v3])

        
        self.play(Transform(v1,sv1),
                Transform(v2,sv2),
                Transform(v3,sv3),
                beta.tracker.animate.set_value(factor2),run_time = 6)

        alpha.tracker.set_value(0)
        alpha.next_to(beta,RIGHT)
        pi.next_to(alpha, RIGHT).shift(LEFT *.1) 
        
        self.play(FadeOut(v1,v2,v3,sv1,sv2,sv3,beta))
        beta.tracker.set_value(1)
        v1, v2, v3, l1,l2,l3 = self.start_situation()

        self.play(Write(alpha),Write(beta),Write(pi))
        self.play(FadeOut(l1,l2,l3))

        degree = .5
        factor = 1.5

        sv1,sv2,sv3 = map(lambda x: self.all_at_once(x,factor,degree), [v1,v2,v3])
        self.play(Transform(v1,sv1),
                Transform(v2,sv2),
                Transform(v3,sv3),
                beta.tracker.animate.set_value(factor),
                alpha.tracker.animate.set_value(degree),
                 run_time = 6)

        l1 = self.label_vector(sv2,MathTex("\\hat{a}"),animate=False)
        self.wait(2)

    def create_head_tracer(self, v1, v2, v3):
        l1 = self.label_vector(vector=v1,label=MathTex(r"\hat{a}"))
        l2 = self.label_vector(vector=v2,label=MathTex(r"\hat{b}"))
        l3 = self.label_vector(vector=v3,label=MathTex(r"\hat{v}"))

        self.play(l1.animate.move_to([v1.get_end()[0]*1.2,v1.get_end()[1]*1.2,v1.get_end()[2]]),
        l2.animate.move_to([v2.get_end()[0]*1.2,v2.get_end()[1]*1.2,v2.get_end()[2]]),
        l3.animate.move_to([v3.get_end()[0]*1.2,v3.get_end()[1]*1.2,v3.get_end()[2]]))


        l1.add_updater(lambda d: d.move_to([v1.get_end()[0]*1.2,v1.get_end()[1]*1.2,v1.get_end()[2]]))
        l2.add_updater(lambda d: d.move_to([v2.get_end()[0]*1.2,v2.get_end()[1]*1.2,v2.get_end()[2]]))
        l3.add_updater(lambda d: d.move_to([v3.get_end()[0]*1.2,v3.get_end()[1]*1.2,v3.get_end()[2]]))
        return l1,l2,l3

    def start_situation(self):
        v1 = self.add_vector([1,0],color = YELLOW)
        l1 = self.label_vector(vector=v1,label=MathTex(r"a"))
        c1 = v1.coordinate_label()
        self.add(c1)
        self.wait(1)
        self.remove(c1)
        v2 = self.add_vector([0,1],color = GREEN)
        l2 = self.label_vector(vector=v2,label=MathTex(r"b"))
        c2 = v2.coordinate_label()
        self.add(c2)
        self.wait(1)
        self.remove(c2)
        v3 = self.add_vector([.5,np.sqrt(3)*.5],color = BLUE)
        l3 = self.label_vector(vector=v3,label=MathTex(r"v"))
        c3 = v3.coordinate_label()
        self.add(c3)
        self.wait(1)
        self.remove(c3)
        return v1,v2,v3,l1,l2,l3

    def all_at_once(self,vector,factor,degree):
        x,y = vector.get_end()[:2]
        matrix = np.array([[np.cos(np.pi*degree),-np.sin(np.pi*degree)], [np.sin(np.pi*degree),np.cos(np.pi*degree)]])
        new = matrix @ np.array([x,y]) * factor
        
        return Vector(new,color = vector.get_color())
            


    def stretch_vector(self,vector,factor):

        new_vector = Vector([i*factor for i in vector.get_end()[:2]],color = vector.get_color())
        return new_vector


class Transform_Matrix_A(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )

    def construct(self):
        degree = 3/4
        alpha = Variable(degree, r"\alpha").shift(UP * 3,LEFT * 3.5)
        pi = Tex(r"$\cdot\pi$",font_size = 80).next_to(alpha, RIGHT).shift(LEFT *.1) 
        self.add_foreground_mobject(alpha,pi)
        matrix = [[np.cos(np.pi*degree),-np.sin(np.pi*degree)], [np.sin(np.pi*degree),np.cos(np.pi*degree)]]
        self.apply_matrix(matrix,run_time = 6)
        self.wait()


class Transform_Matrix_B(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )

    def construct(self):
        degree = -2.25
        beta = Variable(degree, r"\beta").shift(UP * 3,LEFT * 3)
        self.add_foreground_mobject(beta)
        matrix = [[degree,0],[0,degree]]
        self.apply_matrix(matrix,run_time = 6)
        self.wait()

class CosFunctionPlot(MovingCameraScene):
    def construct(self):
        axes = Axes(
            x_range=[0, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=5,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(0, 10.01, 2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        cos_graph = axes.plot(lambda x: np.cos(x), color=BLUE)
        cos_label = axes.get_graph_label(
            cos_graph, "\\cos(x)", x_val=12, direction=UP 
        )
        cop= cos_graph.copy()
        self.play(DrawBorderThenFill(axes),Write(axes_labels))
        self.play(Create(cos_graph))
        self.play(Write(cos_label))
        axes2 = Axes(
            x_range=[-10.3, 0, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=5,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10.01,0, 2),
                "numbers_with_elongated_ticks": np.arange(-10.01,0, 2),
            },
            tips=False,
        ).shift(LEFT * 5)
        self.add(cop)
        self.play(self.camera.frame.animate.set(width = 17).shift(LEFT * 2.5))
        self.play(DrawBorderThenFill(axes2))
        self.play(cop.animate.flip([0,1,0]).shift(LEFT*5))
        self.wait(2)

class SinFunctionPlot(MovingCameraScene):
    def construct(self):
        axes = Axes(
            x_range=[0, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=5,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(0, 10.01, 2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=12, direction=UP 
        )
        cop= sin_graph.copy()
        self.play(DrawBorderThenFill(axes),Write(axes_labels))
        self.play(Create(sin_graph))
        self.play(Write(sin_label))
        axes2 = Axes(
            x_range=[-10.3, 0, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=5,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10.01,0, 2),
                "numbers_with_elongated_ticks": np.arange(-10.01,0, 2),
            },
            tips=False,
        ).shift(LEFT * 5)
        self.add(cop)
        self.play(self.camera.frame.animate.set(width = 17).shift(LEFT * 2.5))
        self.play(DrawBorderThenFill(axes2))
        self.play(cop.animate.flip([0,1,0]).shift(LEFT*5).set_color(RED))
        self.wait(2)   
        self.play(cop.animate.flip([1,0,0]).set_color(GREEN))
        self.wait(2)   
      

class DotProduct(Scene):

    def construct(self):

        m1 = MathTex(r"\langle a , b \rangle")
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"\langle a , b \rangle = \lVert a \rVert \cdot \lVert b \rVert \cdot cos(\alpha)")
        self.play(Transform(m1,m2))
        self.wait(2)


class ShowDotProcuct(VectorScene):
    def construct(self):
        
        plane = self.add_plane(background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.3
            },animate=False).add_coordinates()