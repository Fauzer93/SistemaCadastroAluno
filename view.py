# importando SQLIte
import sqlite3 as lite

#criando conexão
try:
    con = lite.connect('cadastro_alunos.db')
    print('Conexão com o banco de dados realizado com sucesso!')
except lite.Error as e:
    print("Erro ao conectar com o banco de dados:", e)
    
    
# Tabela de cursos ================================================================================

# Criar cursos (Create C )
def criar_curso(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO  Cursos (nome, duracao, preco) VALUES (?,?,?)"
        cur.execute(query,i)
        
# criar_curso(['Python','Semanas', 50])

# Ver todos os cursos (Read R)
def ver_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Cursos')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista



# Atualizar os cursos (Update U )
def atualizar_curso(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Cursos SET nome=?, duracao=?, preco=? WHERE id=?"
        cur.execute(query,i)


# Deletar os cursos (Delete D )
def deletar_curso(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Cursos WHERE id=?"
        cur.execute(query,i)
        


# Tabela de Turmas ================================================================================

# Criar Turmas ( Create C)
def criar_turmas(i):
    with con:
        cur =  con.cursor()
        query =  "INSERT INTO Turmas (nome, curso_nome,data_inicio) VALUES (?, ?, ?)"
        cur.execute(query, i)


# Ver todos os turmas ( Read R)        
def ver_turmas():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM turmas')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista


# Atualizar os Turmas ( Update U )
def atualizar_turmas(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Turmas SET nome=?, curso_nome=?, data_inicio=? WHERE id=?"
        cur.execute(query,i)
        
        
# Deletar os turma ( Delete D )
def deletar_turma(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Turmas WHERE id=?"
        cur.execute(query,i)
        
# Tabela Alunos ================================================================================

# Criar Alunos ( Create C)
def criar_alunos(i):
    with con:
        cur =  con.cursor()
        query =  "INSERT INTO Alunos (nome, email, telefone, sexo, imagem, data_nascimento, cpf, turma_nome) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)
        
        
# Ver Alunos ( Read R)        
def ver_alunos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Alunos')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista



# Atualizar Alunos ( Update U )
def atualizar_alunos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE alunos SET nome=?, email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, cpf=?, turma_nome=? WHERE id=?"
        cur.execute(query,i)
        
# Deletar Alunos ( Delete D )
def deletar_alunos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM alunos WHERE id=?"
        cur.execute(query,i)