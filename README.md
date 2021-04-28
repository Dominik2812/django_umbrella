# umbrella

![loadData](pics/screenshot.png?raw=true "loadData")
## Abstract
Some application do not require stored data from the local database but rather information from either another database (such as an API) or from an underlying algorithm. This project demonstrates how such a case can be realized with Django's Class Based Views in combination with a weather API.
## What is it about?
Get a quick answer if an umbrella or a pulloverover is needed for your upcomming trip. Just type in the place where you wanna go and how long you want to stay there. 

## What you can learn from the code
### Basic Data Path
In *views.py* the class **LocationFormView** derives from the class **FormView**. An empty context object is delivered by the inherited method **get_context_data**. This is passed to another inherited method **form_valid**. Here the context is filled with the weather data that stems from the custom method get_forcast. The **get_forecast** method receives the data that is typed in by the user by a form object from *forms.py*. On the base of the form data and your personal API key a request is send to the weather API ("http://api.weatherapi.com "). The response is then filtered with regards to the data we desire (in this case the rain probability and the minimum temperature). The context object is then sent to the templates where its content is displayed. Note: the **get_forecast** method is 

![loadData](pics/dataflow.png?raw=true "loadData")

### How Class Based Views (CBVs) interact with forms without saving an instance to the database. 

### How to integrate an API in CBVs
### How to use Bootstrap

### Keywords
Class Based Views
FormView
get_context_data
form_valid
get_forecast
wheather API



