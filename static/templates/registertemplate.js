const RegistrationTemplate = `
	<form method="POST"  onclick="Register()">
	<input type="hidden" name="csrfmiddlewaretoken" value="S21EodsxRKasBU3YKcATg7zYQE3pqkbclfxCcfHu1wkOdeX4r3LwQStYy3r6WHDe">
	    <label for="email">
	        Email:
	        <input type="email" password="email" id="email">
	    </label><br>

	    <label for="password">
	        Password:
	        <input type="password" password="password" id="password">
	    </label><br>

	    <input type="submit" value="Create new user">
	</form>
`

function Register(){
  var data = new FormData();
  data.append("csrfmiddlewaretoken", document.getElementByClassName("csrfmiddlewaretoken").value);
  data.append("email", document.getElementById("email").value);
  data.append("password", document.getElementById("password").value);
 
  fetch('http://127.0.0.1:8000/api/v1/signup/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Requested-With': 'XMLHttpRequest',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log('Success:', data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  return false;
}

export { RegistrationTemplate }






























































































































// data(){
//   return {
//     email: '',
//     password: '',
//   }
// },
// methods: {
//   RegisterationForm() {
//     fetch("http://127.0.0.1:8000/api/v1/signup/", {
//     	methods: 'POST',
// 		password: this.password,
// 		email: this.email,
//     }).then(response => {
//       console.log(response);
//       this.response = response.data
//     })
//     this.password = '';
//     this.email = '';
//     this.message = '';
//   }
// }



// function RegisterationForm (){
// 	fetch( 'http://127.0.0.1:8000/api/v1/signup/', {
// 	    method: 'POST',
// 	    // headers: {
// 	    //     // 'Authorization': 'Bearer '+this.token,
// 	    //     'Accept': 'application/json',
// 	    //     'Content-Type': 'application/json;charset=utf-8'
// 	    // },
//         headers: {
// 	      'Content-Type': 'application/json',
// 	      'X-Requested-With': 'XMLHttpRequest',
// 	      'X-CSRFToken': csrftoken,
// 	    },
// 	    body: JSON.stringify({
// 			csrftoken: document.getElementByClassName("csrfmiddlewaretoken"),
// 			email: document.getElementById('email'),
// 	 	    password: document.getElementById('password'),
// 	    })
// 	} )
// 	.then( function( response ){
// 	    if( response.status != 201 ){
// 	        throw response.status;
// 	    }else{
// 	        return response.json();
// 	    }
// 	}.bind(this))
// 	.then( function( data ){
// 	    this.fetchResponse = data;
// 	}.bind(this))
// 	.catch( function( error ){
// 	    // this.fetchError = error;
// 	}.bind(this));
// }




/// function RegisterationForm (){
// 	fetch('http://127.0.0.1:8000/api/v1/signup/', {
// 	  method: 'POST',
// 	  body: JSON.stringify({
// 	    email: document.getElementById('email'),
// 	    password: document.getElementById('password'),
// 	  }),
// 	  headers: {
// 	    'Content-type': 'application/json; charset=UTF-8',
// 	  }
// 	})
// 	  .then(function (response) {
// 	    return response.json()
// 	  })
// 	  .then(function (data) {
// 	    console.log(data)
// 	    email = document.getElementById("email")
// 	    password = document.getElementById("password")
// 	    email.innerHTML = data.email
// 	    password.innerHTML = data.password
// 	  }).catch(error => console.error('Error:', error));
// }

