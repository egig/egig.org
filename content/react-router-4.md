Title: React Router 4
Date: 2017-03-04 21:26
Author: egig
Category: Javascript
Tags: javascript
Slug: react-router-4
Status: published

I want to share about the router library: React Router. At this time I write this post, the most popular react router library: React-Router latest release is on version 4 beta 7. Its totally rewrite from previous version, version 3, which I used.

### Server Rendering
On version 3. there is `match` function to match routes to current request-location. So if yout want to use react-router for server side, you have to do following:

```
match({ routes, location: req.url }, (error, redirectLocation, renderProps) => {

  let html = ReactDOMServer.renderToString(<RouterContext {...renderProps} />);

  })
```

In version 4, its way more easier, you just need to use `StaticRouter`:


```
let html =  ReactDOMServer.renderToString(
			<StaticRouter location={req.url} context={context}>
				<ReactRouter4App />
			</StaticRouter>);
```

By the way, I create simple repo for trying this: <https://github.com/egig/ReactRouter4-Isomorphic-Example>

### Route Matching

It is now suports what path-to-regex supports: <https://github.com/pillarjs/path-to-regexp>. Big resolution for this issue: <https://github.com/ReactTraining/react-router/issues/391>.
