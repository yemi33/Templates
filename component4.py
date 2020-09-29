from engine import TemplateEngine

def component4():
    engine = TemplateEngine(file_path="templates/c4_template.txt")
    
    for i in range(5):
        output = engine.generate(template_name="SHANNON_ZERO")
        print(f"{i} {output} \n")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 4 -- ")
    component4()


