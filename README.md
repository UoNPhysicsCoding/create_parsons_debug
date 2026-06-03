# create-parsons-debug

Small toolkit to build js-parsons interactive problems (rearrange, debug, toggle).

## Setup (use UV)

Install `uv-astral` following the official guide: https://docs.astral.sh/uv/getting-started/installation/

This project requires Python >= 3.8.1. Then from the project root run `uv sync` to create the environment and install project deps. After that activate the created `.venv` and install the package in editable mode:

```powershell
# from project root install / update libraries
uv sync
# In the scripts folder open the python script corresponding to the type of problem and edit the All Caps variables
# to modify the key input. You can set the with_unittests = True to show the student feedback or false if for example
# you want to use the problem in a test.
uv run python ./scripts/<name of python script>
```

## How to deploy

In order for these problems to work you need the html file generated in output. You also need to copy the folder `static` containing the css and javascript into the same folder as the html file wherever you are planning to use it, eg a website. If you want to embed this in your Jupyter notebook, you can use a code cell and the Ipython display module to display the html file. I put them in a .exercises folder so that its hidden from students in the template we created.For example:

```python
from IPython.display import IFrame
IFrame('.exercises/test_problem.html', width=800, height=600)
```

## Running student tests locally

Place student code in `create_parsons_debug/tests/student_tests/student_solution.py` (or update imports in the tests), then run:

## Credit

I have built this largely as a wrapper with modifications to underlying problems using (js-parsons repo)[https://js-parsons.github.io/] as a starting point. Credit where credit is due.

Publications based on js-parsons
--------------------------------

Petri Ihantola and Ville Karavirta. [Two-Dimensional Parson's Puzzles: The Concept, Tools, and First Observations] (http://www.jite.org/documents/Vol10/JITEv10IIPp119-132Ihantola944.pdf). Journal of Information Technology Education: Innovations in Practice, 10:1–14, 2011.

Juha Helminen, Petri Ihantola, Ville Karavirta, and Lauri Malmi. 2012. How do students solve parsons programming problems?: an analysis of interaction traces. In Proceedings of the ninth annual international conference on International computing education research (ICER '12). ACM, New York, NY, USA, 119-126. [DOI=10.1145/2361276.2361300](http://doi.acm.org/10.1145/2361276.2361300)

Ville Karavirta, Juha Helminen, and Petri Ihantola. 2012. A mobile learning application for parsons problems with automatic feedback. In Proceedings of the 12th Koli Calling International Conference on Computing Education Research (Koli Calling '12). ACM, New York, NY, USA, 11-18. [DOI=10.1145/2401796.2401798](http://doi.acm.org/10.1145/2401796.2401798)

Juha Helminen, Petri Ihantola, Ville Karavirta, and Satu Alaoutinen. 2013. How Do Students Solve Parsons Programming Problems? -- Execution-Based vs. Line-Based Feedback. In Proceedings of Learning and Teaching in Computing and Engineering (LaTiCE), 2013  [DOI=10.1109/LaTiCE.2013.26](http://dx.doi.org/10.1109/LaTiCE.2013.26)


Authors
-------

* Ville Karavirta
* Petri Ihantola
* Juha Helminen
* Mike Hewner
