exports.allAccess = (req, res) => {
  res.status(200).send(JSON.stringify({text:"Public Content."}));
};

exports.userBoard = (req, res) => {
  res.status(200).send(JSON.stringify({text:"User Content."}));
};

exports.adminBoard = (req, res) => {
  res.status(200).send(JSON.stringify({text:"Admin Content."}));
};

exports.moderatorBoard = (req, res) => {
  res.status(200).send(JSON.stringify({text:"Moderator Content."}));
};

exports.makeAppointment = (req, res) => {
  res.status(200).send(JSON.stringify({status:200, text:"Make Appointment"}));
}