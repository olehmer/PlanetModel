var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, 
            window.innerWidth/window.innerHeight, 0.1, 1000);
var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);

document.body.appendChild(renderer.domElement);

camera.position.z = 55;

var light = new THREE.PointLight( 0xff0000, 1, 100, 2);
light.position.set(20,0,20);
light.castShadow = true;

scene.add(light);

var spheresize = 1;
var pointLightHelper = new THREE.PointLightHelper( light, spheresize );
scene.add( pointLightHelper );

var ambient = new THREE.AmbientLight( 0x303030);
scene.add(ambient);

var cube_geometry = new THREE.BoxGeometry(10,10,10);
var cube_material = new THREE.MeshLambertMaterial({color:0xffff00});
cube_material.side= THREE.DoubleSide;
var cube = new THREE.Mesh(cube_geometry, cube_material);
scene.add(cube);

animate();


function animate(){
    requestAnimationFrame( animate);

    cube.rotation.y += 0.01;

    renderer.render(scene, camera);
}
