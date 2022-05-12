import { firebaseConfig, auth } from './config.js'

function getUserData(){
    const user = auth.currentUser;
    if (user) {
        // User is signed in, see docs for a list of available properties
        // https://firebase.google.com/docs/reference/js/firebase.User
        // ...
        console.log(user);
    } else {
    // No user is signed in.
    }
}