let signInForm = document.getElementById("SignInForm")
let signUpForm = document.getElementById("SignUpForm")

// Get all necessary DOM elements
const signInButton = document.querySelector('section:first-child button:first-child');
const signUpButton = document.querySelector('section:first-child button:last-child');

// Add click handlers for toggle buttons
signInButton.addEventListener('click', () => {
    signInForm.style.display = 'flex';
    signUpForm.style.display = 'none';
    signInButton.style.background = '#0056b3';
    signUpButton.style.background = '#007bff';
});

signUpButton.addEventListener('click', () => {
    signInForm.style.display = 'none';
    signUpForm.style.display = 'flex';
    signUpButton.style.background = '#0056b3';
    signInButton.style.background = '#007bff';
});

// Initialize the UI to show sign in form by default
window.addEventListener('load', () => {
    signInForm.style.display = 'flex';
    signUpForm.style.display = 'none';
    signInButton.style.background = '#0056b3';
});



//----------------------------- Api ------------------------------------


signInForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    
    let SignInData = {
        username: e.target[0].value,
        password: e.target[1].value,
    }
    console.log(SignInData);
    let res = await axios.post("http://127.0.0.1:8000/user/login", SignInData);
    console.log(res.data);
    // Store the token in local storage for future use
    localStorage.setItem("User", res.data);
    window.location.href = "/frontend/Feed.html";
})


signUpForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    let password = e.target[3].value
    let confirmPassword = e.target[4].value
    if (password!= confirmPassword) {
        alert("Passwords do not match")
        return;
    }
    
    let SignUpData = {
        FullName: e.target[0].value,
        ProfilePic: e.target[1].value,
        UserName: e.target[2].value,
        Password:password,
    }
    console.log(SignUpData);
    let res = await axios.post("http://127.0.0.1:8000/user/register", SignUpData);
    console.log(res.data);
    // Store the token in local storage for future use
    localStorage.setItem("User", res.data);
    window.location.href = "/frontend/Feed.html";
})