## Image Augmentor with Python OpenCV

This is a simple data augmentation tool for image files, intended for use with machine learning data sets.
The tool scans a directory containing image files, and generates new images by performing a specified set of
augmentation operations on each file that it finds. This process multiplies the number of training examples that can
be used when developing a neural network, and should significantly improve the resulting network's performance,
particularly when the number of training examples is relatively small.

Run the utility from the command-line as follows:

    python main.py <image dir> <transform1> <transform2> ...

The `<image dir>` argument should be the path to a directory containing the image files to be augmented.
The utility will search the directory recursively for files with any of the following extensions:
`jpg, jpeg, bmp, png`.

|Code|Description|Example Values|
|---|---|------|
|`rot`|Rotates the image by the specified amount|`rot_90`,`rot_-45`|
|`trans`|Shifts the pixels of the image by the specified amounts in the x and y directions|`trans_20_10`,`trans_-10_0`|


### Examples
Produce 2 output images for each input image, one of which is rotted 5&deg, and one of which is -5&deg:

    python main.py ./my_images rot_5 rot_-5

Produce 1 output image for each input image, by first rotating the image by 90&deg; and then translate it:

    python main.py ./my_images rot_90, trans_1_4

### Operations

#### Rotate
Rotates the image. The angle of rotation is specified by a integer value that is included in the transform argument

    python main.py ./my_images rot_90 rot_180 rot_-90

<img style="border: 1px solid grey" src="http://codebox.net/graphics/image_augmentor/macaw.png" alt="Original Image" width="150" height="150"/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img style="border: 1px solid grey" src="http://codebox.net/graphics/image_augmentor/macaw__rot90.png" alt="Rotated Image" width="150" height="150"/>
<img style="border: 1px solid grey" src="http://codebox.net/graphics/image_augmentor/macaw__rot180.png" alt="Rotated Image" width="150" height="150"/>
<img style="border: 1px solid grey" src="http://codebox.net/graphics/image_augmentor/macaw__rot-90.png" alt="Rotated Image" width="150" height="150"/>

#### Translate
Performs a translation on the image. The size of the translation in the x and y directions are specified by integer values that
are included in the transform argument

    python main.py ./my_images trans_20_20 trans_0_100

<img style="border: 1px solid grey" src="http://codebox.net/graphics/image_augmentor/macaw.png" alt="Original Image" width="150" height="150"/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img style="border: 1px solid grey" src="http://codebox.net/graphics/image_augmentor/macaw__trans20_20.png" alt="Translated Image" width="150" height="150"/>
<img style="border: 1px solid grey" src="http://codebox.net/graphics/image_augmentor/macaw__trans0_100.png" alt="Translated Image" width="150" height="150"/>

