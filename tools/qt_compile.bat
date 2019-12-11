@echo OFF
title python QT ui compile bat file

@echo OFF

::Folder Paths
cd ..\designer\
SET UI_PATH=%cd%\
cd ..\src\SpringSerpent\ui\
SET PY_PATH=%cd%\
cd ..\..\..\resources\
SET RES_PATH=%cd%\

::Screens
SET MAIN_SCREEN=SpringSerpent
SET HOME_SCREEN=HomeScreen
SET NEW_JOB_SCREEN=NewJobScreen
SET MACHINE_SCREEN=MachineScreen
SET JOB_LIBRARY_SCREEN=JobLibraryScreen

:: Resources
SET QRC_FILE=Spring_Serpent_Resources

::Compile ui screens via pyuic5
echo Compiling Main Screen...
pyuic5 --from-imports -x "%UI_PATH%%MAIN_SCREEN%.ui" -o "%PY_PATH%%MAIN_SCREEN%.py"
echo Compiling Home Screen...
pyuic5 --from-imports -x "%UI_PATH%%HOME_SCREEN%.ui" -o "%PY_PATH%%HOME_SCREEN%.py"
echo Compiling New Job Screen...
pyuic5 --from-imports -x "%UI_PATH%%NEW_JOB_SCREEN%.ui" -o "%PY_PATH%%NEW_JOB_SCREEN%.py"
echo Compiling Machine Screen...
pyuic5 --from-imports -x "%UI_PATH%%MACHINE_SCREEN%.ui" -o "%PY_PATH%%MACHINE_SCREEN%.py"
echo Compiling Job Library Screen...
pyuic5 --from-imports -x "%UI_PATH%%JOB_LIBRARY_SCREEN%.ui" -o "%PY_PATH%%JOB_LIBRARY_SCREEN%.py"

::Compile resource file via pyrcc5
echo Compiling Resource File...
pyrcc5 "%RES_PATH%%QRC_FILE%.qrc" -o "%PY_PATH%%QRC_FILE%_rc.py"

echo Completed Compilation for QT Creator