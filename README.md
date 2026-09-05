 Data Trails

1a - The Data Vault
I loaded both the Titanic and student marks datasets using Pandas. I checked the basic information, statistics, missing values, and size of the datasets before making any changes.

1b - The Passenger Records
I used `loc` to find passengers who were above 60 years old. I also used `iloc` to get the first 5 rows and first 4 columns.

1c - The Corrupted File
I cleaned the student data by making the gender values consistent. I also changed the English marks into numbers and removed duplicate records.

1d - The Missing Pieces
I filled the missing student marks using the median of each subject. For the Titanic data, I filled missing ages using the median age for each passenger class.

1e - The Hidden Pattern
I grouped the Titanic passengers by class and calculated the average fare, average age, and survival rate for each class.

1f - The Port Connection
I created a small lookup table to convert the Titanic port codes into their full names and merged it with the main dataset.
