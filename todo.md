# todo
	-upload images 100%
	-segment the images manully 100%
	-generate masks 100%
	-download the masks 100%
	-change region_id on the csv_file 100%
	-create an img_path_list and mask_math_list 100%
	-devide the dataset 100%
	-create a data pipeline(apply different transformations) 100%
	-create a model 100%
	-determine lerning_rate, batch_size 100% (lr: .005, bs: 3)
	-determine the final acivation function 100% (sigmoid)
	-define custom metrics ans loss 100% (mse)
	-train the model 100% (300 epochs)
	-evaluate the model	100% (acc: 90%, loss: 1.5)
	-deploy the model to production 100% (web_app: tensorflow.js, web_service: flask)

## NOTA
### mask/img reversed 100%

```
'squared_mask/IMG_7064_mask.JPG', 
'squared_mask/IMG_7065_mask.JPG', 
'squared_mask/IMG_7071_mask.JPG', 
'squared_mask/IMG_7073_mask.JPG', 
'squared_mask/IMG_7076_mask.JPG', 
'squared_mask/IMG_7077_mask.JPG', 
'squared_mask/IMG_7078_mask.JPG', 
'squared_mask/IMG_7080_mask.JPG', 
'squared_mask/IMG_7083_mask.JPG', 
'squared_mask/IMG_7089_mask.JPG', 
'squared_mask/IMG_7092_mask.JPG', 
'squared_mask/IMG_7101_mask.JPG', 
'squared_mask/IMG_7104_mask.JPG', 
'squared_mask/IMG_7108_mask.JPG', 
'squared_mask/IMG_7112_mask.JPG', 
'squared_mask/IMG_7120__mask.JPG' 
```

### images fliped 

```
'squared_dataset/IMG_7064.JPG', 
'squared_dataset/IMG_7065.JPG', 
'squared_dataset/IMG_7066.JPG', 
'squared_dataset/IMG_7067.JPG', 
'squared_dataset/IMG_7068.JPG', 
'squared_dataset/IMG_7069.JPG', 
'squared_dataset/IMG_7071.JPG', 
'squared_dataset/IMG_7073.JPG', 
'squared_dataset/IMG_7076.JPG', 
'squared_dataset/IMG_7077.JPG', 
'squared_dataset/IMG_7078.JPG', 
'squared_dataset/IMG_7080.JPG', 
'squared_dataset/IMG_7083.JPG', 
'squared_dataset/IMG_7089.JPG', 
'squared_dataset/IMG_7092.JPG', 
'squared_dataset/IMG_7101.JPG', 
'squared_dataset/IMG_7104.JPG', 
'squared_dataset/IMG_7108.JPG', 
'squared_dataset/IMG_7112.JPG', 
'squared_dataset/IMG_7120_.JPG'
```
