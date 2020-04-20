# aiida-scheduler-bundle
Home of custom AiiDA scheduler plugins

# Why do we need it?
AiiDA nicely comes with a handful of scheduler plugins that we can use for running our calculations. However, not all HPCs are configured in a similar fashion that may require minor or major changes in the shipped plugins with AiiDA to make them work for particular HPC. 
The hard way to do it (which I was doing for few month) is as follows:
* forking aiida-core GitHub repository
* add your modified/completely new scheduler plugin to your fork
* go cherry-picking whenever you need to upgrade AiiDA
The easier way is using `aiida-scheduler-bundle`

# How does it work?
It adds custom plugins under the `aiida-scheduler` entry point. So, once you have it installed, you will have extra scheduler plugins in addition to ones shipped with AiiDA. Once you need to configure the computer, you simply provide the entry point for the custom scheduler plugin.

# How to add your custome schduler?
* Simply fork this repository. 
* Create a folder with your desired name.
* add your files inside it.
* add the proper entry points to the `setup.json`.
* if you like, you may kindly open and PR and add your collection to the package so it can contain all possible combinations and plugins to be used by others as well. 




