# i-zone.mobi-auto-temperature
Script used on https://i-zone.mobi/companion to automate keying in temperature for temperature taking

### REQUIREMENTS
* Install Selenium and PyAutoGUI
* A GUI platform to run on (Needed for PyAutoGUI)



### NOTE
* The temperature function checks whether it is morning/afternoon. Temperature generated is based on it.
* Credentials to be stored on a file named ```credentials.txt```
* Enter your own ChromeDriver file path (Not tested on other browsers)
* For PyAutoGUI click on ```Line 69``` , change the coordinates to fit your monitor size.
* Script has **NO VERIFICATION/ERROR CHECK** implemented yet

### credentials.txt
Allows for multiple credentials to be keyed in, but format to be kept the same.
The format are as follows:
```
username,password
alice123,password
bob321,password1
```
