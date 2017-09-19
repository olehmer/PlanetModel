var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, 
                window.innerWidth/window.innerHeight, 0.1, 1000);
var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);

document.body.appendChild(renderer.domElement);

camera.position.y = -55;
camera.up = new THREE.Vector3(0,0,1);
camera.lookAt(new THREE.Vector3(0,0,0));

//var light = new THREE.PointLight( 0xff3333, 1, 100, 2);
//light.position.set(20,0,0);
//light.castShadow = true;
//scene.add(light);
//var spheresize = 1;
//var pointLightHelper = new THREE.PointLightHelper( light, spheresize );
//scene.add( pointLightHelper );

var stellar_light = new THREE.DirectionalLight(0xffffff,0.5);
stellar_light.position.set(-20,0,0);
scene.add(stellar_light);



var ambient = new THREE.AmbientLight( 0x303030);
scene.add(ambient);

var planet = null;

var controls = new THREE.OrbitControls( camera, renderer.domElement );


function animate(){
    requestAnimationFrame( animate);

    planet.rotation.z += 0.002;

    renderer.render(scene, camera);
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize( window.innerWidth, window.innerHeight );
}

function create_planet(){
    /*
     * Load the points for each panel of the planet from the data files. 
     * Display the resulting plant.
     */

    //First read the data from the server
    $.getJSON("planet_data.json", function(data){
        console.log(data.panels);

        //now that we have the data build the planet
        var material = new THREE.MeshLambertMaterial({color:0x77aacc});
        material.side = THREE.DoubleSide;
        var planet_geometry = new THREE.Geometry();

        for( i=0; i<data.panels.length; i++){
            var p1 = new THREE.Vector3(data.panels[i][0][0][0], 
                data.panels[i][0][0][1], data.panels[i][0][0][2]);
            var p2 = new THREE.Vector3(data.panels[i][0][1][0], 
                data.panels[i][0][1][1], data.panels[i][0][1][2]);
            var p3 = new THREE.Vector3(data.panels[i][0][2][0], 
                data.panels[i][0][2][1], data.panels[i][0][2][2]);
            var p4 = new THREE.Vector3(data.panels[i][0][3][0], 
                data.panels[i][0][3][1], data.panels[i][0][3][2]);
            var color_val = data.panels[i][1];

            add_faces_from_points(planet_geometry, p1,p2,p3,p4);


        }
        
        planet_geometry.computeFaceNormals();
        planet_geometry.computeVertexNormals();
        planet = new THREE.Mesh(planet_geometry, material); 

        scene.add(planet);


        animate();
    });
}


function add_faces_from_points(geometry,p1,p2,p3,p4){
    /*
     * Take 4 Vector3 points that form a plane and create a face that is added
     * to the geometry passed in.
     *
     * Inputs:
     * geometry - the geometry that the created faces will be added to
     * p1, p2, p3, p4 - the points of the plane. The points must be ordered
     *                  such that edges drawn from p1->p2->p3->p4 outline the
     *                  desire shape.
     */

    geometry.vertices.push(p1,p2,p3,p4);
    var vert_len = geometry.vertices.length;
    var face1 = new THREE.Face3(vert_len-4, vert_len-3, vert_len-2);
    var face2 = new THREE.Face3(vert_len-4, vert_len-2, vert_len-1);
    geometry.faces.push(face1,face2);
}


$(document).ready(function(){
    create_planet();
});
