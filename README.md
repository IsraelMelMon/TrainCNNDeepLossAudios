# TrainCNNDeepLossAudios

One can download the Mexican pre-prepared /dataset from 
https://drive.google.com/drive/folders/1XzBAKxKom4TAr-Or91dh2rXywnjbWijo?usp=sharing
one the must upload it in a blob storage
Then on the Azure CLI connecting via ssh to the VM, we install all the necessary packages for the azure CLI,

`sudo apt-get update -y`

`sudo apt-get install gcc python3-dev`

`sudo apt install python3-distutils`

`sudo apt-get install -y libssl-dev libffi-dev python3-dev build-essential`

`sudo apt-get update && apt-get install -y libssl-dev libffi-dev python3-dev build-essential`

`curl -L https://aka.ms/InstallAzureCli | bash`

`exec -l $SHELL`

`az login`

we can then download the zipped dataset with 

`az storage blob download --account-name testtestno --container-name dataset --name dataset.zip --file ~/TrainCNNDeepLossAudios/dataset.zip`

supposing nielsendataset is the name of the storage account and the container, and the name of the zip is dataset.zip, and you already git cloned this repo
and are inside TrainCNNDeepLossAudios

extracting the zip with

`sudo apt-get install unzip`

`unzip dataset.zip`
Installing pip2
`sudo apt install python-pip`

`pip2 install -r requirements`
if you have a gpu
`pip2 install tensorflow_gpu==1.4.0`
Then just run and wait for 
`python2 senet_train.py`

## Run in Windows
To run in Windows 10+, you can install miniconda with python 3.8 then downgrade to python 3.6 compatible with tensorflow 1.14
`conda install -c anaconda python=3.6`
and then for cpu
`conda install -c conda-forge tensorflow=1.14`
for gpu

***`conda install -c anaconda tensorflow-gpu=1.14`
`conda install -c conda-forge tensorflow-gpu=1.14 cudatoolkit=9.0`
Install azure CLI on Powershell Conda
`Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi; Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi /quiet'`

## NOTE: Audio files should be named the same

