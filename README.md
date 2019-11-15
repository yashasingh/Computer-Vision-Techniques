## Computer-Vision-Techniques - Topics covered in this repository are as follows:

In this repository the concepts of vision techniques have been implemented right from the basics of kernels and pyramids to the point of using pretrained Alexnet, VGG16 for scene recongnition.

1. Concepts covered  are - Gaussian convolutions, Median filters,  Separable convolutions, Laplacian of Gaussian, Histogram equalization, Low and high pass filters.

2. Matched transformed images using SIFT features, followed by Scene stitching with SIFT features. Next topic covered was Object Recognition with HOG features

3. Data Preprocessing followed by Tiny Image Representation and classification using Nearest Neighbor Classifier. The next step was to use Bag of SIFT Representation as training data for Nearest Neighbor Classifer. Also, used one-vs-all SVMs for classification of Bag of SIFT Representation. Finally, plotting Confusion matrix and analysing classification accuracies of all 3 three methods.

4. The final notebook addresses the problem of small datasets and corrects it by performing Data augmentation - by image mirroring, image rotation and random cropping. Next step is to train the network from scratch. Perform data Normalization and Batch Normalizations for increasing accuracies. Finally, fine Tuning a Pre-Trained Deep Network and deducing inferences by comparison of performances.
