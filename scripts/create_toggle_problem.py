from pathlib import Path
import json
import argparse
import re
import html


TITLE = "Toggle problem"
INSTRUCTIONS = (
    "Construct a function which returns the largest of the two arguments. "
    "You can change the value of a toggleable element by clicking."
)


INITIAL = [
    "def find_largest(a, b):\n",
    "    if $ab > $ab:\n",
    "        return $ab\n",
    "    else:\n",
    "        return $ab\n",
]
UNITTESTS = [
    "import unittestparson\n",
    "class myTests(unittestparson.unittest):\n",
    "  def testOne(self):\n",
    '    self.assertEqual(find_largest(0, 2), 2, "Calling function <code>find_largest(0, 2)</code>.")\n',
    '    self.assertEqual(find_largest(4, 2), 4, "Calling function <code>find_largest(4, 2)</code>.")\n',
    '    self.assertEqual(find_largest(-5, -1), -1, "Calling function <code>find_largest(-5, -1)</code>.")\n',
    "_test_result = myTests().main()",
]
# Toggle: set to True to include unit test feedback in the generated HTML.
# Set `with_unittests` and `shuffle` here (file-level configuration).
WITH_UNITTESTS = True
# Whether to shuffle the displayed lines. For toggle problems we prefer no shuffling.
SHUFFLE = False
TOGGLE_TYPE_HANDLERS = {
    "ab": ["a", "b"]
}
PROBLEM_NAME = "toggle_problem.html"


def build_js_string(lines):
    if not lines:
        return '""'
    return " +\n".join(json.dumps(line) for line in lines)


def create_toggle_problem_html(title, instructions, initial_lines, unittests_lines, toggle_handlers, output_name, with_unittests=True):
    script_dir = Path(__file__).resolve().parent
    template_path = script_dir.parent / "templates" / "template_toggle.html"
    output_path = script_dir.parent / "output" / output_name

    template = template_path.read_text(encoding="utf-8")
    
    def _convert_dollar_to_toggle(s):
        def repl(m):
            key = m.group(1)
            options = TOGGLE_TYPE_HANDLERS[key]
            json_str = json.dumps(options)
            escaped_json = html.escape(json_str)
            return '<span class="jsparson-toggle" data-jsp-options="' + escaped_json + '"></span>'
        return re.sub(r"\$([A-Za-z0-9]+)", repl, s)

    converted_initial = [_convert_dollar_to_toggle(line) for line in initial_lines]
    initial_js = build_js_string(converted_initial)
    # Map Python booleans directly to valid JavaScript literal tokens
    shuffle_js = "true" if SHUFFLE else "false"
    
    # Generate the missing HTML anchor element for the feedback handler
    toggle_handlers_js = json.dumps(toggle_handlers)

    feedback_html = '<a href="#" id="feedbackLink" style="margin-left: 10px;">Run Test</a>'
    

    problem_html = template.replace("TITLE", title)
    problem_html = problem_html.replace("INSTRUCTIONS", instructions)
    problem_html = problem_html.replace("INITIAL", initial_js)
    if WITH_UNITTESTS:
        unittests_js = json.dumps("".join(UNITTESTS))
        problem_html = problem_html.replace("UNITTESTS", unittests_js)
    problem_html = problem_html.replace("TOGGLE_TYPE_HANDLERS", toggle_handlers_js)
    problem_html = problem_html.replace("SHOULD_SHUFFLE", shuffle_js)
    problem_html = problem_html.replace("FEEDBACK_LINKS", feedback_html)


    output_path.write_text(problem_html, encoding="utf-8")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Create a toggle problem HTML file")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--with-unittests', dest='with_unittests', action='store_true', help='Include unit test feedback in generated HTML')
    group.add_argument('--no-unittests', dest='with_unittests', action='store_false', help='Do not include unit test feedback')
    parser.set_defaults(with_unittests=WITH_UNITTESTS)

    created_file = create_toggle_problem_html(
        TITLE,
        INSTRUCTIONS,
        INITIAL,
        UNITTESTS,
        TOGGLE_TYPE_HANDLERS,
        PROBLEM_NAME,
        with_unittests=WITH_UNITTESTS,
    )
    print(f"Created toggle problem file: {created_file}")


if __name__ == "__main__":
    main()
