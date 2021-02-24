# Sparkify Data project
A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.

They have decided to bring you into the project and expect you to create high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and allow easy backfills. They have also noted that the data quality plays a big part when analyses are executed on top the data warehouse and want to run tests against their datasets after the ETL steps have been executed to catch any discrepancies in the datasets.

The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to. 

Provided below are the s3 links for the two datasets that were utilized in this project.
Log data: s3://udacity-dend/log_data
Song data: s3://udacity-dend/song_data

###### Project Files
dag - The folder contain the dag python task and sql script that will be executed for creating and loading data into the tables. 
plugins - This file contains two sub folders: operators folders that contains the custom operator class that will be instantiated from the dag task to load the data into the tables and the help folder that contains the helper class for SQL transformations. 

###### Steps To Read and Load Data 
1. Spin up a Redhsift cluster
2. Open Airflow UI
3. Click on the Admin tab and Choose Connections
4. On the crete connection page, enter the following values:
   (Conn Id: Enter 'aws_credentials'.
    Conn Type: Enter 'Amazon Web Services'.
    Login: Enter you Access Key ID from your IAM User credentials.
    Password: Enter yor Secret access key from your IAM User credential.)
5. Once the values have been entered, Select Save and Add Another
6. On the next create connection page, enter the following values:
   (Conn Id: Enter 'redshift'.
    Conn Type: Enter 'Postgres'.
    Host: Enter the endpoint of your Redshift cluster.
    Schema: Enter the Redshift database name you are connecting to when launching Redshift cluster.
    Login: Enter the username that you created when launching Redshift cluster
    Password: Enter the password that you created when launching Redshift cluster
    Port: Enter the port number)
6. Click Save button once these values has been entered on the create connection page. 
7. Once all the values saved, Airflow is set to be run wth Redshift
8. 



