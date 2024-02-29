// basic code to get server running
const express = require('express')

// Require file system to use local files

// const { Socket } = require('socket.io')
const app = express()
const server = require('https') // create server based on expresss server
const io = require('socket.io')(server) // pass server to socket.io so it knows what server to look for
const {v4: uuidV4} = require('uuid') // remame v4 to uuidV4. this gives a dynamic url
// note: server is only to setup rooms. video chatting is done through computer



app.set('view engine', 'ejs') // render views
app.use(express.static('public')) // set up static folder

app.get('/', (req, res) => {
    res.redirect(`/${uuidV4()}`)
}) // create brand new room

app.get('/:room', (req,res) =>{
    res.render('room', { roomId: req.params.room }) // get room parameter
})

// Creating object of key and certificate 
// for SSL 
const options = { 
    key: fs.readFileSync("server.key"), 
    cert: fs.readFileSync("server.cert"), 
  }; 
    

io.on('connection', socket => {
    // event for when someone joins a room, pass in room id and user id
    socket.on('join-room', (roomId, userId) => {
        socket.join(roomId) // join room with this user
        socket.to(roomId).emit('user-connected', userId)

        socket.on('disconnect', () => {
            socket.to(roomId).emit('user-disconnected', userId)
        })
    })
})

server.createServer(options,app).listen(3000) // server on port 3000

