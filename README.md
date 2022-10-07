# URL SHORTENER
***
## Quickstart guide:

1. Run project from Docker image:
    > docker-compose build <br />
   > docker-compose up
2. Documentation
   > http://127.0.0.1:8000/swagger/
3. Registration process <br>
To register a new user you need to send POST request to http://localhost:8000/accounts/register/ <br>
In request you should provide next parameters: <br>

   > 1 - username <br>
   > 2 - first_name <br>
   > 3 - last_name <br>
   > 4 - password <br>

   Next step is to obtain the access token. You need to send POST request to http://localhost:8000/accounts/token/ <br>
In request you should provide next parameters: <br>

   > 1 - username <br>
   > 2 - password <br>
   
   And you will get the access token ! <br>

4. Creating redirects <br>
To create new redirect you should send a POST request to http://127.0.0.1:8000/r/create/ <br>
In request you should provide the acces token and only one parameter: <br>

   > 1 - url <br>
   > 
Slug will be generated automatically. You will get shorten url as a response. <br>

5. You can also list available shorten URLs, by sending GET request to http://127.0.0.1:8000/r/urls (Authorization needed)
#### More info available in swagger doc.