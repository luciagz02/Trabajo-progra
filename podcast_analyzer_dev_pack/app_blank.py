import datetime
import os
import csv
import json
import uuid

#For easing the ploting
import pandas as pd#data management
import matplotlib.pyplot as plt
import seaborn as sns

#Global variables

MIN_BYTES_DOWNLOAD_200 = 31457280
MIN_BYTES_DOWNLOAD_206 = 1048576
NA = "NA"
KEY_SEPARATOR="_"

#DataModel: in this case an object is used, a dictionary or any other data 
#structure can be used

class Observation:
    def __init__(self):
        pass
    
#Helper functions

def is_valid_method(method):
    """
    This is method to check whether the method used in a request is valid.

    Parameters
    ----------
    method : string
        A non-empty string.

    Returns
    -------
    Boolean
        True if the method is GET, False otherwise.

    """
    
    #FIXME
    return False

def is_valid_status(status):
    """
    This is method to check whether the status of a request is valid.

    Parameters
    ----------
    status : string
         A non-empty string.

    Returns
    -------
    Boolean
        True if the status is 200 or 206, False otherwise.

    """
    #FIXME
    return False
  
def is_valid_resource(resource):
    """
    This is method to check whether the format of a requested resource is valid.

    Parameters
    ----------
    resource : string
        A non-empty string.

    Returns
    -------
    Boolean
        True if the resource ends with mp3.

    """
    #FIXME
    return False
 
def is_valid_user_agent(user_agent):
    """
    This is method to check whether an user agent is a bot.

    Parameters
    ----------
    user_agent : string
        A non-empty string.

    Returns
    -------
    Boolean
        True if the user agent does not contain {"BOT", "SPIDER","CRAWLER", "HERITRIX"},
        false otherwise.

    """
    #FIXME
    return False

def generate_not_valid_request_message(entry):
    """
    This is method that given an entry, validates the request and
    returns the metric error name.

    Parameters
    ----------
    entry : TYPE
        A request.

    Returns
    -------
    string
        Depending on the validation, the method shall return a metric name
        for the error:
            "Bad method",
            "Bad status",
            "Bad format resource"
            "Bot detected",
            "NA" (if unknown)

    """
    #FIXME
    return False

def is_valid_request(entry):
    """
    It is a method that aggregates that different validation functions.
    A request will be valid if it fulfills all validation methods.

    Parameters
    ----------
    entry : TYPE
        request.

    Returns
    -------
    Boolean
        True if the method, status, format resource and user agent are all valid.

    """
    if entry:
        return is_valid_method(entry["method"]) and \
            is_valid_status(entry["status"]) and \
            is_valid_resource(entry["uri_episode"])  and \
            is_valid_user_agent(entry["user_agent"])
    else:
        return False

def is_download (entry, ongoing_downloads, min_bytes):
    """
    This method checks if an input entry in the source dataset can be considered
    a download (200 or 206). This will happened if the number of bytes transferred 
    in the entry request are greater or equal to the min number of bytes 
    for that type of request.

    Parameters
    ----------
    entry : request
        The download entry request.
    ongoing_downloads : dictionary
        The ongoing downloads of some type (200 or 206) identified by id and user agent.
    min_bytes : integer
        The minimum number of bytes to consider this entry request as a download.

    Returns
    -------
    observation : TYPE
        If it is a new download: a new data item containing all input information, 
        a metric name "Download 200" or "Download 206".
        
        None, otherwise, the entry is registered to accumulate bytes but 
        no new download is created.

    """
    #FIXME





    return None

def create_error_observation(metric, uri_episode):
    """
    This method creates an observation error.

    Parameters
    ----------
    metric : string
        The message of a validation error.
    uri_episode : string
        The episode.

    Returns
    -------
    observation : TYPE
        DESCRIPTION.

    """
    #FIXME
    
    #Example with an object
    observation = None
    #observation = Observation()
    #observation.id = str(uuid.uuid4()) #Generate unique ids
    #observation.value = 1
    #observation.metric = metric
    #observation.uri_episode = uri_episode
    return observation

def show_recommendations(recommendations, user):
    """
    This method shows the recomendations generated for a given user.

    Parameters
    ----------
    recommendations : a list of recommend episodes
        The list of recommendations.
    user : string
        The user id.

    Returns
    -------
    None.

    """
    
    
    #FIXME
    
    
    pass
        
def show_stats(stats):
    """
    This method shows the number of processed entries, observations, by
    the type of metric:
        Download 200
        Download 206
        Bad method
        Bad status
        Bad format resource
        Bot detected

    Parameters
    ----------
    stats : dict
        A dictionary of items: metric name (key) and number (value).

    Returns
    -------
    None.

    """
    
    
    #FIXME
    
    
    
    
    pass
 
def show_top_k(top_k):
    """
    This method shows the number of downloads of a dictionary of programs

    Parameters
    ----------
    top_k : dict
        A dictionary of items: program (key) and number (value).

    Returns
    -------
    None.

    """
    
    #FIXME
    
    
    
    
    pass

def get_number (threshold):
    k = int(input("Introduce a number: "))
    while k<threshold:
        k = int(input("Introduce a number: "))
    return k
        

def list_episodes(observations):
    """
    Given a set of observations, processed entries, it returns a set of tuples:
        (episode title, podcast topic)

    Parameters
    ----------
    observations : TYPE
        Observations processed.

    Returns
    -------
    episodes_set : set
         (episode title, podcast topic).

    """
    episodes_set = {}

    #FIXME

    return episodes_set

    

#Program functions

def save_observations_as_csv(observations, filename="observations.csv"):
    """
    Given the observations, entries processed, it saves each observation and 
    its fields in a CSV (Comma Separated Values) file.

    Parameters
    ----------
    observations : list of dict
        Each item contains an observation with all registered fields.
    filename : string, optional
        DESCRIPTION. The default is "observations.csv".

    Returns
    -------
    None.

    """
    
    
    
    #FIXME
    
    
    
    pass


def recommend(observations, episode_set, user="df273cf4-d335-4b7f-b979-17212e8b84d3"):
    """
    Given the observations, entries processed, the episode set, and a user,
    it gives a recommendation of 5 episodes.
    
    To do so, it follows the next process:
        1-Calculate the topics downloaded by an user.
        2-Get the list of episodes in these topics.
        3-Get the number of downloads of these episodes.
        4-Sort the episodes by the number of downloads.
        5-Take the first 5 and return.

    Parameters
    ----------
    observations : list of dict
       Each item contains an observation with all registered fields.
    episode_set : a set of tuples
        (episode title, podcast topic)
    user : TYPE, optional
        DESCRIPTION. The default is "df273cf4-d335-4b7f-b979-17212e8b84d3".

    Returns
    -------
    list
        A list of tuples (episode title, number of downloads).

    """
    recommendations = []
    
    #FIXME
    
    
    #Get the topics downloaded by a user
    #Filter episodes by these topics
    #Calculate the number of downloads per episode
    #Get the number of downloads per candidate episode
       #Optional: filter the episodes that have been already seen by the user
    #Sort candidate episodes downloads
    #Select the first 5
    return recommendations
 


def map_top_episodes(observations):
    """
    Given the observations processed, it returns a dictionary:
        
        episode title (key) and number of downloads (value)

    Parameters
    ----------
    observations : list of dict
       Each item contains an observation with all registered fields.
       
    Returns
    -------
    episode_entries : a dictionary 
        episode title (key) and number of downloads (value).

    """
    episode_entries = {}
  
    #FIXME
    
    
  
    return episode_entries
 
def plot_programs(programs):
    """
    Given a dictionary of programs: program title (key) and number of downlaods (value),
    It plots a bar chart
        
    Parameters
    ----------
    programs : dict
        program title (key) and number of downlaods (value).

    Returns
    -------
    None.

    """
    if programs:
        dataframe = pd.DataFrame(programs, columns=["program","downloads"])
        ax = sns.barplot(x="program", y="downloads", data=dataframe)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        plt.show()
        
        
      
def list_top_programs(observations):
    """
     Given the observations processed, it returns a list of:
         (program title, number of downloads) sorted by the number of downloads.

    Parameters
    ----------
    observations : list of dict
       Each item contains an observation with all registered fields.

    Returns
    -------
    all_top_programs : list of tuples
         (program title, number of downloads).

    """
    all_top_programs = []
  
    #FIXME
  
    
    return all_top_programs
 
def list_top_k_programs(all_top_programs, k):
    """
    Given the result of the list_top_programs, it returns the first k elements.

    Parameters
    ----------
    all_top_programs : list of tuples 
        A sorted list of tuples: (program title, number of downloads).
    k : integer
        A non negative integer number.

    Returns
    -------
    top_k : list of tuples
         (program title, number of downloads).

    """
    top_k = []
 
    #FIXME
    
    return top_k    

def generate_stats(observations):
    """
    
    This method calculates the number of processed entries, observations, by
    the type of metric:
        
        Download 200
        Download 206
        Bad method
        Bad status
        Bad format resource
        Bot detected
        
        
    Parameters
    ----------
    observations : list of dict
       Each item contains an observation with all registered fields.

    Returns
    -------
    stats : dict
        metric (key) and number of observations (value).

    """
    stats = {}
  
    
    #FIXME
    
  
    
  
    return stats

def analyze_dataset(data_entries):
    """
    This method takes the input data, a dictionary of data items, and it applies
    some rules to process each entry:
        
        1-It validates that the entry is valid. If it is not valid, it 
        generates an error observation.
        
        2-It checks if the entry can generate a new download (200 or 206). If it is a new 
        download, it generates a new observation. 
        
        A new observation shall contain the same data as the input and:
            -Metric name: Download 200 or Download 206
            -Value: 1
        

    Parameters
    ----------
    data_entries : list of dict
        A list of dictionaries readed from the CSV file.

    Returns
    -------
    list
        A list of observations. Each observation can be a tuple, a dict or an object.

    """
    ongoing_observations = {}
    on_going_downloads_200 = {}
    on_going_downloads_206 = {}
    
    for entry in data_entries:
        if is_valid_request(entry):
            if entry["status"] == "200":
                observation = is_download(entry, on_going_downloads_200, MIN_BYTES_DOWNLOAD_200)
            elif entry["status"] == "206":
                observation = is_download(entry, on_going_downloads_206, MIN_BYTES_DOWNLOAD_206)
            else:
                observation = None
            
            #It uses an object for observations, if you use another 
            #datastructure, adapt the code
            if observation and observation.id not in ongoing_observations:
                ongoing_observations[observation.id] = observation
   
        else:
            invalid_message = generate_not_valid_request_message(entry)
            observation = create_error_observation(invalid_message, entry["uri_episode"])
            if observation:
                ongoing_observations[observation.id] = observation
  
    return list(ongoing_observations.values())

def load_dataset(filename="data.csv"):
    """
    Given a file of entries to process, it returns a list of dictionaries.
    
    Each item is a dictionary which can be accessed by the column name in 
    the CSV file.

    Parameters
    ----------
    filename : TYPE, optional
        DESCRIPTION. The default is "data.csv".

    Returns
    -------
    A list of entries.

    """
    data = []
    if filename and os.path.isfile(filename):
        csv_file = open(filename, encoding="utf-8") 
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)
        csv_file.close()
    return data

#Menu
def show_menu():
    option = -1
    valid_options = {str(i) for i in range(0,9)}
    while option not in valid_options:
        print("Podcast analyzer")
        print("-------------------")
        print("1-Load dataset.")
        print("2-Analyze dataset.")
        print("3-Generate processing stats report.")
        print("4-List top k of downloaded programs.")
        print("5-Plot top k programs.")
        print("6-Recommend an episode.")
        print("7-Save analysis.")
        print("0-Exit.")
        option = input("Introduce option: ")
        if option not in valid_options:
            print("Invalid option: "+option)
            print("Please introduce a number between 1-8...")
    return option
  
#Main program  

def show_not_analyzed():
    print("\nThe dataset has not been analyzed.\n")

if __name__=="__main__":
    loaded = False
    analyzed = False
    data_entries = []
    #To calculate when the dataset is analyzed.
    observations = []
    all_top_programs = []
    episode_set = set()
    option = "-1"
    while option != "0":
        option = show_menu()
        if option == "1":
            #Clean existing data
            observations.clear()
            all_top_programs.clear()
            episode_set.clear()
            data_entries = load_dataset()
            loaded = True
            analyzed = False
        elif option == "2":
            if loaded:
                observations = analyze_dataset(data_entries) 
                all_top_programs = list_top_programs(observations)
                episode_set = list_episodes(observations)
                data_entries.clear()
                analyzed = True
            else:
                print("\nThe dataset has not been loaded.\n")
        elif option == "3":
            if analyzed:
                stats = generate_stats(observations)
                show_stats(stats)
            else:
                show_not_analyzed()
        elif option == "4":
            if analyzed:
               k = get_number(0)
               top_k = list_top_k_programs(all_top_programs, k)
               show_top_k(top_k)
            else:
                show_not_analyzed()
        elif option == "5":
            if analyzed:
               k = get_number(0)
               top_k = list_top_k_programs(all_top_programs, k)
               plot_programs(top_k)
            else:
                show_not_analyzed()
        elif option == "6":
              if analyzed:
                user=input("Introduce the user id: ")
                recommendations = recommend(observations, episode_set, user) 
                show_recommendations(recommendations, user)
                recommendations.clear()
              else:
                show_not_analyzed()
        elif option == "7":
             if analyzed:
                save_observations_as_csv(observations)
             else:
                show_not_analyzed()
        elif option == "0":
            print("The program is going to finish.")
    