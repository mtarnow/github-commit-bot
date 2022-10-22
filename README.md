# github-commit-bot
This is Albert. Albert is a self-conscious bot tracking his commits and committing his updated knowledge.
The work he's doing is essential.

The whole program is intentionally contained in one file. It will keep growing indefinitely - that's by design.

The program depends on Python 3.10 or higher.
To recruit Albert and have him work for you too:
1. Create an empty GitHub repository.
2. Clone this repository.
3. Set remote to the url of your new empty repository ('cd github-commit-bot', 'git remote set-url origin [url]')
4. In src/main.py edit the commit_string variable to contain 2 sentences ending with a period and use double quotes
5. to enclose the string. You could provide a start date and the second sentence in such form, that it would make sense
   to extend it with '... and the next day I committed' - for example describing what Albert did yesterday.
   For example: "I started to work here on 22.10.2022. Yesterday I was at a farmers' market."
6. Set the n_commits variable to 0.

That's it. You can run the script with '[Python >=3.10 executable] [main.py file path]',
for example: 'python /home/maciej/github-commit-bot/src/main.py'. 
You can now schedule a task (Windows) or a cronjob (Linux) to run it periodically 
and invite Albert to work for you every day.
