# umbrella

![loadData](pics/screenshot.png?raw=true "loadData")
## Abstract
Some applications do not require stored data from the local database but rather information from either another database (such as an API) or from an internal algorithm. This project demonstrates how the input of a form can be internally processed  without using the local database by means of Django's Class Based Views in combination with a weather API.
## What is it about?
Get a quick answer if an umbrella or a pulloverover is needed for your upcomming trip. Just type in the place where you wanna go and how long you want to stay there. 

## What you can learn from the code
### How Class Based Views (CBVs) are used without saving an instance to the database by **FormViews**. 
In *views.py* the class **LocationFormView** derives from the class **FormView**. The **FormView** class is crucial as it does not create or manipulate an object in the local data base. Upon its initial call it creates an empty form object on the base of the class defined in *forms.py*. As a result your browser shows an empty form. If however post requests are send, the form object contains the data that was typed in by the user. This data can then be processed, as described in the following section.  

### How to integrate an API and costumized logic in CBVs
Upon a post request the following procedure is triggered in the *views.py* file. An empty context object is delivered by the inherited method **get_context_data**. This is passed to another inherited method **form_valid**. Here the context is filled with the weather data that stems from the custom method get_forcast. The **get_forecast** method receives the data that is typed in by the user in a form object from *forms.py*. On the base of the form data and your personal API key a request is send to the weather API ("http://api.weatherapi.com "). The response is then filtered with regards to the data we desire (in this case the rain probability and the minimum temperature). The context object is then sent by **form_valid** to the templates where its content is displayed. Note: the **get_forecast** method is representative for both, a method that uses an API and internal logic (filtering). 

![loadData](pics/dataflow.png?raw=true "loadData")
#### Basic Data Path


### How to use Bootstrap
The positioning of the elements is managed by bootstrap flex. 
By using the class **container-fluid**, the *header.html* reaches across the entire viewport while the class **container** confines the residual elements in a more narrow column of the viewport. The **justify-content-center** class  causes child elements to be horizontally centeres. The *header.html* and  *form.html* are placed on top of each other whereas *current.html*, *umbrella.html* and *pullover.html* are placed next to eachother. The former constellation is reached by assigning the **d-flex flex-column** class to the mother element. The side by side placement is reached by simply using **d-flex** in the mother element. With **justify-content between**, the elements contained will be homogeneously distributed. 
Beautiful form fields are achieved by the class **form-control** which are realized by widgets in the *forms.py*. 

![loadData](pics/BootstrapPosition.png?raw=true "loadData")
