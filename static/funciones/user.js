import { firebaseConfig } from './config.js'

// Configuración credenciales acceso
const firebaseApp = firebase.initializeApp(firebaseConfig);
const db = firebaseApp.firestore();
const auth = firebaseApp.auth();

function getUserData(){
    const user = firebase.auth().currentUser;
    if (user) {
        // User is signed in, see docs for a list of available properties
        // https://firebase.google.com/docs/reference/js/firebase.User
        // ...
        console.log(user);
    } else {
    // No user is signed in.
    }
}