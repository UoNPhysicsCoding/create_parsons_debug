from pathlib import Path
import json

TITLE = "Toggle problem"
INSTRUCTIONS = (
    "Construct a function which returns the largest of the three given arguments. "
    "You can change the value of a toggleable element by clicking."
)
INITIAL = [
    "def find_largest(a, b, c):\n",
    "if <span class='jsparson-toggle' data-type='abc'></span> > <span class='jsparson-toggle' data-type='abc'></span>:\n",
    "    return <span class='jsparson-toggle' data-type='abc'></span>\n",
    "elif <span class='jsparson-toggle' data-type='abc'></span> > <span class='jsparson-toggle' data-type='abc'></span>:\n",
    "    return <span class='jsparson-toggle' data-type='abc'></span>\n",
    "else:\n",
    "    return <span class='jsparson-toggle' data-type='abc'></span>\n",
]
UNITTESTS = [
    "import unittestparson\n",
    "class myTests(unittestparson.unittest):\n",
    "  def testOne(self):\n",
    '    self.assertEqual(find_largest(0, 2, 4), 4, "Calling function <code>find_largest(0, 2, 4)</code>.")\n',
    '    self.assertEqual(find_largest(4, 2, 4), 4, "Calling function <code>find_largest(4, 2, 4)</code>.")\n',
    '    self.assertEqual(find_largest(-5, -1, -4), -1, "Calling function <code>find_largest(-5, -1, -4)</code>.")\n',
    '    self.assertEqual(find_largest(7, 2, 4), 7, "Calling function <code>find_largest(7, 2, 4)</code>.")\n',
    "_test_result = myTests().main()",
]
TOGGLE_TYPE_HANDLERS = {
    "abc": ["a", "b", "c"],
}
problem_name = "toggle_problem.html"


def build_js_string(lines):
    if not lines:
        return '""'
    return " +\n".join(json.dumps(line) for line in lines)


def create_toggle_problem_html(title, instructions, initial_lines, unittests_lines, toggle_handlers, output_name):
    script_dir = Path(__file__).resolve().parent
    template_path = script_dir.parent / "templates" / "template_toggle.html"
    output_path = script_dir.parent / "output" / output_name

    template = template_path.read_text(encoding="utf-8")
    initial_js = build_js_string(initial_lines)
    unittests_js = build_js_string(unittests_lines)
    toggle_handlers_js = json.dumps(toggle_handlers)

    problem_html = template.replace("TITLE", title)
    problem_html = problem_html.replace("INSTRUCTIONS", instructions)
    problem_html = problem_html.replace("INITIAL", initial_js)
    problem_html = problem_html.replace("UNITTESTS", unittests_js)
    problem_html = problem_html.replace("TOGGLE_TYPE_HANDLERS", toggle_handlers_js)

    output_path.write_text(problem_html, encoding="utf-8")
    return output_path


if __name__ == "__main__":
    created_file = create_toggle_problem_html(
        TITLE,
        INSTRUCTIONS,
        INITIAL,
        UNITTESTS,
        TOGGLE_TYPE_HANDLERS,
        problem_name,
    )
    print(f"Created toggle problem file: {created_file}")
