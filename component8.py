from engine import TemplateEngine

def component8a():
    engine = TemplateEngine(file_path="templates/c8_template.txt")

    for i in range(5):
        output = engine.generate(template_name="QUATRAIN")
        output_list = output.split('\\n')
        for j in range (len(output_list)):
          print(f"{output_list[j]}")
        print("\n")


def component8b():
    engine = TemplateEngine(file_path="templates/c8_template.txt")

    for i in range(5):
        output = engine.generate(template_name="LIMERICK")
        output_list = output.split('\\n')
        for j in range (len(output_list)):
          print(f"{output_list[j]}")
        print("\n")


def component8c():
    engine = TemplateEngine(file_path="templates/c8_template.txt")

    for i in range(5):
        output = engine.generate(template_name="HAIKU")
        output_list = output.split('\\n')
        for j in range (len(output_list)):
          print(f"{output_list[j]}")
        print("\n")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 8a -- ")
    component8a()
    print("\n\n-- Component 8b -- ")
    component8b()
    print("\n\n-- Component 8c -- ")
    component8c()

