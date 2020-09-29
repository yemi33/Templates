from engine import TemplateEngine

def component6():
    engine = TemplateEngine(file_path="templates/c6_template.txt")
    
    for i in range(5):
        output = engine.generate(template_name="DADAIST")
        output_list = output.split('\\n')
        for j in range (len(output_list)):
          print(f"{output_list[j]}")
        print("\n")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 6 -- ")
    component6()


