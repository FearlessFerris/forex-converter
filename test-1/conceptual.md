### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  Unlike JavaScript, Python runs on a server rather than a browser and will allow users to express high level concepts
  using super clean and easy to read syntax. 

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  You could iterate over the dictionary using a `for in` loop, you could also use the `get()` method on the given dictionary. 

- What is a unit test?

  This type of test will test a single module of code and demonstrate that it will work as expected weather it be not throwing any errors or even in fact throwing errors that are expected under certain circumstances. 

- What is an integration test?

  This will test multiple components together within an application to verify they work as intended. 

- What is the role of web application framework, like Flask?

    These frameworks such as `Flask` will allow developers to more quickly develop and create web applications and services

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

    In requests without `side effects` or server data that does not change arguments are typically passed using a query string
    whereas requests with `side effects` like POST requests, typically are sent as a parameter in a route URL. 


- How do you collect data from a URL placeholder parameter using Flask? 

    You can do this by using `<parameter>` markers around a given parameter in the route url where you can replace the parameter to fit whatever 
    endpoint you are trying to reach.


- How do you collect data from the query string using Flask?

    You can do this by using the `request.args.get()` method, when using this, the `.args` property will allow you to access the actual query parameter
    giving you the ability to edit as you see fit.

- How do you collect data from the body of the request using Flask?

    To do this you can use `request.get_data()` this will give you access to the raw data

- What is a cookie and what kinds of things are they commonly used for?

    Cookies are a name/value pair stored by the client browser, commonly they can be used for: saved shopping cart items, login information, and even website preferences

- What is the session object in Flask?

    The session object is used to track the session data which is a dictionary object that contains a key-value pair of the session variables

- What does Flask's `jsonify()` do?

    This will return a response object in JavaScript Object Notation (JSON) Format
