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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>mcstat</i> - Basic statistics about merged/closed rate.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>numdo</i> - Number of days opened.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>numcc</i> - Number of comments created.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>daywo</i> - Day of the week opened.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>daywc</i> - Day of the week close.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>hourdo</i> - Hour of the day opened.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>hourdc</i> - Hour of the day closed.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>weeko</i> - Week opened.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>weekc</i> - Week closed.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>usero</i> - User who opened.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>userc</i> - User who closed.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>labels</i> - Attached labels.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>numla</i> - Number of lines added.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>numld</i> - Number of lines deleted.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>pullreqafter</i> - Option to consider only pull requests opened on or after this date.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>pullreqbefore</i> - Only consider pull requests opened before this date.<br>
                            
          EXAMPLES:
        1) pull_req_stat.py -u ivanovmsk -r python_programms -p 23 -o mcstat numdo daywo
        2) pull_req_stat.py -u x_man -r myscripts -p all -o all -r python_programms -p 23 -o mcstat numdo daywo
        3) pull_req_stat.py -u mygitacc -r xmlparser_project -p all
       
