module.exports = (sequelize, Sequelize) => {
    const Consult = sequelize.define("consults", {
      username: {
        type: Sequelize.STRING
      },
      category: {
        type: Sequelize.STRING
      },
      phone: {
        type: Sequelize.STRING
      },
      message: {
        type: Sequelize.STRING
      },
      code: {
        type: Sequelize.STRING
      }
    });
  
    return Consult;
  };