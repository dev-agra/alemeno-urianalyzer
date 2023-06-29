This assignment solution is implemented with Django and JavaScript, here front-end is a very basic form for inputting a image which is sent to the backend 
for processing with a DRF API, all relevant library requirements are placed in the .txt file. The endpoint for processing the image is 'process_image',
the webapp is deployed and hosted on render with github repository conected with it that re-deployes the project whenever a new commit is made.
Other deployment schems like Docker with EC2, Nginx proxy were not used as the deployment is only for demonstration purpose.
The webapp is deployed on the url: https://alemeno-urianalyzer-assign.onrender.com/

Instructions to use:
1) Press F12
2) Select a image to test and submit the image file
3) Vist the "Network" section of Inspect Element Tool
4) A "POST" request is made to 'process_image' double click on it
5) A JSON response with RGB values for each of the Urine Strip testing parameter(pH, Blood, etc) is displyed in the "response" section.

The image processing is done as:
![image-processing](https://github.com/dev-agra/alemeno-urianalyzer/blob/master/core_apps/images_app/static/images_app/Screenshot%20(325).png)

The Network Inspect panel:
![network-inspect](https://github.com/dev-agra/alemeno-urianalyzer/blob/master/core_apps/images_app/static/images_app/Screenshot%20(323).png)

The Response is provided as[FireFox-Developer]:
![response](https://github.com/dev-agra/alemeno-urianalyzer/blob/master/core_apps/images_app/static/images_app/Screenshot%20(324).png)

The Response[Chrome]:
![response](https://github.com/dev-agra/alemeno-urianalyzer/blob/master/core_apps/images_app/static/images_app/Screenshot%20(326).png)

