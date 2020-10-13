# TrainCNNDeepLossAudios

One can download the Mexican pre-prepared /dataset from https://drive.google.com/drive/folders/1XzBAKxKom4TAr-Or91dh2rXywnjbWijo?usp=sharing

one the must upload it in a blob storage
and then execute it by 
`az storage blob download --account-name nielsendataset --container-name nielsendataset --name dataset.zip --file ~/TrainCNNDeepLossAudios `
supposing nielsendataset is the name of the storage account and the container, and the name of the zip is dataset.zip, and you already git cloned this repo
to execute the above you need
`curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`
or manually,
`sudo apt-get update`
`sudo apt-get install ca-certificates curl apt-transport-https lsb-release gnupg`
`curl -sL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/microsoft.gpg > /dev/null `
    `AZ_REPO=$(lsb_release -cs)`
`echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" |sudo tee /etc/apt/sources.list.d/azure-cli.list`
    
    `sudo apt-get update`
`sudo apt-get install azure-cli`
`az login`

extracting the zip with
`sudo apt-get install unzip`

`unzip dataset.zip`

Then just run and wait for 
`python2 senet_train.py`
