 translate([xpos,ypos,zpos]){

   union(){

     cube([40,40,4],true);

     cylinder(40,15,5);

     translate([0,0,40])sphere(10);

   }

 }
