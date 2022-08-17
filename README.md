# ⏲ ⏰ 🕰️ Fastimer

[![PyPi](https://img.shields.io/pypi/v/fastimer)](https://pypi.org/project/fastimer/) [![flake8](https://github.com/vkostyanetsky/Fastimer/actions/workflows/flake8.yml/badge.svg)](https://github.com/vkostyanetsky/Fastimer/actions/workflows/flake8.yml) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)   

It is a little CLI timer to track fasts, designed specifically to help you monitor your fasting intervals.  

## 😮 What's this for? There are a lot of apps like this one!

Well, I wrote this one out of annoyance when [Zero](https://www.zerolongevity.com/) once again refused to show me statistics for a date. I was tapping on calendar inside the application, but it was doing nothing ¯\\\_(ツ)\_/¯

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

1. Start New Fast
2. Fasts Browser
3. Statistics  

### Start New Fast

Something is obvious: so, the first command starts a new fast. It will ask you for a length of the fast and enables the timer.

You can control active fast directly from the main menu. For instance, if the fast is active, it can look like this:

```
  ┌───────────────────────────────────────────────────────────────────────────┐
  │  FASTING TIMER                                                            │
  ├───────────────────────────────────────────────────────────────────────────┤
  │                                                                           │
  │    ACTIVE FAST                                                            │
  │                                                                           │
  │    From: Tue, 20:31                                                       │
  │    Goal: Wed, 10:31 (14 hours)                                            │
  │                                                                           │
  │    ######################################-- 97.3%                         │
  │                                                                           │
  │    Elapsed time:   13h 36m                                                │
  │    Remaining:      00h 24m                                                │
  │                                                                           │
  ├───────────────────────────────────────────────────────────────────────────┤
  │                                                                           │
  │    1 - Stop Active Fast                                                   │
  │    2 - Fasts Browser                                                      │
  │    3 - Statistics                                                         │
  │    4 - Exit                                                               │
  │                                                                           │
  └───────────────────────────────────────────────────────────────────────────┘
```

As you can see, the first command above is replaced by another one. Its meaning is obvious as well: begin selected, it asks you whether you want to finish your fast or cancel it. Finishing means you want to store the fast in the app history; cancelling means you want to delete the information about this fast by a reason. 

### Fasts Browser

The second command of the main menu, "Fasts Browser" allows you to browse through your fasts.

By default, it shows you the very last one, but you switch fasts by using [Left] and [Right] buttons on your keyboard. 

```
COMPLETED FAST

From: Mon, 19:27
Goal: Tue, 09:27 (14 hours)

Fasting zones:

- Anabolic:     from Mon, 19:27
- Catabolic:    from Mon, 23:27 <-- you were here
- Fat burning:  from Tue, 11:27
- Ketosis:      from Tue, 19:27
- Anabolic:     from Thu, 19:27

######################################## 101.3%

Elapsed time:   14h 11m
Extra time:     00h 11m

Press [Left] and [Right] to switch fasts.
Press [Esc] to return to the main menu.
```

### Statistics

The `Statistics` command shows you statistical data and [earned achievements](Achievements.md).

For instance:

```
FASTING STATISTICS

Completed Fasts:         32 out of 33
Total Fasting Time:      423h 15m
Average Fast Length:     13h 13m
Longest Fast Length:     18h 12m
Longest Fasting Streak:  20 days
Current Fasting Streak:  2 days

Achievements:
- COPPER SENSE OF PURPOSE (level 2 badge out of 9). Twenty five fasts completed!
- COPPER HABIT (level 2 badge out of 9). Ten completed fasts in a row!
```

## 😌 Questions 

### Where I can see or edit my fasts?

The script stores all the fasts in `fasts.yaml` file in the working directory (where you run the timer). The file is quite human-readable, so you can just open it in your lovely text editor.

For instance, the completed fast in the journal looks like this:

```yaml
- length: 16
  started: 2022-07-20 19:59:14
  stopped: 2022-07-21 12:00:33
```

The first parameter is the length of the fast, the second is the start date of this, and the third is the completion date.

For an active fast, the `stopped` parameter is omitted.