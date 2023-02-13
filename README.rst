.. _Python: https://www.python.org
.. _virtualenv: https://virtualenv.pypa.io
.. _pip: https://pip.pypa.io
.. _Django: https://www.djangoproject.com/
.. _Project composer: https://project-composer.readthedocs.io/en/latest/
.. _Cookiecutter: https://cookiecutter.readthedocs.io/en/stable/
.. _Bireli: https://cookiecutter-bireli.readthedocs.io/


=====================================
Bireli template for a new application
=====================================

This is a template used in `Bireli`_ to create everything for a new application.


Requirements
************

You just need `Cookiecutter`_ version 2.x and obviously a Bireli project where to
add the generated application.


Content
*******

The goal of this application template is to create everything to easily and quickly add
a new application to a Bireli project.

It generates the Composer application and the application module itself with all you
could expect for a Django application (model, url, view, admin, form, template, etc..)
properly structured.

Once deployed into your project the application is ready to work. Application
*deployment* process is explained in included README, it is only about to copy/paste
two directories and edit a file.

The generated application only contains a very basic model *Sample*. Obviously, it won't
fit to your specifications and you may want quickly to work on your own models.

If it is you first experience with Bireli or this application template, we recommend
you first to add it to your project in a dummy branch just to test it.


Usage
*****

Just invoke the `Cookiecutter`_ template to create a new project: ::

    cookiecutter https://github.com/sveetch/cookiecutter-bireli-newapp.git

This will create a directory alike ``foo_newapp`` where ``foo`` would be the
application name filled from cookiecutter interactive prompt.

The first prompt question will be for the *application title* that is the displayed
title. Then it will be used to automatically create proper variables used in code
(module name, class name, etc..) but you are free to edit them yourself, just don't
forget they must be a valid Python identifier.
