from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E' 
    load_dimension_table_insert = """
    INSERT INTO {} {}
    """
    load_dimension_table_truncate = """
    TRUNCATE TABLE {}
    """
    
    @apply_defaults
    def __init__(self,
                 query="",
                 redshift_conn_id="",
                 destination_table="",
                 operation="",
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.query = query
        self.redshift_conn_id = redshift_conn_id
        self.destination_table = destination_table
        self.operation = operation

    def execute(self, context):
        self.log.info('LoadDimensionOperator not implemented yet')
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        if (self.operation == "append"):
            dimension_sql = LoadDimensionOperator.load_dimension_table_insert.format(self.destination_table, self.query)
            redshift.run(dimension_sql)
            self.log.info(f'LoadDimensionOperator has inserted data into {self.destination_table} table')
        
        if (self.operation == "truncate"):
            dimension_sql = LoadDimensionOperator.load_dimension_table_truncate.format(self.destination_table)
            redshift.run(dimension_sql)    
            self.log.info(f'LoadDimensionOperator has truncated data in {self.destination_table} table')
        