from engine import TemplateEngine

def supplementary_challenge2():
  engine = TemplateEngine(file_path="templates/c6_template.txt")
    
  for i in range(5):
    print(f"<{i}>\n")
    output = engine.generate(template_name="DADAIST_ADVANCED")
    output_list = output.split('\\n')
    for j in range (len(output_list)):
      print(f"{output_list[j]}")
    print(" ")

def experiment():
  engine = TemplateEngine(file_path="templates/experimental_dadaist.txt")
    
  for i in range(3):
    output = engine.generate(template_name="SENTENCE3")
    print(f"{i} {output} \n")

def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Supplementary Challenge 2 -- ")
    supplementary_challenge2()

experiment()
