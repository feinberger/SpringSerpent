# Spring Serpent
This is a prototype development project for an automated spring winder developed by Glenn Feinberg. This demonstrates motor functionality with a demo-able user interface used to prove out key requirements for this project. The project final documentation can be found in the documentation folder.

## Notes and Installation
1. Get source code:
```sh
$ git clone https://github.com/feinberger/Temp-o-Matic-Hub-v2.git
```
2. Install pyqt requirements
```sh
$ sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
$ sudo apt-get install qttools5-dev-tools
```
3. Install python dependencies
```sh
$ python3 -m pip install -r requirements.txt
```
4. Build cpp program 
```sh
$ make PLATFORM=RPI
```
5. Navigate to local folder and run application. This starts both servers and the on-board GUI.
```sh
$ python3 main.py
```
6. Run C++ Application in seperate terminal
```sh
$ sudo ./build/Teknic.out
```
