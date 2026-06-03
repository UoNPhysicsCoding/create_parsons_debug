
from pathlib import Path
import json

TITLE = "Debug problem"
INSTRUCTIONS = (
    "A buggy program is shown. Modify, remove or move lines so that the program prints the expected output."
)
# Example initial lines for a small debug problem that should print Hello
INITIAL = [
    "def greet():\n",
    "  print('Hello')\n",
    "greet()\n",
    "unused_var = 1  # distractor\n",
]

VARTESTS = [
    {"initcode": "", "code": "", "variables": {"__output": "Hello\n"}, "message": "Program should print Hello"}
]

PROBLEM_NAME = "debug_problem.html"
# File-level controls
# Include unit test feedback (not typically used for debug problems but provided for consistency)
with_unittests = False
# Whether to shuffle displayed lines. Debug problems should present lines in the correct order.
shuffle = False


def build_js_string(lines):
    if not lines:
        return '""'
    return " +\n".join(json.dumps(line) for line in lines)


def create_debug_problem_html(title, instructions, initial_lines, vartests, output_name):
    script_dir = Path(__file__).resolve().parent
    template_path = script_dir.parent / "templates" / "template_debug.html"
    output_path = script_dir.parent / "output" / output_name

    template = template_path.read_text(encoding="utf-8")
    initial_js = build_js_string(initial_lines)
    vartests_js = json.dumps(vartests)
    # permutation: undefined to allow shuffling, or an identity list to preserve order
    permutation_js = 'undefined' if shuffle else json.dumps(list(range(len(initial_lines))))

    problem_html = template.replace("TITLE", title)
    problem_html = problem_html.replace("INSTRUCTIONS", instructions)
    problem_html = problem_html.replace("INITIAL", initial_js)
    problem_html = problem_html.replace("VARTESTS", vartests_js)
    problem_html = problem_html.replace("PERMUTATION", permutation_js)

    output_path.write_text(problem_html, encoding="utf-8")
    return output_path


def main():
    created_file = create_debug_problem_html(
        TITLE,
        INSTRUCTIONS,
        INITIAL,
        VARTESTS,
        PROBLEM_NAME,
    )
    print(f"Created debug problem file: {created_file}")


if __name__ == "__main__":
    main()

