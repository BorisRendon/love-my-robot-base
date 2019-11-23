const express = require('express')
const app = express()
var path = require('path')
var bodyParser = require('body-parser');
const Mustache = require('mustache')
const fs = require('fs')
//var $ = require('jquery');
const port = 8080

app.use(express.static('public'))

app.use(express.json());

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

let action_string = fs.readFileSync('./actions.json', 'utf8');
let actions = JSON.parse(action_string);

app.get('/', function(req, res){
    const template = fs.readFileSync('views/index.html', 'utf8');

    // get keys for todo
    const keys_string = fs.readFileSync('./keys.json', 'utf8');
    const keys = JSON.parse(keys_string);

    for (let key in keys) {
        keys[key].gap = ((parseInt(key) + 1) * 140) - 20
    }

    //include menu.html
    const menu = fs.readFileSync('views/menu.html', 'utf8');

    //include navbar.html
    const nav = fs.readFileSync('views/navbar.html', 'utf8');

    //include stack.html
    const stack = fs.readFileSync('views/stack.html', 'utf8');

    //include jumbotron.html
    const jumbo = fs.readFileSync('views/jumbotron.html', 'utf8');

    //include modal.html
    const modal = fs.readFileSync('views/modal.html', 'utf8');

    const renderIndex = Mustache.render(template, {menuOptions: keys}, {menu, nav, jumbo, stack, modal});

    res.status(200).send(renderIndex)
})

app.get('/home', function (req, res) {

    // include home.html
    const template = fs.readFileSync('views/home.html', 'utf8');

    // get keys for todo
    const keys_string = fs.readFileSync('./keys.json', 'utf8');
    const keys = JSON.parse(keys_string);

   
    //include navbar.html
    const nav = fs.readFileSync('views/navbar.html', 'utf8');

    //include jumbotron.html
    const jumbo = fs.readFileSync('views/jumbotron.html', 'utf8');

    const renderIndex = Mustache.render(template, {
        menuOptions: keys
    }, {
        nav,
        jumbo
    });

    res.status(200).send(renderIndex)
})


app.get('/actions', function (req, res) {

    const template = fs.readFileSync('views/index.html', 'utf8');

    // get keys for todo
    const keys_string = fs.readFileSync('./keys.json', 'utf8');
    const keys = JSON.parse(keys_string);


    //To add a value to our json
    //actions['actions'].push("Jump")

    for (let key in keys) {
        keys[key].gap = ((parseInt(key) + 1) * 140) - 20
    }

    //include menu.html
    const menu = fs.readFileSync('views/menu.html', 'utf8');

    //include navbar.html
    const nav = fs.readFileSync('views/navbar.html', 'utf8');

    //include stack.html
    const stack = fs.readFileSync('views/stack.html', 'utf8');

    //include jumbotron.html
    const jumbo = fs.readFileSync('views/jumbotron.html', 'utf8');

    //include modal.html
    const modal = fs.readFileSync('views/modal.html', 'utf8');

    const renderIndex = Mustache.render(template, {
        menuOptions: keys, actions_test: actions
    }, {
        menu,
        nav,
        jumbo,
        stack,
        modal
    });

    res.status(200).send(renderIndex)
})

app.post('/task-added', function(req, res){
    //console.log(req.name);
    //exp.push(req.body.name)
    actions['actions'].push(req.body.name)
    console.log(actions['actions'])
    
    //act.push(req.body.name);
})



app.post('/delete', function(req, res){

    console.log('Deleted:\n', req.body.name);

    for (var i = 0; i < actions.actions.length; i++){
        if(actions.actions[i] === req.body.name){
            actions.actions.splice(i,1);
        }
    }
    res.json({
        message: "Deleted."
    })
})

const data = require('./actions.json')

app.post('http://localhost:5000/Lex', function (req, res){

    res.json(data);

})

//app.get('/', (req, res) => res.send('Hello From Express'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))