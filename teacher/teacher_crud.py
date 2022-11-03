""""""

from typing import Any

from db.database import Graph
from helper.write_a_json import write_a_json


class TeacherCRUD():
    """"""
    database = Graph(uri="bolt://44.201.64.103:7687", user="neo4j", password="hint-retrieval-coders")

    def create(self, name: str, ano_nasc: int, cpf: str) -> None:
        """
        Método para criar um professor no BD.
        """
        query = """
            CREATE(:Teacher
                {
                    name: $name,
                    ano_nasc: $ano_nasc,
                    cpf: $cpf
                }
            );
        """

        params = {
            "name": name,
            "ano_nasc": ano_nasc,
            "cpf": cpf
        }

        response = self.database.execute_query(query, params)
        write_a_json(response, 'CREATE')

    def read(self, name: str) -> Any:
        """
        Método para ler um professor do BD baseado em seu nome.
        """
        query = """
            MATCH(t:Teacher)
            WHERE
                t.name = $name
            RETURN t;
        """

        params = {
            "name": name
        }

        response = self.database.execute_query(query, params)
        write_a_json(response, 'READ')

    def update(self, name: str, newCpf: str) -> None:
        """
        Método para atualizar um professor do BD baseado em seu cpf.
        """
        query = """
            MATCH(t:Teacher)
            WHERE
                t.name = $name
            SET t.cpf = $newCpf
            RETURN t;
        """

        params = {
            "name": name,
            "newCpf": newCpf
        }

        response = self.database.execute_query(query, params)
        write_a_json(response, 'UPDATE')

    def delete(self, name: str) -> None:
        """
        Método para deletar um professor do BD baseado em seu nome.
        """
        query = """
            MATCH(t:Teacher)
            WHERE
                t.name = $name
            DELETE t;
        """

        params = {
            "name": name
        }

        response = self.database.execute_query(query, params)
        write_a_json(response, 'DELETE')
