#Beacon
Beacon is a very simple blog engine that just picks up, parses, and serves your blog posts from a Github repository. 

You can adjust the code, templates and styling in Beacon, while leaving your content completely separate and independent. Beacon activates whenever you push new or edited content to your repository and just picks up all the changes. 

---

Beacon assumes the content repo contains a set of Markdown files, one post per file, (folder organization doesn't matter), each of which have a special header that looks like this:

    <!--
    ~~~
    title: "Rails Validations : A Technical Guide"
    publish: yes
    tags: ruby, rails, validation, technical-guide
    slug: /technical-guides/rails-vaildations
    date: 2011-12-05
    ~~~
    -->

All text between the `~~~` characters is parsed as YAML. Beacon currently requires and supports the following properties:

`title`: A text title that is used in the template on the `<title>` and other meta-tags. 

`publish`: a `yes` or `no` flag that determines whether the post will be published. 

`tags`: A comma separated list of tags that apply to the post.

`slug`: The URL slug at which the post will be served. This also serves as a kind of ID for the post. 

`date`: The date which the post should show as being published on, in the `yyyy-mm-dd` format.

---

Beacon runs on **Google App Engine**, and should be able to power most, if not all, blogs well within the free quota. 

Under the hood, it's using:

* Jinja2 templates
* SCSS
* NDB (lots of memcaching)

It currently powers [Hangar](http://hangar.runway7.net), the [Runway 7](http://www.runway7.net) blog. 


<img src="http://code.google.com/appengine/images/appengine-silver-120x30.gif" 
alt="Powered by Google App Engine" />