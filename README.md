VinFluence Version 1.0 08/05/2014
=================================

Background:
VinFluence is an application for wine pairing. It was built on the idea that there has been an increasing amount of wine beginners whose interests have been piqued by this fermented grape juice. Based on the wine varietal, VinFluence will provide pairing suggestions as well as actual highly-rated wine recommendations from Wine.com ready for purchase. 

Created as a web app, VinFluence took on a responsive web design. VinFluence is meant to be viewed on a mobile device, as it makes sense for someone who is on the run with their grocery shopping list to pull out this handy pocket guide for pairing information.

Framework - 
Flask

Style & Templating Languages -
Jinja2, HTML, CSS, JavaScript, Bootstrap, Elastislide

API - 
VinFluence works with the Wine.com API to generate the wine recommendations. This app utilizes Python to make (REST) API calls to Wine.com, which returns JSON content. Prior to this project, I have never worked with APIs. What made this part of the project even more challenging was the obscurity of the documentation and lack of good sample queries since the API is in beta release. 

Caching - 
Before making an API call, VinFluence first checks it's own database using SQLAlchemy to see if there is existing content to return as wine recommendations. If not, it will then make the API call and store the request into the database. Storing these information into the database will allow less API calls to be made and faster load time. 

User Interface -
Created with mobile in mind, this app is responsive and flat in design. The user interface is kept simple, clean, and straightforwardly understable, making VinFluence the ideal cheatsheet when dining out or hosting your next party. 


