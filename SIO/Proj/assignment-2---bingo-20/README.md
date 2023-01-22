# Project 2 - Secure Game - Bingo

This assignment will focus on the implementation of a robust protocol for handling a distributed game. The game under study will be Bingo, which is a game of chance. Implementation will consist of a server (caller) and multiple clients (players) communicating over a network.
Bingo is a game that can take a variable number of players. We will not deal with the monetary dimension of it. Each player receives a card with a random set of  unique numbers (from 1 to , but not all, since ) and those numbers (deck) are then randomly selected by a caller (the game host, the entity that coordinates the evolution of the game) until a player completes a row in their card with the numbers selected so far. That player is the winner. It is possible to have several winners, though.

# Note:
- It was decided amongst the team members to merge the caller.py file with the user.py file was considered, since it was understood to be more adjustable and flexible to work with only two files (user.py & parea.py), always considering the distinction of the entities. In this way, the Caller has as input in the game the nickname: callerpassword, in which it will be recognized as the Caller and only this has access to the main functionalities of the game (e.g. Start the game (!start). It is possible for Caller to enter the game by typing on the command line:

<pre><code>$ python3 user 8080 callerpassword</code></pre>

- Report --> Although it was not explicitly requested to produce a report about this project, as a team, we believe it would be a value-add to carry it out.


---

## Create, use venv and install requirements
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

---

## Playing Area (Server)
Server just needs to be open, there is no operation possible after, all the actions can be done with the clients
```bash
python3 parea.py <port>
```

---

## Player
A player should create a connection to the server with a nickname.
```bash
python3 user.py <port> <nickname>
```

### Actions

&emsp; ```!ping <message>``` &ensp; the unique porpuse of this command is to test the connection to the server

&emsp; ```!global <message>``` &ensp; allows global messages, not needed but its a feature :)

&emsp; ```!users``` &ensp; request current connected users 

&emsp; ```!set_nickname``` &ensp; defines a new nickname






---

## Caller
The Caller is just a user with higher permissions, so, we will use user.py to start its service with the 2nd arguments being a password, this password is known by the server and must be something dificult to brute force.
```bash
python3 user.py <port> <callerpassword>
```

### Actions
The Caller can do everything a user can do, plus:

&emsp; ```!start``` &ensp; Initiates the game, which, if successful, will culminate in a user being declared the winner.

---

## Authors
[João Afonso Ferreira](https://github.com/joaoafonso02), 103037  
[Eduardo Fernandes](https://github.com/EduardoFernandesUA), 102648  
[Guilherme Claro](https://github.com/Gmclaro), 98432   
[Tiago Mostardinha](https://github.com/TiagoMostardinha), 103944
