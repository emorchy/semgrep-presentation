# flake8: noqa: F403, F405
# type: ignore

from manim_slides import Slide, ThreeDSlide
from manim_slides.slide import MANIM, MANIMGL

if MANIM:
    from manim import *
elif MANIMGL:
    from manimlib import *


class Semgrep(Slide):
    def Intro(self):
            #new title: semgrep github readme first part
            #table of contents: what is semgrep, semgrep in multiple languages, semgrep with variable recognition, multiple semgrep patterns, taint analysis
            #explain what semgrep is: semantic-grep
            #explain how 1+1 = 2 and x+1 is caught by semgrep but not grep
            #
            TITLE = Tex("Automated Bug Hunting with Semgrep")
            self.play(Write(TITLE))
            self.wait()
            self.next_slide()
            self.play(FadeOut(TITLE))
            ######### whoami ###############
            whoami = Title(f"whoami", color=ORANGE)
            ssr_logo = ImageMobject("ssr-logo.png").scale(0.25).shift(DOWN*2)
            name = Tex("Ethan Morchy",color=ORANGE).scale(1.5).shift(UP*2)
            occupation = Tex("Hardware/Software Penetration Tester",color=ORANGE).scale(1.25).next_to(name,DOWN)
            quote = Tex(r"Enjoys techno, sci-fi, and cool projects",color=ORANGE).next_to(occupation,DOWN*2)
            self.play(FadeIn(ssr_logo), Write(name), Write(occupation), Write(whoami), Write(quote))
            #self.play(Write(name), Write(occupation), Write(whoami))
            self.wait()
            self.next_slide()
            self.play(*[FadeOut(mob) for mob in self.mobjects])

            ############# TITLE ##############
            title = Title(f"Semgrep")

            ####### TOC ######
            toc = Tex(r"""\begin{itemize}
                      \item What is Semgrep?
                      \item How does Semgrep?
                      \item Usage
                      \begin{itemize}
                      \item Variable Recognition
                      \item Patterns
                      \item Metavariables
                      \end{itemize}
                      \item Semgrep Pro
                      \begin{itemize}
                      \item Taint analysis
                      \end{itemize}
                      \item Best Practices
                      \end{itemize}""").scale(0.75).shift(DOWN*0.5)
            self.play(FadeIn(toc,title))
            self.wait()
            self.remove(toc)
            self.next_slide()

            ############# What is Semgrep ############
            self.remove(title)
            title = Title(f"What is Semgrep?")
            self.add(title)
            logo = SVGMobject(file_name="semgrep-logo-dark.svg").scale(0.75).shift(UP*1)
            slogan = Text("Code scanning at ludicrous speed.").shift(DOWN*1)
            self.play(DrawBorderThenFill(logo), Write(slogan))
            self.wait()
            self.next_slide()
            self.play(FadeOut(logo,slogan))

            #### Grep and semgrep
            name = Tex("Sem","grep").scale(2)
            name[0].set_color(BLUE)
            name[1].set_color(GREEN)
            split = Tex("Semantic", " grep").scale(2)
            split[0].set_color(BLUE)
            split[1].set_color(GREEN)
            #self.play(Transform(title[0],name))
            self.play(Write(name))
            self.wait()
            self.next_slide()
            self.play(ReplacementTransform(name,split))
            self.wait()
            self.next_slide()
            ########### Grep Title #############
            self.play(Unwrite(split[0]))
            #split = split[1]
            self.play(split[1].animate.move_to(UP*2).scale(0.5))
            ul = Underline(split[1], color=GREEN)
            self.play(Create(ul))
            self.wait()
            self.next_slide()
            ######### Grep Code Example #############
            code_c = '''
            int main(){
                int x = 1;
                int y = 2;
                int z = x + 1;
            }'''
            rendered_code = Code(code=code_c, tab_width=4, language="C")
            rendered_code.code = remove_invisible_chars(rendered_code.code)
            self.play(Write(rendered_code))
            self.wait()
            self.next_slide()

            grep_title = Tex("grep 2",color=GREEN).shift(UP*2)
            grep_title_ul = Underline(grep_title, color=GREEN)
            self.play(ReplacementTransform(split[1],grep_title),ReplacementTransform(ul,grep_title_ul))
            grect = SurroundingRectangle(rendered_code.code[2][-2], buff=0.02)
            self.play(Create(grect.set_color(GREEN)))
            self.wait()
            self.next_slide()
            
            semgrep_c = Tex("semgrep -e 2 -l c ",color=BLUE).shift(UP*2)
            sem_ul_c = Underline(semgrep_c, color=BLUE)
            self.play(ReplacementTransform(grep_title,semgrep_c), ReplacementTransform(grep_title_ul, sem_ul_c))
            brect1 = SurroundingRectangle(rendered_code.code[2][-2], buff=0.05) 
            self.play(Create(brect1.set_color(BLUE)))
            brect2 = SurroundingRectangle(rendered_code.code[3][-4:-1], buff=0.05) 
            self.play(Create(brect2.set_color(BLUE)))
            self.wait()
            self.next_slide()

            ############# Python #############
            code_py = '''
            def test(self):
                x = 1
                y = 22
                z = x + 1'''
            semgrep_py = Tex("semgrep -e 2 -l py",color=BLUE).shift(UP*2)
            sem_ul_py = Underline(semgrep_py, color=BLUE)
            rendered_code_py = Code(code=code_py, tab_width=4, language="Python")
            rendered_code_py.code = remove_invisible_chars(rendered_code_py.code)
            #grect_py_1 = SurroundingRectangle(rendered_code_py.code[2][-1], buff=0.02,color=GREEN) 
            #grect_py_2 = SurroundingRectangle(rendered_code_py.code[2][-2], buff=0.02,color=GREEN) 
            #brect1_py = SurroundingRectangle(rendered_code_py.code[2][-1], buff=0.05,color=BLUE) 
            brect2_py = SurroundingRectangle(rendered_code_py.code[3][-3:], buff=0.05,color=BLUE) 
            #self.play(ReplacementTransform(semgrep_c,semgrep_py), ReplacementTransform(sem_ul_c, sem_ul_py), ReplacementTransform(rendered_code, rendered_code_py), ReplacementTransform(brect1,brect1_py),ReplacementTransform(brect2,brect2_py),ReplacementTransform(grect,grect_py))
            #self.play(ReplacementTransform(semgrep_c,semgrep_py), ReplacementTransform(sem_ul_c, sem_ul_py), ReplacementTransform(rendered_code, rendered_code_py), FadeOut(brect1),ReplacementTransform(brect2,brect2_py),ReplacementTransform(grect,grect_py_1), FadeIn(grect_py_2))
            self.play(ReplacementTransform(semgrep_c,semgrep_py), ReplacementTransform(sem_ul_c, sem_ul_py), ReplacementTransform(rendered_code, rendered_code_py), FadeOut(brect1),ReplacementTransform(brect2,brect2_py),FadeOut(grect))
            self.wait()
            self.next_slide()

            ########### Go #############
            code_go = '''
            func main() {
                var x int = 1
                var y int = 2
                var z int = (((x + 1) * 4) - 3 / 1) % 3
            }'''
            semgrep_go = Tex("semgrep -e 2 -l go",color=BLUE).shift(UP*2)
            sem_ul_go = Underline(semgrep_go, color=BLUE)
            rendered_code_go = Code(code=code_go, tab_width=4, language="Go")
            rendered_code_go.code = remove_invisible_chars(rendered_code_go.code)
            #grect_go = SurroundingRectangle(rendered_code_go.code[2][-1], buff=0.02,color=GREEN) 
            brect1_go = SurroundingRectangle(rendered_code_go.code[2][-1], buff=0.05,color=BLUE) 
            brect2_go = SurroundingRectangle(rendered_code_go.code[3][-17:], buff=0.05,color=BLUE) 
            #self.play(ReplacementTransform(semgrep_py,semgrep_go), ReplacementTransform(sem_ul_py, sem_ul_go), ReplacementTransform(rendered_code_py, rendered_code_go), FadeIn(brect1_go),ReplacementTransform(brect2_py,brect2_go),ReplacementTransform(grect_py_1,grect_go), FadeOut(grect_py_2))
            self.play(ReplacementTransform(semgrep_py,semgrep_go), ReplacementTransform(sem_ul_py, sem_ul_go), ReplacementTransform(rendered_code_py, rendered_code_go), FadeIn(brect1_go),ReplacementTransform(brect2_py,brect2_go))
            self.wait()
            self.next_slide()
            self.play(*[FadeOut(mob) for mob in self.mobjects])
            with register_font("cursive.ttf"):
                self.play(Write(Text("Demo Time!",font="cursive").scale(3)))
            self.wait()
            self.next_slide()

            ############## List all Languages #########
            #self.play(FadeOut(sem_ul,brect1_py,brect2_py,grect_py,rendered_code_py,semgrep))
            self.play(*[FadeOut(mob) for mob in self.mobjects])
            title = Title(f"Supported Languages")
            self.play(FadeIn(title))
            languages_1 = Tex(r"""\begin{itemize}
                                \item C
                                \item C++
                                \item C\#
                                \item Go
                                \item Java
                                \item JavaScript
                                \item Kotlin
                                \item Python
                                \item TypeScript
                                \item Ruby
                            \end{itemize}""").scale(0.5).shift(LEFT*3)
            languages_2 = Tex(r"""\begin{itemize}
                                \item Rust
                                \item JSX
                                \item PHP
                                \item Scala
                                \item Swift
                                \item Generic
                                \item JSON
                                \item Terraform
                                \item Apex
                                \item Elixir
                            \end{itemize}""").scale(0.5).shift(LEFT*1)
            languages_exp_1 = Tex(r"""\begin{itemize}
                                \item Bash
                                \item Cairo
                                \item Clojure
                                \item Dart
                                \item Dockerfile
                                \item Hack
                                \item HTML
                                \item Jsonnet
                                \item Julia
                                \item Lisp
                            \end{itemize}""").scale(0.5).shift(RIGHT*1)
            languages_exp_2 = Tex(r"""\begin{itemize}
                                \item Lua
                                \item Ocaml
                                \item R
                                \item Scheme
                                \item Solidity
                                \item YAML
                                \item XML
                            \end{itemize}""").scale(0.5).shift(RIGHT*3)
            languages = Group(languages_1,languages_2,languages_exp_1,languages_exp_2)
            self.play(FadeIn(languages))
            #self.play(Write(languages))
            self.wait()
            self.next_slide()
            self.play(*[FadeOut(mob) for mob in self.mobjects])

    def Semgrep_example(self):
            ############# Example Code ##############
            title = Title(f"What is Semgrep?")
            self.add(title)
            code1 = '''
            int main(){
                str x = "Hello";
                printf(x);
            }'''
            rendered_code_1 = Code(code=code1, tab_width=4, language="C")
            rendered_code_1.code = remove_invisible_chars(rendered_code_1.code)
            code2 = '''
            int main(){
                str x = "Hello";
                str y = "Hello";
                printf(x);
                printf(y);
            }'''
            rendered_code_2 = Code(code=code2, tab_width=4, language="C").shift(LEFT*3)
            rendered_code_2.code = remove_invisible_chars(rendered_code_2.code)
            example_text = Tex("Example Code").shift(UP*2)
            example_ul = Underline(example_text)
            self.play(FadeIn(example_text, example_ul), Write(rendered_code_1))
            left_group = Group(rendered_code_1, example_text, example_ul)
            self.wait()
            self.next_slide()

            ############# Grep Rule 1 ################
            grep_rule_1 = '''grep printf(x) '''
            rendered_grep_rule_1 = Code(code=grep_rule_1, language='bash',insert_line_no=False).shift(RIGHT*3)
            grep_title = Tex("Grep"," Rule").shift(RIGHT*3,UP*2)
            grep_ul = Underline(grep_title)
            self.play(left_group.animate.shift(LEFT*3))
            self.play(FadeIn(grep_title, grep_ul), Write(rendered_grep_rule_1))
            rect = SurroundingRectangle(rendered_code_1.code[2], buff=0.01) #printf(x);
            self.play(FadeIn(rect.set_fill(YELLOW).set_opacity(0.2)))
            self.wait()
            self.next_slide()
            # New code
            self.play(ReplacementTransform(rendered_code_1, rendered_code_2), FadeOut(rect))
            rectx = SurroundingRectangle(rendered_code_2.code[3], buff=0.01) #printf(x);
            self.play(FadeIn(rectx.set_fill(YELLOW).set_opacity(0.2)))
            self.wait()
            self.next_slide()

            ############# Grep Rule 2 ################
            grep_rule_2 = '''grep printf(.*)'''
            rendered_grep_rule_2 = Code(code=grep_rule_2, language='bash',insert_line_no=False).shift(RIGHT*3)
            self.play(ReplacementTransform(rendered_grep_rule_1.code,rendered_grep_rule_2.code), ReplacementTransform(rendered_grep_rule_1, rendered_grep_rule_2))
            #self.remove(rendered_grep_rule_2)
            recty = SurroundingRectangle(rendered_code_2.code[4], buff=0.01) #printf(x);
            self.play(FadeIn(recty.set_fill(YELLOW).set_opacity(0.2)))
            self.wait()
            self.next_slide()

            ############# Semgrep Rule ##############
            rule_code_1 = '''
            rules:
              - id: example_rule
                patterns:

              message: Rule found!
              languages: [c]
              severity: WARNING'''
            rendered_rule_code_1 = Code(code=rule_code_1, tab_width=2, language="yaml", insert_line_no=False).shift(RIGHT*3)
            rendered_rule_code_1.code = remove_invisible_chars(rendered_rule_code_1.code)
            rule_title = Tex("Semgrep"," Rule").shift(RIGHT*3,UP*2)
            rule_ul = Underline(rule_title)
            self.play(ReplacementTransform(grep_title[0],rule_title[0]), ReplacementTransform(grep_title,rule_title),
                      ReplacementTransform(grep_ul,rule_ul),
                      FadeOut(rendered_grep_rule_2),
                      FadeOut(rectx), FadeOut(recty))
            self.play(Write(rendered_rule_code_1))
            self.wait()
            self.next_slide()

            ############# Semgrep printf(x) ##############
            rule_code_x = '''
            rules:
              - id: example_rule
                patterns:
                  - pattern: printf(x);
              message: Rule found!
              languages: [c]
              severity: WARNING'''
            rendered_rule_code_x = Code(code=rule_code_x, tab_width=2, language="yaml", insert_line_no=False).shift(RIGHT*3)
            rendered_rule_code_x.code = remove_invisible_chars(rendered_rule_code_x.code)
            self.play(ReplacementTransform(rendered_rule_code_1,rendered_rule_code_x))
            self.play(FadeIn(rectx));

            self.wait()
            self.next_slide()

            ############# Semgrep printf(y) ##############
            rule_code_y = '''
            rules:
              - id: example_rule
                patterns:
                  - pattern: printf(y);
              message: Rule found!
              languages: [c]
              severity: WARNING'''
            rendered_rule_code_y = Code(code=rule_code_y, tab_width=2, language="yaml", insert_line_no=False).shift(RIGHT*3)

            rendered_rule_code_y.code = remove_invisible_chars(rendered_rule_code_y.code)
            self.play(ReplacementTransform(rendered_rule_code_x,rendered_rule_code_y), FadeOut(rectx))
            self.play(FadeIn(recty));

            self.wait()
            self.next_slide()

            ############# Semgrep pattern-either ##############
            rule_code_either = '''
            rules:
              - id: example_rule
                pattern-either:
                  - pattern: printf(x);
                  - pattern: printf(y);
              message: Rule found!
              languages: [c]
              severity: WARNING'''
            rendered_rule_code_either = Code(code=rule_code_either, tab_width=2, language="yaml", insert_line_no=False).shift(RIGHT*3)
            rendered_rule_code_either.code = remove_invisible_chars(rendered_rule_code_either.code)
            self.play(ReplacementTransform(rendered_rule_code_y,rendered_rule_code_either), FadeOut(recty))
            self.play(FadeIn(rectx), FadeIn(recty));

            self.wait()
            self.next_slide()

            ############# Pattern .... ##############
            rule_code_dots = '''
            rules:
              - id: example_rule
                patterns:
                  - pattern: printf(...);
              message: Rule found!
              languages: [c]
              severity: WARNING'''
            rendered_rule_code_dots = Code(code=rule_code_dots, tab_width=2, language="yaml", insert_line_no=False).shift(RIGHT*3)
            rendered_rule_code_dots.code = remove_invisible_chars(rendered_rule_code_dots.code)
            self.play(ReplacementTransform(rendered_rule_code_either,rendered_rule_code_dots), FadeOut(rectx), FadeOut(recty))
            self.play(FadeIn(rectx), FadeIn(recty));

            self.wait()
            self.next_slide()

            ############# Pattern-not ##############
            rule_code_not = '''
            rules:
              - id: example_rule
                patterns:
                  - pattern: printf(...);
                  - pattern-not: printf(y);
              message: Rule found!
              languages: [c]
              severity: WARNING'''
            rendered_rule_code_not = Code(code=rule_code_not, tab_width=2, language="yaml", insert_line_no=False).shift(RIGHT*3)
            rendered_rule_code_not.code = remove_invisible_chars(rendered_rule_code_not.code)
            self.play(ReplacementTransform(rendered_rule_code_dots,rendered_rule_code_not), FadeOut(recty),FadeOut(rectx))
            #self.play(FadeIn(rectx), FadeIn(recty));

            self.wait()
            self.next_slide()
            arrow1 = Arrow(start=rendered_rule_code_not.code[3],end=rendered_code_2.code[3],color=YELLOW)
            arrow2 = Arrow(start=rendered_rule_code_not.code[3],end=rendered_code_2.code[4],color=YELLOW)
            cross = Cross(rendered_code_2.code[4])
            self.play(Create(arrow1),Create(arrow2), FadeIn(recty),FadeIn(rectx))
            self.wait()
            self.next_slide()
            self.play(Create(cross),FadeToColor(arrow2,color=WHITE),FadeOut(recty))
            self.wait()
            self.next_slide()
            text = Tex("printf(...)"," AND ", "NOT " ,"printf(y)").shift(DOWN*3)
            text[0].set_color(BLUE)
            text[3].set_color(BLUE)
            text[1].set_color(GREEN)
            text[2].set_color(GREEN)
            self.play(FadeIn(text))
            self.wait()
            self.next_slide()
            self.play(*[FadeOut(mob) for mob in self.mobjects])

    def metavariables(self):
            ########### Metavariables ##############
            title = Title("Semgrep Metavariables")
            self.add(title)
            ########### gets() vulnerable code ##############
            code_vuln = '''
            int main(){
                char user[32]; 
                gets(user);
            }'''
            rendered_code_vuln = Code(code=code_vuln, tab_width=4, language="C")
            rendered_code_vuln.code = remove_invisible_chars(rendered_code_vuln.code)

            example_text = Tex("Vulnerable Code").shift(UP*2)
            example_ul = Underline(example_text)
            self.play(FadeIn(example_text, example_ul), Write(rendered_code_vuln))
            left_group = Group(rendered_code_vuln, example_text, example_ul)
            self.wait()
            self.next_slide()
            self.play(left_group.animate.shift(LEFT*4))

            ########## gets() rule code #############
            rule_code_vuln = '''
            rules:
              - id: gets_rule
                patterns:
                  - pattern: gets($BUF);
              message: gets() writes to "$BUF"
              languages: [c]
              severity: WARNING'''
            rendered_rule_code_vuln = Code(code=rule_code_vuln, tab_width=2, language="yaml", insert_line_no=False).shift(RIGHT*3)
            rendered_rule_code_vuln.code = remove_invisible_chars(rendered_rule_code_vuln.code)

            grep_title = Tex("Semgrep "," Rule").shift(RIGHT*3,UP*2)
            grep_ul = Underline(grep_title)

            rect_gets = SurroundingRectangle(rendered_code_vuln.code[2], buff=0.02) #printf(x);
            self.play(FadeIn(grep_title, grep_ul), Write(rendered_rule_code_vuln))
            self.play(FadeIn(rect_gets.set_fill(YELLOW).set_opacity(0.2)))
            self.wait()
            self.next_slide()

            ########## gets() message ##########
            message = Text('gets() writes to "user"',font='Monospace').shift(DOWN*3)
            self.play(FadeIn(message))
            self.wait()
            self.next_slide()
            self.play(FadeOut(message))

            ########### fgets() vulnerable code ##############
            code_fgets = '''
            int main(){
                char user[32]; 
                fgets(user, 64, stdin);
            }'''
            rendered_code_fgets = Code(code=code_fgets, tab_width=4, language="C",insert_line_no=False).shift(LEFT*4)
            rendered_code_fgets.code = remove_invisible_chars(rendered_code_fgets.code)
            self.play(ReplacementTransform(rendered_code_vuln,rendered_code_fgets), FadeOut(rect_gets))
            self.wait()
            self.next_slide()

            ########## fgets() rule code #############
            rule_code_fgets = '''
            rules:
              - id: gets_rule
                patterns:
                  - pattern: |
                      $TYPE $BUF[$SIZE];
                      fgets($BUF,$MAX,stdin);
              message: fgets() overflows "$BUF"
              languages: [c]
              severity: WARNING'''
            rendered_rule_code_fgets = Code(code=rule_code_fgets, tab_width=2, language="yaml", insert_line_no=False).shift(RIGHT*3,DOWN*.5)
            rendered_rule_code_fgets.code = remove_invisible_chars(rendered_rule_code_fgets.code)
            self.play(ReplacementTransform(rendered_rule_code_vuln,rendered_rule_code_fgets))
            self.wait()
            self.next_slide()

            ########### fgets() color code ############
            self.play(
                    FadeToColor(rendered_rule_code_fgets.code[4][0:5],color=RED),    #$TYPE
                    FadeToColor(rendered_rule_code_fgets.code[4][5:9],color=ORANGE), #$BUF
                    FadeToColor(rendered_rule_code_fgets.code[4][10:15],color=YELLOW),#$SIZE
                    FadeToColor(rendered_rule_code_fgets.code[5][6:10],color=ORANGE), #$BUF
                    FadeToColor(rendered_rule_code_fgets.code[5][11:15],color=BLUE), #$MAX
                    FadeToColor(rendered_rule_code_fgets.code[6][25:29],color=ORANGE), #$BUF

                    FadeToColor(rendered_code_fgets.code[1][0:4],color=RED),    #char
                    FadeToColor(rendered_code_fgets.code[1][4:8],color=ORANGE), #user
                    FadeToColor(rendered_code_fgets.code[1][9:11],color=YELLOW),#32
                    FadeToColor(rendered_code_fgets.code[2][6:10],color=ORANGE), #user
                    FadeToColor(rendered_code_fgets.code[2][11:13],color=BLUE), #64
                    )

            self.wait()
            self.next_slide()
            rect_fgets = SurroundingRectangle(rendered_code_fgets.code[1:3], buff=0.02) #printf(x);
            self.play(FadeIn(rect_fgets.set_fill(YELLOW).set_opacity(0.2)))
            self.wait()
            self.next_slide(loop=True)

            ########## fgets() problem (no meta comparison) ######
            rect_fgets.set_z_index(2) #places above all rendered code
            temp = list(code_fgets)
            temp[85:87] = "12"
            code_fgets = ''.join(temp)
            rendered_code_fgets_1 = Code(code=code_fgets, tab_width=4, language="C",insert_line_no=False).shift(LEFT*4)
            rendered_code_fgets_1.code = remove_invisible_chars(rendered_code_fgets_1.code)
            rendered_code_fgets_1.code[1][0:4].set_color(RED)    #char
            rendered_code_fgets_1.code[1][4:8].set_color(ORANGE) #user
            rendered_code_fgets_1.code[1][9:11].set_color(YELLOW)#32
            rendered_code_fgets_1.code[2][6:10].set_color(ORANGE) #user
            rendered_code_fgets_1.code[2][11:13].set_color(BLUE) #64
            temp[85:87] = "24"
            code_fgets = ''.join(temp)
            rendered_code_fgets_2 = Code(code=code_fgets, tab_width=4, language="C",insert_line_no=False).shift(LEFT*4)
            rendered_code_fgets_2.code = remove_invisible_chars(rendered_code_fgets_2.code)
            rendered_code_fgets_2.code[1][0:4].set_color(RED)    #char
            rendered_code_fgets_2.code[1][4:8].set_color(ORANGE) #user
            rendered_code_fgets_2.code[1][9:11].set_color(YELLOW)#32
            rendered_code_fgets_2.code[2][6:10].set_color(ORANGE)#user
            rendered_code_fgets_2.code[2][11:13].set_color(BLUE) #64
            temp[85:87] = "64"
            code_fgets = ''.join(temp)
            rendered_code_fgets_3 = Code(code=code_fgets, tab_width=4, language="C",insert_line_no=False).shift(LEFT*4)
            rendered_code_fgets_3.code = remove_invisible_chars(rendered_code_fgets_3.code)
            rendered_code_fgets_3.code[1][0:4].set_color(RED)    #char
            rendered_code_fgets_3.code[1][4:8].set_color(ORANGE) #user
            rendered_code_fgets_3.code[1][9:11].set_color(YELLOW)#32
            rendered_code_fgets_3.code[2][6:10].set_color(ORANGE)#user
            rendered_code_fgets_3.code[2][11:13].set_color(BLUE) #64
            self.play(Transform(rendered_code_fgets,rendered_code_fgets_1))
            self.play(Transform(rendered_code_fgets_1,rendered_code_fgets_2))
            self.play(Transform(rendered_code_fgets_2,rendered_code_fgets_3))

            #self.wait()
            self.next_slide()
            self.play(FadeOut(rendered_code_fgets_1),FadeOut(rendered_code_fgets_3))

            ########## fgets() modified rule code #############
            rule_code_fgets_mod = '''
            rules:
              - id: gets_rule
                patterns:
                  - pattern: |
                      $TYPE $BUF[$SIZE];
                      fgets($BUF,$MAX,stdin);
                  - metavariable-comparison:
                      comparison: $MAX > $SIZE
              message: fgets() overflows "$BUF"
              languages: [c]
              severity: WARNING'''
            rendered_rule_code_fgets_mod = Code(code=rule_code_fgets_mod, tab_width=2, language="yaml", insert_line_no=False).shift(RIGHT*3,DOWN*1)
            rendered_rule_code_fgets_mod.code = remove_invisible_chars(rendered_rule_code_fgets_mod.code)
            rendered_rule_code_fgets_mod.code[4][0:5].set_color(RED)    #$TYPE
            rendered_rule_code_fgets_mod.code[4][5:9].set_color(ORANGE) #$BUF
            rendered_rule_code_fgets_mod.code[4][10:15].set_color(YELLOW)#$SIZE
            rendered_rule_code_fgets_mod.code[5][6:10].set_color(ORANGE) #$BUF
            rendered_rule_code_fgets_mod.code[5][11:15].set_color(BLUE) #$MAX
            rendered_rule_code_fgets_mod.code[7][11:15].set_color(BLUE) #$MAX
            rendered_rule_code_fgets_mod.code[7][16:22].set_color(YELLOW) #$SIZE
            rendered_rule_code_fgets_mod.code[8][25:29].set_color(ORANGE) #$BUF

            self.play(ReplacementTransform(rendered_rule_code_fgets,rendered_rule_code_fgets_mod))
            self.wait()
            self.next_slide()

            ########## fgets() loop ###########
            matched = MathTex("64", ">", "32").shift(DOWN*2,LEFT*4)
            matched[0].set_color(BLUE)
            matched[1].set_color(GREEN)
            matched[2].set_color(YELLOW)
            unmatched_1 = MathTex("12", "<", "32").shift(DOWN*2,LEFT*4)
            unmatched_1[0].set_color(BLUE)
            unmatched_1[1].set_color(GREEN)
            unmatched_1[2].set_color(YELLOW)
            temp[85:87] = "12"
            code_fgets = ''.join(temp)
            rendered_code_fgets_1 = Code(code=code_fgets, tab_width=4, language="C",insert_line_no=False).shift(LEFT*4)
            rendered_code_fgets_1.code = remove_invisible_chars(rendered_code_fgets_1.code)
            rendered_code_fgets_1.code[1][0:4].set_color(RED)    #char
            rendered_code_fgets_1.code[1][4:8].set_color(ORANGE) #user
            rendered_code_fgets_1.code[1][9:11].set_color(YELLOW)#32
            rendered_code_fgets_1.code[2][6:10].set_color(ORANGE)#user
            rendered_code_fgets_1.code[2][11:13].set_color(BLUE) #64
            self.play(FadeIn(matched))
            self.wait()
            self.next_slide()
            self.play(Transform(rendered_code_fgets_3,rendered_code_fgets_1),Transform(matched,unmatched_1),FadeOut(rect_fgets))
            self.wait()
            self.next_slide()
            self.play(*[FadeOut(mob) for mob in self.mobjects])

    def pro(self):
        title = Title("Semgrep Pro Features")
        pro = Tex(r"""\begin{itemize}
                   \item Cross-file analysis (\textit{interfile})
                   \item Cross-function taint analysis (\textit{interprocedural})
                   \item Enterprise Languages (e.g. Salesforce Apex)
                  \end{itemize}""")
        self.play(FadeIn(title),Write(pro))
        self.wait()
        self.next_slide()
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def taint(self):
        #self.play(*[FadeOut(mob) for mob in self.mobjects])
        ########### Taint Analysis ##############
        title = Title("Taint Analysis")
        code_title = Tex("Vulnerable Code").shift(UP*2.5,LEFT*3)
        code_ul = Underline(code_title)

        code_taint = '''
        import os

        def receive():
            user_input = input()
            # do stuff with user_input
            return user_input

        def test():
            data = receive()
            # do stuff with data
            os.system(data)'''

        rendered_code = Code(code=code_taint, tab_width=2, language="python",style="native").shift(LEFT*3)
        rendered_code.code = remove_invisible_chars(rendered_code.code)

        self.play(FadeIn(title),FadeIn(code_title,code_ul),Write(rendered_code))
        self.wait()
        self.next_slide()

        ################## Non-taint mode ##############
        rule_title = Tex("Semgrep "," Rule").shift(RIGHT*3.5,UP*2.5)
        rule_ul = Underline(rule_title)
        rule_code = '''
        rules:
          - id: cmd_injection
            patterns:
              - pattern: |
                  $VAR = input()
                  ...
                  os.system($VAR)
          languages: [python]
          severity: WARNING'''
        rendered_rule_code = Code(code=rule_code, tab_width=2, language="yaml", insert_line_no=False).shift(RIGHT*4)
        rendered_rule_code.code = remove_invisible_chars(rendered_rule_code.code)
        self.play(FadeIn(rule_title, rule_ul),Write(rendered_rule_code))
        self.wait()
        self.next_slide()

        ####### Why non-taint mode doesn't work ########
        arrow1 = Arrow(start=rendered_rule_code.code[4],end=rendered_code.code[3],color=RED)
        arrow2 = Arrow(start=rendered_rule_code.code[6],end=rendered_code.code[10],color=RED)
        self.play(Create(arrow1),Create(arrow2))
        self.wait()
        self.next_slide()

        user_input = rendered_code.code[3][0:10].copy()
        data = rendered_code.code[10][10:14].copy()
        ne = MathTex(r"\neq").scale(2).move_to(DOWN*3)
        self.play(user_input.animate.scale(2).next_to(ne,LEFT).set_color(RED), FadeIn(ne.set_color(RED)), data.animate.scale(2).next_to(ne,RIGHT).set_color(RED))
        self.wait()
        self.next_slide()

        self.play(FadeOut(ne),FadeOut(user_input),FadeOut(data),FadeOut(arrow1),FadeOut(arrow2))
        self.wait()
        self.next_slide()

        ########## Taint Mode ##############
        taint_rule_code = '''
        rules:
          - id: cmd_injection
            mode: taint
            pattern-sources:
              - pattern: input()
            pattern-sinks:
              - pattern: os.system(...)
            message: CMD injection!
            languages: [python]
            severity: WARNING'''

        rendered_rule_code_taint = Code(code=taint_rule_code, tab_width=2, language="yaml", insert_line_no=False).shift(RIGHT*3.5)
        rendered_rule_code_taint.code = remove_invisible_chars(rendered_rule_code_taint.code)
        self.play(ReplacementTransform(rendered_rule_code,rendered_rule_code_taint),rendered_code.animate.shift(LEFT*0.5))
        rect = SurroundingRectangle(rendered_code.code[10], buff=0.03, color=PURPLE)
        self.play(FadeIn(rect.set_fill(PURPLE).set_opacity(0.3)))
        self.wait()
        self.next_slide()

        ############## Taint Flow ###############
        A1 = Arrow(start=rendered_code.code[3][-7], end=rendered_code.code[3][9],color=PURPLE,buff=0)
        A2 = Arrow(start=rendered_code.code[3][0], end=rendered_code.code[5][0],color=PURPLE,buff=0)
        A3 = Arrow(start=rendered_code.code[5][-1], end=rendered_code.code[2][0],color=PURPLE,buff=0)
        B1 = Arrow(start=rendered_code.code[10][-5], end=rendered_code.code[8][0],color=GREEN,buff=0)
        B2 = Arrow(start=rendered_code.code[8][0], end=rendered_code.code[8][5],color=GREEN,buff=0)
        B3 = Arrow(start=rendered_code.code[8][5], end=rendered_code.code[2][0],color=GREEN,buff=0)

        self.play(
                FadeToColor(rendered_rule_code_taint.code[4][-7:],color=PURPLE),
                FadeToColor(rendered_rule_code_taint.code[6][-14:],color=GREEN),
                )

        self.wait()
        self.next_slide()

        self.play(Create(A1))
        self.play(Create(A2))
        self.play(Create(A3))
        self.wait()
        self.next_slide()

        self.play(Create(B1))
        self.play(Create(B2))
        self.play(Create(B3))
        self.wait()
        self.next_slide()

        ############## Code variation ############
        code_taint_sneaky = '''
        import os.system as executeme

        def receive():
            user_input = input()
            # do stuff with user_input
            return user_input

        def test():
            data = receive()
            # do stuff with data
            executeme(data)'''
        rendered_rule_code_sneaky = Code(code=code_taint_sneaky, tab_width=2, language="python", style="native").shift(LEFT*3.5)
        rendered_rule_code_sneaky.code = remove_invisible_chars(rendered_rule_code_sneaky.code)
        rectnew = SurroundingRectangle(rendered_rule_code_sneaky.code[10], buff=0.01)
        self.play(ReplacementTransform(rendered_code,rendered_rule_code_sneaky),ReplacementTransform(rect,rectnew.set_fill(PURPLE).set_opacity(0.3)))
        self.wait()
        self.next_slide()

        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def best_rule_tips(self):
        title = Title("Best Semgrep Rule Tips")
        rule_tips = Text("""
                    - Criticality: How dangerous is the match? (CRIT, HIGH, MEDIUM, LOW)

                    - Confidence: What is the True Positive Rate (TPR)? (HIGH, MEDIUM, LOW)
                    
                    - Coverage: Is every scenario for the vulnerability covered? (HIGH, MEDIUM, LOW)
                        """, line_spacing=1, font="Monospace", t2c={"CRIT":PURPLE,"HIGH":RED,"MEDIUM":YELLOW,"LOW":GREEN},t2w={"Criticality":BOLD,"Confidence":BOLD,"Coverage":BOLD}).scale(0.4)
        self.play(FadeIn(title),Write(rule_tips))
        self.wait()
        self.next_slide()
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def best_command_tips(self):
        title = Title("Best Semgrep Command Tips")
        tips = Text(r"""
                    -c (auto|rule.yml)      : config (auto: default semgrep rules | rule.yml: local rule)
                    --timeout 0             : Specifies timeout before skipping rule (default: 5s)
                    --max-target-bytes 0    : Maximum file size (default: 1MB)
                    --<format>-output file  : Outputs findings to file 
                        + <format>: text, json, sarif, gitlab-sast, gitlab-secrets, junit-xml, emacs, vim
                    --pro                   : Activates Pro Feature
                    -j VAL                  : Runs jobs in parallel (default: core count or 1 with --pro)
                        + Semgrep recommends 4-8 GB of memory per job
                        + Negligible impact on small code. Memory consumption can cause crashes.
                    """,line_spacing=1,font="Monospace",
                    t2c={'-c':RED,'--timeout':ORANGE,'--max-target-bytes':YELLOW,'--<format>-output':GREEN,'--pro':BLUE,'-j':PURPLE}
                    ).scale(0.4)
        best = Text("semgrep scan -c <rule.yml> --pro -j 8 --timeout 0 --max-target-bytes 0 <target file/dir>",
                    t2c={'-c':RED,'--timeout':ORANGE,'--max-target-bytes':YELLOW,'--<format>-output':GREEN,'--pro':BLUE,'-j':PURPLE}
                    ).shift(DOWN*3).scale(0.45)
        self.play(FadeIn(title),Write(tips))
        self.play(Write(best))
        self.wait()
        self.next_slide()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        with register_font("cursive.ttf"):
            self.play(Write(Text("Demo Time!",font="cursive").scale(3)))
        self.wait()
        self.next_slide()
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def end(self):
        #self.play(*[FadeOut(mob) for mob in self.mobjects])
        with register_font("cursive.ttf"):
            thanks = Text("Thank You!",font="cursive").scale(3).shift(UP*1.5)
        website = Tex("https://emorchy.github.io/",color=BLUE).scale(1.5).next_to(thanks,DOWN*2)
        ssr_website = Tex("https://somersetrecon.com/blog",color=ORANGE).scale(1.5).next_to(website,DOWN)
        signal_logo = SVGMobject(file_name="signal-logo.svg").scale(0.75)
        signal_username = Tex("eagle.42").scale(1.5).next_to(signal_logo, RIGHT)
        group = Group(signal_logo,signal_username).next_to(ssr_website,DOWN)
        self.play(Write(thanks),DrawBorderThenFill(signal_logo), Write(signal_username), Write(website), Write(ssr_website))
        self.wait()
        self.next_slide()

    def construct(self):
        self.Intro()
        self.Semgrep_example()
        self.metavariables()
        self.pro()
        self.taint()
        self.best_rule_tips()
        self.best_command_tips()
        self.end()
