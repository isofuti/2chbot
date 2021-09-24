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
        f = open('pastthread.txt', 'r+')
        pastthread = str(f.readlines())
        dc = []
        faplist = []
        webmlist = []

        threads = Browser.load_threads()

        for thread in threads:

            try:

                wordsinposttext = thread.find_element_by_xpath('.//article[@class="post__message post__message_op"]')
                posttext = str(wordsinposttext.text)

                if len(posttext) <= 150 and len(posttext) > 0:

                    wordsinposttext = Filters.string_preparation(posttext)
                    href = thread.find_element_by_xpath('.//a').get_attribute('href')

                    checkbannedwords = Filters.findbanned(wordsinposttext)

                    if checkbannedwords is False:

                        category = Filters.findcategory(model, vectorizer, posttext)

                        if str(category) == 'fap':

                            if thread not in dc and href not in pastthread:
                                    missedpost = thread.find_element_by_xpath('.//div[@class="thread__missed desktop"]')
                                    dc.append(thread)
                                    faplist.append(posttext)
                                    missedtext = str(missedpost.text)
                                    faplist.append(missedtext)
                                    faplist.append(href)
                                    f.write(href)
                                    
                        if str(category) == 'webm':

                            if thread not in dc and href not in pastthread:
                                    missedpost = thread.find_element_by_xpath('.//div[@class="thread__missed desktop"]')
                                    dc.append(thread)
                                    webmlist.append(posttext)
                                    missedtext = str(missedpost.text)
                                    webmlist.append(missedtext)
                                    webmlist.append(href)
                                    f.write(href)

            except Exception as e:
                print(href)
                print(e)
                continue

        if len(faplist) != 0 or len(webmlist) != 0:
            WebHook.send_hook(faplist, webmlist)

        else:
            print('Not Found')
            
        sys.exit()

Program.MainProgram()
