# Park-access-registration-system
HUAWEI Kunpeng App Developer Competition
- Fixed questions
- Link of Works: http://124.71.57.148:5000/visitor/visitoradmin

## Function implementation
### Python Flask Framework
* B/S architecture，the front end and the back end are separated B/S架构，前后端分离
* Based on Werkzeug WSGI toolkit and Jinja2 template engine 基于Werkzeug WSGI工具包和Jinja2模板引擎
![image](https://user-images.githubusercontent.com/57136383/185093349-c3752549-4344-4874-b7ea-c4fd57e54520.png)
### HUAWEI CLOUD Server Deployment Process
First prepare the flask file locally and then transfer it to the HUAWEI CLOUD server through sftp, then install the aarch64 (ARMv8-A) instruction set version of anaconda on the service, and then install the arm version of python and some necessary packages through conda.
Set up the application and connect to the HUAWEI CLOUD database terminal (gaussDB) in the same network segment. The application automatically generates the corresponding database and form.
Then develop the corresponding ingress port (ipv4 5000 TCP) on the server firewall to make the application available for external access.
Complete deployment.

### Function demonstration
-Register people entering and leaving the park during the epidemic period
Login is required before entering the park.

![image](https://user-images.githubusercontent.com/57136383/185093634-f8180e27-1863-4b04-9542-a7fc8a5bdc68.png)

New users need to provide personal information and register.

![image](https://user-images.githubusercontent.com/57136383/185093772-d0ef84a6-6543-4def-b403-20451dd4dee2.png)

Generate QR code for park personnel, and obtain the entry and exit records of the park according to the QR code.

![image](https://user-images.githubusercontent.com/57136383/185093983-11701669-3e30-4964-a681-8096d8e8051f.png)

The system also has standardized log output.

![image](https://user-images.githubusercontent.com/57136383/185094158-29b8e935-0323-46c8-9196-2f08713fad30.png)

At the same time, travel records of park personnel can also be queried.

![image](https://user-images.githubusercontent.com/57136383/185094383-dccbe23d-3720-402f-a90c-0c23561bd91b.png)

### Architecture & Performance
Function point 1: Deploy applications using Huawei ECS
Function point 2: Use HUAWEI CLOUD database GaussDB to store data
Feature point 3: Use HUAWEI CLOUD Firewall to filter traffic

![image](https://user-images.githubusercontent.com/57136383/185094831-c339dc0b-c704-4bad-875c-2a898814c5c8.png)

-Advantages
1) Simple, Flask's routing and routing functions are set by decorators, and developers do not need to match other files
2) Low coupling, Flask is compatible with a variety of databases and templates
3) Very suitable for developing APIs for web services
4) 100% use of HUAWEI CLOUD services

## Value of Business Scenario
1) Solved the problem of cross-infection caused by the pen used for registration, slow writing caused queues to cause crowds to gather, and the change of guards caused people to not know the number of people entering and leaving.
2) It can reduce contact, register efficiently, and greatly improve the efficiency of prevention and control registration.
3) Make epidemic prevention and control investigation more accurate, convenient and efficient.

