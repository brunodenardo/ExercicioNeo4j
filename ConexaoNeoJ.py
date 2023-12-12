from neo4j import GraphDatabase

class ConexaoNeoJ:


    URI = "neo4j+ssc://8f5424ac.databases.neo4j.io"
    AUTH = ("neo4j", "qtVtF8fEmCuFLlav61gkd20Ao6Dbv2_Xtx9FlLlsu-0")

    def conectar(self):
        driver = GraphDatabase.driver(self.URI, auth= self.AUTH)
        return driver



