import sqlite3

#Conectando o banco de dados,caso não exista, ele será criado
connection = sqlite3.connect('hospital.db')
cursor = connection.cursor()
commit = connection.commit()



#Criando as Tabelas
#connection.execute('CREATE TABLE IF NOT EXISTS paciente (id INTEGER PRIMARY KEY NOT NULL, nome VARCHAR(50), idade INTEGER,problema TEXT)')

#connection.execute('CREATE TABLE IF NOT EXISTS paciente (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)')

#connection.execute  ('CREATE TABLE IF NOT EXISTS funcionário (id_func PRIIMARY KEY INTEGER, nome TEXT, profissão TEXT, horario TEXT)')

#connection.execute('CREATE TABLE IF NOT EXISTS médico(id_med INTEGER PRIMARY KEY,nome TEXT,horario TEXT,area TEXT)')

#connection.execute('CREATE TABLE IF NOT EXISTS farmaceutica(id_f INTEGER PRIMARY KEY ,nome_f TEXT,responsável TEXT)')

#connection.execute('CREATE TABLE IF NOT EXISTS sala (número INTEGER PRIMARY KEY,setor TEXT)  '


#Inserindo dados na tabela
#cursor.execute (  '''INSERT INTO paciente (Id,Nome,Idade,Problema)VALUES(222,'Jonas alves santos',28,'Virose')''')"""

#cursor.execute('''
# INSERT INTO farmaceutica(id_f,nome_f,responsável) VALUES(1,'Johnson_e_Johnsons',#'Oswaldo junior')
#''')

#cursor.execute('''
#INSERT INTO médico (id_med,nome,horario,area)
 #VALUES (48,'Kleber Silva','Das 7h até 17h30','Cardiologista')              ''')

#cursor.execute('''
#INSERT INTO sala(número,setor,andar)
#VALUES(6,'Regulação e avaliação em saúde',1)
#''')

cursor.execute('''
INSERT INTO funcionário (id_func,nome,profissão,horario)
VALUES(77,'Lucia Mara De Oliveira','Enfermeira','Das 10h até as 19h45')
''')

connection.commit()

"""cursor.execute('''
INSERT INTO paciente(id,nome,idade,problema) VALUES(77,'Kevin Mendes',20,'Dor no joelho(provável água no joelho)')
''')"""


''''''

