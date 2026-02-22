# 🐍 Python Practice Projects

&nbsp;

A collection of **14 beginner-to-intermediate Python projects** built entirely in the terminal.
Each project focuses on a different concept — from string manipulation and file I/O to games,
timers, and password security. Great for anyone learning Python by doing.

&nbsp;

---

&nbsp;

## 📂 Project Overview

&nbsp;

```
python_practise_projects/
│
├── 01  ─  1_self_intro_script_generator.py       #  Personalized intro paragraph generator
|
├── 02  ─  2_stylish_bio_generator.py             #  Social media bio builder with 3 styles
|
├── 03  ─  3_simple_bill_splitter.py              #  Split bills evenly among friends
|
├── 04  ─  4_minutes_alive_calculator.py          #  Convert age → days / hours / minutes
|
├── 05  ─  5_emoji_enhancer_for_messages.py       #  Inject emojis after keywords in a message
|
├── 06  ─  6_daily_learn_journal_blogger.py       #  Append timestamped learning entries to file
|
├── 07  ─  7_terminal_based_task_list_manager.py  #  Full CRUD to-do list saved to tasks.txt
|
├── 08  ─  8_password_strength_checker.py         #  Check strength & suggest strong passwords
|
├── 09  ─  9_set_countdown_timer.py               #  Live MM:SS countdown in the terminal
|
├── 10  ─  10_color_mixer.py                      #  Mix two colours and get the result
|
├── 11  ─  11_guess_the_word.py                   #  Unscramble a jumbled word game
|
├── 12  ─  12_guess_number_game.py                #  Guess 1–100 in 10 attempts
|
├── 13  ─  13_calculator.py                       #  4-operation calculator with recursion
|
├── 14  ─  14_related_word_game.py                #  Timed word association game with scoring

```

&nbsp;

---

&nbsp;

## 🗂️ Projects by Category

&nbsp;

```
  ┌─────────────────────┬────────────────────────────────────────────────────┐
  │                     │                                                    │
  │   📝  Generators    |   #01  Self Intro Generator                        │
  │                     │   #02  Stylish Bio Generator                       │
  │                     │                                                    │
  ├─────────────────────┼────────────────────────────────────────────────────┤
  │                     │                                                    │
  │   🔢  Calculators   │   #03  Bill Splitter                               │
  │                     │   #04  Minutes Alive Calculator                    │
  │                     │   #13  Simple Calculator                           │
  │                     │                                                    │
  ├─────────────────────┼────────────────────────────────────────────────────┤
  │                     │                                                    │
  │   💾  File I/O      │   #06  Daily Learning Journal                      │
  │                     │   #07  Terminal Task Manager                       │
  │                     │                                                    │
  ├─────────────────────┼────────────────────────────────────────────────────┤
  │                     │                                                    │
  │   🎮  Games         │   #10  Color Mixer                                 │
  │                     │   #11  Guess the Word                              │
  │                     │   #12  Guess the Number                            │
  │                     │   #14  Word Association Game                       │
  │                     │                                                    │
  ├─────────────────────┼────────────────────────────────────────────────────┤
  │                     │                                                    │
  │   🛠️  Utilities     │   #05  Emoji Enhancer                              │
  │                     │   #08  Password Strength Checker                   │
  │                     │   #09  Countdown Timer                             │
  │                     │                                                    │
  └─────────────────────┴────────────────────────────────────────────────────┘
```

&nbsp;

---

&nbsp;

## 📋 Project Details

&nbsp;
&nbsp;

---

&nbsp;

### 01 — Self Intro Script Generator

&nbsp;

> **Concepts:** `input()` · f-strings · `datetime` · string formatting

&nbsp;

Takes user details and generates a warm, formatted self-introduction paragraph
with a decorative star border and today's date stamped at the bottom.

&nbsp;

```
   User Input                   Processing                    Output
   ──────────                   ──────────                    ──────

   Name        ──┐
   Age         ──┤                                            ********************************
   City        ──┼──────────►  Build intro  ──────────►       Hello! My name is Riya...
   Profession  ──┤              paragraph                     Logged on: 2025-06-14
   Hobby       ──┘              + add date                    ********************************
```

&nbsp;

**▶  Run:** `python 1_self_intro_script_generator.py`

&nbsp;

---

&nbsp;

### 02 — Stylish Bio Generator

&nbsp;

> **Concepts:** `input()` · functions · f-strings · file write · `textwrap`

&nbsp;

Generates a short social media bio in one of 3 layout styles.
Optionally saves the result to a `.txt` file.

&nbsp;

```
   Input Details
   ─────────────
   Name  ·  Profession  ·  Passion  ·  Emoji  ·  Website

                     │
                     ▼

            ┌─────────────────────────────────┐
            │       Choose Layout Style        │
            │                                  │
            │   1.  Simple Lines               │
            │   2.  Vertical Flair   🔥         │
            │   3.  Emoji Sandwich   ✨         │
            └──────────────┬───────────────────┘
                           │
               ┌───────────┴───────────┐
               │                       │
          Save to .txt             Print only
           file  💾              to terminal 🖥️
```

&nbsp;

**▶  Run:** `python 2_stylish_bio_generator.py`

&nbsp;

---

&nbsp;

### 03 — Simple Bill Splitter

&nbsp;

> **Concepts:** `input()` · loops · `round()` · exception handling

&nbsp;

Collects the names of everyone at the table, divides the total bill evenly,
and prints each person's share inside a clean summary box.

&nbsp;

```
   Enter number of people : 3
   Enter names            : Aman, Neha, Ravi
   Enter total bill       : 1200

                  │
                  ▼

          share  =  1200  /  3  =  400.00

                  │
                  ▼

        ┌──────────────────────────────────────┐
        │                                      │
        │   Total bill  :  1200                │ 
        │                                      │
        │   Aman  owes  400.00 rupees          │
        │   Neha  owes  400.00 rupees          │
        │   Ravi  owes  400.00 rupees          │
        │                                      │
        └──────────────────────────────────────┘
```

&nbsp;

**▶  Run:** `python 3_simple_bill_splitter.py`

&nbsp;

---

&nbsp;

### 04 — Minutes Alive Calculator

&nbsp;

> **Concepts:** arithmetic · `float()` · `round()` · loops · exception handling

&nbsp;

Converts an age in years into total days, hours, and minutes
using the formula: `age x 365.25 x 24 x 60`.

&nbsp;

```
   Input:  Age  =  25

                  │
                  ▼

        ┌──────────────────────────────────────────┐
        │                                          │
        │   days     =  25 x 365.25  =    9,131    │
        │   hours    =  days  x 24   =  219,144    │
        │   minutes  =  hours x 60   = 13,148,640  │
        │                                          │
        └──────────────────────────────────────────┘

                  │
                  ▼

   You are approximately:
     ·  9,131       days old
     ·  219,144     hours old
     ·  13,148,640  minutes old

                  │
                  ▼

   Try again? (y / n)
```

&nbsp;

**▶  Run:** `python 4_minutes_alive_calculator.py`

&nbsp;

---

&nbsp;

### 05 — Emoji Enhancer for Messages

&nbsp;

> **Concepts:** `dict` · `.split()` · `.strip()` · string iteration

&nbsp;

Scans every word in a typed message and appends a matching emoji after
recognised keywords. Case-insensitive and handles surrounding punctuation.

&nbsp;

```
   Keyword → Emoji Map
   ────────────────────────
   love   →   ❤️
   happy  →   😊
   code   →   💻
   tea    →   ☕️
   music  →   🎵
   food   →   🍕


   Input  :  "I love to code and drink tea when happy."

                        │
                        ▼  (word-by-word scan + dict lookup)

   Output :  "I love ❤️  to code 💻  and drink tea ☕️  when happy 😊."
```

&nbsp;

**▶  Run:** `python 5_emoji_enhancer_for_messages.py`

&nbsp;

---

&nbsp;

### 06 — Daily Learning Journal Logger

&nbsp;

> **Concepts:** `datetime` · file append `"a"` mode · formatted strings

&nbsp;

Prompts for today's learning entry and an optional productivity rating (1–5),
then appends the timestamped entry to `learning_journal.txt` — never overwrites.

&nbsp;

```
   User Input
   ──────────────────────────────────────────────
   Entry  :  "Learned about list comprehensions"
   Rating :   4  (out of 5)

                  │
                  ▼  (append mode — file grows each day)

        ┌──────────────────────────────────────────────┐
        │   learning_journal.txt                       │
        │                                              │
        │   📆  2025-06-14  -  10:45 AM               │
        │   Learned about list comprehensions          │
        │   Productivity Rating: 4                     │
        │   ──────────────────────────────────────     │
        │                                              │
        │   📆  2025-06-15  -  09:10 AM  ← next day   │
        │   Practiced recursion problems               │
        │   Productivity Rating: 5                     │
        │   ──────────────────────────────────────     │
        │   ...                                        │
        └──────────────────────────────────────────────┘
```

&nbsp;

**▶  Run:** `python 6_daily_learn_journal_blogger.py`

&nbsp;

---

&nbsp;

### 07 — Terminal Task List Manager

&nbsp;

> **Concepts:** file I/O · `match` statement · list of dicts · CRUD operations

&nbsp;

A fully persistent to-do list. Tasks survive between runs because they are
written to `tasks.txt`. Supports add, view, complete, and delete.

&nbsp;

```
        ┌──────────────────────────────────────┐
        │          Task List Manager           │
        │                                      │
        │   1.  Add Task                       │
        │   2.  View Tasks                     │
        │   3.  Mark Task as Complete          │
        │   4.  Delete Task                    │
        │   5.  Exit                           │
        └──────────────┬───────────────────────┘
                       │
          ┌────────────┼──────────────────────┐
          │            │                      │
         Add          View            Mark Done / Delete
          │            │                      │
          ▼            ▼                      ▼
      Append        Print list          Update status /
      to list       with ✅ / ☐         Remove entry
          │            │                      │
          └────────────┴──────────────────────┘
                       │
                       ▼  (saved after every single action)

              tasks.txt
              ──────────────────────────────────
              Buy groceries         ||  not_done
              Finish Python project ||  done
              Read a book           ||  not_done
```

&nbsp;

**▶  Run:** `python 7_terminal_based_task_list_manager.py`

&nbsp;

---

&nbsp;

### 08 — Password Strength Checker

&nbsp;

> **Concepts:** `string` · `random` · `getpass` · list comprehensions · conditionals

&nbsp;

Checks a password against 5 security rules, reports every failure,
and always suggests a randomly generated strong 12-character password.

&nbsp;

```
   Password Input  (hidden on screen via getpass)

                  │
                  ▼

        ┌──────────────────────────────────────────┐
        │           Strength Check Rules           │
        │                                          │
        │   ☐   Length >= 8 characters            │
        │   ☐   Has at least one lowercase letter  │
        │   ☐   Has at least one uppercase letter  │
        │   ☐   Has at least one digit             │
        │   ☐   Has at least one special char      │
        │         ( !  @  #  $  %  ^  &  * ... )  │
        └──────────────┬───────────────────────────┘
                       │
            ┌──────────┴──────────┐
            │                     │
        All pass              Any fail
            │                     │
       "Strong ✅"          List issues ❌
                                  │
                                  ▼
                     Suggested password:
                        " kR#9mZqL@2wP "
```

&nbsp;

**▶  Run:** `python 8_password_strength_checker.py`

&nbsp;

---

&nbsp;

### 09 — Countdown Timer

&nbsp;

> **Concepts:** `time.sleep()` · `divmod()` · `\r` overwrite · input validation

&nbsp;

Accepts seconds from the user and shows a live MM:SS countdown
that rewrites itself in place on the same terminal line.

&nbsp;

```
   Input:  90  seconds

                  │
                  ▼

   Timer started...

   Time left:  01:30
   Time left:  01:29
   Time left:  01:28
        ...
   Time left:  00:02
   Time left:  00:01

                  │
                  ▼

   ⏰  Time's up!  Take a break and move on to the next task.
```

&nbsp;

**▶  Run:** `python 9_set_countdown_timer.py`

&nbsp;

---

&nbsp;

### 10 — Color Mixer

&nbsp;

> **Concepts:** `dict` with tuple keys · `while` loop · `.lower()`

&nbsp;

Enter any two colour names and the app looks them up in a predefined mix table
to tell you the resulting colour. Order of input doesn't matter.

&nbsp;

```
   Mix Lookup Table
   ─────────────────────────────────────
   red   +  blue    →   purple
   red   +  yellow  →   orange
   blue  +  yellow  →   green
   blue  +  green   →   teal
   white +  red     →   pink
   red   +  green   →   brown


   Input:   red   +   blue

                  │
                  ▼   (lookup both orderings in dict)

   "When you mix red and blue, you get purple 🎨"

                  │
                  ▼

   Mix more colors? (y / n)
```

&nbsp;

**▶  Run:** `python 10_color_mixer.py`

&nbsp;

---

&nbsp;

### 11 — Guess the Word

&nbsp;

> **Concepts:** `random.shuffle()` · `list()` · loops · string comparison

&nbsp;

Picks a random word from a preset word bank, scrambles the letters,
and challenges you to unscramble it correctly.

&nbsp;

```
   Word Bank
   ─────────────────────────────────────────
   python  ·  coding  ·  game  ·  computer
   fun  ·  learn

                  │
                  ▼  random.choice()  +  random.shuffle()

   Scrambled word:  "t h o n p y"

                  │
                  ▼

   User guesses:  "python"

                  │
            ┌─────┴──────┐
            │             │
         Correct        Wrong
            │             │
     "🎉 Congrats!"   "😢 The word was: python"
            │             │
            └──────┬───────┘
                   │
                   ▼
           Try again? (y / n)
```

&nbsp;

**▶  Run:** `python 11_guess_the_word.py`

&nbsp;

---

&nbsp;

### 12 — Guess the Number Game

&nbsp;

> **Concepts:** `random.randint()` · nested loops · `try/except` · comparison operators

&nbsp;

The computer picks a secret number between 1 and 100.
You have 10 attempts, with a directional hint after every guess.

&nbsp;

```
   Secret number  =  random integer  ( 1 – 100 )
   Max attempts   =  10

                  │
                  ▼

        ┌──────────────────────────────────────────┐
        │                                          │
        │   Attempt  1 / 10  →  Guess:  50         │
        │   ▸  "Too low!  Try higher."             │
        │                                          │
        │   Attempt  2 / 10  →  Guess:  75         │
        │   ▸  "Too high!  Try lower."             │
        │                                          │
        │   Attempt  3 / 10  →  Guess:  63         │
        │   ▸  "🎉 Correct! Solved in 3 attempts!" │
        │                                          │
        └──────────────────────────────────────────┘

                  │
                  ▼

   Play again? (yes / no)
```

&nbsp;

**▶  Run:** `python 12_guess_number_game.py`

&nbsp;

---

&nbsp;

### 13 — Simple Calculator

&nbsp;

> **Concepts:** functions · `try/except` · `float()` · recursion

&nbsp;

Performs one of four arithmetic operations on two numbers.
Calls itself recursively if the user wants another calculation.

&nbsp;

```
   ==== Simple Calculator ====

   1.  +   Addition
   2.  -   Subtraction
   3.  *   Multiplication
   4.  /   Division

                  │
                  ▼   (choose 1 – 4)

        ┌──────────────────────────────────┐
        │                                  │
        │   add ( x, y )   →   x + y      │
        │   sub ( x, y )   →   x - y      │
        │   mul ( x, y )   →   x * y      │
        │   div ( x, y )   →   x / y      │
        │         ( division by 0 caught ) │
        │                                  │
        └───────────────┬──────────────────┘
                        │
                        ▼

   Another calculation?  →  calls  main()  again  ♻️
```

&nbsp;

**▶  Run:** `python 13_calculator.py`

&nbsp;

---

&nbsp;

### 14 — Word Association Game

&nbsp;

> **Concepts:** `time.time()` · `random.choice()` · dict · scoring · loops

&nbsp;

A prompt word appears and you must type a related word as fast as possible.
Speed matters — the slower you answer, the fewer points you earn (max 5 per round).

&nbsp;

```
   Word Association Table  (sample)
   ─────────────────────────────────────────────────
   sky    →   blue · cloud · red · fly · sun
   water  →   drink · ocean · swim · fish · boat
   dog    →   pet · bark · walk · loyal · puppy
   ...


   Prompt:  D O G
   Quick!  Type a related word:
   >  "bark"      ← answered in  1.2 seconds

                  │
                  ▼

   points  =  max( 1,  5 - int(1.2) )  =  4 pts  ✅

   Score:  4 / 5 possible points

                  │
                  ▼

   Play again? (yes / no)


   ─────────────────────────────────────────────────
   Scoring Formula
   ─────────────────────────────────────────────────
   points  =  max( 1,   5  -  seconds_taken )
                    ↑              ↑
               minimum 1      time taken to answer
   ─────────────────────────────────────────────────
```

&nbsp;

**▶  Run:** `python 14_related_word_game.py`

&nbsp;

---

&nbsp;

## 🧠 Python Concepts Coverage

&nbsp;

```
  ┌──────────────────────────────────────────────────────────────────────────┐
  │                        Concepts Map                                      │
  │                                                                          │
  │   Input / Output       ████████████████████████   All 14 projects        │
  │                                                                          │
  │   f-strings            ████████████████████       #01–08 · #12–13        │
  │                                                                          │
  │   Loops (while/for)    ██████████████████████     #03–14                 │
  │                                                                          │
  │   Functions (def)      ████████████████           #03 · #04 · #08 · #13  │
  │                                                                          │
  │   Dictionaries         ████████████               #05 · #10 · #14        │
  │                                                                          │
  │   File I/O             ████████                   #06 · #07              │
  │                                                                          │
  │   Exception Handling   ████████                   #03 · #04 · #08–09·#12 │
  │                                                                          │
  │   random module        ██████                     #11 · #12 · #14        │
  │                                                                          │
  │   datetime module      █████                      #01 · #06              │
  │                                                                          │
  │   time module          ████                       #09 · #14              │
  │                                                                          │
  │   match statement      ██                         #07                    │
  │                                                                          │
  │   getpass module       █                          #08                    │
  │                                                                          │
  └──────────────────────────────────────────────────────────────────────────┘
```

&nbsp;

---

&nbsp;

## 🚀 How to Run Any Project

&nbsp;

```bash
# Clone the repository
git clone https://github.com/your-username/python_practise_projects.git
cd python_practise_projects

# Run any project directly — no pip installs needed
python 1_self_intro_script_generator.py
python 7_terminal_based_task_list_manager.py
python 12_guess_number_game.py
```

&nbsp;

> **Requirements:** Python 3.10 or higher (project 07 uses the `match` statement introduced in 3.10).
> No external libraries are needed — all projects use the Python standard library only.

&nbsp;

---

&nbsp;

## 📄 License

&nbsp;

Open source under the [MIT License](LICENSE).

&nbsp;
