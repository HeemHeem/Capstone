// Included in index.html. Behavioral code and the Metered room management goes here
let localStream; // local camerad feed and microphone
let remoteStream; // connected users camera and microphone data

// init function that runs upon first arriving on page
let init = async() => {
    localStream = await navigator.mediaDevices.getUserMedia({video:true, audio:false}) // request permission for camera and audio
    document.getElementById('user-1').srcObject = localStream
}

init()