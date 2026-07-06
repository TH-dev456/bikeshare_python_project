#### Date created: 02-July-2026

# Bikeshare Python Project

## Description

In this project, use `bikeshare.py` to explore three bikeshare datasets for three US cities: Washington, DC, Chicago, and New York City.

The script follows a prompt-based experience...

### Script Overview:

1. Filter the datasets based on three filters: city, month, and day. The datasets contain entries from January to June of 2017.

2. View the raw data which includes 6 columns:
	- `Start Time`
	- `End Time`
	- `Trip Duration`
	- `Start Station`
	- `End Station`
	- `User Type`
	- `Gender`
	- `Birth Year`

	The last two are available for Chicago and New York City.

3. Answer yes/no questions to view statistics for popular travel times, popular stations, average and total trip durations, and user statistics.

4. Restart or terminate the script.

## Files Used

The project uses the following `.csv` files, provided by Udacity:

- washington.csv
- chicago.csv
- new_york_city.csv

## Credits

1. `chunker()` was taken from the course.

2. Microsoft co-pilot free desktop version was used to refine the for loop in `raw_data()` and the while loop in `user_input()`.

3. The for loop in user_stats():
https://stackoverflow.com/questions/36973387/accessing-first-column-of-pandas-value-counts

4. Display time in `Year Month Day hour minute second` format:
https://realpython.com/ref/builtin-functions/divmod/