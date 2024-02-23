const socket = io('/')

// get reference to video grid
const videoGrid = document.getElementById('video-grid')
// refer to peerJS for documentation as it creates new ids for people
const myPeer = new Peer(undefined, {
    host: '/',
    port: '3001'
})

// keep track of callsbeing made
const peers = {}

// create video element
const myVideo = document.createElement('video')
myVideo.muted = true // stop your own audio from playing back to you

// connect video
navigator.mediaDevices.getUserMedia({
    video: true,
    audio: true
}).then(stream =>{
    addVideoStream(myVideo, stream)

    // list to when someone tries to call and answer then send stream
    myPeer.on('call', call =>{
        call.answer(stream)

        const video = document.createElement('video')
        call.on('stream', userVideoStream =>{
            addVideoStream(video, userVideoStream)
        })
    })
    // connect users
    socket.on('user-connected', userId => {
        connectToNewUser(userId, stream)
    })
})


socket.on('user-disconnected', userId =>{
    if (peers[userId]) peers[userId].close()
})


myPeer.on('open', id => {
    socket.emit('join-room', ROOM_ID, id)
})


// play video 
function addVideoStream(video, stream){
    video.srcObject = stream
    video.addEventListener('loadedmetadata', () => {
        video.play()
    })
    videoGrid.append(video)
}

function connectToNewUser(userID, stream){
    const call = myPeer.call(userID, stream)
    call.on('stream', userVideoStream => {
        addVideoStream(video, userVideoStream)
    }) // take in other user stream
    
    // remove video when someone leaves
    call.on('close', () => {
        video.remove()
    })

    // ever user is now connected to a call you make
    peers[userId] = call
}