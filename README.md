

#  -------------------***Twitter-Feed-Analysis***------------------


## User Story:
   The target customers for this project are people who are using twitter. users can track the hottest topics or famous stars  or events they concerns on by inputing keywords in this program. this project will download some twitter feeds in a time peroid which is user set through twitter API, then we get the reaslut of analysis by uploading the contents to google natural language API. basing on database for google natural language API, the program will return users how many percentage is positive attitude regarding the tpoics, stars and events. 
   
 ##  Architecture
![EC601_mini_project (1)](https://user-images.githubusercontent.com/55214297/65456685-dde69100-de17-11e9-87dd-ae89dc077a24.png) 

## before start:
   Before running this python programe, please make sure that you have tweepy and google cloud library. of course python you have. In additon, you need have keys for twitter API and google cloud API. if not,trying following source, I hope they will help you.
   
   
 ### 1.Checking tweepy and install: 
  
        python
        
        import tweepy
     
   If there is no error, tweepy should be installed,
          **if there are some errors**: 
             [instal tweepy in the termindal](https://pypi.org/project/tweepy/#history)
                
         pip install tweepy
                
   ####   **Also having trouble**:
   ##### I got trouble in this step, maybe the reason is that I use virtualbox with ubuntu. [Try to install virtualenv](https://cloud.google.com/python/setup). Then open virtualen then try again :
                    
         source env/bin/activate
                    
         pip install tweepy  
         
 ###  2. Setting up google API
 
   
   -  [create a project in google cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects)                                                                                                                   
   -  [Getting Started with Authentication](https://cloud.google.com/docs/authentication/getting-started)
           
          pip install google-cloud-language
           
          pip install google-cloud-vision
          
          export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"
 
  ###  3. Getting search results from twitter
   -   [We first use twitter API to get searching results, and the returning information are in json format.]
   -   [Then we process these data and get the information we want, like the content, like amounts and retweet amounts.]
          

            
       
