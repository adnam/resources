# -*- coding: utf8 -*-
"""
Model HTTP resources

Examples:
    
    from resources import JsonResource
    
    # Create an API resource object
    my_api = JsonResource('http://example.com/api')
    
    # Alternatively with a configuration, parameters same as requests.request()
    my_api = JsonResource('http://example.com/api', \
            options={"auth": ('admin', 'adminPwd')})

    # Create a shortcut to a specific resource within the API
    users = my_api.users

    # Post data to that resource returns a (status_code, result) tuple
    status, new_user = users.post(data={"name": "Steve", "email"="steve@example.com"})
    
    # The json response is automatically decoded
    name = new_user["data"]["name"]
    
    # Fetch a specific resource
    rabbit = my_api.rabbits[6385].get()

    # And delete it
    rabbit = my_api.rabbits[6385].delete()

"""

from .resources import Resource, JsonResource


