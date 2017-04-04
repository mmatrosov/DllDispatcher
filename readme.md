# Intro

DllDispatcher is the tool that allows to associate different applications with dll files based on bitness. One application for 32-bit dlls and another for 64-bit dlls. A notable (and the only that comes to my mind) example is associating dlls with corresponding versions of [Dependency Walker](http://www.dependencywalker.com).

# Installation

1. Install python. The tool was tested with python v3.6.1
2. Clone or download the repository
3. Set proper path to python executable in `DllDispatcher.bat`
4. Set proper path to associated applications in `DllDispatcher.py`
5. Associate dll files with `DllDispatcher.bat`