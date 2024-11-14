# RAG-E API Documentation


### [Creating](#creating)
- [Create bot](#create-bot)
- [Delete bot](#delete-bot)

### [Bot Manage](#bot-manage)
- [Launch bot](#launch-bot)
- [Stop bot](#stop-bot)
- [Add wishes](#add-wishes)
- [Get users bots](#get-users-bots)
- [Add bot owner](#add-bot-owner)
- [Remove bot owner](#remove-bot-owner)

### [Transfer](#transfer)
- [Upload videos](#upload-videos)
- [Adding data](#adding-data)
- [Get bot data](#get-bot-data)

### [Prompting](#prompting)
- [Prompt text-text](#prompt-text)
- [Prompt text-voice](#prompt-voice)

### [Clients](#clients)
- [Add customer](#add-customer)
- [Remove customer](#remove-customer)

# Creating

### Create bot
Create bot from user id.
```html request
POST /api/create_bot
```
Usage example:
```html request
Input:
    user_id: USER ID
    multipart/form-data
        files: <files>
    
Output:     
    {
        "bot_id": BOT_ID_HASH_STRING,
        "status": "success"
    }
```

### Delete bot
Delete created bot.
```html request
DELETE /api/delete_bot
```
Usage example:
```html request
Input:
    {
        "user_id": USER_ID
        "bot_id": BOT_ID_HASH_STRING
    }

Output:
    {
        "status": "success"
    }
```


# Bot Manage

### Launch bot
Launch created bot 
```html request
POST /api/launch_bot
```
Usage example:
```html request
Input:
    {
        "user_id": USER ID
        "bot_id": BOT_ID_HASH_STRING
    }

Output:
    {
        "status": "success"
    }
```

### Stop bot
Stop launched bot.
```html request
POST /api/stop_bot
```
Usage example:
```html request
Input:
{
    "user_id": USER_ID
    "bot_id": BOT_ID_HASH_STRING
}

Output:
{
    "status": "success"
}
```

### Add wishes
Add wishes to a created bot.
```html request
POST /api/add_wishes
```
Usage example:
```html request
Input:
    {
        "user_id": USER ID,
        "bot_id": BOT_ID_HASH_STRING,
        "wishes": "make everything shortly"
    }
Output:
    {
        "status": "success"
    }
```

### Add bot owner
Add owner to a created bot.
```html request
POST /api/add_owner
```
Usage example:
```html request
Input:
    {
        "bot_id": BOT_ID_HASH_STRING,
        "bot_owner_user_id": USER ID of existing owner,
        "new_owner_user_id": USER ID of new owner
    }

Output:
    {
        "status": "success"
    }
```

### Remove bot owner
Remove owner from created bot.
```html request
DELETE /api/remove_owner
```
Usage example:
```html request
Input:
    {
        "bot_id": BOT_ID_HASH_STRING,
        "bot_owner_user_id": USER ID of existing owner,
        "new_owner_user_id": USER ID of deleting owner,
    }

Output:
    {
        "status": "success"
    }
```


### Get users bots
Get user's bots' ids from user id.
```html request
GET /api/get_users_bots
```
Usage example:
```html request
Input:
    user_id: User ID

Output:
{
    bots_ids: [
        BOT_ID_HASH_STRING,
        ...
        BOT_ID_HASH_STRING
    ]
}
```


# Transfer

### Upload videos.
Add video files to a created bot.
```html request
POST /api/upload_videos
```
Usage example:
```html request
Input:
    bot_id: BOT_ID_HASH_STRING
    user_id: USER ID
    files: list of files to upload

Output:
    {
        "status": "success"
    }
```

### Adding data
Add files to an existing bot. 
```html request
POST /api/add_data
```

Usage example:
```html request
Input:
    bot_id: BOT_ID_HASH_STRING
    user_id: USER ID
    files: list of files to upload

Output:
    {
        "status": "success"
    }
```

### Get bot data
Get files from existing bot.
```html_request
POST /api/get_bot_data
```

Usage example:
```html request
Input:
    {
        bot_id: BOT_ID_HASH_STRING
        user_id: USER ID
    }
Output:
    file.zip - archive file with bot's data.
```


# Prompting

### Prompt text
Get text answer from text prompt.
```html request
POST /api/prompt/text
```

Usage example:
```html request
Input:
    {
        "bot_id": BOT_ID_HASH_STRING,
        "prompt": "Text prompt to a model"
    }

Output:
    {
        "text": "Answer from the model",
        "status": "success"
    }
```

### Prompt voice
Get voice answer from text prompt.
```html request
POST /api/prompt/voice
```

Usage example:
```html request
Input:
    {
        "bot_id": BOT_ID_HASH_STRING,
        "prompt": "Text prompt to a model"
    }

Output:
    .wav file - answer from the model.
```

# Clients

### Add customer
Add customer to a customer database.
```html request
POST /api/add_customer
```
Usage example:
```html request
Input:
{
    "user_id": USER ID of new customer,
    "admin_id": ADMIN_PASSWORD
}

Output:
{
    "status": "success"
}
```

### Remove customer
Remove customer from a customer database.
```html request
DELETE /api/remove_customer
```
Usage example:
```html request
Input:
{
    "user_id": USER ID of removing customer,
    "admin_id": ADMIN_PASSWORD
}

Output:
{
    "status": "success"
}
```
