const { authJwt } = require("../middleware");
const controller = require("../controllers/consult.controller");

module.exports = function(app) {
  app.use(function(req, res, next) {
    res.header(
      "Access-Control-Allow-Headers",
      "x-access-token, Origin, Content-Type, Accept"
    );
    next();
  });

    app.post(
        "/api/consult/create",
        [authJwt.verifyToken],
        controller.create
    );

    app.post(
        "/api/consult/usecode",
        [authJwt.verifyToken],
        controller.usecode
    );
8
    // app.get(
    //     "/api/consult/get",
    //     [authJwt.verifyToken],
    //     controller.allAccess
    // );

    /**************//*

  app.get(
    "/api/test/user",
    [authJwt.verifyToken],
    controller.userBoard
  );

  app.get(
    "/api/test/mod",
    [authJwt.verifyToken, authJwt.isModerator],
    controller.moderatorBoard
  );

  app.get(
    "/api/test/admin",
    [authJwt.verifyToken, authJwt.isAdmin],
    controller.adminBoard
  );

  app.post(
    "/api/appointments/create",
    [authJwt.verifyToken],
    controller.userBoard
  )

  *//*************** */
};