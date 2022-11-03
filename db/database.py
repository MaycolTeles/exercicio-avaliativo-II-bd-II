from neo4j import GraphDatabase


class Graph:
    def __init__(self, uri: str, user: str, password: str):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_db(self) -> None:
        """"""
        with open('db/queries.cypher') as queries_file:
            queries = queries_file.read().strip().split('\n')

        for query in queries:
            if query:
                # print(f"QUERY {idx}: {query}")
                self.execute_query(query)

    def execute_query(self, query, parameters=None):
        data = []
        with self.driver.session() as session:
            results = session.run(query, parameters)
            for record in results:
                data.append(record)
            return data
