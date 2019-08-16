const express = require('express');
const session = require('cookie-session'); // gestion des cookies
const bodyParser = require('body-parser'); // récupèration des paramètres en POST
var urlencodedParser = bodyParser.urlencoded({ extended: false });

// paramétrage du moteur de rendu=, des fichiers statiques, des sessions
const app = express()
.set('view engine', 'pug')
.use(express.static('public'))
.use(session({secret: 'tod0l1$t'}));

// création des routes et démarrage du serveur
app.use((req, res, next) => {
	if (req.session.tasks == undefined) {
		req.session.tasks = ["Make app with Node", "RESTfull easily routing"];
	}
	next();
})
.get('/', (req, res) => {
	res.render('index', { tasks: req.session.tasks });
})
.get('/delTask/:id', (req, res) => {
	req.session.tasks.splice(req.params.id, 1);
	res.redirect('/');
})
.post('/addTask', urlencodedParser, (req, res) => {
	req.session.tasks.push(req.body.task);
	res.redirect('/');
})
.get('/reset', (req, res, next) => {
	req.session.tasks = undefined;
	next();
})
.use((req, res, next) => {
	res.redirect('/');
})
.listen(8080);