function LoginForm(){
    var form = document.getElementById('form')

    form.addEventListener('submit', function (e) {
        e.preventDefault()

        var username = document.getElementById('username').value
        var password = document.getElementById('password').value

        fetch('http://127.0.0.1:8000/api/v1/register', {
        method: 'POST',
        body: JSON.stringify({
            username: username,
            password: password,

        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
        }
        })
        .then(function (response) {
            return response.json()
        })
        .then(function (data) {
            console.log(data)
            username = document.getElementById("username")
            password = document.getElementById("bd")
            username.innerHTML = data.username
            password.innerHTML = data.password
        }).catch(error => console.error('Error:', error));
    });
}

export { LoginForm } 


