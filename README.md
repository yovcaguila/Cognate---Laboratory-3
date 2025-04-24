![image](https://github.com/user-attachments/assets/f9241063-d8fd-4f50-bf07-b45c723184a8)# Laboratory 3: Develop & Deploy a Web App inside a VirtualBox Linux VM
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

