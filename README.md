# Visual learning PDF exercis file generator [![Build Status](https://travis-ci.org/bieli/visual-learning-generator.png)](https://travis-ci.org/bieli/visual-learning-generator)
=====


How to run?
-----

$ python3.7 -m venv venv
$ source venv/bin/activate
(venv) $ pip3 install -r requirements.txt
(venv) $ python3 visuallearning.py
(venv) $ evince visuallearning.pdf # to view output PDF generated file


How to run unit test ?
----

$ python3.7 -m venv venv
$ source venv/bin/activate
(venv) $ pip3 install -r requirements-dev.txt
(venv) $ make tests

