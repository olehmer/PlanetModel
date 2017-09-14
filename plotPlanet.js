var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, 
window.innerWidth/window.innerHeight, 0.1, 1000);
var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

var material = new THREE.MeshStandardMaterial({color:0x00cc00});
var geometry = new THREE.Geometry();
geometry.vertices.push( new THREE.Vector3(-50,50,0));
geometry.vertices.push( new THREE.Vector3(50,-50,0));
geometry.vertices.push( new THREE.Vector3(50,50,0));

var face = new THREE.Face3(0,1,2);

geometry.faces.push(face);

scene.add( new THREE.Mesh( geometry, material));


function animate(){
    requestAnimationFrame( animate);
    renderer.render(scene, camera);
}
animate();

