# ⏲ ⏰ 🕰️ Fastlog

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A little console timer to calculate fasting zones. I wrote this out of annoyance when [Zero](https://www.zerolongevity.com/) once again refused to show me the statistics it accumulates. I tap on the calendar, it does nothing. Geez-Louise!

It's not that hard, after all, so I just did it on my own.

## 😮 What's this for?

The script copies part of the Zero functionality in the Timer section. If you've ever used it, you know what I mean.

## 🙃 How to use it?

There is only one script, so the answer is rather obvious:

```commandline
py fastlog.py
```

Being executed, the script shows you a menu with three commands available: 

1. Display fast
2. Start fast
3. End fast

The first one shows you how active fast is going on. For instance:

```
CURRENT FAST:    16 HOURS

Elapsed time:    00:38:27
Remaining:       15:21:33
        
Started:  Wed, 21:15
Goal:     Thu, 13:15
```

The second command starts a new fast, and the third one ends the active one.

## 😌 Where to see my fasts?

The script stores all the fasts in the `journal.yaml` file. It is human-readable, so you can just open it in your lovely text editor. 