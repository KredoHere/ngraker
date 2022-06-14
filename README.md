# Ngraker
I played a lot of minecraft with my friends. Unfortunately not everyone has ability to forward their ports to expose minecraft server. Some of them (including me) use tunnels like "ngrok". The one thing is that the free plan of ngrok limits you to random IP and port. I needed to update it on noip and tell my friends the port on every server startup. 

That's why I've made this bot. It is simple and does its job. It automatically updates everything on noip. Also it has built in autimatic message sending on startup and some for-fun features like random responses. You can also check the ping of server using ping command. 




## Installation

First of all, It requires python in version 3.

```bash
sudo apt-get install python3 python3-pip
```

I suggest using `screen` if bot is gonna run headless.

```bash
sudo apt-get install screen
```

Install required packages:

```bash
pip install pyngrok discord noipy
```
**Make sure the noipy package is available through PATH after installation!**\
If not, [here](https://linuxize.com/post/how-to-add-directory-to-path-in-linux/) is a guide how to add it.



## Configuration

This is an explaination of available config:\
\
Discord:

```bash
discord_token = Your bot token You can find on discord developer portal.
```
```bash
discord_channel = ID of channel Your bot will send automatic messages. 
```
\
Ngrok:
```bash
ngrok_token = Token You can find on ngrok dashboard.
```
```bash
port = port You want to be exposed.
```
\
I won't explain noip config - string names speak for themself.

## Features

- `Ping command` - gives both DDNS and ngrok Ping.
- `Hi` - Bot simply responds from random text in the list.


## Issues

Feel free to open issues.\
I am also accessible on discord: **Pastel137#4809**


