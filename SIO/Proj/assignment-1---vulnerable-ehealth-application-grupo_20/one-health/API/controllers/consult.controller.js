const db = require("../models");

const generateCode = () => {
    let letters = '0123456789ABCDEF';
    code = "";
    for (let i=1; i<20; i++){
        if( i%5==0 ) code += "-"
        else code += letters[Math.floor(Math.random()*16)];
    }
    return code;
}

exports.create = async (req,res) => {
    fetch('http://localhost:8081/api/auth/user', {method:'GET', headers:{'x-access-token': req.get('x-access-token')}})
        .then(userRes=>userRes.json())
        .then(user=>{
            let consult = {
                username: user.username,
                category: req.body.category,
                phone: req.body.phone,
                message: req.body.message,
                code: generateCode()
            }

            // add to bd
            db.consult.create(consult)
                .then(result => {
                    res.status(200).send({ok:"ok", user, consult})
                })
                .catch(err => {
                    res.status(500).send({message:"Could not make the appointment"});
                })

        })
}

exports.usecode = async (req,res) => {
    const r = (min,max) => Math.floor((Math.random()*(max-min) + min)*10)/10;
    let test = [
        r(3.5,5.0),
        r(6,31),
        r(11,36),
        r(38,126),
        r(0.2,1.3),
        r(7,17),
        r(8.4,10.2),
        r(98,107),
        r(0.7,1.2),
        r(65,105),
        r(100,250),
        r(0.65,1.05),
        r(3.6,5.0),
        r(137,145),
        r(6.3,8.2),
        r(227,467)
    ]
    db.consult.findOne({
        where: {
            code: req.body.code
        }
    }).then(row => {
        if(!row) return res.status(404).send({ message: "Consult not found" })
        return res.status(200).send({test})
    })
}