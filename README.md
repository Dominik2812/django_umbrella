# umbrella

![loadData](pics/screenshot.png?raw=true "loadData")

## Abstract
Some applications do not require stored data from the local database but rather information from either another database (such as an API) or from an internal algorithm. This project demonstrates how the input of a form can be internally processed without using the local database utilizing Django's **Class-Based Views** in combination with a **weather API** and **Google AutoComplete**.
## What is it about?
Get a quick answer if an umbrella or a pullover is needed for your upcoming trip. Just type in the place where you wanna go and how long you want to stay there. 

## What you can learn from the code
### How to hide your sensitive data such as API keys and secrete Django keys
The App uses the following sensitive keys: API key for the weather data, DjangoSecreteKey and the GoogleMaps API key. Those are stored in secret.py on my local desk and loaded into my python files. In my .gitignore secret.py is included; in this way, I can comfortably run my code at home and at the same time update the code on GitHub without exposing my keys. To run the code create your own secret.py under "umbrella_app". 

### How Class Based Views (CBVs) are used without saving an instance to the database by **FormViews**. 
In *views.py* the class **LocationFormView** derives from the class **FormView**. The **FormView** class is crucial as it does not create or manipulate an object in the local database. Upon its initial call, it creates an empty form object on the base of the class defined in *forms.py*. As a result, your browser shows an empty form. If however post requests are sent, the form object contains the data that was typed in by the user. This data can then be processed, as described in the following section.  

### How to integrate an API and customized logic in CBVs
Upon a post request, the following procedure is triggered in the *views.py* file. An empty context object is delivered by the inherited method **get_context_data**. This is passed to another inherited method **form_valid**. Here the context is filled with the weather data that stems from the custom method get_forcast. The **get_forecast** method receives the data that is typed in by the user in a form object from *forms.py*. Based on the form data and your personal API key a request is sent to the weather API ("http://api.weatherapi.com "). The response is then filtered with regards to the data we desire (in this case the rain probability and the minimum temperature). The context object is then sent by **form_valid** to the templates where its content is displayed. Note: the **get_forecast** method is representative for both, a method that uses an API and internal logic (filtering). 

![loadData](pics/dataflow.png?raw=true "loadData")
#### Basic Data Path

### How to use Bootstrap
The positioning of the elements is managed by bootstrap flex. 
By using the class **container-fluid**, the *header.html* reaches across the entire viewport while the class **container** confines the residual elements in a more narrow column of the viewport. The **justify-content-center** class causes child elements to be horizontally centered. The *header.html* and  *form.html* are placed on top of each other whereas *current.html*, *umbrella.html* and *pullover.html* are placed next to each other. The former constellation is reached by assigning the **d-flex flex-column** class to the mother element. The side-by-side placement is reached by simply using **d-flex** in the mother element. With **justify-content between**, the elements contained will be homogeneously distributed. 
Beautiful form fields are achieved by the class **form-control** which are realized by widgets in the *forms.py*. 

![loadData](pics/BootstrapPosition.png?raw=true "loadData")

### How to use Google Maps Autocomplete API
To facilitate your search an autocomplete function is includes via a javascript file in the static/umbrella_app/google_maps.js. The functionality will be described in short in the following, for a more detailed description please visit https://developers.google.com/maps/documentation/javascript/places-autocomplete and https://developers.google.com/maps/gmp-get-started. 

The *index.html* loads the *"umbrella_app\google_maps.js"* file from the static path. 

![loadData](pics/loadScript.png?raw=true "loadData")

In this file are two functions. The **initAutocomplete()** enables the autocomplete mechanism. This function alone will provide you with suggestions of places while typing. The input field needs to have the id="autocomplete" (see *forms.py*). A Listener is added **onPLaceChanged()**  which enables you to choose one of the suggestions by click or enter. 

![loadData](pics/google_maps.png?raw=true "loadData")

Now to make these functions work, they have to be imported. At the end of the *index.html* a script tag is created which downloads the required, realized by the following code: 

![loadData](pics/createScriptTag.png?raw=true "loadData")

In this way, you don't have to hard code your API key into the script. 
