from engine import TemplateEngine

def component10():
    engine = TemplateEngine(file_path="templates/c10_template.txt")
    for i in range (5):
      print(f"<{i}>\n")
      for i in range(3):
          output = engine.generate(template_name="POEM")
          output_word_list = output.split()
          
          if output_word_list[3][0] == "a" or output_word_list[3][0] == "e" or output_word_list[3][0] == "o" or output_word_list[3][0] == "u":
            output_word_list[2] = "an"
          else: 
            output_word_list[2] = "a"

          final_output = ""
          for j in range(len(output_word_list)):
            final_output += f"{output_word_list[j]} "
          
          print(f"{final_output} \n")
      print("one\ntwo\nthree\n.\n.\n.\nboom\n")
      print("Although\n\n")

      output1 = engine.generate(template_name="LUMP1")
      output2 = engine.generate(template_name="LUMP2")
      output3 = engine.generate(template_name="LUMP3")
      output4 = engine.generate(template_name="LUMP4")
      output5 = engine.generate(template_name="LUMP5")
      output6 = engine.generate(template_name="LUMP6")

      print(output1+"\n"+output2+"\n"+output3+"\n"+output4+"\n"+output5+"\n"+output6)

      
  



def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 10 -- ")
    component10()
  

