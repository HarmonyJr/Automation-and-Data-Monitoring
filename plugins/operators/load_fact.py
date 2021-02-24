from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):
    
    load_fact_table_insert = """
    INSERT INTO {} {}
    """
    load_fact_table_truncate = """
    TRUNCATE TABLE {}
    """
    
    @apply_defaults
    def __init__(self,
                 query="",
                 redshift_conn_id="",
                 destination_table="",
                 operation="",
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.query = query
        self.redshift_conn_id = redshift_conn_id
        self.destination_table = destination_table
        self.operation = operation

    def execute(self, context):
        self.log.info('LoadFactOperator not implemented yet')
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        if (self.operation == "append"):
            facts_sql = LoadFactOperator.load_fact_table_insert.format(self.destination_table, self.query)
            redshift.run(facts_sql)
            self.log.info(f'LoadFactOperator has inserted data into {self.destination_table} table')
        
        if (self.operation == "truncate"):
            facts_sql = LoadFactOperator.load_fact_table_truncate.format(self.destination_table)
            redshift.run(facts_sql)    
            self.log.info(f'LoadFactOperator has truncated data in {self.destination_table} table')

