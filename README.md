# Love My Robot
Este repositorio contiene todo lo necesario para que usted inicie el desarrollo del proyecto.

Note como cada proyecto vive asiladamente dentro de su propio folder.


Use este README para llenarlo con su informacion:

- Usage
- Alguna explicacion extra.


# Compilar / Build

docker-compose build --parallel


# Correr y compilar antes

docker-compose up --build



# Correr

docker-compose up

docker-compose down -v

# Probar solo un app y compilar antes

docker-compose up --build lex

# Installation (Step-by-step) 

As first step, you have to [git] clone this repo:

```git
git clone https://github.com/BorisRendon/love-my-robot-base.git
```



Once you clone the repo, you have to go to the main directory of the project:

```bash
cd love-my-robot-base
```


## GUI 

This is the first part of our project.

Go to the gui folder:


```bash
cd gui
```
 

Now, you have to install all the dependecies to execute correctly this project:

```npm
npm install
```


## Lex

Then, after you install the dependecies of GUI, you need to install the dependecies of Lex, our final part of the project.

First, if you are in love-my-robot-base/gui, then:

```pip
cd ..
```
Go to lex dir:

```pip
cd lex
```


Run the following command to install the rest of requirements:

```pip
pip install -r requirements.txt
```
 

Now you are ready to start playing with Cozmo! :D

# Running the project

## GUI

Run:

```bash
node server.js
```

> Open you localhost in the port 8080/home

## Lex


```bash
python lex.py
```