# CS 355 Project

## Language & Libraries
We used Python 3.11 and the libraries rsa, socket, threading, and hashlib to complete this project.

## How to run
Use Python version 3.11 or higher

Note:
If you are on windows you may need to uninstall older versions of python

Install package rsa:
https://pypi.org/project/rsa/

You must connect Alice and Bob on the same machine

## Test files
https://drive.google.com/drive/folders/1_PdcwszAfHYBMPjnIoZQMQ57U31Pn0WI?usp=drive_link

## Code Description
When the program is first run, you will be given the option to either be the host or connect to a host. The connection is made using the socket library in Python.

After you get both Alice and Bob to connect with each other, they will then type in the files that were given by the company, one by one. When they type out the name of the 5 files and hit the enter key, both the sender and receiver will see the hash of each of the files. There is a 0.5-second buffer in between the sending of each hash. The sender will see it as You:(Hash) and the recipient will see it as Stranger:(Hash). The hash is encrypted using SHA-256 and the connection between Alice and Bob is encrypted with RSA. After the files have been sent, the connection will close.


## Protocol
Both Alice and Bob will enter the filenames of the 5 text files they were given (in the directory running the program).
Then they will manually compare their own hashes to the other’s.


## Adversary Capability Assumptions
The adversary could act as Bob or Alice.

The adversary could be a passive listener.


## Security Goals
Our security goal is that a passive adversary, Alice, or Bob do not learn more about the content of each other's files than they already know.

We know that using SHA-256 to hash the files given by the company is secure because the chance of collision between two unique files is negligible (as of November 29, 2023, SHA-256 has no known collisions). The file size ~500 MB fits within the restriction of the size of SHA-256.

If Alice or Bob act as the adversary, that is one of them tries to learn more about the other person’s file contents, our scheme prevents that. If Alice and Bob both have the same files, they will see the hashes are the same. They still don’t learn anything new because they know the content of their own files. If they have different files, they will see that the hashes are different. They still don’t learn anything new about the content of the other person's files since they cannot reverse SHA-256. 

If there is a passive adversary, they will only see the hashes encrypted with RSA. RSA is believed to be secure, so the passive adversary will not learn anything about the plaintexts, or in this case, the hashes.
