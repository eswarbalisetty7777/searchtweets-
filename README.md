# searchtweets-
[Backend Project] Searching Tweets 
Problem 
Engineers at Noovi have built their own search engine, and now it’s time to add tweets! After building an initial version of their tweet search system, they believe it can be better. Right now, it returns the most recent tweet (highest timestamp) whose tweet text contains all of the words in the query. The Noovi team wants your to help improve it in 3 specific ways: 
. They want searching to be faster on a large set of tweets 
. They want to return the top 5 most recent tweets instead of a single tweet . They want to be able to handle search operators like logical and &, logical or |, and logical not !, as well as grouping by parentheses ( and ) . Please see the specification below for examples. 
They have given you their current prototype and a subset of tweet data and tasked you with improving it in the above ways. 
Running the starter code: 
python starter_code.py (requires python 3.7 or greater) 
go test index_test.go (requires golang) 
Query language specification 
The current Noovi prototype retrieves a tweet that contains all the given words in the query. The spaces between the words in the query act as implied logical ANDs, where each word separated by spaces must be in the returned tweet. 
To extend the query language, we will be explicit about logical ANDs in queries, and we task you to add functionality to your search function to parse and evaluate the following operators: 
& (ampersand) means logical AND (both the word/expression to the left and right must exist in the resulting tweet
| = (pipe) means logical OR (either the word/expression to the left or the right must be in the resulting tweet, or both) 
! (exclamation point) means logical NOT (the returned tweets should NOT contain the following word/expression following this operator) 
Spaces in the query will just exist to separate out words and operators from one another 
You can assume the OR operator | is between a single word/expression: 
Valid: 
Noovi & is & (fast | (very & quick)) 
Noovi & is & (fast | quick) 
Noovi | Neeva 
Invalid: 
Noovi & is & fast | very & quick (this would be ambiguous without parentheses or prioritizing symbols over one another) 
The logical NOT operator only applies to the word or expression immediately following it: 
Noovi & fast & !quick & fun should return tweets with words “Noovi” AND “fast” AND “fun” AND without “quick” 
Noovi & search & fast & !(slow | sluggish) should return tweets with “Noovi” AND “search” AND “fast” but neither slow nor sluggish. 
