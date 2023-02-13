{{ '=' * cookiecutter.application_name|length }}
{{ cookiecutter.application_name }}
{{ '=' * cookiecutter.application_name|length }}

*Generated from cookiecutter-bireli-newapp=={{ cookiecutter._bireli_newapp_version }}*

This is the install notice for this created new application structure.

Install
*******

This generated directory contains two folders: ::

    .
    ├── composition_repository/{{ cookiecutter.application_module }}/
    └── django-apps/{{ cookiecutter.application_module }}/

Copy each ``{{ cookiecutter.application_module }}`` folder in their respective parent
directory into your project.

When it is done, you just have to edit your project config ``pyproject.toml``. Search
for the variable ``collection`` in section ``[tool.project_composer]`` and add this new
line: ::

    "{{ cookiecutter.application_module }}",

Then use the Composer checking command and ensure Composer has found your application
part modules (settings, urls, etc..).

If it's ok, you can start to work on it. Remember that this new application have no
migrations yet (to let you develop your own models). So you will need to create your
application migrations and apply them before to use your application.

It is required you clean this application from unused sample stuff before to commit it
into your project.
