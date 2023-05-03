# ig_hastag_liker_bot
IG bot that likes posts of a given list of hastags

This code is for an Instagram bot that logs into an Instagram account, 
finds and likes posts related to a specified hashtag. 

It uses the Selenium package to automate the process of logging in and interacting with the Instagram website.

The code imports necessary modules such as Selenium's WebDriver, Keys, and Service classes, as well as time, random, and datetime modules. It then defines several constants such as a time and random constant for simulating human-like behavior, hashtags to search for, and path, and user credentials for logging in.

It defines a class called "Instabot" that contains methods for logging in, finding posts based on a specified hashtag, and liking those posts. In the login method, the bot navigates to the Instagram login page, accepts cookies, enters the provided username and password, and submits the login form. In the find_hashtag_posts method, the bot navigates to a page containing relevant posts based on the specified hashtag. In the like_posts method, the bot likes the specified number of posts by clicking on the like button and moves on to the next post.

Finally, the code instantiates the Instabot class, logs in, finds and likes posts, quits the WebDriver instance, and writes a log file to record the start and end times of the task.

Make sure to fill in the "TODO"s.
