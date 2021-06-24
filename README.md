# api-streaming-bots
🤖 API for streaming bots (Twitch, YouTube and Facebook)

# Details

## YouTube

To use bot for YouTube livechat first you need to get oauth access token with endpoint `localhost:3000/v1/youtube/oauth/get_token` it would automatically redirect you to login with your Google account and to give bot access to manage account. After that you would need to create oauth file to save access token with endpoint `localhost:3000/v1/youtube/start?msg=&id=&access_token=` where msg is for message you want to send, id is for livestream id and access_token which you get from last endpoint. This endpoint is for saving access token to file and automatically redirect to starting bot. After that you can use only `localhost:3000/v1/youtube?id=&msg=` without access_token parameter.

### YouTube endpoints

```
/v1/youtube/oauth/get_token             Getting access token
/v1/youtube/start                       Saving access token to file and automatically start to use bot
                                        Queries:
                                        id           (required)
                                        msg          (required)
                                        access_token (required)
/v1/youtube                             Use this if you already have saved access token
                                        Queries:
                                        id           (required)
                                        msg          (required)
```
