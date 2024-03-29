import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { GridHelper } from 'three/src/helpers/GridHelper.js';
import { XYZLoader } from 'three/examples/jsm/loaders/XYZLoader.js';


var camera, controls, scene, renderer;

let points;
let line;
let drawCount;
let MAX_POINTS;



class App {
    
    init() {
        
        scene = new THREE.Scene();
        renderer = new THREE.WebGLRenderer();
        renderer.setSize( window.innerWidth, window.innerHeight );
        document.body.appendChild( renderer.domElement );
        
        camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 1, 10000 );
        camera.position.set( 0, 20, 100 );
        
        controls = new OrbitControls( camera, renderer.domElement );
        
        window.addEventListener( 'resize', onWindowResize, false );
    
        function onWindowResize(){
    
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
    
            renderer.setSize( window.innerWidth, window.innerHeight );
    
        }
    
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
    
        controls.screenSpacePanning = false;
    
        controls.minDistance = 10;
        controls.maxDistance = 500;
    
        //grid
        var size = 100;
        var divisions = 20;
        var colorCenterLine = 0x333333;
        var colorGrid = 0x222222;
        var gridHelper = new THREE.GridHelper( size, divisions, colorCenterLine, colorGrid );
        scene.add( gridHelper );
    
        var lineMaterial = new THREE.LineBasicMaterial( { color: 0xEFFF33 } );
        
        //loader test
        var geometry = new THREE.BufferGeometry();
        const loaderPoints = new XYZLoader();
        const loaderLine = new XYZLoader();
    
        loaderPoints.load( 'xyz_output/xyz_polygons.txt', function ( geometry ) {
            
            geometry.center();
            
            const vertexColors = ( geometry.hasAttribute( 'color' ) === true );
            
            const material = new THREE.PointsMaterial( { size: 0.1, vertexColors: vertexColors } );
            
            points = new THREE.Points( geometry, material );
            scene.add( points );                    
        });
    
        loaderLine.load( 'xyz_output/xyz_polygons.txt', function ( geometry ) {
            
            geometry.center();
                            
            // draw range
            console.log("geometry count: " + geometry.attributes.position.count)
            MAX_POINTS = geometry.attributes.position.count + 1;
            drawCount = 2; // draw the first 2 points only
            geometry.setDrawRange( 0, drawCount )
            
            //connecting points
            line = new THREE.Line(geometry, lineMaterial);
            scene.add(line);
            
            //total sum distances of line
            line.computeLineDistances();
            let lineSum = line.geometry.getAttribute("lineDistance");
            console.log("line sum: " + lineSum.getX(lineSum.count - 1));
        });
    
        animate();
        
    }

}


// for further reference on how to animate the line draw visit: https://jsfiddle.net/xvnctbL0/2/

function animate() {
    
    setTimeout( function() {

        requestAnimationFrame( animate );

    }, 1000 / 30 );
    
    // requestAnimationFrame( animate );

    drawCount = ( drawCount + 1 ) % MAX_POINTS;

    line.geometry.setDrawRange( 0, drawCount );

    // required if controls.enableDamping or controls.autoRotate are set to true
    controls.update();

    render();

}
function render() {

    renderer.render( scene, camera );
}

export default App;
