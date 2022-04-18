# Mechanical Drawing with Blender

Here we will look at using Blender for mechanical drawing.
Carefully using a 3D programming can help ensure that your understanding of the construction is correct.
The completed model can later be used for photorealistic renders.

## Set units

The acrylic is .125inch so lets change the units to *imperial* and the *length* to *inches* in the *Scene Properties* tab.

![](/home/arielc/Documents/School/emergentobjectsS22/emergentobjects/blender/mech_units.jpg)

## Scale the cube

Press the N key to open the *Item tab*. Resize the cube to be the bottom of the structure. 2.5" x 2.5" x .125"

![Screenshot_20220417_093727.png](/home/arielc/Dropbox/school/emergentobjectsS22/emergentobjects/blender/Screenshot_20220417_093727.png)

## Make the screw holes.

Save the hole locations with the base outline and export it as an SVG file from your vector graphics program.

![Screenshot_20220417_101946.png](/home/arielc/Dropbox/school/emergentobjectsS22/emergentobjects/blender/Screenshot_20220417_101946.png)

You can import the SVG file into blender.

![2.png](/home/arielc/Dropbox/school/emergentobjectsS22/emergentobjects/blender/2.png)

The SVG file imports as a group of curves. You can make them into a single object by assigning a parent object. Move the drawing to directly under the cube.

![Screenshot_20220417_094121.png](/home/arielc/Dropbox/school/emergentobjectsS22/emergentobjects/blender/Screenshot_20220417_094121.png)

Hide the cube and place cylinders where the circles are.

![Screenshot_20220417_094632.png](/home/arielc/Dropbox/school/emergentobjectsS22/emergentobjects/blender/Screenshot_20220417_094632.png)

Add a *Boolean* modifier three times and select a different cylinder for each.

![Screenshot_20220417_091531.png](/home/arielc/Dropbox/school/emergentobjectsS22/emergentobjects/blender/Screenshot_20220417_091531.png)

![Screenshot_20220417_091611.png](/home/arielc/Dropbox/school/emergentobjectsS22/emergentobjects/blender/Screenshot_20220417_091611.png)

![Screenshot_20220417_092503.png](/home/arielc/Dropbox/school/emergentobjectsS22/emergentobjects/blender/Screenshot_20220417_092503.png)

## More walls

Create the remaining walls. Reduce the size of each wall to account for the .125" wall thickness. One option to get the correct size is to create a 2.5" x 2.5" wall, position it and look for any overlap that you need to account for.

Position each wall in the correct location.

Click on the XYZ view tool switch to an orthogonal view. Press **G** to *grab* and **X, Y, or Z** to move along an axis.

*Middle mouse* and *shift + middle mouse* can be helpful as well.

![Screenshot_20220417_095246.png](/home/arielc/Dropbox/school/emergentobjectsS22/emergentobjects/blender/Screenshot_20220417_095246.png)

![Screenshot_20220417_100011.png](/home/arielc/Dropbox/school/emergentobjectsS22/emergentobjects/blender/Screenshot_20220417_100011.png)

![Screenshot_20220417_095918.png](/home/arielc/Dropbox/school/emergentobjectsS22/emergentobjects/blender/Screenshot_20220417_095918.png)

![Screenshot_20220417_100609.png](/home/arielc/Dropbox/school/emergentobjectsS22/emergentobjects/blender/Screenshot_20220417_100609.png)

![Screenshot_20220417_100648.png](/home/arielc/Dropbox/school/emergentobjectsS22/emergentobjects/blender/Screenshot_20220417_100648.png)

![Screenshot_20220417_100650.png](/home/arielc/Dropbox/school/emergentobjectsS22/emergentobjects/blender/Screenshot_20220417_100650.png)

## Measurelt (optional)

The measurelt add-on can be turned on in the preferences. The documentation is available from there as well. 

You can use this tool to create measurement annotation lines.

![Screenshot_20220417_083618.png](/home/arielc/Dropbox/school/emergentobjectsS22/emergentobjects/blender/Screenshot_20220417_083618.png)

![Screenshot_20220417_205357.png](/home/arielc/Dropbox/school/emergentobjectsS22/emergentobjects/blender/Screenshot_20220417_205357.png)
