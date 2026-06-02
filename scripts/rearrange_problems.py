
from pathlib import Path
import json

TITLE = "Test problem"
INSTRUCTIONS = "Do what you want"
INITIAL = [
    'def is_true(boolean_value):\n',
    '  if boolean_value:\n',
    '    return True\n',
    '  return False\n',
    '  return true #distractor\n',
]

problem_name = "test_problem.html"


def build_initial_js(initial_lines):
    if not initial_lines:
        return '""'
    return " +\n".join(json.dumps(line) for line in initial_lines)


def create_problem_html(title, instructions, initial_lines, output_name):
    script_dir = Path(__file__).resolve().parent
    template_path = script_dir.parent / "templates" / "template_rearrange.html"
    output_path = template_path.parent.parent / "output" / output_name

    template = template_path.read_text(encoding="utf-8")
    initial_js = build_initial_js(initial_lines)

    problem_html = template.replace("TITLE", title)
    problem_html = problem_html.replace("INSTRUCTIONS", instructions)
    problem_html = problem_html.replace("INITIAL", initial_js)

    output_path.write_text(problem_html, encoding="utf-8")
    return output_path


if __name__ == "__main__":
    created_file = create_problem_html(TITLE, INSTRUCTIONS, INITIAL, problem_name)
    print(f"Created problem file: {created_file}")

