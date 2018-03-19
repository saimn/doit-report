# Report command for [doit](https://github.com/pydoit/doit).

This plugin for [doit](https://github.com/pydoit/doit) add a new `report`
command, which shows an ASCII or HTML report with the task execution status.

*Note:* this plugin uses [Astropy](https://github.com/astropy/astropy/)'s
[Table](http://docs.astropy.org/en/latest/table/index.html) class to create
a table and print it either to the console in ASCII format or to an HTML page.
Astropy is an heavy dependency (it requires Numpy) for this small plugin, but it
was the easiest way to go for now and I didn't find similar features in
a lighter package.

Example console output:

![console output](https://user-images.githubusercontent.com/311639/34677091-4be1ae52-f48f-11e7-83c7-94d259193176.png)

And HTML:

![HTML output](https://user-images.githubusercontent.com/311639/34677129-69749560-f48f-11e7-96bf-d9f3e994eb04.png)


