# Self-derived organ attention for unpaired CT-MRI deep domain adaptation based MRI segmentation: Jue Jiang, ... Harini Veeraraghavan
This is the code for the organ attention based unpaired domain adaptation and MRI segmentation method. The core novelty of this approach is an organ attention discriminator that combines the images with the segmentation probability maps for computing mismatch between the synthesized and target modalities. The segmentation probability maps can be combined either through concatenation (default), dot product attention, or additive attention. We implemented this method using standard U-net segmentation architecture, a split U-net architecture, and the denseFCN architecture. 

More details of the method and the architectures are available in the paper accepted to Physics in Medicine and Biology 2020 paper. Link to the paper will be made available soon. 

## Prerequisities
Python, PyTorch, Numpy, Scipy, Matplotlib, and a recent NVIDIA GPU
## Train
python train.py  --dataroot ./dataset/maps --name model_seg --model Organ_attention.py --checkpoints_dir ./output/ --batchSize 2 --Net [Unet|DenseNet|Split-Unet] --Organ_Attention_Type [concat|dot|add]
## NOTE
This code is being updated: 
## Acknowledgement

