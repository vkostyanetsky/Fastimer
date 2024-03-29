# Changelog

## 1.3.1 - 2023-08-22

### Added

- Good old CLI interface (instead of menu).
- Coloring some messages to make them easy to spot.

### Changed

- Menu has been removed.
- Support for the modern package versions.

## 1.2.3 - 2023-02-11

### Added

* New hotkeys were added for the fast browser.

### Fixed

* Some bugs were fixed.

## 1.2.2 - 2022-08-21

### Fixed

* Fixed a library version in a description of the package.

## 1.2.1 - 2022-08-20

### Added

* Updated the auxiliary library `vkostyanetsky.cliutils`. 

## 1.2.0 - 2022-08-17

### Added

* The main menu items were renamed.
* Added an option to cancel an active fast.
* Information about an active fast now displays in the main menu.  
* Implemented an interface allows a user to have a look at previous fasts. 
* Added more precise description for each achievement & a page with [the full list](ACHIEVEMENTS.md) of possible awards.

### Fixed

* The `Statistics` command received a new logic to calculate fasting streaks (I hope this one will last us for a good while).
* The `Statistics` command now considers a fast as completed only if it did not end earlier than planned. 

## 1.1.1 - 2022-07-28

### Fixed

* The `Display Active Fast` command now properly shows `Extra time` parameter for a completed fast, instead of `Remaining: None`.
* The `Display Fasting Statistics` command now properly calculates fasting streaks.

## 1.1.0 - 2022-07-26

### Added

* A new `Display Fasting Statistics` menu option. Shows the number of fasts, total fasting hours, achievements, and other accumulated information.
* A progress bar to show how much of fast is done (see the `Display Active Fast` command).
* Fasting zones calculation (see the `Display Active Fast` command). 

### Fixed

* If a fast goal is less than a current moment, the `Display Active Fast` command will show excess time instead of negative remaining time (as before).
* Microseconds were removed from dates in the `fasts.yaml` file.

## 1.0.3 - 2022-07-22

### Added

* Basic fasts management (start, stop, and view).
* Providing a user various information about an active fast (length, elapsed time, remaining time, etc.).
* Ability to work in any directory if installed via pip.