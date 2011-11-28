#Beacon
Beacon is a very simple blog engine that just picks up, parses, and serves your blog from a Github repository. 

You can adjust the code, templates and styling in Beacon, while leaving your content completely separate and independent. Beacon activates whenever you push new or edited content to your repository and just picks up all the changes. 

Beacon runs on Google App Engine, and should be able to power most, if not all, blogs well within the free quota. 

Under the hood, it's using:

* Jinja2 templates
* SCSS
* NDB (lots of caching)

It currently powers [The Hangar](http://hangar.runway7.net), the [Runway 7](http://www.runway7.net) blog. 


<img src="http://code.google.com/appengine/images/appengine-silver-120x30.gif" 
alt="Powered by Google App Engine" />