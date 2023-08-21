# ⏱️ ⏰ 🕰️ Fastimer

[![PyPi](https://img.shields.io/pypi/v/fastimer)](https://pypi.org/project/fastimer/) [![pylint](https://github.com/vkostyanetsky/Fastimer/actions/workflows/pylint.yml/badge.svg)](https://github.com/vkostyanetsky/Fastimer/actions/workflows/pylint.yml) [![black](https://github.com/vkostyanetsky/Fastimer/actions/workflows/black.yml/badge.svg)](https://github.com/vkostyanetsky/Fastimer/actions/workflows/black.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

It is a simple CLI timer to track fasts, designed specifically to help you monitor your fasting intervals.  

## 😮 What's this for?

Yeah, there are plenty of apps like this one, you are right. I wrote this one simply out of annoyance when [Zero](https://www.zerolongevity.com/) app for Android once again refused to show me a fast I did. I was tapping on calendar inside the application, but it was doing nothing.

Have no idea what was wrong with it. Anyway, the task is not that hard, so I just wrote my own timer ¯\\\_(ツ)\_/¯

## 🙃 How to install it?

I have nothing to surprise you here:

```commandline
pip install fastimer
```

## 🙂 How to use it?

It is a console application. So you can run this:

```commandline
fastimer --help
```

The script will show you available commands. 

By default, Fastimer supposes that you store your data in `%USERPROFILE%\Fastimer`. Of course, you can store it anywhere else (using a directory junction, for instance).

## Starting a New Fast

First of them is `start`. Something is obvious: this starts a new fast. Usage:

```commandline
fastimer start 20
```

Twenty here is a number of hours you are going to spend fasting. You can omit this option (default is 16).

## Control The Ongoing Fast

Once you have started a fast, it is convenient to use `fastimer show` command. It shows elapsed time, remaining time and something that looks like a progress bar to visualize your spilled blood, sweat, and tears :-)

Here is an example:

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

## Stopping The Ongoing Fast

When the fast is active, the `fastimer stop` command allows you to stop your fast when you decided to do so. It means that the fast is over, and you wish to store the fast in the app's history.

## Cancelling The Ongoing Fast

Another option to do it is `fastimer cancel`.  It means you wish to delete the information about this fast by some reason. 

### Information

```commandline
fastimer info
```

This command shows you statistical data and earned [achievements](ACHIEVEMENTS.md).

For instance:

```
FASTING STATISTICS

Completed Fasts:         33 out of 34
Total Fasting Time:      437h 26m
Average Fast Length:     13h 15m
Longest Fast Length:     18h 12m
Longest Fasting Streak:  20 days
Current Fasting Streak:  3 days

Achievements:
- COPPER WALKER (level 2 badge out of 9). Twenty five fasts completed!
- COPPER MAN OF HABIT (level 2 badge out of 9). Ten completed fasts in a row!
```

## 😌 Questions 

### Where can I see or edit my fasts?

The script stores all the fasts in `fasts.yaml` file in the working directory (where you run the timer). It has [YAML](https://en.wikipedia.org/wiki/YAML) format, which is quite human-readable, so you can just open it in your lovely text editor.

For instance, the completed fast in the journal looks like this:

```yaml
- length: 16
  started: 2022-07-20 19:59:14
  stopped: 2022-07-21 12:00:33
```

The first parameter is the length of the fast, the second is the start date of this, and the third is the completion date.

For an active fast, the `stopped` parameter is omitted.