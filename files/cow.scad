difference() {
	resize(newsize=[110,105,100]) sphere(r=10);
	translate([-55,-55,-110]) cube(110);
}
difference() {
	resize(newsize=[110,105,75]) sphere(r=10);
	translate([-55,-55,110]) cube(110);
}
translate([50,0,50]) resize(newsize=[80,85,75]) sphere(r=10);

translate([-25,25,-50]) huv();
translate([-25,-25,-50]) huv();
translate([25,25,-50]) huv();
translate([25,-25,-50]) huv();

translate([0,0,-35]) uder();

module huv() {
	hull() {
		resize(newsize=[30,30,20]) sphere(r=10);
		translate([0,0,15]) resize(newsize=[20,20,20]) sphere(r=10);
	}
}

module uder() {
	resize(newsize=[45,45,25]) sphere(r=10);
	translate([-10,10,-10]) rotate([-30,180,45]) nob();
	translate([-10,-10,-10]) rotate([30,180,-45]) nob();
	translate([10,10,-10]) rotate([-30,180,-45]) nob();
	translate([10,-10,-10]) rotate([30,180,45]) nob();
}

module nob() {
	hull() {
		resize(newsize=[10,10,5]) sphere(r=10);
		translate([0,0,5]) resize(newsize=[5,5,5]) sphere(r=10);
	}
}