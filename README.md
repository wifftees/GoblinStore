# Goblin Store
Telegram store with admin page for users tracking, and sending messages.
### How to setup project
1. Clone repository > ```git clone https://github.com/wifftees/GoblinStore ```
2. Install requirements (Python required) > ```pip install requirements.txt```
3. Add your bot token, database username and password in a config file
### Run scripts
- To run server > ``` python server/app.py ```
- To run bot > ``` python bot/start_polling.py ```
### Database
User document
``` 
{
  user_id,
  username,
  chat_id,
  first_name,
  second_name,
  email,
  cart: <array>,
  premium: <boolean>
}
```
Product document
``` 
{
  id,
  product_name,
  url: <url for cloud store>,
  description,
  category: <weapon / poison / armor>
}
```
