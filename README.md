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

The script shows you a menu with four commands available: 

1. Start New Fast
2. Manage Active Fast
3. Display Statistics  

Something is obvious: so, the first command starts a new fast. The second one displays submenu: 

1. End Fast
2. Cancel Fast
3. Display Fast

The first command here enables you to end active fast, second one means the cancelling of active fast. Third one shows you how active fast is going on.

For instance:  

```
ACTIVE FAST

Started:        Mon, 20:19
Goal:           Tue, 14:19 (18 hours)

Fasting zones:

- Anabolic:     from Mon, 20:19
- Catabolic:    from Tue, 00:19 <-- you are here
- Fat burning:  from Tue, 12:19
- Ketosis:      from Tue, 20:19
- Deep ketosis: from Thu, 20:19

Elapsed time:   13:38
Remaining:      04:21

| ##############################---------- | 75.8%
```

The `Display Statistics` command shows you some statistics & [achievements](Achievements.md) you were able to unlock (total fasting time, average fast length etc.).

For instance:

```
FASTING STATISTICS

Completed Fasts:         8
Total Fasting Time:      120h 59m
Average Fast Length:     15h 7m
Longest Fast Length:     18h 12m
Longest Fasting Streak:  3 days
Current Fasting Streak:  1 days

Achievements:
- WOODEN PERSISTENCE (level 1 badge out of 9). Five fasts completed!
```

## 😌 Where I can see or edit my fasts?

The script stores all the fasts in `fasts.yaml` file in the working directory. The file is quite human-readable, so you can just open it in your lovely text editor.

For instance, the completed fast in the journal looks like this:

```yaml
- length: 16
  started: 2022-07-20 19:59:14
  stopped: 2022-07-21 12:00:33
```

The first parameter is the length of the fast, the second is the start date of this, and the third is the completion date.

For an active fast, the `stopped` parameter is omitted.