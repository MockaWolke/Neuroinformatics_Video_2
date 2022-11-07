from manim import *
import numpy as np

config.verbosity = "WARNING"








class ShowDotProduct(VectorScene):
    def construct(self):
        

        head = Tex(r"Angle Preserving Matrices").shift(UP*2)
        self.play(Write(head))
        m1 = MathTex(r"\langle a , b \rangle")
        self.play(Write(m1))
        self.wait(2)
        self.play(m1.animate.shift(LEFT * 2))
        m2 = MathTex(r"= \lVert a \rVert \cdot \lVert b \rVert \cdot cos(\alpha)").next_to(m1,RIGHT)
        self.play(Write(m2))
        self.wait(2)
        
        self.play(FadeOut(head,m1,m2))

        plane = self.add_plane(background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.3
            },animate=False).add_coordinates()

        
        a = self.add_vector([1,0],color = YELLOW)
        la = self.label_vector(a,"a")
        ca = a.coordinate_label()
        self.play(Write(ca))
        self.wait(2)
        self.play(FadeOut(la,ca))

        b = self.add_vector([0,1],color=GREEN)
        lb = self.label_vector(b,"b")
        cb = b.coordinate_label()
        self.play(Write(cb))
        self.wait(2)
        self.play(FadeOut(lb,cb))

        m1 = MathTex(r"\langle a , b \rangle = ").shift(UP*3,RIGHT*1.5)
        m2 = MathTex(r"\lVert a \rVert \cdot \lVert b \rVert \cdot ").next_to(m1,RIGHT)
        m3 = MathTex(r"cos(\alpha)").next_to(m2,RIGHT)
        self.play(Write(m1))
        self.play(Write(m2))
        self.play(Write(m3))

        angle = Angle(a,b,radius= .7)
        alpha = MathTex("\\alpha").move_to(angle)
        group = VGroup(angle,alpha)
        self.play(Write(group))
        self.wait(2)

        
        angle = Angle(a,b,dot=True,radius= .7)
        self.play(Transform(group,angle),Transform(m3, MathTex(r"cos(90^\circ)").next_to(m2,RIGHT)))
        self.wait(2)
        self.play(Transform(m3, MathTex(r"0").next_to(m2,RIGHT)))
        self.wait(2)
        m4 = MathTex(r" = 0").next_to(m3,RIGHT)
        self.play(Write(m4))
        self.wait(2)

        beta = Variable(1, r"\beta").shift(UP*3,LEFT*3)
        self.play(Write(beta))
        self.wait(2)

        self.play(Transform(a,Vector([2.5,0],color = YELLOW)),Transform(b,Vector([0,2.5],color = GREEN)),beta.tracker.animate.set_value(2.5),run_time = 3)
        self.wait(2)
        
        n1,n2 = Vector([-2.5,0],color = YELLOW),Vector([0,-2.5],color = GREEN)
        angle2=Angle(n1,n2,radius = 0.7,dot=True)
        self.play(Transform(a,n1),Transform(b,n2),Write(angle2),FadeOut(angle,group),beta.tracker.animate.set_value(-2.5),run_time = 3)
        self.wait(2)
        self.play(FadeOut(beta))

        group = VGroup(a,b,angle2)
        self.play(Rotating(group,radians=1 * PI,about_point=ORIGIN))
        self.wait(2)


class B_Reverse(MovingCameraScene):
    def construct(self):

        old = MathTex(r"B_{\beta} = \begin{pmatrix} \beta & 0 \\ 0 & \beta\end{pmatrix}, b \neq 0").move_to([0,2,0])
        self.play(Write(old))
        self.wait(2)
        
        m = MathTex(r"B_{\beta} = \begin{pmatrix} 1\cdot  \beta & 0 \\ 0 & 1 \cdot \beta\end{pmatrix}").align_to(old,LEFT)
        self.play(Write(m))
        self.wait(2)
        self.play(m.animate.shift(1.5*LEFT))
        m1 = MathTex(r"= \beta \cdot \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}").next_to(m,RIGHT) 
        self.play(Write(m1))
        self.wait(2)

        formula = VGroup(m,m1)
        self.play(formula.animate.shift(1.5*LEFT))
        m2 = MathTex(r"= \beta \cdot \mathit{I}_2").next_to(formula,RIGHT) 
        self.play(Write(m2))

        formula = formula.add(m2)



        self.wait(2)
        new = MathTex(r"\langle B_{\beta} a , B_{\beta} b \rangle").shift(RIGHT * 15)
        self.add(new)

        self.play(self.camera.frame.animate.move_to(new))
        self.wait(2)

        self.play(new.animate.shift(LEFT * 2))
        new1 = MathTex(r"= \langle \beta \cdot \mathit{I}_2 a , \beta \cdot \mathit{I}_2 b \rangle").next_to(new,RIGHT)
        self.play(Write(new1))
        self.wait(2)
        group_new = VGroup(new,new1)
        self.play(group_new.animate.shift(LEFT * 2))
        new2 = MathTex(r"= \langle \beta \cdot a , \beta \cdot b \rangle").next_to(group_new,RIGHT)
        self.play(Write(new2))
        self.wait(2)
        group_new = group_new.add(new2)
        self.play(group_new.animate.shift(LEFT))
        new3 = MathTex(r"= \beta^2 \cdot \langle a , b \rangle").next_to(group_new,RIGHT)
        self.play(Write(new3))
        self.wait(2)

        group_new = group_new.add(new3)
        self.play(Transform(group_new,MathTex(r"\langle B_{\beta} a , B_{\beta} b \rangle = \beta^2 \cdot \langle a , b \rangle").shift(RIGHT * 15)))

        self.wait(2)

        self.play(self.camera.frame.animate.move_to(ORIGIN))
        self.wait(2)
        self.play(Transform(formula, MathTex(r"B_{\beta} = \beta \cdot \mathit{I}_2") ))

        self.wait(2)

        inverse = MathTex(r"(B_{\beta})^{-1} =").shift(DOWN * 2,LEFT * 1) 
        change = MathTex("?").next_to(inverse,RIGHT)
        self.play(Write(inverse),Write(change))
        self.wait(2)
        m1 = MathTex(r"(\beta \cdot \mathit{I}_2)^{-1}").next_to(inverse,RIGHT) 
        self.play(Transform(change,m1))

        self.wait(2)
        inverse_group = VGroup(inverse,change)
        self.play(inverse_group.animate.shift(LEFT))
        m1 = MathTex(r"= \frac{1}{\beta}\cdot\mathit{I}_2").next_to(inverse_group,RIGHT)
        self.play(Write(m1))
        self.wait(2)
        inverse_group.add(m1)
        self.play(inverse_group.animate.shift(LEFT))
        m1 = MathTex(r"=  B_{\frac{1}{\beta}}").next_to(inverse_group,RIGHT)
        self.play(Write(m1))
        self.wait(2)

class A_Orthogonal(Scene):
    def construct(self):
        m = MobjectMatrix([[MathTex(r"\cos(\alpha)").scale(.7),MathTex(r"\sin(\alpha)").scale(.7)],[MathTex(r"-\sin(\alpha)").scale(.7),MathTex(r"\cos(\alpha)").scale(.7)]])
        name = MathTex(r"A_{\alpha}=").next_to(m,LEFT)
        ortho = Tex("Orthogonal Matrix").shift(UP *2)

        self.play(Write(name),Write(m))
        self.wait(2)

        self.play(Write(ortho))
        self.wait(2)

        self.play(m.animate.shift(DOWN * 2),name.animate.shift(DOWN * 2))

        c1 = SurroundingRectangle(m.get_columns()[0],color=BLUE)
        self.play(Write(c1))
        self.wait(1)
        c2 = SurroundingRectangle(m.get_columns()[1])
        self.play(Write(c2))

        a = MathTex(r"\langle \begin{pmatrix} \cos(\alpha) \\ \sin(\alpha) \end{pmatrix}, \begin{pmatrix} -\sin(\alpha) \\ \cos(\alpha) \end{pmatrix} \rangle").scale(.7)
        group = VGroup(c1,c2)
        self.play(Transform(group,a))

        self.wait(2)
        self.play(group.animate.shift(LEFT*3))
        b = MathTex(r"= \cos(\alpha) \cdot -\sin(\alpha) + \cos(\alpha) \cdot sin(\alpha)").scale(.7).next_to(group,RIGHT) 
        self.play(Write(b))
        self.wait(2)
        self.play(group.animate.shift(LEFT*0.2),b.animate.shift(LEFT*0.2))
        c = MathTex("= 0").scale(.7).next_to(b,RIGHT)
        self.play(Write(c))
        self.wait(2)

        self.play(FadeOut(group,b,c))
        self.wait(2)
        c1 = SurroundingRectangle(m.get_columns()[0],color=BLUE)
        self.play(Write(c1))

        a = MathTex(r"\lvert\lvert \begin{pmatrix} \cos(\alpha) \\ \sin(\alpha) \end{pmatrix} \rvert\rvert = \sqrt{\langle \begin{pmatrix} \cos(\alpha) \\ \sin(\alpha) \end{pmatrix},\begin{pmatrix} \cos(\alpha) \\ \sin(\alpha) \end{pmatrix} \rangle}").scale(.7)

        self.play(Transform(c1,a))
        self.wait(2)
        self.play(c1.animate.shift(2.5 * LEFT))
        b = MathTex(r"= \sqrt{\cos(\alpha)^2 + \sin(\alpha)^2}").scale(.7).next_to(c1,RIGHT)
        self.play(Write(b))
        c = MathTex(r"= 1").next_to(b,RIGHT).scale(.7)

        self.play(Write(c))
        self.wait(2)


class A_Reverse(MovingCameraScene):
    def construct(self):
        
        title = Tex(r"Inversing $A_{\alpha}$").shift(UP*2)
        self.add(title)
        self.wait(2)
        name = MathTex(r"(A_{\alpha})^{-1}=").shift(LEFT)
        self.play(Write(name))
        self.wait(2)
        inverse = MathTex(r"A_{\alpha}^T").next_to(name)
        self.play(Write(inverse))
        self.wait(2)
        group = VGroup(name,inverse)
        self.play(group.animate.shift(LEFT * 2))

        is_even = MathTex("=").next_to(group,RIGHT)
        matrix = MathTex(r"\begin{pmatrix} cos(\alpha) & -sin(\alpha) \\ sin(\alpha) & cos(\alpha)\end{pmatrix} ").next_to(is_even,RIGHT)
        new_group = VGroup(is_even,matrix)

        self.play(Write(new_group))

        self.wait(2)

        rule = MathTex(r"A_{\alpha} \cdot A_{\alpha}^T = \begin{pmatrix} 1 &0 \\ 0 & 1\end{pmatrix}").move_to([19,2,0])
        self.add(rule)
        self.play(self.camera.frame.animate.shift(19*RIGHT))


        big = MathTex( r"\begin{pmatrix} cos(\alpha) & -sin(\alpha) \\ sin(\alpha) & cos(\alpha)\end{pmatrix} \cdot  \begin{pmatrix} cos(\alpha) & sin(\alpha) \\ -sin(\alpha) & cos(\alpha)\end{pmatrix} ").scale(0.7).move_to([19,0,0])
        
        self.play(Create(big))
        self.wait(2)
        og_with = self.camera.frame_width
        self.play(big.animate.next_to([19-(self.camera.frame_width*0.5)-2,0,0],RIGHT),self.camera.frame.animate.set(width=self.camera.frame_width*1.3))
        bigr = MathTex( r"=\begin{pmatrix} cos(\alpha)^2 + sin(\alpha)^2  & \cos(\alpha) sin(\alpha) - \cos(\alpha)sin(\alpha) \\ \cos(\alpha) sin(\alpha) - \cos(\alpha)sin(\alpha) & \cos(\alpha)^2+  sin(\alpha)^2\end{pmatrix} ").scale(0.7).next_to(big,RIGHT)
        self.play(Create(bigr))
        self.wait(2)
        self.play(Transform(bigr,MathTex( r"=\begin{pmatrix} 1 & \cos(\alpha) sin(\alpha) - \cos(\alpha)sin(\alpha) \\ \cos(\alpha) sin(\alpha) - \cos(\alpha)sin(\alpha) & 1\end{pmatrix} ").scale(0.7).next_to(big,RIGHT)))
        self.wait(2)
        self.play(Transform(bigr,MathTex(r"= \begin{pmatrix} 1 &0 \\ 0 & 1\end{pmatrix}").scale(0.7).next_to(big,RIGHT)))
        self.wait(2)

       
        name = MathTex(r"(A_{\alpha})^{-1}=").move_to([35,0,0]).shift(LEFT*1.5)
        self.add(name)
        self.play(self.camera.frame.animate.set(width = og_with).move_to([35,0,0]))

        self.wait(2)
        self.play(name.animate.shift(LEFT*1.5))
        m = MathTex(r"\begin{pmatrix} cos(\alpha) & sin(\alpha) \\ -sin(\alpha) & cos(\alpha)\end{pmatrix}").next_to(name,RIGHT)
        self.play(Write(m))
        self.wait(2)
        cos_rule = MathTex(r"\cos(\alpha) = \cos(-\alpha)").move_to(name).shift(UP*2,LEFT*1.5)
        self.play(Write(cos_rule))
        self.wait(2)

        # cos part


        self.play(self.camera.frame.animate.shift(UP*20))

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
        ).move_to([35,20,0])
        axes_labels = axes.get_axis_labels()
        cos_graph = axes.plot(lambda x: np.cos(x), color=BLUE)
        cos_label = axes.get_graph_label(
            cos_graph, "\\cos(x)", x_val=12, direction=UP 
        ).move_to([35,23,0])
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
        ).move_to([35,20,0]).shift(LEFT * 5)
        self.add(cop)
        self.play(self.camera.frame.animate.set(width = 17).shift(LEFT * 2.5))
        self.play(DrawBorderThenFill(axes2))
        self.play(cop.animate.flip([0,1,0]).shift(LEFT*5))
        self.wait(2)

        self.play(self.camera.frame.animate.set(width = og_with).move_to([35,0,0]))
        self.remove(axes,axes2,axes_labels,cos_graph,cos_label,cop)

        self.wait(2)
        self.play(Transform(m,MathTex(r"\begin{pmatrix} cos(-\alpha) & sin(\alpha) \\ -sin(\alpha) & cos(-\alpha)\end{pmatrix}").next_to(name,RIGHT)))

        sin_rule = MathTex(r"\sin(\alpha) = -\sin(-\alpha)").move_to([35,0,0]).shift(UP*2,RIGHT*4.5)
        self.play(Write(sin_rule))

        self.wait(2)

        # sin 
        self.play(self.camera.frame.animate.shift(UP*20))
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
        ).move_to([35,20,0])
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=12, direction=UP ).move_to([35,23,0])
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
        ).move_to([35,20,0]).shift(LEFT * 5)
        self.add(cop)
        self.play(self.camera.frame.animate.set(width = 17).shift(LEFT * 2.5))
        self.play(DrawBorderThenFill(axes2))
        self.play(cop.animate.flip([0,1,0]).shift(LEFT*5).set_color(RED))
        self.wait(2)   
        self.play(cop.animate.flip([1,0,0]).set_color(GREEN))
        self.wait(2)

        self.play(self.camera.frame.animate.set(width = og_with).move_to([35,0,0]))
        self.remove(axes,axes2,axes_labels,sin_graph,sin_label,cop)

        self.wait(2)
        self.play(Transform(m,MathTex(r"\begin{pmatrix} cos(-\alpha) & -sin(-\alpha) \\ sin(-\alpha) & cos(-\alpha)\end{pmatrix}").next_to(name,RIGHT)))
        self.wait(2)

        self.play(self.camera.frame.animate.move_to(ORIGIN))
        self.play(Transform(new_group,MathTex(r"= \begin{pmatrix} cos(-\alpha) & -sin(-\alpha) \\ sin(-\alpha) & cos(-\alpha)\end{pmatrix}").next_to(group,RIGHT)))
        group = group.add(new_group)

        self.wait(2)
        self.play(group.animate.shift(LEFT*1.5))
        sol = MathTex(r"= A_{-\alpha}").next_to(group,RIGHT)
        self.play(Write(sol))
        self.wait(2)


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
   
        vectors = VGroup(v1,v2,v3)     

        self.wait(1)        
        self.play(Rotating(vectors,radians=2 * PI,about_point= ORIGIN),
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
        self.wait(2)
        alpha.tracker.set_value(0)
        alpha.next_to(beta,RIGHT)
        pi.next_to(alpha, RIGHT).shift(LEFT *.1) 
        
        self.play(FadeOut(v1,v2,v3,sv1,sv2,sv3,beta))
        beta.tracker.set_value(1)
        v1, v2, v3, l1,l2,l3 = self.start_situation(show_labels = False,animate_labeling = False)
        self.wait(2)
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

    def start_situation(self,show_labels = True,animate_labeling = True):
        v1 = self.add_vector([1,0],color = YELLOW,animate=animate_labeling)
        
        l1 = self.label_vector(vector=v1,label=MathTex(r"a"),animate=animate_labeling)
        if show_labels: 
            c1 = v1.coordinate_label()
            self.add(c1)
            self.wait(1)
            self.remove(c1)
        v2 = self.add_vector([0,1],color = GREEN,animate=animate_labeling)
        l2 = self.label_vector(vector=v2,label=MathTex(r"b"),animate=animate_labeling)
        if show_labels: 
            c2 = v2.coordinate_label()
            self.add(c2)
            self.wait(1)
            self.remove(c2)

        v3 = self.add_vector([.5,np.sqrt(3)*.5],color = BLUE,animate=animate_labeling)
        l3 = self.label_vector(vector=v3,label=MathTex(r"v"),animate=animate_labeling)
        if show_labels:
            c3 = MathTex(r"\begin{bmatrix} \frac{1}{2} \\ \frac{\sqrt{3}}{2} \end{bmatrix} ").move_to([1.5,1.5,0])
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
        self.wait(2)
        formula2 = MathTex(r"""\hat{a} = \begin{bmatrix} 0 & -1 \\ 1 & 0\end{bmatrix} \cdot a""").move_to(formula)
        self.play(Transform(formula,formula2))
        
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

        formula2 = MathTex(r"""\hat{a} = \begin{bmatrix} \sqrt{2} &  \\ 0 & \sqrt{2}\end{bmatrix} \cdot \begin{bmatrix} 0 & -1 \\ 1 & 0\end{bmatrix} \cdot a""").move_to(formula).shift(RIGHT*0.3)
        self.play(Transform(formula,formula2))
        self.wait(2)

        formula2 = MathTex(r"""\hat{a} = \begin{bmatrix} 0 & -\sqrt{2}  \\ \sqrt{2} & 0\end{bmatrix} \cdot a""").move_to(formula)
        self.play(Transform(formula,formula2))
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


    


    def start_situation(self,show_labels = True,animate_labeling = True):
        v1 = self.add_vector([1,0],color = YELLOW,animate=animate_labeling)
        
        l1 = self.label_vector(vector=v1,label=MathTex(r"a"),animate=animate_labeling)
        if show_labels: 
            c1 = v1.coordinate_label()
            self.add(c1)
            self.wait(1)
            self.remove(c1)
        v2 = self.add_vector([0,1],color = GREEN,animate=animate_labeling)
        l2 = self.label_vector(vector=v2,label=MathTex(r"b"),animate=animate_labeling)
        if show_labels: 
            c2 = v2.coordinate_label()
            self.add(c2)
            self.wait(1)
            self.remove(c2)

        v3 = self.add_vector([.5,np.sqrt(3)*.5],color = BLUE,animate=animate_labeling)
        l3 = self.label_vector(vector=v3,label=MathTex(r"v"),animate=animate_labeling)
        if show_labels:
            c3 = MathTex(r"\begin{bmatrix} \frac{1}{2} \\ \frac{\sqrt{3}}{2} \end{bmatrix} ").move_to([1.5,1.5,0])
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


class Test(VectorScene):
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
    
        nums = 100
        ar = np.linspace(0,2,num = nums)
        self.play(Transform(formula,self.get_matrix(0)))
        
        self.wait(1)

        for val in ar:
            self.play(alpha.tracker.animate.set_value(val),
            Rotating(vector2,radians=2 * PI / nums,about_point= ORIGIN),
            Transform(formula,self.get_matrix(val)),
            run_time = 6/nums)
        self.wait(2)

    def get_matrix(self,alpha):

        vals = [np.cos(np.pi*alpha),-np.sin(np.pi*alpha),np.sin(np.pi*alpha),np.cos(np.pi*alpha)]
        vals = np.round(vals,decimals=2)

        matrix = MathTex(r"""\begin{bmatrix} cos(%s) & -sin(%s) \\ sin(%s) & cos(%s)\end{bmatrix}"""% (vals[0],vals[1],vals[2],vals[3])).shift(UP * 3) 
        return matrix