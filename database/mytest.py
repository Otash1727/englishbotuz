import mysql.connector as sq
from config import host,database1,user1,passwd




def sql_test():
    global base_test,cur_test
    base_test=sq.connect(host=host,password=passwd,user=user1,database=database1)
    cur_test=base_test.cursor()
    if base_test:
        print(' Link +')
        cur_test.execute("CREATE TABLE  IF NOT EXISTS test_url(test_kuni VARCHAR(255),test_vaqti VARCHAR(255),link VARCHAR(255))")
        base_test.commit()
        cur_test.execute("INSERT INTO test_url(test_kuni,test_vaqti,link) VALUES(NULL,NULL,NULL)")
        base_test.commit()
''' royhat oldindan tuzib qoyilgan boladi '''

async def test_add_command(state,message):
    async with state.proxy() as file_test:
            cur_test.execute("UPDATE test_url SET link=%s WHERE test_kuni=%s AND test_vaqti=%s",(message.text,file_test['test_day'],file_test['test_time'],))
            base_test.commit()
            
async def select_data(state,message):
    async with state.proxy() as file_test:
        polo6=('SELECT test_kuni,test_kuni FROM test_url WHERE test_kuni=? AND test_vaqti=?',(file_test['test_day'],file_test['test_time'],))
        cur_test.execute(polo6)
        polo7=cur_test.fetchall()
        return polo7

async def into_data(state,message,jk1):
    async with state.proxy()as file_test:
        cur_test.execute('INSERT INTO test_url(test_kuni,test_vaqti,link) VALUES(%s,%s,%s)',(file_test['test_day'],file_test['test_time'],jk1,))
        base_test.commit()

            
