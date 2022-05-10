import { firebaseConfig } from './config.js'

// Configuración credenciales acceso
const firebaseApp = firebase.initializeApp(firebaseConfig);
const db = firebaseApp.firestore();
const auth = firebaseApp.auth();

// LOG IN
// function loginMail(){
//     console.log('Iniciando login...');

//     // Datos de entrada
//     const email = document.getElementById('emailUsuario').value
//     const password = document.getElementById('passwordUsuario').value

//     console.log(email, password);

//     firebase.auth().signInWithEmailAndPassword(email, password)
//     .then((userCredential) => {
//         // Signed in
//         var user = userCredential.user;
//         console.log('¡SESIÓN INICIADA!');
//         console.log(user);
//         // Redireccionamiento a la nueva vista
//         // ...
//     })
//     .catch((error) => {
//         var errorCode = error.code;
//         var errorMessage = error.message;
//         console.log('ERROR: código: ', errorCode);
//         console.log('ERROR: mensaje: ', errorMessage);
//     });
// }

// LOG OUT
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