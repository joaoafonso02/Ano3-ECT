let path = window.location.pathname
let activeNavLink = [
    path=='/html/index.html' ? 'active' : '',
    path=='/html/about.html' ? 'active' : '',
    path=='/html/insertCode.html' ? 'active': ''
]

str = `
<nav class="navbar navbar-expand-lg navbar-light shadow-sm">
<div class="container">
    <a class="navbar-brand" href="index.html"><span class="text-primary">e</span>HealthCorp</a>

    <div class="collapse navbar-collapse" id="navbarSupport">
    <ul class="navbar-nav ml-auto">
                        
        <li class="nav-item ${activeNavLink[0]}">
            <a class="nav-link" href="index.html">Home</a>
        </li>
        <li class="nav-item ${activeNavLink[1]}">
            <a class="nav-link" href="about.html">About Us</a>
        </li>
        <li class="nav-item ${activeNavLink[2]}">
            <a class="nav-link" href="insertCode.html">Use Code</a>
        </li>
        <li id="navbarLoginItem" class="nav-item">
            
        </li>
        <li id="navbarLoginButton" class="nav-item">
            
        </li>
        </ul>
    </div> <!-- .navbar-collapse -->
    </div> <!-- .container -->
</nav>
`;

document.querySelector("#header").innerHTML = str;

