# kvizz-bot

Kvizz-bot is one way of playing [the online quiz-game of OlÃ­s](https://kvizz.olis.is) automatically. The bot guesses random options and saves them for later use. After learning all the answers, each instance of the bot can play ca. 150 games per hour.

The bot can score unlimited coupons for overpriced candy bars. But please don't - it's probably immoral! ð±

~~July 15th 2021 - The bot does not work any more as the quiz prevents the email format used.~~

~~July 21st 2021 - It's working again!~~

September 1st 2021 - The game is now offline. 

![Could not load demo](https://github.com/thrkll/kvizz-bot/blob/main/demo.gif "Three instances of the bot")


### How to run

ð Edit settings in kvizz-bot.py

ð `python kvizz-bot.py`


### Requirements
ð¦ Selenium + Firefox webdriver

ð Python 3


### Versions
* **1.2** Email is now constructed from combinations of single dots to prevent repetition, as neither plus-filters or consecutive dots are allowed any more.

* **1.1** Changes to email_manipulator as email method has been patched (+ symbols in email-address not allowed). Timestamp is now in the form of dots.

* **1.0** kvizz-bot.py
