# Capstone
1.  To launch your own video calling website you will need download npm which comes with Node.js

2.  Install Firebase console, click Add project, and name the project. For example - CapstoneWebRTC.

3.  Create the project and add databases. Since this project uses two databases - Firestores cloud firestore database and their Realtime Database,
    you will need to create new databases which can usually be found on the left tab. Select "Start in Testmode" and then click Enable after reading the
    disclaimer

4.  Clone this repository using ```git clone https://github.com/HeemHeem/Capstone/tree/main/CapstoneWebRTC.``` or by copying the files. Make sure after you have copied
    the files that you are in the CapstoneWebRTC directory or whatever you decide to name it.

5.  Using your terminal you will need to install the command line interface (CLI) using "npm -g install firebase-tools"

6.  Authorize the Firebase CLI by running ```firebase login```. After you have logged in, you will need to associate your app with the Firebase Project you created earlier
    which can be done using ```firebase use --add```. You will then be prompted to select your Project ID and then give your project an alias - use "default" for our situation
    but you can use different aliases for production stages

7.  To test the app locally, you will need to run ```firebase serve --only hosting``` which will show that you are hosting the webstite on http://localhost:5000

8.  To deploy the project online and use it on the web you will need to use ```firebase deploy```

9.  You will then be prompted to launch the website, which in our case is this:
                    
                        https://capstone-video-calling.web.app/
                    
    NOTE: THIS LINK NAME MIGHT CHANGE DEPENDING ON WHAT WE WOULD LIKE TO CALL THE APP



This project was based off of the webRTC and firebase codelab. For more information checkout this link:
                    
                    https://webrtc.org/getting-started/firebase-rtc-codelab
                    





********************************************** DISCLAIMER ***************************************
This is for a capstone project and may not fully work after a certain time period due to security restrictions
******************************************** END DISCLAIMER *************************************




