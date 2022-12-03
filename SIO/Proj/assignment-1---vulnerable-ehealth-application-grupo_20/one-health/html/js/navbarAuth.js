

let apiURL = window.location.origin.split(":")
apiURL = apiURL[0] + ":" + apiURL[1] + ":8081/api/auth/user"
document.querySelector("#navbarLoginItem").innerHTML = '';
fetch(apiURL, {method:'GET', headers:{'x-access-token':localStorage.getItem('x-access-token')}})
    .then(resp=>resp.json())
    .then(resp=>{
        console.log(resp)
        if (resp.status==200) {
            let elem = '<div class="px-3 text-primary">'+resp.username+'</div>';
            let ebutton = '<div class="btn btn-danger ml-lg-3" onclick="authLogout()">Logout</div>';
            document.querySelector("#navbarLoginItem").innerHTML = elem;
            document.querySelector("#navbarLoginButton").innerHTML = ebutton;
        } else {
            let elem = '<a class="btn btn-primary ml-lg-3" href="login.html">Login / Register</a>';
            document.querySelector("#navbarLoginItem").innerHTML = elem;
            document.querySelector("#navbarLoginButton").innerHTML = '';
        }
    })

const authLogout = () => {
    if(!confirm("YOU ARE BEING LOGGED OUT, u wish to procede?")) document.getElementById("confirm").hidden=false
    console.log(1)
    localStorage.removeItem('x-access-token')
    window.location.reload()
}


