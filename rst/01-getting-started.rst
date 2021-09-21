Getting Started
###############

In this series of notes, we will create a |GUI| for the |MM| Designer
application, a tool intended to help model builders design a variety of model
airplanes. This application uses the |OSC| tool to visualize a design, and |PY|
to perform analysis work on the design. Users of this tool will only need to
install the application we will be creating and |OSC| to begin their design
work.

These notes are not intended for end-users of the application. Rather, they are
intended for software developers who might wish to contribute to the project.
The notes are presented in the form of a diary laying out the development of
the application. MY long history of teaching college-level  computer science
courses contributes to my writing style, which I hope proves useful to future
contributors.

Project Setup
*************

This application is being written in Python, a language commonly used to teach
software development these days. |PY| is freely available and can be installed
on any modern computer.

I prefer to work from the command line in developing software. Part of that
comes from a desire to know exactly how my project is set up and how you manage
it. I have always asked my students to learn how to manage project this way so
they really understand the development process. Other developers prefer to use
an |IDE|. The choice is yours.

All projects need to have a home on the developer's system, and in today's
development world, all |PY| projects are managed using a |VENV| which serves to
keep app project dependencies separate from other software that might be on
that system. |PY| can create the |VENV|, but since I develop on a Mac, I prefer
to use the DirEnv_ tool to set up the project. Furthermore, I use a common
project management tool called Make_ to both document the steps needed to
manage a project, and simplify running those steps.

Step1: Create the Project Directory
===================================

This is simple. Pick a place on your system where you will be managing projects. On my system, I use a directory named **_dev** in my home directory. This project will be named **qtMMD** so this is the command I use to set up the project:

..	vode-block:: shell

	$ cd _dev
	$ mkdir qtMMD

Step2: Create the |VENV|
========================

Before we can create any code, we need to set up the |VENV|. I will document
the steps needed to do this by writing the start of a project **Makefile**
which will be used by the Make_ tool to run commands.

..	note::

    I will not detail how to use Make_ in these notes. More information can be
    found on my teaching website at https://www.co-pylit.org.

..	literalinclude::	../Makefile
	:linenos:
	:caption: Makefile

With this file in place, we set up the |VENV| as follows:

..  $ make venv

Step 3: Install Depencencies
============================

Most |PY| project rely on libraries of code weitten by other developers. These libraries are usually posted on the |PYPI| website and installed using the **pip** tool which is provided with |PY| installers. We create a single file named **requirements.txt** where we list all the components we will need to set up this project.

Here is the start on that for this project:

..  literalinclude::    ../requirements.txt
    :linenos:
    :caption: requirements.txt

With this file in place, installing the dependencies looks like this:

..  code-block:: shell

    $ make reqs

..  note::

    You can run this command any time you add a new component to the
    **requirements.txt** file. **pip** checks the version numbers on each
    component and only installs those that are not currently present in the
    |VENV|.


Step 4: Setting up Documentation
================================

If documenting your project is not one of the first things you think about as a
developer, you are doing things wrong!

I use the popular documentation dool Sphinx_ to document my projects. We will
need to install Sphinx_, but that is already handled by adding the line in the
**requirements.txt** file.

We do need a bit more setup to be able to build documentaton.

All documentation files will be writtin in a markup language called |RST|, ans
stored in an **rst** subdirectory in the project directory. The command we set
up in the **Makefile** will process these **rst** files and save generated HTML
files for the documentataion in the **docs** folder. We will publish those web
pages for publicj view in a later step.


