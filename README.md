# ⏲ ⏰ 🕰️ Fastimer

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![PyPi](https://img.shields.io/pypi/v/fastimer)](https://pypi.org/project/fastimer/)

It is a little CLI timer to track fasts, designed specifically to help you monitor your fasting intervals.  

## 😮 What's this for? There are a lot of apps like this!

Well, I wrote this one out of annoyance when [Zero](https://www.zerolongevity.com/) once again refused to show me the statistics for a date. I was tapping on the calendar, but the app was doing nothing ¯\\\_(ツ)\_/¯

Have no idea what was wrong with it. Anyway, the problem is not that hard, so I just wrote my own timer.

## 🙃 How to install it?

```commandline
pip install fastimer
```

## 🙂 How to use it?

Simply run the script in the directory where you want to store data:

```commandline
fastimer
```

The script shows you a menu with three commands available: 

1. Display Fast
2. Start Fast
3. End Fast

The first one shows you how active fast is going on. For instance:

```
Started:        Mon, 20:19
Goal:           Tue, 14:19 (18 hours)

Elapsed time:   04:15
Remaining:      13:44

| #########------------------------------- | 23.7%
```

The second command starts a new fast, and the third one ends the active one.

## 😌 Where I can see or edit my fasts?

The script stores all the fasts in `journal.yaml` file in the working directory. The file is quite human-readable, so you can just open it in your lovely text editor.

For instance, the completed fast in the journal looks like this:

```yaml
- length: 16
  started: 2022-07-20 19:59:14.210099
  stopped: 2022-07-21 12:00:33.906634
```

The first parameter is the length of the fast, the second is the start date of this, and the third is the completion date.

For an active fast, the last parameter is omitted.