# textrank

This is a simple Flask app that allows a client to request the TextRank of a webpage for bitcoin via the 21 marketplace.

## Pre-requisites

 - Python3.x installed
 - 21 libraries installed
 - Logged into 21 and joined the 21 marketplace
 - Flask

## Starting the server

Starting the server is as simple as running the following command:

```
$ python3 ./src/textrank.py
```

This will start the server and will connect the app to your 21 wallet in which whenever there are any request to the `/rank`
endpoint 100 satoshis will be deposited to your wallet.

## Publish the app to the 21 marketplace

Each app in the 21 marketplace requires that there be a manifest file which is not included in this project due to security reasons.
A sample manifest file can be found [here](https://21.co/learn/intro-to-21/manifest.yaml) or use the following sample:

```yml
info:
  title: 'Hello, World!'
  description: 'Say hello to the world!'
  ## TODO: Replace this IP address with your 21 address
  ##       You can get your IP address by running the following command
  ## python3 -c 'from two1.commands.util import zerotier; print(zerotier.get_address("21mkt"))'
  x-21-quick-buy: '21 buy "http://10.244.108.173:5000/hello"'
  x-21-category: utilities
  x-21-app-image: "https://cdn.filepicker.io/api/file/x6J1kiKyT9WhjmbqBrAb"
  x-21-total-price:
    min: 3000
    max: 3000
  contact:
    ## TODO: Replace this information with your own
    name: Satoshi Nakamoto
    email: satoshi@example.com
## TODO: Replace this IP address with your 21 address
##       You can get your IP address by running the following command
## python3 -c 'from two1.commands.util import zerotier; print(zerotier.get_address("21mkt"))'
host: 10.244.108.173:5000
schemes:
  - http
basePath: /
x-21-manifest-path: /manifest
```

Once you have filled out the manifest file with all of your information and placed the file in the manifest directory of the prject,
let's publish the app to the marketplace using the command:

```
$ 21 publish submit ./path/to/manifest.yml
```

if successful you will get the following output:

```
You might need to enter your superuser password.
Publishing Hello, World! at http://10.244.137.115:5000/ to 21market.
Hello, World! successfully published to 21market. It may take a couple of minutes for your app to show up in the marketplace.
You can view your app at https://21.co/mkt.
```

## LICENSE

MIT
