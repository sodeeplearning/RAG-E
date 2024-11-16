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
- [Upload audios](#upload-audios)
- [Adding data](#adding-data)
- [Get bot data](#get-bot-data)

### [Prompting](#prompting)
- [Prompt text-text](#prompt-text-from-text)
- [Prompt text-voice](#prompt-voice-from-text)
- [Prompt voice-text](#prompt-text-from-voice)
- [Prompt voice-voice](#prompt-voice-from-voice)

### [Clients](#clients)
- [Add customer](#add-customer)
- [Remove customer](#remove-customer)

# Creating

### Create bot
Create bot from user id.
```html request
POST /api/create_bot
```
Usage guide:
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
Usage guide:
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
Usage guide:
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
Usage guide:
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
Usage guide:
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
Usage guide:
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
Usage guide:
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
Usage guide:
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
Usage guide:
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

### Upload audios
Add audio files to a created bot.
```html request
POST /api/upload_audios
```
Usage guide:
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

Usage guide:
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

Usage guide:
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

### Prompt text from text
Get text answer from text prompt.
```html request
POST /api/prompt/text
```

Usage guide:
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

### Prompt voice from text
Get voice answer from text prompt.
```html request
POST /api/prompt/voice
```

Usage guide:
```html request
Input:
    {
        "bot_id": BOT_ID_HASH_STRING,
        "prompt": "Text prompt to a model"
    }

Output:
    .wav file - answer from the model.
```

### Prompt text from voice
Get text answer from voice prompt.
```html request
POST /api/prompt/from_voice/text
```

Usage guide:
```html request
Input:
    bot_id: BOT_ID_HASH_STRING
    file: Audio file with voice prompt.

Output:
    {
        "text": Model's answer
    }
```

### Prompt voice from voice
Get voice answer from voice prompt.
```html request
POST /api/prompt/from_voice/voice
```

Usage guide:
```html request
Input:
    bot_id: BOT_ID_HASH_STRING
    file: Audio file with voice prompt.

Output:
    file: Audio file with voice answer.
```


# Clients

### Add customer
Add customer to a customer database.
```html request
POST /api/add_customer
```
Usage guide:
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
Usage guide:
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
