
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

PROBLEM_NAME = "rearrange_problem.html"
# File-level controls
# For rearrange problems we want shuffling by default so students must reorder lines
with_unittests = False
shuffle = True


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
    permutation_js = 'undefined' if shuffle else json.dumps(list(range(len(initial_lines))))

    problem_html = template.replace("TITLE", title)
    problem_html = problem_html.replace("INSTRUCTIONS", instructions)
    problem_html = problem_html.replace("INITIAL", initial_js)
    problem_html = problem_html.replace("PERMUTATION", permutation_js)
    # Insert or remove the feedback link depending on with_unittests
    feedback_html = '' if with_unittests else '<a href="#" id="feedbackLink">Get Feedback</a>'
    problem_html = problem_html.replace("FEEDBACK_LINKS", feedback_html)

    output_path.write_text(problem_html, encoding="utf-8")
    return output_path


def main():
    created_file = create_problem_html(TITLE, INSTRUCTIONS, INITIAL, PROBLEM_NAME)
    print(f"Created problem file: {created_file}")


if __name__ == "__main__":
    main()

