Designing a messaging web service
------

I have decided to include the name of the application and the version of the API in the URL to separates this service from others that can be running on the same system. The API version is also included in the URL that can help with making updates in the future without affecting applications that rely on the older functions. 

Here are the API end-points:

- GET			
    - http://[IP]/v1/mma/messages/all		
    - Retrieve list of messages
- GET			
    - http://[IP]/v1/mma/messages			
    - Retrieve a message
- POST		    
    - http://[IP]/v1/mma/messages			
    - Create a new message
- PUT			
    - http://[IP]/v1/mma/messages			
    - Update and existing message		
- DELETE		
    - http://[IP]/v1/mma/messages			
    - Delete a message


Example:
-  http://127.0.0.1:5000/v1/mma/messages/all


Parameter: 
- id: 			unique identifier for messages. Numeric type.
- message: 		message description. Text type.
- palindrome: 	TRUE/FALSE.

Our application was written in python and Flask web framework was used to creat the REST API services. The application has been dockerized and can be installed by runnig the install.sh script. The install scrtipt will build a docker image and then run a container that our application will be running inside. 

To install the app, unzip the package and go to root directory of the package and run 'sudo ./install.sh'. Before that make sure Docker is installed in your environment. Once you see this message 'Successfully built <container_ID>' in the terminal, run 'sudo docker pa -a' to make sure the container is running and then check the logs to confirm the app has started and ready for service 'sudo docker logs mma-app'. 

*Testing*
----

If you have curl installed in your environment, you can run the api_test.sh script to test the API. 

*Kubernetes*
----

Kubernetes deployment was not fully tested for this application. The deployment.yml file was not fully tested and can be used to continue with the kubernetes development task. The docker image should exist in the local repo on the host in which you are running the deployment from. 