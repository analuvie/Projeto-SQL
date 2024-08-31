import sqlite3
conexao = sqlite3.connect(r'C:\Users\luisa\OneDrive\Área de Trabalho\SQLATV\ATVSQL')
cursor = conexao.cursor()

#Criar tabela alunos
#cursor.execute("CREATE TABLE alunos(id INT, nome VARCHAR(100), idade VARCHAR(2), curso VARCHAR(15));")

#Criar cinco alunos par a tabela
#cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES(1,'cintia', '18', 'farmácia');")
#cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES(2,'felipe', '24', 'engenharia');")
#cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES(3,'sarah', '20', 'psicologia');")
#cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES(4,'paula', '29', 'engenharia');")
#cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES(5,'caio', '29', 'medicina');")
#cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES(6,'jade', '23', 'enfermagem');")

#Consultas básicas
#selecionar todos os registros da tabela alunos
#cursor.execute('SELECT * FROM alunos')

# Selecionar o nome e a idade dos alunos com mais de 20 anos
#cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
#dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
#for alunos in dados:
#    print(alunos)

#Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

#cursor.execute("SELECT * FROM alunos WHERE curso='engenharia'ORDER BY nome")
#dados = cursor.execute("SELECT * FROM alunos WHERE curso='engenharia'ORDER BY nome")
#for alunos in dados:
#    print(alunos)

# Conte o valor total de alunos que tem na tabela
#cursor.execute("SELECT COUNT(*) FROM alunos")
#dados = cursor.execute("SELECT COUNT(*) FROM alunos")
#for alunos in dados:
#    print(alunos)

#Atualize o nome de um aluno da tabela
#cursor.execute('UPDATE alunos SET idade="28" where id="2"')

# Remova um aluno pelo seu ID
#cursor.execute('DELETE FROM alunos where id=1')

# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto),
# idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela

#cursor.execute('CREATE TABLE clientes(id INTEGER PRIMARY KEY, nome VARCHAR(100), saldo FLOAT(7))')
#cursor.execute('ALTER TABLE clientes ADD COLUMN idade INT(3)')
#cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, 'ana', '18', '100')")
#cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, 'luisa', '24', '370.6')")
#cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, 'felipe', '22', '90')")
#cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, 'josé', '38', '1320.8')")
#cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(5, 'dorian', '36', '870')")
#cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(6, 'rodrigo', '30', '50')")

# Selecione o nome e a idade dos clientes com idade superior a 30 anos.
#mostrar = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
#for clientes in mostrar:
#    print(clientes)

# Calcule o saldo médio dos clientes.
#cursor.execute('SELECT AVG(saldo) FROM clientes')
#media = cursor.fetchone()
#print(media)

# Encontre o cliente com o saldo máximo.
#cursor.execute('SELECT nome, saldo FROM clientes ORDER BY saldo DESC LIMIT 1')
#saldomax = cursor.fetchone()
#print(saldomax)

# Conte quantos clientes têm saldo acima de 1000.
#cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
#maisde1000 = cursor.fetchone()
#print(maisde1000)

# 7 a) Atualize o saldo de um cliente específico.
#cursor.execute('UPDATE clientes SET saldo="1200" WHERE saldo=50')

#b) Remova um cliente pelo seu ID.
#cursor.execute('DELETE FROM clientes WHERE id=1')

#8 Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id
#da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes".
#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

 
# Criando uma tabela chamada compras com os campos id, cliente_id, produto e valor
#cursor.execute('CREATE TABLE compras(id INTEGER PRIMARY KEY AUTOINCREMENT, clientes_id INTEGER, produto VARCHAR(30), valor REAL, FOREIGN KEY (clientes_id) REFERENCES clientes(id))')

# Inserindo compras associadas a clientes
#cursor.execute("INSERT INTO compras (clientes_id, produto, valor) VALUES (3, 'fogão', 2500.00)")
#cursor.execute("INSERT INTO compras (clientes_id, produto, valor) VALUES (4, 'geladeira', 1500.00)")
#cursor.execute("INSERT INTO compras (clientes_id, produto, valor) VALUES (5, 'air fryer', 250.00)")
#cursor.execute("INSERT INTO compras (clientes_id, produto, valor) VALUES (3, 'liquidificador', 200.00)")

#Selecionando os clientes, compras e o produto
#cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM compras JOIN clientes ON compras.clientes_id = clientes.id')
#compras = cursor.fetchall()
#for compra in compras:
#    print(f"Cliente: {compra[0]}, Produto: {compra[1]}, Valor: R${compra[2]:.2f}")









conexao.commit()  # Certifique-se de salvar as alterações no banco de dados







# Para enviar as informações
conexao.commit()

# Importante para não dar conflito no sistema gerenciador do computador
conexao.close()