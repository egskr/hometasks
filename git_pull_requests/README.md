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
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>-o</i> List of available options:<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; all - Show all statistics (default value).<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; mcstat - Basic statistics about merged/closed rate.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;numdo - Number of days opened.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;numcc - Number of comments created.<br>
                            daywo - Day of the week opened.<br>
                            daywc - Day of the week close.<br>
                            hourdo - Hour of the day opened.<br>
                            hourdc - Hour of the day closed.<br>
                            weeko - Week opened.<br>
                            weekc - Week closed.<br>
                            usero - User who opened.<br>
                            userc - User who closed.<br>
                            labels - Attached labels.<br>
                            numla - Number of lines added.<br>
                            numld - Number of lines deleted.<br>
                            pullreqafter - Option to consider only pull requests opened on or after this date.<br>
                            pullreqbefore - Only consider pull requests opened before this date.<br>
                            
          EXAMPLES:
        1) pull_req_stat.py -u ivanovmsk -r python_programms -p 23 -o mcstat numdo daywo
        2) pull_req_stat.py -u x_man -r myscripts -p all -o all -r python_programms -p 23 -o mcstat numdo daywo
        3) pull_req_stat.py -u mygitacc -r xmlparser_project -p all
       
