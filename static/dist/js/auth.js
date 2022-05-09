// Configuración credenciales acceso
const firebaseApp = firebase.initializeApp({ 
    apiKey: "AIzaSyAXP_MEtzVz6-mEyfjXt0Z-OIEOcSXqDYs",
    authDomain: "automed-cl.firebaseapp.com",
    projectId: "automed-cl",
    storageBucket: "automed-cl.appspot.com",
    messagingSenderId: "509880148775",
    appId: "1:509880148775:web:4e2309ac39885f7829ff02",
    measurementId: "G-GYY8CEF4NW"
   });
const db = firebaseApp.firestore();
const auth = firebaseApp.auth();

function loginMail(){
    // Datos de entrada
    const email = document.getElementById('emailUsuario').value
    const password = document.getElementById('passwordUsuario').value

    console.log(email, password);

    firebase.auth().signInWithEmailAndPassword(email, password)
    .then((userCredential) => {
        // Signed in
        var user = userCredential.user;
        console.log('¡SESIÓN INICIADA!');
        console.log(user);
        // Redireccionamiento a la nueva vista
        // ...
    })
    .catch((error) => {
        var errorCode = error.code;
        var errorMessage = error.message;
        console.log('ERROR: código: ', errorCode);
        console.log('ERROR: mensaje: ', errorMessage);
        });
    }

    function logout(){
        firebase.auth().signOut().then(() => {
            // Sign-out successful.
            console.log('Sesión terminada.');
        }).catch((error) => {
            // An error ocurred.
            var errorCode = error.code;
            var errorMessage = error.message;
            console.log('ERROR: código: ', errorCode);
            console.log('ERROR: mensaje: ', errorMessage);
    });
}