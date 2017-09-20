var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, 
                window.innerWidth/window.innerHeight, 0.1, 1000);
var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);

document.body.appendChild(renderer.domElement);

camera.position.y = -200;
camera.up = new THREE.Vector3(0,0,1);
camera.lookAt(new THREE.Vector3(0,0,0));



//var ambient = new THREE.AmbientLight( 0xffffff);
//scene.add(ambient);

var planet = null;

var controls = new THREE.OrbitControls( camera, renderer.domElement );


function animate(){
    requestAnimationFrame( animate);

    //planet.rotation.z += 0.0005;

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
            var color_val = new THREE.Color(data.panels[i][1]);

            add_faces_from_points(planet_geometry, p1,p2,p3,p4, color_val);


        }
        

        var material = new THREE.MeshBasicMaterial({color: 0xffffff, 
            vertexColors: THREE.FaceColors,
            side: THREE.DoubleSide});
        planet = new THREE.Mesh(planet_geometry, material); 

        planet_geometry.computeFaceNormals();
        planet_geometry.computeVertexNormals();

        scene.add(planet);

        animate();
    });
}


function add_faces_from_points(geometry,p1,p2,p3,p4, color){
    /*
     * Take 4 Vector3 points that form a plane and create a face that is added
     * to the geometry passed in.
     *
     * Inputs:
     * geometry - the geometry that the created faces will be added to
     * p1, p2, p3, p4 - the points of the plane. The points must be ordered
     *                  such that edges drawn from p1->p2->p3->p4 outline the
     *                  desired shape.
     */

    geometry.vertices.push(p1,p2,p3,p4);
    var normal = new THREE.Vector3(0,0,0);
    normal.crossVectors(p1,p2);
    var vert_len = geometry.vertices.length;
    var face1 = new THREE.Face3(vert_len-4, vert_len-3, vert_len-2, normal, color);
    var face2 = new THREE.Face3(vert_len-4, vert_len-2, vert_len-1, normal, color);
    geometry.faces.push(face1,face2);
}


$(document).ready(function(){
    create_planet();
});
