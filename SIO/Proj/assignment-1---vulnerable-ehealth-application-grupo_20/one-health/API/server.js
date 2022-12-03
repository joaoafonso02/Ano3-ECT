const express = require("express");
const cors = require("cors");
const waitPort = require("wait-port");

const app = express();

let whitelist = ['http://localhost:5500', 'http://127.0.0.1:5500','http://localhost:8080', 'http://127.0.0.1:8080']
let corsOptions = {
  origin: (origin, callback) => {
    if (whitelist.indexOf(origin !== -1)) callback(null, true)
    else callback(new Error('Not allowed by CORS'))
  }
};

app.use(cors(corsOptions));

// parse requests of content-type - application/json
app.use(express.json());

// parse requests of content-type - application/x-www-form-urlencoded
app.use(express.urlencoded({ extended: true }));

// simple route
app.get("/", (req, res) => {
  res.json({ message: "Welcome to bezkoder application." });
});


function delay(time) {
  return new Promise(resolve => setTimeout(resolve, time));
} 
const initializeSQL = async () => {
  
  require('./routes/auth.routes')(app);
  require('./routes/user.routes')(app);
  require('./routes/consult.routes')(app);

  const db = require("./models");
  const Role = db.role;
  const User = db.user;
  const Consult = db.consult;

  const connectToDB = () => {
    db.sequelize.sync({force: true}).then(() => { // db.sequelize.sync({force: true}) makes the db reset at start
      console.log('Drop and Resync Db');
      initial();
      console.log("ALL DB INITIAL DONE")
    }).catch( async err=>{
      console.log(err);
      await delay(1000);
      connectToDB();
    })
    console.log("TRYING3");

    
    function initial() {
      Role.create({
        id: 1,
        name: "user"
      });
      
      Role.create({
        id: 2,
        name: "moderator"
      });
      
      Role.create({
        id: 3,
        name: "admin"
      });
    
    // User.create({
      //   username: "admin",
      //   email: "admin@ua.pt",
      //   password: bcrypt.hashSync("password", 8)
      // })
      const authController = require('./controllers/auth.controller')
      authController.signup({body:{username:'admin',email:'admin@ua.pt',password:'password'}}, {send:()=>{}, status:()=>{}})
      authController.signup({body:{username:'edu',email:'edu@ua.pt',password:'password'}}, {send:()=>{}, status:()=>{}})
    }
  }
  connectToDB();
    
}
initializeSQL();


// set port, listen for requests
const PORT = process.env.PORT || 8081;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}.`);
});