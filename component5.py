from engine import TemplateEngine

def component5a():
  engine = TemplateEngine(file_path="templates/c5_template.txt")
  for _ in range(5):
    print(engine.generate(template_name="PLOT_SKELETON"),end='\n\n')


def component5b():
  engine = TemplateEngine(file_path="templates/c5_template.txt")
  for _ in range(5):
    print(engine.generate(template_name="PLOT_PROSE1"),end='\n\n')


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 5a -- ")
    component5a()
    print("\n\n-- Component 5b -- ")
    component5b()

