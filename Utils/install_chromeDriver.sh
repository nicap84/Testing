#!/bin/bash
# download and install latest chromedriver for linux or mac.
# required for selenium to drive a chromedriver browser.

install_dir="/usr/local/bin"
latestChromeDriver=curl http://chromedriver.storage.googleapis.com/LATEST_RELEASE
echo $latestChromeDriver
if [[ $(uname) == "Darwin" ]]; then
    url="http://chromedriver.storage.googleapis.com/$latestChromeDriver/chromedriver_mac64.zip"
elif [[ $(uname) == "Linux" ]]; then
    url="http://chromedriver.storage.googleapis.com/$latestChromeDriver/chromedriver_linux64.zip"
else
    echo "can't determine OS"
    exit 1
fi
echo $url
curl -s -L "$url" | tar -xz
chmod +x chromedriver
sudo mv chromedriver "$install_dir"
echo "installed $latestChromeDriver"
