## Flask framework for web applications

this simple application asks for your name and that is it. The goal was to understand design of a web application using Flask. 
Any web application follows some design principles (those thigs that you ask why and the answer is because). In general , for a flask aplication the parts are: 
  - application.py (or appy.py) contains the py code controling the application
  - requirements.txt contains a list of all libraries
  - statics/ folder with all static code 
  - templates/ folder with the different routes .html
  
  One of the common design patters is MVC - Model View Controller - 
    - Model: contains the application data (sql database, csv ,..) 
    - View: presents the model data to the user 
    - Controller: the piece connecting view and model. 
    
   
  ![Prof David Malac CS50 Harvard](statics/MVC_DesignPatern.PNG)
  
  In this applcation I use "GET" and "POST", and templates like layout.html 
