// Included in index.html. Behavioral code and the Metered room management goes here
let localStream; // local camerad feed and microphone
let remoteStream; // connected users camera and microphone data
let peerConnection; // create a peerconnection variable
// init function that runs upon first arriving on page
let init = async() => {
    localStream = await navigator.mediaDevices.getUserMedia({video:true, audio:false}) // request permission for camera and audio
    document.getElementById('user-1').srcObject = localStream

    createOffer()
}

let createOffer = async () => {
    peerConnection = new RTCPeerConnection() // create connection object

    remoteStream = new MediaStream() // setup media stream for user 2
    document.getElementById('user-2').srcObject = remoteStream

    let offer = await peerConnection.createOffer() // create offer
    await peerConnection.setLocalDescription(offer)

    console.log('Offer:', offer)
}


init()