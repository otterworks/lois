LCM OpenCV Image Spy (LOIS)
===========================

dependencies
------------

```
sudo apt install python3 python3-pip python3-venv python3-opencv
```

install
-------

```
python3 -m venv /tmp/lois
source /tmp/lois/bin/activate
lcm-gen -p --ppath src/lois/lcmtypes src/lois/lcmtypes/*.lcm
python3 -m pip install .
```

run spy
-------
```
python3 -m lois.spy vim1
```

extract images from a log
-------------------------
```
python3 -m lois.extract -v example.lcmlog vim0
```
