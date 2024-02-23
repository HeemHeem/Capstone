// Included in index.html. Behavioral code and the Metered room management goes here
let localStream; // local camerad feed and microphone
let remoteStream; // connected users camera and microphone data
let peerConnection; // create a peerconnection variable


// create free google stunt server - may not need it rn only doing it locally
const servers = {
    iceServers:[
        {
            urls:['stun:stun1.1.google.com:19302', 'stun:stun2.1.google.com:19302']
        }
    ]
}


// init function that runs upon first arriving on page
let init = async() => {
    localStream = await navigator.mediaDevices.getUserMedia({video:true, audio:false}) // request permission for camera and audio
    document.getElementById('user-1').srcObject = localStream

    createOffer()
}

let createOffer = async () => {
    peerConnection = new RTCPeerConnection(servers) // create connection object

    remoteStream = new MediaStream() // setup media stream for user 2
    document.getElementById('user-2').srcObject = remoteStream

    // add audio tracks
    localStream.getTracks().forEach((track) =>{
        peerConnection.addTrack(track, localStream)
    })

    // event listener for remote peer audio tracks and when it adds tracks
    peerConnection.ontrack = (event) =>{
        event.streams[0].getTracks().forEach((track)=>{
            remoteStream.addTrack()
        })
    }


    // create ice candidate
    peerConnection.onicecandidate = async (event) => {
        if(event.candidate){
            console.log('New ICE candidate:', event.candidate)
        }
    }


    let offer = await peerConnection.createOffer() // create offer
    await peerConnection.setLocalDescription(offer)

    console.log('Offer:', offer)
}


init()