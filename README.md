# SegVal-WSI


# Introduction
Applications of deep-learning (DL) algorithms in digital pathology have been in great interest   in recent years [1]. For applications related to digital pathology (for example, in the case of designing applications for TILs-scoring, as will be discussed shortly), segmentation is often a major stage. For example, it is shown that tumor-infiltrating lymphocytes (TILs) are important in cancer prognosis [2]. In clinical practice, pathologists’ visual assessment of TILs in biopsies and surgical resections of human epidermal growth factor receptor-2 positive (HER2+) and triple-negative breast cancers (TNBC) results in a quantitative score (TILs-score). Advances in ML algorithms in digital pathology pave the way for designing algorithms to automatically generate TILs-scores using whole slide images (WSIs). However, to design an automated TILs-scoring algorithm, the first stage is to design a segmentation algorithm to segment the tissue into tumoral and tumor-associated stromal regions. In later stages, a detection algorithm is also designed to detect “Lymphocytes”   in the stromal regions. Based on the outputs of these segmentation and detection algorithms, a TILs-score, as a quantitative biomarker can be calculated automatically [3]. Hence, segmentation algorithms    play a major role in a DL-based application in digital pathology.

With the segmentation annotations (in the form of segmentation masks) manually delineated by expert clinicians, a DL algorithm could be trained to automatically segment the tissue into tumoral and stromal regions. However, it is very burdensome and even infeasible to obtain segmentation annotations in the entire tissue regions of a WSI. This is due to the sheer size of WSIs in digital pathology applications in the range of 100,000 pixels in each of the two dimensions. Hence, a common practice is to select several regions of interests (ROIs) for segmentation annotations. As a result, segmentation annotations are obtained across several whole slide images, each containing several ROIs annotated in different locations. 

One example is shown in the figure below wherein three ROIs in a single WSI are annotated by expert clinicians to train a segmentation algorithm.

 ![image](https://github.com/DIDSR/SegVal-WSI/assets/68286434/01fb2f4e-cc03-41a7-829a-784efa015606)

Figure 1. Left hand side shows the entire whole slide image usually with a size on the order of 100,000 by 100,000 pixels. Three selected ROIs are chosen and annotated. One ROI is shown on the right-hand side with the segmentation mask highlighting different tissue regions (image courtesy: https://tiger.grand-challenge.org).

After training a segmentation algorithm, these algorithms should be properly evaluated. As discussed previously, providing segmentation annotations in the entire tissue region of a whole slide image is not feasible. Instead, several ROIs are annotated. It is critically important to have proper test methodologies for aggregation when evaluating the performance of segmentation algorithms in digital pathology applications.

Note: We assume that the segmentation reference standard is already obtained   through an established method in selected ROIs   of a set of whole slide images and we only focus on evaluating the performance of the segmentation algorithms as compared to these reference standard annotations.


References 
1) Janowczyk A, Madabhushi “A. Deep learning for digital pathology image analysis: A comprehensive tutorial with selected use cases”. J Pathol Inform. 2016; 7:29. Jul 26, 2023.
2) C. Denkert et al., “Tumour-infiltrating lymphocytes and prognosis in different subtypes of breast cancer: a pooled analysis of 3771 patients treated with neoadjuvant therapy”, The Lancet Oncology, 19, 2018, 40-50. 
3) Arian Arab, et. al., “Effect of color normalization on deep learning segmentation models for tumor-infiltrating lymphocytes scoring using breast cancer histopathology images”. Proc. SPIE 12471, Medical Imaging 2023: Digital and Computational Pathology, 124711H, April 6, 2023.


# Method Description

We briefly describe the methods in this tool to evaluate performance of segmentation algorithms applied to digital pathology whole slide image applications. For an extended review of the methods and performance results refer to the following: 
Reference (TiGER Paper). 

We assume that the test dataset contains N WSIs from N patients with one WSI per patient (i=1,2, ...N, where i is the index of the ith WSI and N is the total number of WSIs). Each WSI contains a number of ROIs annotated (M<sub>1</sub>, M<sub>2</sub>, M<sub>3</sub>, …  where M<sub>i</sub> is the number of ROIs annotated for the ith WSI, the total number of ROIs annotated across the entire set of WSIs is M= ∑M<sub>i</sub>). 
For each ROI, a reference segmentation mask is obtained. The reference segmentation masks will be compared to the algorithm-generated segmentation masks. If the segmentation algorithm is designed to segment the tissue into C classes,   for each ROI, a C×C confusion matrix can be obtained, and a Dice score for each of the C class labels can be found (cm<sub>ij</sub> refers to the confusion matrix of the j<sup>th</sup> ROI of the i<sup>th</sup> whole slide image).

Calculating Dice-Score from the Confusion Matrix  
For a C-class segmentation task, by comparing the reference standard annotations to the algorithm’s outputs, a confusion matrix of dimensions C×C can be obtained. From the confusion matrix, for each class, a Dice score can be calculated. 
In a one-versus-the-rest approach, a class is defined as positive and the rest as negative, and a 2×2 confusion matrix can be obtained for each of the C classes. From the 2×2 confusion matrix, a Dice score   for the positive class can be obtained (TP, FP, FN, and TN are obtained by comparing the algorithm’s predictions and the ground truth labels at the pixel level):

![image](https://github.com/DIDSR/SegVal-WSI/assets/68286434/865e9873-9043-4aac-868a-d7c084a4e7e4)

For each of the class labels, a Dice score can be obtained. If the reference standard annotations contain the positive class, a Dice score is obtained; otherwise, a Dice score is not assigned for that specific class (NaN). 

For example, an ROI in a single WSI is shown below. The segmentation annotations contain three different class labels (C=3, with label values of 0, 1, and 2). As a result, three Dice score values for each of the class labels are obtained:
![image](https://github.com/DIDSR/SegVal-WSI/assets/68286434/1212cfba-34e1-4253-8b03-c115b0405022)

As another example, three ROIs in a single whole slide image, along with the reference standard annotations and the algorithm’s predictions are shown in the figure below. As can be seen, for each of the ROIs, a confusion matrix can be obtained and since this is a 3-class segmentation task, for each of the class labels and for each of the ROIs a Dice score value can be obtained:
![image](https://github.com/DIDSR/SegVal-WSI/assets/68286434/288ae780-3f53-4f4e-8b28-32deefa95c6c)

As can be seen from the figure above, for the first ROI, the ground truth annotations contain all the three class labels and hence three Dice score values are obtained for each of the three class labels (Dice score values of 0.0138, 0.8636, 0.8358).

For the second ROI, since two of the class labels are absent in the ground truth annotations, for these classes, Dice score values are not assigned (“NaN” values). A Dice score value of 0.4797 is obtained for the class shown with the red mask.

For the third ROI, since one of the class labels is absent in the ground truth annotation, a Dice score of “NaN” is assigned for that class and Dice score values of 0.9189 and 0.9445 are obtained for the other two classes.






