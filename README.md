# MLBFantasyPredictor
pulls data from espn website and uses this data to rank players based on how impactful they are in a roto fantasy baseball league
to use this file.
download the Hitter_MLB.py file and navigate to where the file downloaded in terminal
type in the command "vim Hitter_MLB.py" change the last line's path to wherever you want to store the csv file that
  will be downloaded to your machine -- to change the line, you must type "i" first to start inputting
    after this, type "escape", ":wq" to write and quit vim
Now, you are back in the terminal and need to run the program,
  "pip install requests beautifulsoup4 pandas", enter
    "python3 Hitter_MLB.py", enter
this should create a csv file on your desktop with the data from the 2021 mlb season.
