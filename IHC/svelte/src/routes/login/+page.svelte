<link rel="stylesheet" href="src/routes/myprojects/styles.css">

<script lang="ts">
    let credentials = {usr: "admin", password: "1234"}
    let credentials2 = {usr: "Bradley_Henderson", password: "1234"}
    

    function submitSignin(){
        let usr = document.querySelector("#formSigninUsername").value
        let password = document.querySelector("#formSigninPassword").value
        const users = credentials
        const users2 = credentials2

        console.log(credentials.length)
            console.log("EW")
            if(users['usr'] == usr && users['password'] == password || users2['usr'] == usr && users2['password'] == password){
                window.location.href='/'
            }
            else {
                showAlert("Unkown username or password, try again!");
            }
    }

    let message = "";


    function showAlert(msg) {
        setTimeout(() => {
            message = "";
        }, 3000);
        message = msg;
    }
</script>

<section class="text-center text-lg-start">
	<div class="container my-2">
        {#if message}
            <div class="alert">{message}</div>
        {/if}
		<br>

    <!-- Jumbotron -->
    <div class="container py-5" >
        <div class="row g-0 align-items-center justify-content-center">

        
        <div class="col-lg-6 mb-5 mb-lg-0" style="margin-top:180px">
            
        
            <div class="card cascading-right" style="
                background: hsla(0, 0%, 100%, 0.55);
                backdrop-filter: blur(30px);

                ">
            
            <div class="card-body p-5 shadow-4 text-center" id="formsdsd">
                <!-- Pills navs -->
                            
                <ul class="nav nav-pills nav-justified mb-3" id="ex1" role="tablist">
                    <li class="nav-item" role="presentation">
                        <button class="nav-link active" id="tab-login" data-bs-toggle="pill" data-bs-target="#pills-login" type="button" role="tab" aria-controls="pills-login" aria-selected="true">Login</button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link" id="tab-register" data-bs-toggle="pill" data-bs-target="#pills-register" type="button" role="tab" aria-controls="pills-register" aria-selected="false">Register</button>
                    </li>
                    
                </ul>
                    <div class="tab-content" id="pills-tabContent">
                    <div class="tab-pane show active" id="pills-login" role="tabpanel" aria-labelledby="pills-login">
                            <form>
                        <br>
                    
                        <!-- Username input -->
						<div class="form-outline mb-4">
							<label class="form-label" for="loginName">Username</label>
							<input id="formSigninUsername" type="text" placeholder="Bradley_Henderson" class="form-control" style="text-align: center;"/>
						</div>
						

                        <!-- Password input -->
                        <div class="form-outline mb-4">
							<label class="form-label" for="loginPassword">Password</label>
							<input id="formSigninPassword" type="password" class="form-control" style="text-align: center;"/>
                		</div>

                <!-- 2 column grid layout -->
                <div class="row mb-4" >
                    <div class="col-md-6 d-flex justify-content-center">
                    <!-- Checkbox -->
                    <div class="form-check mb-3 mb-md-0">
                        <input class="form-check-input"  type="checkbox" value="" id="loginCheck" checked />
                        <label class="form-check-label" for="loginCheck"> Remember me </label>
                    </div>
                    </div>

                    <div class="col-md-6 d-flex justify-content-center">
                    <!-- Simple link -->
                    <a href="#!">Forgot password?</a>
                    </div>
                </div>

                <!-- Submit button -->
                <div id="formSignin" onsubmit="submitSignin() " >
                <button type="submit" class="btn btn-primary btn-block mb-4" on:click={submitSignin}>
                    Sign in
                    </button>
                </div>

                <!-- Register buttons -->
                <div class="text-center">
                    <p>Not a member? <a href="#pills-register" data-bs-target="#pills-register" id="registerBtn">Register</a>
                    </p>
                </div>
                </form>
            
            
            
            </div>




            <div class="tab-pane" id="pills-register" role="tabpanel" aria-labelledby="tab-register">
                
                <form>

                        <!-- Name input -->
                        <!-- <div class="form-outline mb-4">
                            <label class="form-label" for="registerName">Name</label>  
                            <input id="formSignupName" type="text" id="registerName" class="form-control" />
                        </div> -->

                        <!-- Username input -->
                        <div class="form-outline mb-4">
                            <label class="form-label" for="registerUsername">Username</label>
                            <input id="formSignupUsername" type="text" class="form-control" />
                        </div>

                        <!-- Email input -->
                        <div class="form-outline mb-4">
                            <label class="form-label" for="registerEmail">Email</label>
                            <input id="formSignupEmail" type="email" class="form-control" />
                            
                        </div>

                        <!-- Password input -->
                        <div class="form-outline mb-4">
                            <label class="form-label" for="registerPassword">Password</label>
                            <input id="formSignupPassword1" type="password"  class="form-control" />
                            
                        </div>

                        <!-- Repeat Password input -->
                        <div class="form-outline mb-4">
                            <label class="form-label" for="registerRepeatPassword">Repeat password</label>
                            <input id="formSignupPassword2" type="password" class="form-control" />
                        
                        </div>

                        <!-- Checkbox -->
                        <div class="form-check d-flex justify-content-center mb-4">
                            <input id="formSignupCheck" class="form-check-input me-2" type="checkbox" value="" checked
                            aria-describedby="registerCheckHelpText" />
                            <label class="form-check-label" for="registerCheck">
                            I have read and agree to the terms
                            </label>
                        </div>

                        <!-- Submit button -->
                        <button id="formSignup" class="btn btn-primary btn-block mb-3">Register</button>
                </form>
            
            
            </div>
            
            </div>
        
<!-- Submit button -->


</div>
</div>
</div>


<!-- <div class="col-lg-4 mb-3 mb-lg-0">
    <img src="{{ url_for('static', filename='imgs/blueCyb2.png') }}" class="w-40 rounded-4 shadow-4" alt="" height=600px style="margin-left: 60px;">
    </div>
     -->

</div>
</div>
<!-- Jumbotron -->
</section>


<style>

	#formsdsd{
		border: 1px solid black;
		border-radius: 10px;
	}

    .alert {
        background-color: red;
        color: white;
        text-align: center;
        padding: 10px;
        margin-top: 10px;
        width: 100%;

    }


</style>   