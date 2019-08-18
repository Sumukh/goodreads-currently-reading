# Goodreads Currently Reading

This application serves as a simple API to list what books you are reading on Goodreads in a friendly JSON format. It wraps another helper API.

# Deployment instruction

To [deploy](https://zeit.co/docs/v2/deployments/basics) this application, with [Now installed](https://zeit.co/docs/v2/getting-started/installation), run the following from your terminal:

```shell
$ now secrets add goodreads-key "your-goodreads-api-key"
$ now -e GOODREADS_API_KEY=@goodreads-key
$ now
```

# License

Source code: MIT