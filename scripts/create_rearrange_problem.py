"""----------------------------------------------------------------------------------------------
# Everything you need to change is below here
------------------------------------------------------------------------------------------------"""

TITLE = "Rearrange example problem"
INSTRUCTIONS = "The aim of this problem is to produce a function which tests whether the supplied parameter boolean value is True or False. Drag and drop the lines into the box below in the correct order. When you think you have the correct solution press `Give Feedback`. You can start again by pressing `Reset Problem`"
INITIAL = [
    'def is_true(boolean_value):\n',
    '  if boolean_value:\n',
    '    return True\n',
    '  return False\n',
    '  return true #distractor\n', 
]

PROBLEM_NAME = "rearrange_problem.html"
WITH_UNITTESTS = False
SHUFFLE = True


"""----------------------------------------------------------------------------------------------
# Everything you need to change is above here
------------------------------------------------------------------------------------------------"""

from pathlib import Path
import json
import os
import re

import re
import os
from pathlib import Path

import re
import os

def get_inlined_html(html_content, base_path='./.exercises'):
    """
    Transforms HTML so it contains all CSS and JS content internally.
    """
    def replace_resource(match):
        tag = match.group(0)
        path = match.group(1) # The path like 'static/parsons.js'
        
        # Point to the real location of your static assets
        full_path = Path(base_path) / path
        
        if full_path.exists():
            content = full_path.read_text(encoding='utf-8')
            if path.endswith('.css'):
                return f"<style>{content}</style>"
            elif path.endswith('.js'):
                return f"<script>{content}</script>"
        else:
            print(f"DEBUG: !!! File NOT found at {full_path.absolute()}")
            return tag
        return tag # Return original if not found

    # This regex handles both single and double quotes
    return re.sub(r'<(?:link|script)[^>]*?(?:href|src)=["\']([^"\']+?\.(?:css|js))["\'][^>]*?>', 
                  replace_resource, html_content)
    


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
    
    # Map Python booleans directly to valid JavaScript literal tokens
    shuffle_js = "true" if SHUFFLE else "false"
    unittests_js = "true" if WITH_UNITTESTS else "false"
    
    # Generate the missing HTML anchor element for the feedback handler
    feedback_html = '<a href="#" id="feedbackLink" style="margin-left: 10px;">Give Feedback</a>'

    problem_html = template.replace("TITLE", title)
    problem_html = problem_html.replace("INSTRUCTIONS", instructions)
    problem_html = problem_html.replace("INITIAL", initial_js)
    problem_html = problem_html.replace("SHOULD_SHUFFLE", shuffle_js)
    problem_html = problem_html.replace("WITH_UNITTESTS", unittests_js)
    problem_html = problem_html.replace("FEEDBACK_LINKS", feedback_html)

    # In create_problem_html, update the call to:
    # Change './.exercises' to the actual path where your 'static' folder lives
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent  # This assumes your script is in /scripts
    inline_html = get_inlined_html(problem_html, base_path=str(project_root))
    output_path.write_text(inline_html, encoding="utf-8")
    return output_path


def main():
    created_file = create_problem_html(TITLE, INSTRUCTIONS, INITIAL, PROBLEM_NAME)
    print(f"Created problem file: {created_file}")


if __name__ == "__main__":
    main()

