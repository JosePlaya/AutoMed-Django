export const BASE_URL_API = 'https://us-central1-automed-cl.cloudfunctions.net/webApi/'

export const firebaseConfig = { 
    apiKey: "AIzaSyAXP_MEtzVz6-mEyfjXt0Z-OIEOcSXqDYs",
    authDomain: "automed-cl.firebaseapp.com",
    projectId: "automed-cl",
    storageBucket: "automed-cl.appspot.com",
    messagingSenderId: "509880148775",
    appId: "1:509880148775:web:4e2309ac39885f7829ff02",
    measurementId: "G-GYY8CEF4NW"
}

// Configuración credenciales acceso
// const firebaseApp = firebase.initializeApp(firebaseConfig);
// const db = firebaseApp.firestore();


export function returnAuth(){
    const firebaseApp = firebase.initializeApp(firebaseConfig);
    return auth = awaitfirebaseApp.auth();
}