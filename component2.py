from engine import TemplateEngine

def component2a():
    for i in range(5):
        engine = TemplateEngine(file_path="templates/c1_template.txt", random_seed = 3)
        output = engine.generate(template_name="NO_CORPUS")
        print(f"{i} {output}")


def component2b():
    engine = TemplateEngine(file_path="templates/c2_template.txt", random_seed = 3)

    for i in range(10):
        output = engine.generate(template_name="PROBABILISTIC")
        print(f"{i} {output}")


def component2c():
    engine = TemplateEngine(file_path="templates/c2_template.txt", random_seed = 3)

    for i in range(10):
        output = engine.generate(template_name="OPTIONAL")
        print(f"{i} {output}")


def component2d():
    engine = TemplateEngine(file_path="templates/c2_template.txt", random_seed = 3)

    for i in range(10):
        output = engine.generate(template_name="OPTIONAL2")
        print(f"{i} {output}")


def component2e():
    engine = TemplateEngine(file_path="templates/c2_template.txt")
    print("\nCapitalizing the first character of each line...\n")
    for i in range(5):
        output = engine.generate(template_name="LOWERCASE").capitalize()

        print(f"{i} {output}")
    
    print("\nNow onto capitalizing every character...\n")
    for i in range(5):
        output = engine.generate(template_name="LOWERCASE")

        final_output = ""
        for j in range(len(output)):
          final_output+= output[j].capitalize()

        print(f"{i} {final_output}")


def component2f():
    engine = TemplateEngine(file_path="templates/c2_template.txt")

    for i in range(10):
        output = engine.generate(template_name="CONJUGATION")
        output_word_list = output.split()
        
        if output_word_list[3][0] == "a" or output_word_list[3][0] == "e" or output_word_list[3][0] == "i" or output_word_list[3][0] == "o" or output_word_list[3][0] == "u":
          output_word_list[2] = "an"
        else: 
          output_word_list[2] = "a"
        
        if output_word_list[7][0] == "a" or output_word_list[7][0] == "e" or output_word_list[7][0] == "i" or output_word_list[7][0] == "o" or output_word_list[7][0] == "u":
          output_word_list[6] = "an"
        else: 
          output_word_list[6] = "a"
        
        final_output = ""
        for j in range(len(output_word_list)):
          final_output += f" {output_word_list[j]}"
        
        print(f"{i} {final_output}")

def component2g():
    engine = TemplateEngine(file_path="templates/c2_template.txt")

    for i in range(5):
        output = engine.generate(template_name="NEWLINE")
        output_list = output.split('\\n')
        for j in range (len(output_list)):
          print(f"{output_list[j]}")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 2a -- ")
    component2a()
    print("\n\n-- Component 2b -- ")
    component2b()
    print("\n\n-- Component 2c -- ")
    component2c()
    print("\n\n-- Component 2d -- ")
    component2d()
    print("\n\n-- Component 2e -- ")
    component2e()
    print("\n\n-- Component 2f -- ")
    component2f()
    print("\n\n-- Component 2g -- ")
    component2g()

output = "My name is Yemi\nMy name is Yemi"
print(output.split("\n"))

component2g()


