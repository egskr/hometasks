# Hometasks for Python Devops 2017

<H2>Github pull requests statistics collector</H2>

<h3>ABOUT PROGRAM:</h3>
    pull_req_stat.py collects and displays pull requests statistics from Github.<br>
    It's possible to output all statistic parametres or separate parametres.<br><br>
    <b>It has 3 mandatory arguments:</b><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'-u' - Github username,<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'-r' - Github repository name,<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'-p' - pull request number.<br>
    Also it has optional parameter '-o' - for parameters filtering.  
        

<br><b>Optional arguments:</b><br>
  -h, --help            show this help message and exit
  -user USER, -u USER   Github username. Required: yes
  -repo REPO, -r REPO   Github repo. Required: yes
  -pullreqnum PULLREQNUM, -p PULLREQNUM
                        Pull Request Number. {int} or {'all'}. Required: yes
  --version, -v         show program's version number and exit
  -o [{all,mcstat,numdo,numcc,daywo,daywc,hourdo,hourdc,weeko,weekc,labels,numla,numld,pullreqafter,pullreqbefore} [{all,mcstat,numdo,numcc,daywo,daywc,hourdo,hourdc,weeko,weekc,labels,numla,numld,pullreqafter,pullreqbefore} ...]]
                        List of available options:
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
                            pullreqbefore - Only consider pull requests opened before this date.
                            
          EXAMPLES:
        1) pull_req_stat.py -u ivanovmsk -r python_programms -p 23 -o mcstat numdo daywo
        2) pull_req_stat.py -u x_man -r myscripts -p all -o all -r python_programms -p 23 -o mcstat numdo daywo
        3) pull_req_stat.py -u mygitacc -r xmlparser_project -p all
       
