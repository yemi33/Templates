from engine import TemplateEngine

def component7a():
    engine = TemplateEngine(file_path="templates/c7_template.txt")
    
    for i in range(10):
        output = engine.generate(template_name="ALPHABETICAL")
        print(f"{i} {output} \n")


def component7b():
    engine = TemplateEngine(file_path="templates/c7_template.txt")
    
    for i in range(10):
        output = engine.generate(template_name="LONGER")
        print(f"{i} {output} \n")


def component7c():
    engine = TemplateEngine(file_path="templates/c7_template.txt")
    
    for i in range(10):
        output = engine.generate(template_name="PALINDROME")
        output_list = output.split()
        output2 = output_list[::-1]
        output3 =""
        for j in range(len(output2)):
          output3+=f"{output2[j]} "
        
        print(f"{i} {output}and {output3} \n")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 7a -- ")
    component7a()
    print("\n\n-- Component 7b -- ")
    component7b()
    print("\n\n-- Component 7c -- ")
    component7c()

