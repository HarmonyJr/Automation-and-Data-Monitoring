# Sparkify Data project
A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.

They have decided to bring you into the project and expect you to create high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and allow easy backfills. They have also noted that the data quality plays a big part when analyses are executed on top the data warehouse and want to run tests against their datasets after the ETL steps have been executed to catch any discrepancies in the datasets.

The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to.


###### Project Files
data folder - The folder contains the song_data and log_data zip files. The song_data zip file contains the song_data JSON log files 
which contain information on the songs. The log_data zip file contains the user activity log files which contain information on the user activities. 

dl.cfg - This cponfig file contains AWS credentials

etl.py - This python script is used to load the whole datasets. It contains procedures for creating database connection, processing log files and closing the connection. 
