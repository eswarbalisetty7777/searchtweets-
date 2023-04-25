"""
Please use Python version 3.7+
"""

import csv
from typing import List, Tuple
from collections import defaultdict

class TweetIndex:
    # Starter code--please override
    def __init__(self):
        self.list_of_tweets = []
        self.index=defaultdict(list)
        self.tweetsTimeStampMap={}
        self.LATEST_TWEETS=5
        self.OPERATORS = set(['&', '|', '(', ')', '!'])
        self.PRIORITY = {'&': 2, '|': 1, '!': 3}


    def formatInput(self,query:str):
        query = query.lower()
        query = query.replace(" ", "")
        queryList = []
        word = ""
        for ch in query:
            if ch >= 'a' and ch <= 'z':
                word += ch
            else:
                if word != "":
                    queryList.append(word)
                word = ""
                queryList.append(ch)
        if word!="":
            queryList.append(word)
        return queryList

    # create index
    def createIndex(self):
        for tweet in list_of_tweets:
            self.tweetsTimeStampMap[tweet[0]]=tweet[1]
            for word in str(tweet[1]).lower().split():
                # compare previous timestamp to avoid duplicates
                if len(self.index[word])>0 and self.index[word][-1]==tweet[0]:
                    continue
                self.index[word].append(tweet[0])
        # reverse the list (sort timestamps in decreasing order)
        for key in self.index:
            self.index[key]=self.index[key][::-1]




    # convert infix to postfix
    def infix_to_postfix(self,expression:[str]):

        stack = []
        output = []
        for ch in expression:
            if ch not in self.OPERATORS:
                output.append(ch)
            elif ch == '(':
                stack.append('(')
            elif ch == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            else:

                while stack and stack[-1] != '(' and self.PRIORITY[ch] < self.PRIORITY[stack[-1]]:
                    output.append(stack.pop())
                stack.append(ch)

        while stack:
            output.append(stack.pop())

        return output







    # Starter code--please override
    def process_tweets(self, list_of_timestamps_and_tweets: List[Tuple[str, int]]) -> None:
        """
        process_tweets processes a list of tweets and initializes any data structures needed for
        searching over them.

        :param list_of_timestamps_and_tweets: A list of tuples consisting of a timestamp and a tweet.
        """
        for row in list_of_timestamps_and_tweets:
            timestamp = int(row[0])
            tweet = str(row[1])
            self.list_of_tweets.append((tweet, timestamp))



    def notQuery(self,pList):
        result=[]
        pIndex=0
        for i in range(len(list_of_tweets)-1,-1,-1):
            if pIndex<len(pList) and i==pList[pIndex]:
                pIndex+=1
            else:
                result.append(i)
        return result




    # and query
    def andQuery(self,pList,qList):
        result=[]
        pIndex=0
        qIndex=0
        while pIndex<len(pList) and qIndex<len(qList):
            if pList[pIndex]==qList[qIndex]:
                result.append(pList[pIndex])
                pIndex+=1
                qIndex+=1
            elif pList[pIndex]>qList[qIndex]:
                pIndex+=1
            else:
                qIndex+=1
        return result
    # or query
    def orQuery(self,pList,qList):
        result=[]
        pIndex=0
        qIndex=0
        while pIndex<len(pList) and qIndex<len(qList):
            if pList[pIndex]==qList[qIndex]:
                result.append(pList[pIndex])
                pIndex+=1
                qIndex+=1
            elif pList[pIndex]>qList[qIndex]:
                result.append(pList[pIndex])
                pIndex+=1
            else:
                result.append(qList[qIndex])
                qIndex+=1
        while pIndex<len(pList):
            result.append(pList[pIndex])
            pIndex+=1
        while qIndex<len(qList):
            result.append(qList[qIndex])
            qIndex+=1
        return result


    # Starter code--please override
    def search(self, query: str) -> List[Tuple[str, int]]:
       
        queryList=ti.infix_to_postfix(ti.formatInput(query))
        stack=[]
        for word in (queryList):
            if word not in self.OPERATORS:
                stack.append(self.index.get(word,[]))
            else:
                if word=="!":
                    pList = stack.pop()
                    stack.append(ti.notQuery(pList))
                else:
                    pList = stack.pop()
                    qList = stack.pop()
                    if word=="&":
                        stack.append(ti.andQuery(pList,qList))
                    elif word=="|":
                        stack.append(ti.orQuery(pList,qList))
        searchResults = stack.pop()
        topSearchResults=[]
        for idx in range(min(len(searchResults),self.LATEST_TWEETS)):
            topSearchResults.append(str(searchResults[idx])+" - "+ti.tweetsTimeStampMap[searchResults[idx]])

        return  topSearchResults


        # list_of_words = query.split(" ")
        result_tweet, result_timestamp = "", -1
        # for tweet, timestamp in self.list_of_tweets:
        #     words_in_tweet = tweet.split(" ")
        #     tweet_contains_query = True
        #     for word in list_of_words:
        #         if word not in words_in_tweet:
        #             tweet_contains_query = False
        #             break
        #     if tweet_contains_query and timestamp > result_timestamp:
        #         result_tweet, result_timestamp = tweet, timestamp
        # return [(result_tweet, result_timestamp)] if result_timestamp != -1 else []

if __name__ == "__main__":
    # A full list of tweets is available in data/tweets.csv for your use.
    tweet_csv_filename = "../data/small.csv"
    list_of_tweets = []
    with open(tweet_csv_filename, "r") as f:
        csv_reader = csv.reader(f, delimiter=",")
        for i, row in enumerate(csv_reader):
            if i == 0:
                # header
                continue
            timestamp = int(row[0])
            tweet = str(row[1])
            list_of_tweets.append((timestamp, tweet))

    ti = TweetIndex()
    ti.process_tweets(list_of_tweets)
    ti.createIndex()
    # query="Noovi & is  & ( fast|   (   very&quick))"
    query="special & neeva & make"
    # query="Noovi & is & fast &!(slow | sluggish)"
    # query="Only & we & ( special | Neeva ) | boring"
    # print(ti.infix_to_postfix(ti.formatInput(query)))
    print(ti.search(query))







    # delete whitespaces
    # query=query.replace(" ","")
    # print(query)
    # print(ti.infix_to_postfix(query))
    # assert ti.search("hello") == ('hello this is also neeva', 15)
    # assert ti.search("hello me") == ('hello not me', 14)
    # assert ti.search("hello bye") == ('hello bye', 3)
    # assert ti.search("hello this bob") == ('hello neeva this is bob', 11)
    # assert ti.search("notinanytweets") == ('', -1)
    print("Success!")
