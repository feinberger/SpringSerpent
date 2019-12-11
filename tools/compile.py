import os


def compile_qt_ui():
    # Get current working directory
    current_directory = os.getcwd()
   
    # Add .bat file to path
    compile_file = os.path.join(current_directory, "qt_compile.bat")

    # Run bat file to compile .ui to .py
    os.system('"' + compile_file + '"')


if __name__ == "__main__":
    compile_qt_ui()
