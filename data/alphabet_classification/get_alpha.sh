#!/usr/bin/env sh
# This scripts downloads the alphabet training data and unzips it.

DIR="$( cd "$(dirname "$0")" ; pwd -P )"
cd $DIR

echo "Downloading..."

wget --no-check-certificate http://cl.ly/473w163M1g2D/download/alphabet_training_data.zip

echo "Unzipping..."

unzip alphabet_training_data.zip

echo "Done."
