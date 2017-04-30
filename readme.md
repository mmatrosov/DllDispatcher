# Intro

DllDispatcher is the tool that allows to associate different applications with dll files based on bitness. One application for 32-bit dlls and another for 64-bit dlls. A notable (and the only that comes to my mind) example is associating dlls with corresponding versions of [Dependency Walker](http://www.dependencywalker.com).

# Installation

1. Install python. The tool was tested with python v3.6.1
2. Install `pywin32` package
3. Clone or download the repository
4. Set proper paths to associated applications in `DllDispatcher.ini`
5. Associate `.dll` files with `DllDispatcher.bat`
6. Optionally, set proper path to python executable in `DllDispatcher.bat` (`python.exe` from system path is used by default)
