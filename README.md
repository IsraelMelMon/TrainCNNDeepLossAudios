# TrainCNNDeepLossAudios

One can download the Mexican pre-prepared /dataset from https://drive.google.com/drive/folders/1XzBAKxKom4TAr-Or91dh2rXywnjbWijo?usp=sharing
one the must upload it in a blob storage
Then
`sudo apt-get update -y`

`sudo apt-get install gcc python3-dev`

`sudo apt install python3-distutils`

`sudo apt-get install -y libssl-dev libffi-dev python3-dev build-essential`

`sudo apt-get update && apt-get install -y libssl-dev libffi-dev python3-dev build-essential`

`curl -L https://aka.ms/InstallAzureCli | bash`

`exec -l $SHELL`

`az login`

and then execute it by 
`az storage blob download --account-name nielsendataset --container-name nielsendataset --name dataset.zip --file ~/TrainCNNDeepLossAudios `
or 
`az storage blob download --account-name nielsendataset --container-name nielsendataset --name dataset.zip --file /home/nielsenpoc/TrainCNNDeepLossAudios/dataset.zip`

supposing nielsendataset is the name of the storage account and the container, and the name of the zip is dataset.zip, and you already git cloned this repo
extracting the zip with
`sudo apt-get install unzip`

`unzip dataset.zip`

Then just run and wait for 
`python2 senet_train.py`
