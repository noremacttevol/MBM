Day-10_Part-002
 hristopher Turnbull
0 minutes 3 seconds0:03
Christopher Turnbull 0 minutes 3 seconds
Okay, let's talk about preprocessing. So here's the bottom line. When we try to create machine learning models using machine learning algorithms, what we have to remember is that the algorithms are still just computer programs and they're still kind of dumb. The idea of preprocessing then is that we take the information that we're feeding them
Christopher Turnbull 0 minutes 22 seconds
and we simplify it before actually giving it to the algorithm.
Christopher Turnbull 0 minutes 27 seconds
Right, so it's kind of like we're dumbing down the information to help the algorithm understand it.
Christopher Turnbull 0 minutes 32 seconds
And believe it or not, this is an extremely common practice in the industry. In fact, you pretty much always do this in some way or another when you use a machine learning algorithm on your data, because again, like I said, the algorithms themselves can be kind of dumb.
Christopher Turnbull 0 minutes 50 seconds
Now, pre-processing isn't just one technique. It's actually just a huge collection of all sorts of different techniques. It's more of a broad concept. There's different things we could do that would technically count as pre-processing, such as just cleaning the data and basically checking it for errors.
Christopher Turnbull 1 minute 8 seconds
like missing values or duplicates or nested values or just the structures wrong, that would count as one form of pre-processing. We might combine other data sets together to make sure everything kind of, how do I say this simply, to make sure the machine can look at everything all at once instead of having to handle
Christopher Turnbull 1 minute 30 seconds
different separated data sets. That's what data integration would be. The machine learning algorithm often struggles to understand separated data sets. You kind of have to put all the pieces together for it to see the picture.
Christopher Turnbull 1 minute 45 seconds
That's another example. Data transformation is kind of one of the biggest ones right over here. There's all sorts of other things we could do besides just cleaning it up and putting it together.
Christopher Turnbull 1 minute 55 seconds
Things like encoding it as numbers so that the algorithm's math equation can handle that data. Changing the representation of a feature just to simplify it. What else we got? Scaling our data is a whole thing we could talk about. And basically, like I said, there's a million different things that can go into data transformation.
Christopher Turnbull 2 minutes 18 seconds
Oh, and dropping features, that's another big one. Dropping features, reducing irrelevant columns, and things like that. So all of these things are really important because, like we said, the machine learning model is like a baby brain. It doesn't have common sense. We'd like to think that it does, but in reality, it's still a machine.
Christopher Turnbull 2 minutes 36 seconds
And while we will often still use the computer programs available to us to do these steps, we're still going to use the computer to do a lot of these steps. These steps are often something that our algorithm itself doesn't do on its own.
Christopher Turnbull 2 minutes 53 seconds
So that's the idea behind data pre-processing. That's actually where the term pre-processing comes from. Before we have the model try to process the data, we pre-process it. Right?
Christopher Turnbull 3 minutes 6 seconds
So that's the idea.
Christopher Turnbull 3 minutes 9 seconds
And so of course, for this next question here, how is this different from training or data collection? This is kind of the idea, right? We can see through this flow chart. Data collection is just the very first step before we do all of these different pre-processing steps. And then finally train the model at the very, very end.
Christopher Turnbull 3 minutes 30 seconds
Now, do we always need to perform pre-processing on our data? Do we need to? Technically, no. There are some cases where you can just take your raw data and if you have a good type of algorithm, usually deep learning would be the solution here. You can basically just, you know, force feed the algorithm, all of the data, just
Christopher Turnbull 3 minutes 49 seconds
completely as it is without doing any other pre-processing. And in theory, there are some cases where this can work and the algorithm can handle them. So I don't want to say that we should never, or let me rephrase that. I don't want to say that we should always do pre-processing. There are some algorithms that can kind of sort of
Christopher Turnbull 4 minutes 9 seconds
handle our data and sometimes you know it's overkill, right? Sometimes it's like, okay, I don't need to dumb this down too much because at a certain point I'm just wasting time.
Christopher Turnbull 4 minutes 20 seconds
But if we don't perform pre-processing, it's kind of like we see in this GIF right here. It's literally like we're spoon-feeding just this giant...
Christopher Turnbull 4 minutes 28 seconds
giant massive bit of information straight in the model and it's going to struggle to actually interpret it.
Christopher Turnbull 4 minutes 35 seconds
In most cases too, actually, the program can't even swallow it like this cartoon creature can here, right? The cartoon bird can swallow this. The model can't even always do that. A lot of times it'll crash.
Christopher Turnbull 4 minutes 48   seconds
Right, so.
Christopher Turnbull 4 minutes 50 seconds
This is 1 analogy for how I like to look at it and why we do pre-processing.
Christopher Turnbull 4 minutes 56 seconds
This is 1 final analogy, which honestly you shouldn't do this anyways, but...
Christopher Turnbull 5 minutes 3 seconds
I like to make the analogy of a garbage disposal too, which, just for the record, it's never a good idea to put your trash on the garbage disposal. If you're doing that, please stop. But just to even...
Christopher Turnbull 5 minutes 16 seconds
Further extend that point. Sometimes some of you guys might know your garbage disposal can kind of handle like little tiny bits of food. You know what I mean? If you wash your, if you just wash your dish off and you just have a little bit of food in there, it's not a big deal, right? Your garbage disposal doesn't get stuck. But if you're trying to put like some giant chunk of food that's left over, like a whole,
Christopher Turnbull 5 minutes 36 seconds
freaking turkey that you didn't eat, right? Or something like that, and you shove it down the garbage disposal. Now this thing's clogged. Now you got to go fix that.
Christopher Turnbull 5 minutes 45 seconds
Well, the way that I, this is just an analogy.
Christopher Turnbull 5 minutes 48 seconds
But the way that I kind of look at it is pre-processing is kind of like making sure that our food has been thoroughly chopped up or, you know, there's just tiny bits left before we try to put it into our model. Because if we put these giant unprocessed chunks into the model, it's usually going to struggle with them.
Christopher Turnbull 6 minutes 6 seconds
This is just another way of looking at it.
Christopher Turnbull 6 minutes 9 seconds
Please don't put trash on your garbage disposal, though. All right. We're going to look at some other specific examples of pre-processing, like I said. But I will pause for a second in case there are any questions on that so far.
