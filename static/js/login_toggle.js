document.addEventListener('DOMContentLoaded', (event) => {
    const container = document.getElementById('container');
    const registerBtn = document.getElementById('register');
    const loginBtn = document.getElementById('login');
    const registerLink = document.getElementById('register-link');
    const loginLink = document.getElementById('login-link');

    registerBtn.addEventListener('click', () => {
        container.classList.add("active");
    });

    loginBtn.addEventListener('click', () => {
        container.classList.remove("active");
    });

    registerLink.addEventListener('click', () => {
        container.classList.add("active");
    });

    loginLink.addEventListener('click', () => {
        container.classList.remove("active");
    });

});