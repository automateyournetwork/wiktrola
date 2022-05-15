# wiktrola
Transform any Wikipedia page into an MP3 file!

## Installing the bot
To install the bot there are a few simple steps:
#### Ubuntu Linux 
##### The following instructions are based on Windows WSL2 and Ubuntu however any flavour of Linux will work with possibly slightly different commands.

##### Confirm Python 3 is installed

#####
```console

$ python3 -V
Python 3.9.10

```

##### Create and activate a virtual environment

######
```console

$ sudo apt install python3-venv
$ python3 -m venv wiktrola
$ source wiktrola/bin/activate
(wiktrola)$

```
##### Install the bot
```console

(message_room)$pip install wiktrola

```
### Windows

#### [Download Python](https://python.org)
#### Create and activate a virtual environment
#####
```console

C:\>python3 -m venv wiktrola
C:\>wiktrola\Scripts\activate
(wiktrola) C:\>

```
#### Install the requirements
```console

(message_room)$pip install wiktrola

```

## Using the bot
### Run the bot as an interactive session
```console

(wiktrola)$ wiktrola

```
### The form questions:

##### Question 1 - What is the title of the Wikipedia page you want to convert?

### The bot will then display all Wikipeida pages related to that title.

### If your title matches a page in the list, the bot will then create an audio file for that page.

### Be patient as the bot may take a while to create the audio file.

### The audio file will open in your browser