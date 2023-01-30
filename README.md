Read and sum ELEVATION GAIN for given sport art in the MapMyRun app
=============

Update 30.1.2023
------
There has been some changes in the MapMyRun web pages, and therefore not only the locators
do not work anymore, but the whole structure of the activities on the Dashboard 
is different comparing to the situation in 2022. The whole code need to be redone.

About
------
Although the statistics provided by MapMyRun app are great 
(you can filter by activities, month and year), there is no 
summary info about the elevation gained. And that is something 
I wanted. 

This script is in Python and uses Selenium WebDriver for Chrome to navigate to MapMyRun app
and read desired data (elevation) concerning a specific sport in specific month and year.

How it is done
--------------
You only have to define a csv file, where the result will be saved.
Then it automatically
- load the webpage mapmyrun.com
- get over the cookie popup window
- log in (you can either hardcode your credentials in info_user file, or, if you leave it empty,
  you will be asked to type it: email into the console, password into a popup window.)
- **sometimes a captcha appears, this you have to pass yourself**
- the dashboard of the current month opens
- if the current month and year fulfill your settings (config.txt)
 read all the activities on the page. Then, check one by one if the
 particular sport fulfill the settings. If yes, go to this particular
 exercise, read the elevation gain and return it.
- continue as long as the settings (year, month) are satisfied
- a log file is saved in the main directory

How to run
-------------
- define your settings in the config.txt file
- create, if not present, an empty csv file
- run the main.py file

config.txt
-------------
Define for which sport you want to read the elevation. As an example, "Walk" and "Nordic, Walk" are used.
Note, that the names have to correspond MapMyRun sports. You can write several sport arts separated by a semicolon: 
_sport_list = Walk; Nordic, Walk_

Define which years to include. Reading of the data starts always in the current month and year and 
go to the past. Define the oldest year you want to include. So if you want to go through years 2021 and 2022:
_years = 2021_

Define months for which you want to calculate the elevation. Separate the month by a colon: 
_months = May, April, January, February, March_
If the month being processed is not on the list, it will be skipped. Even if you want only one month from 
a particular year, all month are checked.

If any of the info is missing, a ValueError is raised.

Problems
-------------
- Sometimes, there is a problem when dealing with th cookies window and sometimes not. No idea why.
_selenium.common.exceptions.WebDriverException: Message: target frame detached_
- From time to time a maintenance window appears while going through individual months. For now a refresh of the page is implemented and it works.

ToDo
-------------
Go directly to a particular month and year without the need to start in the current month and year and going back in time.
