#!/usr/bin/python
import requests
import datetime
import argparse


#ARGUMENTS PROCESSING
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description='''ABOUT PROGRAMM:
    %(prog)s collects and displays pull requests statistics from Github.
    It's possible to output all statistic parametres or separate parametres.
    It has 3 mandatory arguments:
        '-u' - Github username,
        '-r' - Github repository name,
        '-p' - pull request number.
    Also it has optional parameter '-o' - for parameters filtering.

    EXAMPLES:
        1) %(prog)s -u ivanovmsk -r python_programms -p 23 -o mcstat numdo daywo
        2) %(prog)s -u x_man -r myscripts -p all -o all -r python_programms -p 23 -o mcstat numdo daywo
        3) %(prog)s -u mygitacc -r xmlparser_project -p all
        ''')
parser.add_argument("-user", "-u", help="Github username. Required: yes", required=True)
parser.add_argument("-repo", "-r", help="Github repo. Required: yes", required=True)
parser.add_argument("-pullreqnum", "-p", help="Pull Request Number. {int} or {'all'}. Required: yes", required=True)
parser.add_argument('--version', '-v', action='version', version='%(prog)s Ver. 1.0 (17.03.2017). '
                                                                 'Created by Yahor Skrabkou')
parser.add_argument("-o", nargs='*', help='''List of available options:
    all - Show all statistics (default value).
    mcstat - Basic statistics about merged/closed rate.
    numdo - Number of days opened
    numcc - Number of comments created.
    daywo - Day of the week opened.
    daywc - Day of the week close
    hourdo - Hour of the day opened.
    hourdc - Hour of the day closed.
    weeko - Week opened.
    weekc - Week closed.
    usero - User who opened.
    userc - User who closed.
    labels - Attached labels.
    numla - Number of lines added.
    numld - Number of lines deleted.
    pullreqafter - Option to consider only pull requests opened on or after this date.
    pullreqbefore - Only consider pull requests opened before this date.''',
 choices=['all', 'mcstat', 'numdo', 'numcc', 'daywo', 'daywc', 'hourdo', 'hourdc', 'weeko', 'weekc', 'labels', 'numla',
          'numld', 'pullreqafter', 'pullreqbefore'])

prs = parser.parse_args()
username = prs.user

options = prs.o
if (options is None) or ('all' in options):
    options = ['mcstat', 'numdo', 'numcc', 'daywo', 'daywc', 'hourdo', 'hourdc', 'weeko', 'weekc', 'usero', 'userc',
     'labels', 'numla', 'numld', 'pullreqafter', 'pullreqbefore', 'additional']


reponame = prs.repo
pullreqnum = prs.pullreqnum

contributors_url = 'https://api.github.com/repos/{}/{}/pulls?state=all'.format(username, reponame)
mycreds = ('egskr', '556b528b9b841a36caa893d300938fd79')
request = requests.get(contributors_url, auth=mycreds).json()


#HEADER WRITING
def write_header():
    print("=" * 90)
    print("                P U L L   R E Q U E S T S   S  T  A  T  I  S  T  I  C  S        ")
    print("=" * 90)


class Checking(object):
    """This class executes different types of checks"""
    def __init__(self, request):
        self.request = request

    def entered_data_checking(self):
        if type(request) is dict:
            print("Wrong Github user name or repo name. Try again")
            exit()

    def pullsListDefinition(self):
        pullsList = []
        for i in range(len(request)):
            pullsList.append(request[i]['number'])
        return pullsList

    def entered_pullreqnum_checking(self, pullreqnum):
        if int(pullreqnum) not in pullsList:
            print("Pull request #{} doesn't exist. Available requests: {} Try again".format(pullreqnum, pullsList))
            exit()


class Auxiliary(object):
    """This class helpes to process different queries and operations"""
    def __init__(self, request):
        self.request = request
    def merged_closed_rate(self):
        mergedCount = 0
        closedCount = 0
        for i in range(len(request)):
            if request[i]["state"] == "closed":
                closedCount += 1
            if request[i]["merged_at"] != None:
                mergedCount += 1
        return "Merged/Closed rate: merged: {} / closed: {}".format(mergedCount, closedCount)

    def date_to_day_quantity(self, date_string):
        date_string = (date_string.split('T')[0]).split("-")
        old_date = datetime.date(int(date_string[0]), int(date_string[1]), int(date_string[2]))
        today_date = datetime.date.today()
        if old_date != today_date:
            return (str(today_date - old_date)).split()[0]
        else:
            return 0

    def comments_counter(self, whichRequest):
        if whichRequest == 'all':
            commentlink = 'https://api.github.com/repos/{}/{}/issues/comments'.format(username, reponame)
            commentrequest = requests.get(commentlink, auth=mycreds).json()
        else:
            commentlink = 'https://api.github.com/repos/{}/{}/issues/{}/comments'.format(username, reponame, whichRequest)
            commentrequest = requests.get(commentlink, auth=mycreds).json()

        return (len(commentrequest))

    def get_day_of_week(self, datastring):
        if datastring is not None:
            mydat = datastring.split("T")[0]
            year, month, day = (int(x) for x in mydat.split('-'))
            ans = datetime.date(year, month, day)
            return ans.strftime("%A")
        else:
            return "Not closed"

    def get_week_of_year(self, datastring):
        if datastring is not None:
            mydat = datastring.split("T")[0]
            year, month, day = (int(x) for x in mydat.split('-'))
            return datetime.date(year, month, day).isocalendar()[1]
        else:
            return "Not closed"

    def who_closed(self, whichRequest):
            issueslink = 'https://api.github.com/repos/{}/{}/issues/{}/events'.format(username, reponame,
                                                                                         whichRequest)
            issuesrequest = requests.get(issueslink, auth=mycreds).json()
            return issuesrequest[0]['actor']['login']

    def get_labels(self, whichRequest):
            issueslink = 'https://api.github.com/repos/{}/{}/issues/{}/events'.format(username, reponame,
                                                                                          whichRequest)
            issuesrequest = requests.get(issueslink, auth=mycreds).json()
            for i in range(len(issuesrequest)):
                if issuesrequest[i]['event'] == 'labeled':
                    return issuesrequest[0]['label']['name']
                return "No labels"

    def get_num_added_deleted_lines(self, whichRequest, add_or_del):
        issueslink = 'https://api.github.com/repos/{}/{}/pulls/{}'.format(username, reponame, whichRequest)
        issuesrequest = requests.get(issueslink, auth=mycreds).json()
        if add_or_del == "add":
            return issuesrequest['additions']
        else:
            return issuesrequest['deletions']


class Output(Auxiliary):
    """This class is responsible for output of information"""
    def __init__(self, request):
        self.request = request
        write_header()
        print("Analized account: {}".format(username))
        print("Analized repostiry: {}".format(reponame))
        print("Number of pullrequests: {}".format(len(pullsList)))
        options_a = "all" if len(options) is 17 else options
        print("Options: {}".format(options_a))
        print("=" * 40)
        self.aux = Auxiliary(request)
        print("Number of comments created (for all requests): {}".format(self.aux.comments_counter('all')))

    def optionsToOutputDefining_common(self):
        if 'mcstat' in options:
            print(self.aux.merged_closed_rate())

    def optionsToOutputDefining(self, requestInArray, currReqVal):
        if (len(options) != 1) and ('mcstat' in options):
            print("\n*****Pull request #{}*****".format(currReqVal))
        if 'additional' in options:
            print("Pull request Title: {}".format(request[int(requestInArray)]["title"]))
            print("Request initiator: {}".format(request[int(requestInArray)]["user"]["login"]))
            print("State: {}".format(request[int(requestInArray)]["state"]))
            print("When was created: {}".format(request[int(requestInArray)]["created_at"]))
        if 'numdo' in options:
            print("Number of days opened: {}".format(self.aux.date_to_day_quantity(request[requestInArray]["created_at"])))
        if 'numcc' in options:
            print("Number of comments created (for this request): {}".format(self.aux.comments_counter(currReqVal)))
        if 'daywo' in options:
            print("Day of the week opened: {}".format(self.aux.get_day_of_week(request[requestInArray]["created_at"])))
        if 'hourdo' in options:
            print("Hour of day opened: {}".format(((request[requestInArray]["created_at"]).split("T")[1])[:-4]))
        if 'weeko' in options:
            print("Week opened: {}".format(self.aux.get_week_of_year(request[requestInArray]["created_at"])))
        if 'usero' in options:
            print("User who opened: {}".format(request[requestInArray]["user"]["login"]))
        if 'daywc' in options:
            print("Day of the week closed: {}".format(
                    self.aux.get_day_of_week(request[requestInArray]["closed_at"])))
        if 'weeko' in options:
            print("Week closed: {}".format(
                    self.aux.get_week_of_year(request[requestInArray]["closed_at"])))
        if 'hourdc' in options:
            if (request[requestInArray]["closed_at"]) is not None:
                print("Hour of day closed: {}".format(((request[requestInArray]["created_at"]).split("T")[1])[:-4]))
            else:
                print("Hour of day closed: Not closed")
        if 'userc' in options:
            if (request[requestInArray]["closed_at"]) is not None:
                print("User who closed: {}".format(self.aux.who_closed(currReqVal)))
            else:
                print("User who closed: Not closed")
        if 'labels' in options:
                print("Attached labels: {}".format(self.aux.get_labels(currReqVal)))
        if 'numla' in options:
                print("Number of lines added: {}".format(self.aux.get_num_added_deleted_lines(currReqVal, 'add')))
        if 'numld' in options:
                print("Number of lines deleted: {}".format(self.aux.get_num_added_deleted_lines(currReqVal, 'del')))



# CHECKS
globalcheck = Checking(request)

globalcheck.entered_data_checking()  # Checking for github name and repo is correct
pullsList = globalcheck.pullsListDefinition()

if pullreqnum != 'all':
    globalcheck.entered_pullreqnum_checking(pullreqnum)  # Checking for entered pull request number exists



# OUTPUT INFO
outInfo = Output(request)

outInfo.optionsToOutputDefining_common()

requestsToProcessingDict = {}

for i in range(len(request)):
    requestsToProcessingDict.update({request[i]['number']: i})

whichRequests = []
if pullreqnum == 'all':
    whichRequests = pullsList
else:
    whichRequests.append(pullreqnum)


for i in whichRequests:
    outInfo.optionsToOutputDefining(requestsToProcessingDict[int(i)], i)

# OUTPUT STATISTICS OF OPENED ON OR AFTER THIS DATE 
print("=" * 30)
not_today_req = []
today_req = []
for i in whichRequests:
    date_string = request[requestsToProcessingDict[int(i)]]['created_at'].split('T')[0].split('-')
    old_date = datetime.date(int(date_string[0]), int(date_string[1]), int(date_string[2]))
    today_date = datetime.date.today()
    if old_date != today_date:
        not_today_req.append(request[requestsToProcessingDict[int(i)]]['number'])
    else:
        today_req.append(request[requestsToProcessingDict[int(i)]]['number'])

print("\nPull requests opened today: ")
for i in today_req:
    print("Pull request: #{}".format(i))

print("\nPull requests opened before today: ")
for i in not_today_req:
    print("Pull request: #{}".format(i))

print("=" * 90)