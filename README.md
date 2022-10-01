
# Three Factor Authentication 
Add a layer of security to the old 2FA, using Facial Recognition, and mark the time of the users when they log in.

## Abstract
Presently the risk of Cyber Attacks has increased a lot. Do you know how frequently malicious hackers attack our data and privacy? Every 39 seconds! According to reliable estimates, Cybercrimes are expected to cost the world around 6 trillion dollars annually by 2021. Shocking, right? During last year, over 10 billion data breaches were recorded worldwide, And 79% of companies have experienced at least one in the past 18 months.

So it's clear that you need something more to protect your Data and Privacy, and my Project could provide an additional layer of security to all those systems which are more venerable to cyber thefts. I implemented a Face Recognition of the users with a Unique ID for securely authenticating a session.

## Approach
I have implemented a three-factor authentication system, which provides an additional layer security to the old 2FA, with the help of Facial Recognition.

- Factor-1:(Something You Have) Basic Email + Password Authentication.
- Factor-2:(Something You Know) Use Microsoft authenticator to scan QR-Code, generate a TOTP.
- Factor-3:(Something You Are) Facial Biometrics of the user were used to validate his presence.

## Introduction

### Technologies and Packages used in this project,
- Python
- Face Recognition and OpenCV
- Numpy
- Python flask for http server.
- HTML, CSS and Bootstrap for UI
- Operating System

### Features
- Recognize the face of the user.
- Mark the time when user face is recognized in the 3-Factor Login.



### Conclusion
3-factor authentication is preferred, as it is much more difficult for an intruder to overcome. With just a password, an attacker only has to have a single attack skill and wage a single successful attack to impersonate the victim. With multi-factor authentication, the attack must have multiple attack skills and wage multiple successful attacks simultaneously in order to impersonate the victim. This is extremely difficult and, thus, a more resilient logon solution.
