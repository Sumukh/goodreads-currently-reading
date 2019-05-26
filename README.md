# Python Flask on ZEIT Now

[Demo](https://python-flask.now-examples.now.sh)

This directory is a brief example and starter app for [Flask](http://flask.pocoo.org), ready to deploy on [ZEIT Now](https://zeit.co/now).

To get started with this project yourself, use the following command from [Now CLI](https://zeit.co/docs/v2/getting-started/installation#now-cli):

```shell
$ now init python-flask
```

> Alternatively, create a project, and Git repository, with this example template [using the ZEIT dashboard](https://zeit.co/new/python-flask).

Once initialized locally, you will see the files `/index.py` and `/about/index.py` which each correspond to a route, `/` and `/about`, respectively. Each file defines a [Flask wildcard catch-all](http://flask.pocoo.org/snippets/57/) so that we can utilize the routing layer in the Now Platform defined in `now.json`.

In this case, no routes are defined in `now.json`, so we can rely on the filesystem for routing.

To [deploy](https://zeit.co/docs/v2/deployments/basics) this application, with [Now installed](https://zeit.co/docs/v2/getting-started/installation), run the following from your terminal:

```shell
$ now
```

Alternatively, your new Flask app can be automatically deployed and aliased using [Now for GitHub](https://zeit.co/docs/v2/integrations/now-for-github) or [Now for GitLab](https://zeit.co/docs/v2/integrations/now-for-gitlab). Pushing these files to a new repository with a `now.json` file in the root, and with either [Now for GitHub](https://zeit.co/docs/v2/integrations/now-for-github) or [Now for GitLab](https://zeit.co/docs/v2/integrations/now-for-gitlab) configured for that repository, means your site will be automatically deployed for every push and pull/merge request, and aliased for every push to the default branch!

## Included In This Starter

This starter project includes:
- A `/index.py` file that responds to the `/` route.
- A `/about/index.py` file that responds to the `/about` route.
- A pre-defined `Pipfile` that installs Flask as a dependency and defines the Python runtime version.
- A generated `Pipfile.lock` that ensures exact versions of dependencies to avoid the risk of automatically upgrading packages that depend upon each other and breaking your project dependency tree.

## Resources

For more resources on how to configure your new Flask app to do more with Now or to deploy any other kind of application, see the following:

- [New to Now? Get a quick introduction](https://zeit.co/docs/v2/getting-started/introduction-to-now)
- [Learn the basics of deployment on Now](https://zeit.co/docs/v2/deployments/basics)
- [Learn how to configure your Now deployments](https://zeit.co/docs/v2/deployments/configuration)
- [Learn how to configure Now Routes for redirects, caching, and more](https://zeit.co/docs/v2/deployments/routes)
- [Learn how to alias your deployment to a domain or other unique shareable URLs](https://zeit.co/docs/v2/domains-and-aliases/introduction)

For more information on Flask itself, [see their documentation](http://flask.pocoo.org/docs/).

