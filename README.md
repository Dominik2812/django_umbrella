# umbrella

![loadData](pics/screenshot.png?raw=true "loadData")
## Abstract
Some application do not require stored data from the local database but rather information from either another database (such as an API) or from an underlying algorithm. This project demonstrates how such a case can be realized with Django's Class Based Views in combination with a weather API.
## What is it about?
Get a quick answer if an umbrella or a pulloverover is needed for your upcomming trip. Just type in the place where you wanna go and how long you want to stay there. 

## What you can learn from the code
### How Class Based Views (CBVs) are used without saving an instance to the database by **FormViews**. 
In *views.py* the class **LocationFormView** derives from the class **FormView**. The **FormView** class is crucial as it does not create or manipulate an object in the local data base. Upon its initial call it creates an empty form object on the base of the class defined in *forms.py*. As a result your browser shows an empty form. If however post requests are send, the form object contains the data that was typed in by the user. This data can tehn be processed, as described in the following section.  

### How to integrate an API in CBVs
Upon a post request the following procedure is triggered in the *views.py* file. An empty context object is delivered by the inherited method **get_context_data**. This is passed to another inherited method **form_valid**. Here the context is filled with the weather data that stems from the custom method get_forcast. The **get_forecast** method receives the data that is typed in by the user by a form object from *forms.py*. On the base of the form data and your personal API key a request is send to the weather API ("http://api.weatherapi.com "). The response is then filtered with regards to the data we desire (in this case the rain probability and the minimum temperature). The context object is then sent by **form_valid** to the templates where its content is displayed. Note: the **get_forecast** method is representative for both, a method that uses an API and interenal logic. 

![loadData](pics/dataflow.png?raw=true "loadData")
#### Basic Data Path


### How to use Bootstrap

### Keywords
Class Based Views
FormView
get_context_data
form_valid
get_forecast
wheather API



