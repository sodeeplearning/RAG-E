# RAG-E API Documentation

## Content:

### [Creating](#creating)
- [Create bot](#create-bot)
- [Delete bot](#delete-bot)

### [Bot Manage](#bot-manage)
- [Launch bot](#launch-bot)
- [Stop bot](#stop-bot)
- [Get users bots](#get-users-bots)

### [Transfer](#transfer)
- [Upload videos](#upload-videos)
- [Adding data](#adding-data)
- [Get bot data](#get-bot-data)

### [Prompting](#prompting)
- [Prompt text-text](#prompt-text)
- [Prompt text-voice](#prompt-voice)

## Creating

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


## Bot Manage

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


## Transfer

### Upload videos.
Add video files to a created bot.
```html request
POST /api/upload_videos
```
Usage example:
```html request
Input:
    bot_id: BOT_ID_HASH_STRING
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
    files: list of files to upload

Output:
    {
        "status": "success"
    }
```

### Get bot data
Get files from existing bot.
```html_request
GET /api/get_bot_data
```

Usage example:
```html request
Input:
    bot_id: BOT_ID_HASH_STRING

Output:
    file.zip - archive file with bot's data.
```


# Prompting

## Prompt text
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

## Prompt voice
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
