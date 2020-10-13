# TrainCNNDeepLossAudios

One can download the Mexican pre-prepared /dataset from https://drive.google.com/drive/folders/1XzBAKxKom4TAr-Or91dh2rXywnjbWijo?usp=sharing

one the must upload it in a blob storage
and then execute it by 
`az storage blob download --account-name nielsendataset --container-name nielsendataset --name dataset.zip --file ~/TrainCNNDeepLossAudios `
supposing nielsendataset is the name of the storage account and the container, and the name of the zip is dataset.zip, and you already git cloned this repo
to execute the above you need
`curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`

extracting the zip with
`sudo apt-get install unzip`

`unzip dataset.zip`

Then just run and wait for 
`python2 senet_train.py`
