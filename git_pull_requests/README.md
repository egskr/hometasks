# Hometasks for Python Devops 2017

<H2>Github pull requests statistics collector</H2>

<h3>ABOUT PROGRAM:</h3>
    pull_req_stat.py collects and displays pull requests statistics from Github.<br>
    It's possible to output all statistic parametres or separate parametres.<br><br>
    <b>It has 3 mandatory arguments:</b><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'<i>-u'</i> - Github username,<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'<i>-r'</i> - Github repository name,<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'<i>-p'</i> - pull request number.<br>
    Also it has optional parameter '<i>-o'</i> - for parameters filtering.  
        

<br><b>Optional arguments:</b><br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>-h</i>, --help            show this help message and exit<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>-user</i> USER, <i>-u</i> USER   Github username. Required: yes<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>-repo</i> REPO, <i>-r</i> REPO   Github repo. Required: yes<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>-pullreqnum</i> PULLREQNUM, <i>-p</i> PULLREQNUM  Pull Request Number. {int} or {'all'}. Required: yes<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>--version</i>, <i>-v</i>     show program's version number and exit<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>-o</i> [{all,mcstat,numdo,numcc,daywo,daywc,hourdo,hourdc,weeko,weekc,labels,numla,numld,pullreqafter,pullreqbefore} [{all,mcstat,numdo,numcc,daywo,daywc,hourdo,hourdc,weeko,weekc,labels,numla,numld,pullreqafter,pullreqbefore} ...]]
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
       
