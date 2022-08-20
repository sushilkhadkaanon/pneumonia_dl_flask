LIVE APP: https://cnn-xray.herokuapp.com/
# pneumonia_dl_flask
Web Application (flask) for Pneumonia using Convolution Neural Network. 

Pneumonia is an infection that inflames the air sacs in one or both lungs. 
It kills more children younger than 5 years old each year than any other infectious disease, such as HIV infection, malaria, or tuberculosis. 
Diagnosis is often based on symptoms and physical examination. Chest X-rays may help confirm the diagnosis.

This dataset contains 5,856 validated Chest X-Ray images which is taken from https://data.mendeley.com/datasets/rscbjbr9sj/3.
A 13 layered Deep Neural Network was trained on this dataset and the accuracy was around 90%.

Using flask web framework, I created a web application using the model which predicts whether the input x-ray image is infected with pneumonia or not.
Thanks to
Daniel Kermany,
Kang Zhang and 
Michael Goldbaum
for making the dataset publicly and freely available.

Model's accuracy is 89% whereas it's loss is about 0.28.


![acc_loss](https://user-images.githubusercontent.com/50844865/185703973-9ff190aa-06c3-49c0-9ce3-5e9bcf88744f.png)

Here are images showing model's architecture and the screenshots of the web application:

![index](https://user-images.githubusercontent.com/50844865/185704246-d97247ac-4154-4be3-83b5-0e7656c9474b.png)
![uploading](https://user-images.githubusercontent.com/50844865/185704257-f051b277-fc0b-476e-9ae0-dcb87f168361.png)
![uploaded](https://user-images.githubusercontent.com/50844865/185704266-b29f58e6-fa6a-4495-a627-ff328c545275.png)
![negative](https://user-images.githubusercontent.com/50844865/185704273-b7ef61b4-e749-4679-b969-f5888feb109d.png)
![positive](https://user-images.githubusercontent.com/50844865/185704275-1db096e1-5747-45e9-96a9-5965665aa9c6.png)

![model_arch](https://user-images.githubusercontent.com/50844865/185704649-cd1e564b-d7f1-4d49-86b0-dbbcbae53650.png)
