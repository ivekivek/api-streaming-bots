const express = require('express')
let router = express.Router()

const {exec} = require('child_process')
const { json } = require('body-parser')

router.get('/v1/youtube/oauth/get_token', (req, res) => {
	exec('python src/youtube/get_token.py', (err, data, st) => {
		if (err) res.json({ message: err })
		else {
			res.json({ message: 'sign up in new tab/browser' })
		}
	})
})

router.get('/v1/youtube/start', (req, res) => {
	let access_token = req.query.access_token
	let id = req.query.id
	let msg = req.query.msg

	exec(`python src/youtube/make_oauth.py ${access_token}`, (err, data, st) => {
		if (err) res.json({ message: err })
		else {
			res.redirect(`/v1/youtube?id=${id}&msg=${msg}`)
		}
	})
})

router.get('/v1/youtube', (req, res) => {
	let id = req.query.id
	let msg = req.query.msg

	exec(`python src/youtube/example.py ${id} ${msg}`, (err, data, st) => {
		if (err) res.json({ message: err })
	})
})

router.get('/v1/youtube/stop', (req, res) => {
	exec('taskkill /F /IM Python.exe', (err, data, st) => {
		if (err) res.json({ message: err })
		else {
			res.json({ message: data })
		}
	})
})

router.get('/v1/twitch', (req, res) => {
	let msg = req.query.msg
	let gjk = req.query.gjk

	exec(`python src/start-twitch.py ${msg}`, (err, data, st) => {
		if (err) res.json({ message: err })
		else {
			console.log(data)
		}
	})
})

router.get('/v1/facebook', (req, res) => {
	let id = req.headers.id

	exec(`python src/start-facebook.py ${id}`, (err, data, st) => {
		if (err) res.json({ message: err })
		else {
			res.json({
				message: data,
				id: id
			})
		}
	})
})

router.get('/', (req, res) => {
	res.json({
		Facebook: {
			link: '/v1/facebook',
			Headers: 'token and id',
		},
		Twitch: {
			link: '/v1/twitch',
			Headers: 'msg'
		}
	})
})

module.exports = router