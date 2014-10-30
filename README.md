# resources

Interact with HTTP resources

### Examples:
    
Create an API resource object

    from resources import JsonResource
    my_api = JsonResource('http://example.com/api')
    
Alternatively with a configuration, parameters same as requests.request()

    my_api = JsonResource('http://example.com/api', \
            options={"auth": ('admin', 'adminPwd')})

Create a shortcut to a specific resource within the API

    users = my_api.users
    
The variable "users" now points to 'http://example.com/api/users'. Now POSTing data to that resource returns a (status_code, result) tuple:

    status, new_user = users.post(data={"name": "Steve", "email"="steve@example.com"})
    
The json response is automatically decoded

    name = new_user["data"]["name"]
    
Fetch a specific resource

    status, rabbit = my_api.rabbits[6385].get()

And delete it

    status, _ = my_api.rabbits[6385].delete()

