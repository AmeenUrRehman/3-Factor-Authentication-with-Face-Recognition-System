
# Three Factor Authentication 
Made a project which add a layer of security to the old 2FA, using Facial Recognition, and mark the time of the users when they log in.

## Abstract
Presently the risk of Cyber Attacks has increased a lot. Do you know how frequently malicious hackers attack our data and privacy? Every 39 seconds! According to reliable estimates, Cybercrimes are expected to cost the world around 6 trillion dollars annually by 2022. Shocking, right? During last year, over 10 billion data breaches were recorded worldwide, And 79% of companies have experienced at least one in the past 18 months.

So it's clear that we need something more to protect our Data and Privacy, and my Project could provide an additional layer of security to all those systems which are more venerable to cyber thefts. I implemented a Face Recognition of the users with a Unique ID for securely authenticating a session.

## Approach
I have implemented a three-factor authentication system, which provides an additional layer security to the old 2FA, with the help of Facial Recognition.

- Factor-1: (Something You Have) Basic Email + Password Authentication.
- Factor-2: (Something You Know) Use Scanner to scan QR-Code for password.
- Factor-3: (Something You Are) Facial Biometrics of the user were used to validate his presence. <br>

![3-factor](https://user-images.githubusercontent.com/83868776/193419136-a172b038-6432-4761-8d97-7eef60679270.jpg)

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

### Functioning
- <b>Factor-1: (Something You Have) Users log in with their email and password :hugs:.</b>  

![Login_page](https://user-images.githubusercontent.com/83868776/193450228-0a665af1-bc61-40a6-bf7b-466bfb14fccd.png)

- <b>Factor-2: (Something You Know) Users can use the scanner to Scan QR codes for passwords to login into 2nd Factor. :innocent:. </b>

![2nd Login](https://user-images.githubusercontent.com/83868776/193451034-3ef70de0-1b11-4740-8581-57a4375f64b6.png)
 - <b>Factor-3: (Something You Are) Webcam identifies the Users face in real time and mark the time at which the webcam recognized the user. It reveals the ID of the user which the user can use to login into the 3rd Factor :sunglasses: of the Three Factor Authentication. </b>
 
![3rd login with face recogntion](https://user-images.githubusercontent.com/83868776/193453665-53652b6a-5ef2-4f22-92ec-701b8f989532.png)

<b> Login time of the user.<br><b>

![user_login_time](https://user-images.githubusercontent.com/83868776/193452819-bac17d43-a494-4edd-9730-ff4620c2b417.png)


- <b> You are logged into the Personal Page of the website with security :partying_face: <b>. 

![home_page](https://user-images.githubusercontent.com/83868776/193452612-0c2b4857-0474-4fe6-aa4c-9ef28db1bc0c.png)

If Users are not able :pleading_face: to Login with any of the factor authentication they will redirect to factor-1 :disappointed_relieved: of the Three Factor Authentication.

### Conclusion
3-factor authentication is preferred, as it is much more difficult for an intruder to overcome. With just a password, an attacker only has to have a single attack skill and wage a single successful attack to impersonate the victim. With multi-factor authentication, the attack must have multiple attack skills and wage multiple successful attacks simultaneously in order to impersonate the victim. This is extremely difficult and, thus, a more resilient logon solution.
