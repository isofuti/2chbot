#####################################
#       Code by SochnoeAnime        #
#      github.com/SochnoeAnime      #
#       2021, Nizhny Novgorod       #
#####################################
import pickle
from browser import Browser
from filters import Filters
from hook import WebHook
import sys
import time

class Program():

    def MainProgram():

        print(time.asctime())

        file = open('trainedmodel.pkl', 'rb')

        model, vectorizer = pickle.load(file)
        print('Model Loaded')
        f = open('C:/Ass-coding/2chbot/2chbot/pastthread.txt', 'r+')
        pastthread = str(f.readlines())
        dc = []#an array to avoid repetition
        faplist = []#array with fap content
        webmlist = []#array with webm content

        threads = Browser.load_threads()#open a browser, go to the site and parse all threads

        #check each found thread
        for thread in threads:

            try:

                wordsinposttext = thread.find_element_by_xpath('.//article[@class="post__message post__message_op"]')#find the text of the main post
                posttext = str(wordsinposttext.text)

                if len(posttext) <= 150 and len(posttext) > 0:#check if there are characters in the main post

                    wordsinposttext = Filters.string_preparation(posttext)#select only Cyrillic and Latin characters

                    checkbannedwords = Filters.find_banned(wordsinposttext)#we find ban words

                    if checkbannedwords is False:

                        href = thread.find_element_by_xpath('.//a').get_attribute('href')#take a link to the thread
                        category = Filters.find_category(model, vectorizer, posttext)#define the category

                        if category == 'fap':

                            if thread not in dc and href not in pastthread:
                                    missedpost = thread.find_element_by_xpath('.//div[@class="thread__missed desktop"]')#missed posts in a thread, usually shows the thread so popular
                                    dc.append(thread)
                                    faplist.append(posttext)
                                    missedtext = str(missedpost.text)
                                    faplist.append(missedtext)
                                    faplist.append(href)
                                    f.write(href)
                                    
                        if category == 'webm':

                            if thread not in dc and href not in pastthread:
                                    missedpost = thread.find_element_by_xpath('.//div[@class="thread__missed desktop"]')#missed posts in a thread, usually shows the thread so popular
                                    dc.append(thread)
                                    webmlist.append(posttext)
                                    missedtext = str(missedpost.text)
                                    webmlist.append(missedtext)
                                    webmlist.append(href)
                                    f.write(href)

            except Exception as e:
                print(href)#if there are not enough posts in the thread to display how many posts we missed
                print(e)#usually the error indicates that it cannot find "thread__missed desktop", which means the thread is not yet filled
                continue

        if len(faplist) != 0 or len(webmlist) != 0:
            WebHook.send_hook(faplist, webmlist)

        else:
            print('Not Found')
            
        sys.exit()

Program.MainProgram()
