# from pprintpp import pprint as pp
from db.database import Graph
from helper.write_a_json import write_a_json

from teacher.teacher_crud import TeacherCRUD

db = Graph(uri="bolt://44.201.64.103:7687", user="neo4j", password="hint-retrieval-coders")


# CREATING THE DATABASE
db.create_db()


# Questão 01
# A
query = """
    MATCH(t:Teacher)
    WHERE
        t.name = "Renzo"
    RETURN
        t.ano_nasc, t.cpf;
"""

response = db.execute_query(query)
write_a_json(response, "1A")


# B
query = """
    MATCH(t:Teacher)
    WHERE
        t.name STARTS WITH "M"
    RETURN
        t.name, t.cpf;
"""

response = db.execute_query(query)
write_a_json(response, "1B")


# C
query = """
    MATCH(c:City)
    RETURN
        c.name;
"""

response = db.execute_query(query)
write_a_json(response, "1C")

# D
query = """
    MATCH(s:School)
    WHERE
        s.number >= 150 AND s.number <= 550
    RETURN
        s.name, s.address, s.number;
"""

response = db.execute_query(query)
write_a_json(response, "1D")

# Questão 02
# A
query = """
    MATCH(t:Teacher)
    RETURN
        MIN(t.ano_nasc), MAX(t.ano_nasc);
"""

response = db.execute_query(query)
write_a_json(response, "2A")

# B
query = """
    MATCH(c:City)
    RETURN
        AVG(c.population);
"""

response = db.execute_query(query)
write_a_json(response, "2B")

# C
query = """
    MATCH(c:City)
    WHERE
        c.cep = "37540-000"
    RETURN
        REPLACE(c.name, "a", "A");
"""

response = db.execute_query(query)
write_a_json(response, "2C")

# D
query = """
    MATCH(t:Teacher)
    RETURN
        SUBSTRING(t.name, 2, 1);
"""

response = db.execute_query(query)
write_a_json(response, "2D")

# Questão 03

# A
teacher_crud = TeacherCRUD()


# B
name = 'Chris Lima'
ano_nasc = 1956
cpf = '189.052.396-66'

teacher_crud.create(name, ano_nasc, cpf)


# C
name = "Chris Lima"

response = teacher_crud.read(name)


# D
name = "Chris Lima"
cpf = "162.052.777-77"

teacher_crud.update(name, cpf)


# CLOSING CONNECTION
db.close()
