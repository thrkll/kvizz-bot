# kvizz-bot

Kvizz-bot is one way of playing [the online quiz-game of Olís](https://kvizz.olis.is) automatically. The bot guesses random options and saves them for later use. After learning all the answers, each instance of the bot can play ca. 150 games per hour. 

The bot can score unlimited coupons for overpriced candy bars, but please don't - it's probably immoral!

~~July 15th 2021 - The bot does not work as the quiz prevents the email format used.~~

July 21st 2021 - It's working again!

![Could not load demo](https://github.com/thrkll/kvizz-bot/blob/main/demo.gif "Three instances of the bot")



### How to run

1. Edit settings in kvizz-bot.py
2. `python kvizz-bot.py`

### Requirements 
Selenium + Firefox webdriver

Python 3

### Versions 
* **1.2** Email is now constructed from combinations of single dots to prevent repitition, as neither plus-filters or consecutive dots are allowed any more. 

* **1.1** Changes to email_manipulator as email method has been patched (+ symbols in email-address not allowed). Timestamp is now in the form of dots. 

* **1.0** kvizz-bot.py
