from engine import TemplateEngine

def component9():
    engine = TemplateEngine(file_path="templates/c9_template.txt")

    for i in range(5):
        output = engine.generate(template_name="STRACHEY")
        ending = engine.generate(template_name="ENDING")

        output_list_for_cap = output.split(" ")
        output_list_for_cap[0] = output_list_for_cap[0].capitalize()
        output_list_for_cap[1] = output_list_for_cap[1].capitalize()
        output_beginning_capped = ""
        for k in range(len (output_list_for_cap)):
          output_beginning_capped +=f"{output_list_for_cap[k]} "

        output_list = output_beginning_capped.split('\\n')
        for j in range (len(output_list)):
          print(f"{output_list[j]}")

        ending_list = ending.split('\\n')
        for j in range (len(ending_list)):
          print(f"                                                     {ending_list[j]}")

        print("\n")
        


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 9 -- ")
    component9()
