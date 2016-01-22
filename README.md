### This is the very simple [FOS Jump](https://fosjump.github.io) Generator

##### Why *FOS Jump* ?
Because findig how to be helpful in the Free/OpenSource comunity is still not straight forward.

Also:

- **Fact n°1**: There are a lot of people who want to help with the FLOS movement because they simply love the idea of it, but they just don't know how they want to do so (not sure what they want to code, or even if they want to code). 

- **Fact n°2**: At the same time: There are a lot of different materials out there that could help one get involved in the FLOS movement (like OpenHatch and Github's tool, and some specific projects with their well organized how-to-contrib documentation and welcoming community), 

- **So**: I thought it might be nice to regroup the tools available in one website ([FOS Jump](https://fosjump.github.io/)) and let people chose which one they feel more comfortable using.

*TL;DR* : This is not about creating the tools, it's about regrouping them in a very simple and user friendly way.


##### Why the generator? 
Because other static web generators are too complex for the needs of the project. (pip install -r requirements.txt)
It's really easy, you can even ignore everything and only check the *Data/* folder for modifications. 

### The project structure:

It's really simple:
* *generate.py*: One python program to generate the website (into the *output/* folder) using [jinja2](http://jinja.pocoo.org/) templating. 
* *template/*: contains the Jinja2 templates
* *Data/*: contains the files you might want to eddit (please follow their simple format):
	* *projects.yml*: contains all the project links. Note that, if you add a project, you need to add an image for it in the *projectsImage/* folder.

		```yaml
			"ProjectName":
			    text: "that explains what the project is about"
			    linkName: "The button to clic"
			    linkURL: https://how.tojoin.the/project
			    image: imagename.jpg
		```	

	* *other.yml*: contains the other links and videos

		```yaml
			videos:
				"video name":
					link: http://the.link.to/it
			....
			interesting:
	    			"a Name": 
					text: " This link is supposed to help finding other Open Source projects to contribute to"
					link: https://the.actual.link/

		```
	* *contribute.md*: markdown content of [contrib.html](https://fosjump.github.io/contrib.html)
		

Modifying one file can be enough to make the wanted changes (Again: *Data/links.yaml* to add or modify a project in the website's [main page](https://fosjump.github.io/). And *Data/other.yaml* for the [Other Materials](https://fosjump.github.io/other.html) page).


### How to contribute to **FOS Jump** ?

Anyone can propose:

* FOS Projects with **good how-to-contribute readings**;
* Websites that help finding projects FOS Projects to participate to;
* Videos about the subject;
* Or any other idea for improving the platform.

There are three main ways to proceed:

#### 1. Making a pull request ([github project]()).

#### 2. Via github issues: 
* Adding links by commenting to [newProjectLink issue](https://github.com/fosjump/fosjump/issues/2) or [otherLinks issue](https://github.com/fosjump/fosjump/issues/1)
* Proposing a modification or something else by [creating a new issue](https://github.com/fosjump/fosjump/issues)

####3. Or sending an email to fosjump@tutanota.com (if you don't have a github account)


#### **IMPORTANT**: 
Only links to FOS projects that are new-commers-friendly are accepted in *the main list*. 

Any type of contribution is welcomed.

