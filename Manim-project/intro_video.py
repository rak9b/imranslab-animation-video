from manim import *
import numpy as np
import math


# Constants
FRAME_RATE = 30
DURATION_BRANDING = 10
DURATION_INTRO = 20

# Color Palette
DARK_BLUE = "#003366"
LIGHT_BLUE = "#66CCFF"
WHITE = "#FFFFFF"
LIGHT_GRAY = "#F0F0F0"
DARK_GRAY = "#333333"
GRADIENT_COLORS = [LIGHT_BLUE, DARK_BLUE]

# ------------------------------
# Utility Functions
# ------------------------------
def animated_text(text, color=WHITE, scale=1.0):
    t = Text(text, color=color).scale(scale)
    t.set_stroke(width=0.7, color=BLACK, opacity=0.6)
    return t

def add_particles(scene, n=15, radius=0.05, color=LIGHT_BLUE):
    """Adds small floating circles for subtle particle effects."""
    particles = VGroup()
    for _ in range(n):
        x = (scene.camera.frame_width / 2) * (2 * np.random.rand() - 1)
        y = (scene.camera.frame_height / 2) * (2 * np.random.rand() - 1)
        c = Circle(radius=radius, color=color, fill_opacity=0.4, stroke_width=0)
        c.move_to([x, y, 0])
        particles.add(c)
    scene.add(particles)
    scene.play(
        LaggedStart(*[FadeIn(c, scale=0.3, run_time=1.2) for c in particles], lag_ratio=0.1),
        run_time=2
    )
    # Add floating animation
    for p in particles:
        floating_animation(p, amplitude=0.1, frequency=np.random.uniform(0.3, 0.6))
    return particles

# Floating animation helper (stable start)
def floating_animation(mobject, amplitude=0.1, frequency=0.1):
    time_tracker = ValueTracker(0)
    def updater(mob):
        t = time_tracker.get_value()
        mob.set_y(mob.initial_y + amplitude * math.sin(2 * math.pi * frequency * t))
    mobject.initial_y = mobject.get_y()
    mobject.add_updater(updater)
    mobject.time_tracker = time_tracker  # store for scene update

# ------------------------------
# Scene Classes
# ------------------------------
class OpeningBranding(Scene):
    def construct(self):
        self.camera.background_color = LIGHT_GRAY

        # Background gradient shape
        bg_rect = Rectangle(width=14, height=8, fill_color=LIGHT_BLUE, fill_opacity=0.12, stroke_opacity=0)
        floating_animation(bg_rect, amplitude=0.02, frequency=0.2)
        self.add(bg_rect)

        # Logo
        logo = ImageMobject("assets/images/imranslab_logo.png").scale(0.5)
        logo.generate_target()
        logo.target.scale(1.02).shift(UP * 0.2).rotate(0.1)

        # Slogan with gradient
        slogan = animated_text("We Are Experts In Design, App, and Developments", scale=0.9)
        slogan.set_color_by_gradient(*GRADIENT_COLORS)
        slogan.next_to(logo, DOWN)

        # Particle effects
        particles = add_particles(self, n=20)

        # Animate logo and slogan
        self.play(
            LaggedStart(
                MoveToTarget(logo, run_time=2),
                FadeIn(logo, scale=0.7),
                lag_ratio=0.2
            )
        )
        self.play(Write(slogan, run_time=2))

        # Add stable floating effect AFTER they appear
        floating_animation(logo, amplitude=0.1, frequency=0.1)
        floating_animation(slogan, amplitude=0.05, frequency=0.1)

        # Keep objects floating during branding duration
        self.wait(DURATION_BRANDING)

        # Exit animation
        self.play(
            logo.animate.scale(0.7).fade(1),
            slogan.animate.shift(UP).fade(1),
            FadeOut(particles),
            FadeOut(bg_rect),
            run_time=2
        )

class PersonalIntroduction(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Background animated circles
        bg_circles = VGroup()
        for i in range(3):
            circle = Circle(
                radius=2.5 + i, 
                color=LIGHT_BLUE, 
                fill_opacity=0.04, 
                stroke_width=1.5
            ).shift(DOWN*0.5)
            floating_animation(circle, amplitude=0.02, frequency=0.2+i*0.1)
            bg_circles.add(circle)
            self.add(circle)

        # Animated texts
        intro_text = animated_text("Hello! I'm MD.RAKIBUL ISLAM (Rakib)", color=DARK_BLUE, scale=1.3)
        fun_fact = animated_text("Fun fact: I love building web projects and exploring AI", color=DARK_GRAY, scale=0.8)
        uni_text = animated_text("I'm MERN stack devoloper", color=DARK_BLUE, scale=0.8)
        excitement = animated_text("Excited to join Imran's Lab!", color=LIGHT_BLUE, scale=1.1)

        fun_fact.next_to(intro_text, DOWN)
        uni_text.next_to(fun_fact, DOWN)
        excitement.next_to(uni_text, DOWN)

        # Entrance animations
        self.play(FadeIn(intro_text, shift=UP*0.5, scale=0.8, run_time=1.5))
        self.play(FadeIn(fun_fact, shift=RIGHT*0.5, scale=0.8, run_time=1.5))
        self.play(FadeIn(uni_text, shift=LEFT*0.5, scale=0.8, run_time=1.5))
        self.play(Write(excitement, run_time=1.8))

        # Floating animation for texts
        floating_animation(intro_text, amplitude=0.05, frequency=0.5)
        floating_animation(fun_fact, amplitude=0.03, frequency=0.7)
        floating_animation(uni_text, amplitude=0.03, frequency=0.6)
        floating_animation(excitement, amplitude=0.05, frequency=0.8)

        # Slow background rotation
        self.play(Rotate(bg_circles, angle=PI/12, run_time=DURATION_INTRO, rate_func=linear))

        # Wait
        self.wait(DURATION_INTRO)

        # Exit animations
        self.play(
            intro_text.animate.scale(0.8).shift(UP*2).fade(1),
            fun_fact.animate.shift(DOWN*2).fade(1),
            uni_text.animate.shift(DOWN*2).fade(1),
            excitement.animate.shift(UP*2).fade(1),
            FadeOut(bg_circles),
            run_time=2
        )

class ClosingBranding(Scene):
    def construct(self):
        self.camera.background_color = LIGHT_GRAY

        # Background gradient shape
        bg_rect = Rectangle(width=14, height=8, fill_color=LIGHT_BLUE, fill_opacity=0.08, stroke_opacity=0)
        floating_animation(bg_rect, amplitude=0.04, frequency=0.4)
        self.add(bg_rect)

        # Thank you text
        thank_you = animated_text("Thank you for watching!", color=DARK_BLUE, scale=1.5)
        thank_you.set_color_by_gradient(LIGHT_BLUE, DARK_BLUE)
        slogan = animated_text("Stay curious and keep learning with Imranslab", color=DARK_GRAY, scale=0.8)
        slogan.next_to(thank_you, DOWN)

        # Background floating circles
        particles = add_particles(self, n=15, radius=0.05, color=LIGHT_BLUE)

        # Entrance animations
        self.play(FadeIn(thank_you, shift=UP*0.5, scale=0.8, run_time=2))
        self.play(Write(slogan, run_time=2))

        # Floating animation
        floating_animation(thank_you, amplitude=0.05, frequency=0.5)
        floating_animation(slogan, amplitude=0.03, frequency=0.7)

        # Wait
        self.wait(DURATION_BRANDING)

        # Exit
        self.play(
            thank_you.animate.scale(0.7).fade(1),
            slogan.animate.fade(1),
            FadeOut(bg_rect),
            FadeOut(particles),
            run_time=2
        )
