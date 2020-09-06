# web-content-classification
This is an exercise to practice classifying website content (betting or non betting website)

This exercise has 2 parts:
Part 1 - Generating the dictionary of keywords.
Part 2 - Using the dictionary of keywords to classify a website.

Part 1
1. Gather manualy as much as possible gambling website. Then list the URLs of the websites in a text file.

2. Using the URL list, create a Python script that will visit those websites, parse out the keywords and generate a dictionary of Gambling-related terms. This dictionary can be any file format (text, json, csv, etc.) that you will be using in Part 2. You can use any method that you deem necessary to generate the appropriate keywords.
	- INPUT: yourscript1.py <the text file with the gambling URLs>
	- OUTPUT: dictionary file

Part 2
Using the dictionary from Part 1, create a Python script that will expect a URL input, and then generate a classification if it's a Gambling site or not.
	- INPUT: yourscript2.py <Any URL>
	- OUTPUT1: Gambling site
	- OUTPUT2: Non-Gambling site
