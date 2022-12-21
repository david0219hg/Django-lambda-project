## Bank project by David Hurtado

- Main branch has the code for working in local and to_deploy branch has some changes in order to be able to deploy the project with zappa library.

- for running the project in local run it with the dockerfile that is in this project

- for running the project locally run python manage.py runserver
- for running the test run python manage.py test

- The current project is deployed in this host: https://dnkge4u668.execute-api.us-east-1.amazonaws.com/
and for accessing the endpoints deployed it would be necessary to  first enter in the browser https://dnkge4u668.execute-api.us-east-1.amazonaws.com/dev/

The project was deployed with zappa, zappa does the cloudformation and configures the project that works with event bridge, api gateway and lambdas. The DB that I configured to this project is postgres with RDS service, aurora could be a better option but for practicity due that this is a test project I didn't create it with aurora.

The project runs in debug=True for having a better way to try the project, because Django Rest Framework gives an interface for its endpoints. For seeing these possibilities write the url in the browser.

- creating title:
  http verb: POST
  url /titles/
  example of body in json format: 
    {
        "title_id": "USD",
        "title": "DOLAR",
        "clasification": "DIV",
        "value": "500.000.000",
        "creation_date": "2022-03-14",
        "expiration_date": "2023-03-15",
        "fee_paid": "y",
    }

- for getting total quantity of registered titles:
  http verb: GET 
  url /titles/quantity/

- register the payment of a fee:
  http verb: PUT
  url /titles/?title_id=value
  value could be: USD
  example of body in json format:
  {"fee_paid": "y"}

- Modify creation date of specific group of an specific group of instances
  http verb: PUT
  url /titles/?creation_date=value
  value could be: 2022-01-25
  example of body in json format:
  {"creation_date": "2022-02-01"}

- eliminate an specific title
  http verb: DELETE
  url /titles/?title_id=value
  value could be: USD

- show all titles:
  http verb: GET
  url /titles/
