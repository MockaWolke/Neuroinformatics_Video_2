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

class A_Orthonormal(Scene):
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
