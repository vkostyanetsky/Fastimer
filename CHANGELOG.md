# Changelog

## [Unreleased]

### Fixed

* The `Display Active Fast` command now properly shows `Extra time` parameter for a completed fast, instead of `Remaining: None`. 

## [1.1.0] - 2022-07-26

### Added

* A new `Display Fasting Statistics` menu option. Shows the number of fasts, total fasting hours, achievements, and other accumulated information.
* A progress bar to show how much of fast is done (see the `Display Active Fast` command).
* Fasting zones calculation (see the `Display Active Fast` command). 

### Fixed

* If a fast goal is less than a current moment, the `Display Active Fast` command will show excess time instead of negative remaining time (as before).
* Microseconds were removed from dates in the `fasts.yaml` file.

## [1.0.3] - 2022-07-22

### Added

* Basic fasts management (start, stop, and view).
* Providing a user various information about an active fast (length, elapsed time, remaining time, etc.).
* Ability to work in any directory if installed via pip.