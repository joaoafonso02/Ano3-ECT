const scene = new THREE.Scene();

function createGarageScene(scene) {
    const floorGeometry = new THREE.PlaneGeometry(50, 50);
    const floorMaterial = new THREE.MeshLambertMaterial({ color: 0x555555 });
    const floor = new THREE.Mesh(floorGeometry, floorMaterial);
    floor.rotation.x = -Math.PI / 2;
    scene.add(floor);

    const wallGeometry = new THREE.BoxGeometry(50, 20, 1);
    const wallMaterial = new THREE.MeshLambertMaterial({ color: 0xeeeeee });
    const backWall = new THREE.Mesh(wallGeometry, wallMaterial);
    backWall.position.z = -25;
    scene.add(backWall);

    const leftWall = new THREE.Mesh(wallGeometry, wallMaterial);
    leftWall.rotation.y = Math.PI / 2;
    leftWall.position.x = -25;
    scene.add(leftWall);

    const rightWall = new THREE.Mesh(wallGeometry, wallMaterial);
    rightWall.rotation.y = -Math.PI / 2;
    rightWall.position.x = 25;
    scene.add(rightWall);

    const frontWall = new THREE.Mesh(wallGeometry, wallMaterial);
    frontWall.position.z = 25;
    scene.add(frontWall);

    const carGeometry = new THREE.BoxGeometry(5, 2, 3);
    const carMaterial = new THREE.MeshLambertMaterial({ color: 0xff0000 });

    const car1 = new THREE.Mesh(carGeometry, carMaterial);
    car1.position.set(-10, -10, -15);
    scene.add(car1);

    const car2 = new THREE.Mesh(carGeometry, carMaterial);
    car2.position.set(10, -10, -15);
    scene.add(car2);

    const car3 = new THREE.Mesh(carGeometry, carMaterial);
    car3.position.set(0, -10, 15);
    scene.add(car3);
}

createGarageScene(scene);

const camera = new THREE.PerspectiveCamera(55, window.innerWidth / window.innerHeight, 0.01, 1000)
camera.position.z = 25;
camera.position.x = 9;
camera.position.y = -10;

const controls = new OrbitControls( camera, renderer.domElement );

//controls.update() must be called after any manual changes to the camera's transform
camera.position.set( 0, 20, 100 );
controls.update();

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

renderer.setClearColor(0xffff);
renderer.clear();


const light = new THREE.PointLight(0xffffff, 1, 100);
light.position.set(0, 10, 25);
scene.add(light);

function animate() {
    requestAnimationFrame(animate);
    renderer.setClearColor(0xffffff);
    renderer.clear();
    renderer.render(scene, camera);
}
animate();
