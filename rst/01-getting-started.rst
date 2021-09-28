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

This is simple. Pick a place on your system where you will be managing projects. On my system, I use a directory named **_dev** in my home directory. This project will be named **QtMMD** so this is the command I use to set up the project:

..	code-block:: shell

	$ cd _dev
	$ mkdir QtMMD

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

Most |PY| project rely on libraries of code written by other developers. These
libraries are usually posted on the |PYPI| website and installed using the
**pip** tool which is provided with |PY| installers. We create a single file
named **requirements.txt** where we list all the components we will need to set
up this project.

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

I use the popular documentation tool Sphinx_ to document my projects. We will
need to install Sphinx_, but that is already handled by adding the line in the
**requirements.txt** file.

We do need a bit more setup to be able to build documentaton.

All documentation files will be written in a markup language called |RST|, and
stored in an **rst** subdirectory in the project directory. The command we set
up in the **Makefile** will process these **rst** files and save generated HTML
files for the documentation in the **docs** folder. We will publish those web
pages for public view in a later step.

Here is how we generate the documentation:

..  code-block:: shell

    $ make docs

Step 5: Project Testing
=======================

All code developed for this project will be tested! I am using the PyTest_ tool
for this purpose since it supports the graphical environment we will be using
very nicely.

Basically, all we need to get started is to install PyTest_ and create a
**tests** directory. Any file within that directory that starts with **test_**
will be processed by PyTest_ and the results will be displayed on the console.
A simple starting test file that checks the versions of the important
components we need is shown below:

..  literalinclude::    ../tests/test_versions.py
    :linenos:
    :caption:    tests/test_versions.py

Running the tests is simple using our **Makefile**:

..  command-output:: make test
    :cwd:   ../

Step 6: Git and Github
======================

Any project worth working on deserves to be managed using a good *Source Code
Control System*. Today the best tool for that job is Git_. This free tool can
be installed on all systems and manages all files in a project by creating a
hidden directory named **.git** in the project folder. Once you are managing
the project with Git_, it makes sense to host the project files on a public
server where other devleopers can access your work. |GH| is my choice for
this server, so we will set things up there. An added bonus in using |GH| is
that the project documentation can be published on their web server meaning you
get  project website for free!

To start managing your project using Git_, use this command while working at th
e top-level project directory:

..  code-block:: shell

    $ git init

We will not actually want to manage everything in the project directory. We
tell Git_ not to manage certain files and directories by creating a
**.gitignore** file. For this project the file I use looks like this:

..  literalinclude::    ../.gitignore
    :linenos:
    :caption:   .gitignore

Hosting on |GH|
---------------

Once we have the project under Git_ management, we can set things up on
|GH|. Assuming you have an account there, create a new project repository
named **qtMMD**. You do not need to do anything other than create that
repository now. Once you click on the "Create" button, you will see a screen
telling you what to do next. Since we already have a working copy of the
project on our development system, all we need to do at this point is connect
our local project to the new |GH| repository.

..  code-block:: shell

    $ git remote add origin master https://github.com/rblack42/qtMMD.git
    $ git status
    $ git add .
    $ git commit -m "Initial project setup"
    $ git push origin master

..  todo::

    Add documentation explaining Git_ basics.

Step 7: Continuous Testing on |GH|
==================================

With |GH| set up and PyTest_ working, we can ask |GH| to tun tests on our
project code ever time we "push" changes to the project to the |GH| server.
This feature is nice in that it lest us test our code on all three major
platforms: Windows, Mac, and Linux. All of this is automatic once things are
set up!

Getting this testing running requires setting up a control file under a new
directory named **.github**. Here is the file we will be using:

..  literalinclude::    ../.github/workflows/python-app.yml
    :linenos:
    :caption:   .github/workflows/python-app.yml

Basically this file set up |GH| so it creates a new machine for each
platform, checks out out project and installs all required dependencies, then
runs the project tests. If all of this works, |GH| posts a graphics file
that we can view to see the result. This image is called a "badge" and
developers commonly put them in a **README** file that will display on |GH|
when you navigate to the project using your web browser.

Here is our basic **README** file:

..  literalinclude::    ../README.rst
    :linenos:
    :caption: README.rst

|GH| will turn this |RST| file into a nice web page for you automatically.
