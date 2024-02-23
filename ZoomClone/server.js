// basic code to get server running
const express = require('express')
const app = express()
const server = require('http').Server(app) // create server based on expresss server
const io = require('socket.io')(server) // pass server to socket.io so it knows what server to look for
// note: server is only to setup rooms. video chatting is done through computer

server.listen(3000) // server on port 3000
