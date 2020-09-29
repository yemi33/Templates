from engine import TemplateEngine

def component1a():
    engine = TemplateEngine(file_path="templates/c1_template.txt")
    
    for i in range(5):
        output = engine.generate(template_name="NO_CORPUS")
        print(f"{i} {output}")

def component1b():
    engine = TemplateEngine(file_path="templates/c1_template.txt")
    
    for i in range(5):
        output = engine.generate(template_name="YES_CORPUS")
        print(f"{i} {output}")
    
def component1c():
    engine = TemplateEngine(file_path="templates/c1_template.txt")
    
    for i in range(5):
        output = engine.generate(template_name="MY_CORPUS")
        print(f"{i} {output}")


def component1d():
    engine = TemplateEngine(file_path="templates/c1_template.txt")
  
    multi_line_output = ""
    output1 = engine.generate(template_name="NO_CORPUS")
    output2 = engine.generate(template_name="YES_CORPUS")
    output3 = engine.generate(template_name="MY_CORPUS")
    output4 = engine.generate(template_name="HOPEFULLY_POETIC")
    multi_line_output += output1 + output2 + output3 + output4
    print(f"{multi_line_output}")
    


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 1a -- ")
    component1a()
    print("\n\n-- Component 1b -- ")
    component1b()
    print("\n\n-- Component 1c -- ")
    component1c()
    print("\n\n-- Component 1d -- ")
    component1d()