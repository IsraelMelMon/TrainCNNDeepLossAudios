#!/bin/bash
fileid="0B7EVK8r0v71pOXBhSUdJWU1MYUk"
filename="new_dataset.ZIP"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}