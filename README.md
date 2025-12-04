# Advent of Code

My solutions to [Advent of Code](adventofcode.com) puzzles, written in **Python**.

## Structure of the repository

```
📂AoC
├─── 📄template.py
└─── 📂YEAR
     ├─── 📂inputs
	 |   └─── 📄day-N.txt
     └─── ⚙️day-N.py
```

- The file `📄template.py` contains a template for the files with the solution code of the day.
- The folders `📂YEAR` (named after the year, e.g. `2024`) contain all the files related to the year.
- The files `⚙️day-N.py` (where `N` is the number of the day, e.g. `day-1`) contain the solution code of the day.
- The `📂inputs` folder contains all the input files (named the same way as the solution code files, but with the `.txt` extension).

The `📂inputs` folder isn't in the repository's code, according to the Advent of Code ToS, but is required to run the code.

## How to run the code

1. Make sure that you have Python [installed](https://www.python.org/downloads/) on your device.
2. [Clone the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) in your device.
3. Open the repository using the console of your OS (e.g. [cmd](https://it.wikipedia.org/wiki/Cmd.exe) for Windows).
4. Start the desired file using the command `python YEAR/day-N.py`, replacing `YEAR` with the year and `N` with the day of the puzzle you want to see the code (e.g. `python 2024/day-1.py`).

Before the last step, make sure that you have created the `📂inputs` folder inside the selected year and that you have created, inside that folder, the `day-N.txt` file, containing the input of the puzzle.
You can get your puzzle input subscribing to [Advent of Code](https://adventofcode.com/2024/events) and going to the URL `https://adventofcode.com/YEAR/day/N/input`.
As always, `YEAR` is the year and `N` is the day of the desired puzzle.

## Use of my code

This software is shared as open source.
However, if you use it in your own solutions, consider giving acknowledgement to me, linking back this repo.