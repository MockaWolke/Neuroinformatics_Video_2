from manim import *
import numpy as np

config.verbosity = "WARNING"








class ShowDotProduct(VectorScene):
    def construct(self):
        
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

        m2 = MathTex(r"\langle a , b \rangle = \lVert a \rVert \cdot \lVert b \rVert \cdot cos(\alpha)").shift(UP*3,RIGHT*3)
        self.play(Write(m2))

        angle = Angle(a,b,radius= .7)
        alpha = MathTex("\\alpha").move_to(angle)
        group = VGroup(angle,alpha)
        self.play(Write(group))
        self.wait(2)

        m1 = MathTex(r"\langle a , b \rangle = \lVert a \rVert \cdot \lVert b \rVert \cdot cos(90^\circ)").move_to(m2)
        angle = Angle(a,b,dot=True,radius= .7)
        self.play(Transform(group,angle),Transform(m2,m1))
        self.wait(2)
        self.play(Transform(m2,MathTex(r"\langle a , b \rangle = \lVert a \rVert \cdot \lVert b \rVert \cdot 0").move_to(m2)))
        self.wait(2)
        self.play(Transform(m2,MathTex(r"\langle a , b \rangle = 0").move_to(m2)))
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


class B_Reverse(Scene):
    def construct(self):

        m = MathTex(r"B_{\beta} = \begin{bmatrix} \beta & 0 \\ 0 & \beta\end{bmatrix}, b \neq 0")
        self.play(Write(m))
        self.wait(2)
        m1 = MathTex(r"B_{\beta} = \begin{bmatrix} 1\cdot  \beta & 0 \\ 0 & 1 \cdot \beta\end{bmatrix}") 
        self.play(Transform(m,m1))
        self.wait(2)
        m1 = MathTex(r"B_{\beta} = \beta \cdot \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}") 
        self.play(Transform(m,m1))
        self.wait(2)
        m1 = MathTex(r"B_{\beta} = \beta \cdot \mathit{I}_2") 
        self.play(Transform(m,m1))
        self.wait(2)
        m1 = MathTex(r"\langle B_{\beta} a , B_{\beta} b \rangle")
        self.play(Transform(m,m1))
        self.wait(2)
        m1 = MathTex(r"\langle B_{\beta} a , B_{\beta} b \rangle = \langle \beta \cdot \mathit{I}_2 a , \beta \cdot \mathit{I}_2 b \rangle")
        self.play(Transform(m,m1))
        self.wait(2)
        m1 = MathTex(r"\langle B_{\beta} a , B_{\beta} b \rangle = \langle \beta \cdot a , \beta \cdot b \rangle")
        self.play(Transform(m,m1))
        self.wait(2)
        m1 = MathTex(r"\langle B_{\beta} a , B_{\beta} b \rangle = \beta^2 \cdot \langle a , b \rangle")
        self.play(Transform(m,m1))
        self.wait(2)

        m1 = MathTex(r"B_{\beta} = \beta \cdot \mathit{I}_2") 
        self.play(Transform(m,m1))
        self.wait(2)

        m1 = MathTex(r"(B_{\beta})^{-1} =   \mathit{I}_2^{-1} \beta^{-1}") 
        self.play(Transform(m,m1))
        self.wait(2)

        m1 = MathTex(r"(B_{\beta})^{-1} =   \mathit{I}_2 \frac{1}{\beta}") 
        self.play(Transform(m,m1))
        self.wait(2)

        m1 = MathTex(r"(B_{\beta})^{-1} =  B_{\frac{1}{\beta}}") 
        self.play(Transform(m,m1))
        self.wait(2)


class A_Orthonormal(Scene):
    def construct(self):
        m = MobjectMatrix([[MathTex(r"\cos(\alpha)").scale(.7),MathTex(r"\sin(\alpha)").scale(.7)],[MathTex(r"-\sin(\alpha)").scale(.7),MathTex(r"\cos(\alpha)").scale(.7)]])
        name = MathTex(r"A_{\alpha}=").next_to(m,LEFT)
        self.play(Write(name),Write(m))
        self.wait(2)
        c1 = SurroundingRectangle(m.get_columns()[0],color=BLUE)
        self.play(Write(c1))
        self.wait(1)
        c2 = SurroundingRectangle(m.get_columns()[1])
        self.play(Write(c2))

        a = MathTex(r"\langle \begin{pmatrix} \cos(\alpha) \\ \sin(\alpha) \end{pmatrix}, \begin{pmatrix} -\sin(\alpha) \\ \cos(\alpha) \end{pmatrix} \rangle").scale(.7).shift(UP*2)
        group = VGroup(c1,c2)
        self.play(Transform(group,a))
        # self.remove(group)
        self.wait(2)
        self.play(group.animate.shift(LEFT*3))
        b = MathTex(r"= \cos(\alpha) \cdot -\sin(\alpha) + \cos(\alpha) \cdot sin(\alpha)").next_to(group,RIGHT).shift(LEFT*1.3).scale(.7)
        self.play(Write(b))
        self.wait(2)
        self.play(Transform(b,MathTex("= 0").next_to(group,RIGHT).scale(.7)))
        self.wait(2)

        self.play(FadeOut(group,b))
        self.wait(2)
        c1 = SurroundingRectangle(m.get_columns()[0],color=BLUE)
        self.play(Write(c1))

        a = MathTex(r"\lvert\lvert \begin{pmatrix} \cos(\alpha) \\ \sin(\alpha) \end{pmatrix} \rvert\rvert = \langle \begin{pmatrix} \cos(\alpha) \\ \sin(\alpha) \end{pmatrix},\begin{pmatrix} \cos(\alpha) \\ \sin(\alpha) \end{pmatrix} \rangle").scale(.7).shift(UP*2)

        self.play(Transform(c1,a))
        self.wait(2)
        self.play(c1.animate.shift(4 * LEFT))
        b = MathTex(r"= \cos(\alpha)^2 + \sin(\alpha)^2").scale(.7).next_to(c1,RIGHT)
        self.play(Write(b))
        c = MathTex(r"= 1").next_to(b,RIGHT).scale(.7)

        self.play(Write(c))
        self.wait(2)


class A_Reverse(Scene):
    def construct(self):
        
        name = MathTex(r"(A_{\alpha})^{-1}=").shift(LEFT)
        self.play(Write(name))
        self.wait(2)
        inverse = MathTex(r"A_{\alpha}^T").next_to(name)
        self.play(Write(inverse))
        self.wait(2)
        self.play(Transform(inverse,MobjectMatrix([[MathTex(r"\cos(\alpha)").scale(.7),MathTex(r"-\sin(\alpha)").scale(.7)],[MathTex(r"\sin(\alpha)").scale(.7),MathTex(r"\cos(\alpha)").scale(.7)]]).next_to(name,RIGHT)))

        self.wait(2)

        self.clear()

        big = MathTex( r"\begin{bmatrix} cos(\alpha) & -sin(\alpha) \\ sin(\alpha) & cos(\alpha)\end{bmatrix} \cdot  \begin{bmatrix} cos(\alpha) & sin(\alpha) \\ -sin(\alpha) & cos(\alpha)\end{bmatrix} ").shift(LEFT*4).scale(0.6)
        self.play(Write(big))
        bigr = MathTex( r"=\begin{bmatrix} cos(\alpha)^2 + sin(\alpha)^2  & \cos(\alpha) sin(\alpha) - \cos(\alpha)sin(\alpha) \\ \cos(\alpha) sin(\alpha) - \cos(\alpha)sin(\alpha) & \cos(\alpha)^2+  sin(\alpha)^2\end{bmatrix} ").next_to(big,RIGHT).scale(0.6).shift(LEFT*2.8)
        self.play(Write(bigr))

        self.play(Transform(bigr,MathTex(r"= \begin{bmatrix} 1 &0 \\ 1 & 0\end{bmatrix}").scale(0.6).next_to(big,RIGHT)))
        self.wait(2)

        self.clear()
        name = MathTex(r"(A_{\alpha})^{-1}=").shift(LEFT)
        self.play(Write(name))
        m = MathTex(r"\begin{bmatrix} cos(\alpha) & sin(\alpha) \\ -sin(\alpha) & cos(\alpha)\end{bmatrix}").scale(.6).next_to(name,RIGHT)
        self.play(Write(m))
        self.wait(2)
        cos_rule = MathTex(r"\cos(\alpha) = \cos(-\alpha)").shift(UP*2,LEFT*3).scale(0.6)
        self.play(Write(cos_rule))
        self.wait(2)

        self.play(Transform(m,MathTex(r"\begin{bmatrix} cos(-\alpha) & sin(\alpha) \\ -sin(\alpha) & cos(-\alpha)\end{bmatrix}").scale(.6).next_to(name,RIGHT)))

        sin_rule = MathTex(r"\sin(\alpha) = -\sin(-\alpha)").shift(UP*2,RIGHT*3).scale(0.6)
        self.play(Write(sin_rule))

        self.wait(2)

        self.play(Transform(m,MathTex(r"\begin{bmatrix} cos(-\alpha) & -sin(-\alpha) \\ sin(-\alpha) & cos(-\alpha)\end{bmatrix}").scale(.6).next_to(name,RIGHT)))

        self.wait(2)
        self.play(name.animate.shift(LEFT*2),m.animate.shift(LEFT*2))
        sol = MathTex(r"= A_{-\alpha}").next_to(m,RIGHT)
        self.play(Write(sol))
        self.wait(2)