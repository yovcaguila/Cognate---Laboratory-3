# Laboratory 3: Develop & Deploy a Web App inside a VirtualBox Linux VM
This is a simple, minimalist web application built with **Flask**, designed with a clean black-and-white aesthetic. 
The app includes three pages: **Home**, **About**, and **Contact** (with form handling).

## Framework Used
- **Python 3**
- **Flask** (micro web framework)
- **HTML/CSS** (custom styling with a minimalist black-and-white theme)

## How to Run the Project
1. Open your virtual machine (Ubuntu)
2. Clone or Download the Project
3. Open Terminal
4. Go to flask_app directory
```
cd flask_app
python3 my_app
```
or Run the Flask App
```
flask run --host=0.0.0.0 --port=5000
```
5. Open Browser and Visit:
```
http://localhost:5000
```
6. In Host Machine Browser, Visit:
```
http://<vm-ip>:5000
```
Get IP using:
```
ip a or hostname -I
```

## Issues Encountered and Solutions
### Cannot Access App from Browser (on Host)
Cause: VirtualBox networking not properly configured
Solution:
- Use Bridged Adapter to assign a local network IP.
- Or set up Port Forwarding in NAT mode.

## Reflection
#### What challenges did you face during the deployment process?
- 	The challenge I faced during the deployment process was first not being able to open the web application on the host machine. I looked at the problem and found that the network was not set to bridged adapter. Second, creating the web application was difficult because I needed to go back and forth from the file directory when designing and creating the HTML and CSS files.
#### What did you learn about configuring Linux servers for hosting web apps?
- 	I learned that configuring Linux servers for hosting web applications is not simple. In the terminal, there are a lot of commands, and when a typographical error is made, it will not work. Thus, it taught me to be cautious when inputting commands in the terminal for a smooth process.
#### Which framework did you find easiest to use and why?
- 	I found Flask the easiest to use because it only uses minimal dependencies, making it easy to learn and use for beginners. Also, I have common knowledge regarding Python, which made it much easier to implement the scripts as my back-end.
#### How does deploying in a VM simulate real-world cloud hosting?
- 	Deploying a virtual machine simulates real-world cloud hosting by allowing users to still access the web application with the host machine. With the IP address of the virtual machine, I was able to access the web application using my browser on my laptop.

## Screenshots
### Terminal showing server running

---

![image](https://github.com/yovcaguila/Cognate---Laboratory-3/blob/main/Screenshots/Screenshot%202025-04-24%20125542.png?raw=true)

### Web App Running Inside the VM

---

![image](https://github.com/yovcaguila/Cognate---Laboratory-3/blob/main/Screenshots/Screenshot%202025-04-24%20125306.png?raw=true)
![image](https://github.com/yovcaguila/Cognate---Laboratory-3/blob/main/Screenshots/Screenshot%202025-04-24%20125315.png?raw=true)
![image](https://github.com/yovcaguila/Cognate---Laboratory-3/blob/main/Screenshots/Screenshot%202025-04-24%20125402.png?raw=true)
![image](https://github.com/yovcaguila/Cognate---Laboratory-3/blob/main/Screenshots/Screenshot%202025-04-24%20125410.png?raw=true)

### Host Machine Accessing the Web App

---

![image](https://github.com/yovcaguila/Cognate---Laboratory-3/blob/main/Screenshots/Screenshot%202025-04-24%20125446.png?raw=true)
![image](https://github.com/yovcaguila/Cognate---Laboratory-3/blob/main/Screenshots/Screenshot%202025-04-24%20125453.png?raw=true)
![image](https://github.com/yovcaguila/Cognate---Laboratory-3/blob/main/Screenshots/Screenshot%202025-04-24%20125517.png?raw=true)
![image](https://github.com/yovcaguila/Cognate---Laboratory-3/blob/main/Screenshots/Screenshot%202025-04-24%20125523.png?raw=true)

---

