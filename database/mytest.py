import sqlite3 as sq




def sql_test():
    global base_test,cur_test
    base_test=sq.connect('test_url.db')
    cur_test=base_test.cursor()
    if base_test:
        print(' Link +')
        base_test.execute("CREATE TABLE  IF NOT EXISTS test_url(test_kuni TEXT,test_vaqti,link )")
        base_test.commit()
        # cur_test.execute("INSERT INTO test_url(test_kuni,test_vaqti,link) VALUES(NULL,NULL,NULL)")
        # base_test.commit()
''' royhat oldindan tuzib qoyilgan boladi '''

async def test_add_command(state,message):
    async with state.proxy() as file_test:
            cur_test.execute("UPDATE test_url SET link=? WHERE test_kuni=? AND test_vaqti=?",(message.text,file_test['test_day'],file_test['test_time'],))
            base_test.commit()
            
async def select_data(state,message):
    async with state.proxy() as file_test:
        return cur_test.execute('SELECT test_kuni,test_kuni FROM test_url WHERE test_kuni=? AND test_vaqti=?',(file_test['test_day'],file_test['test_time'],)).fetchall()

async def into_data(state,message,jk1):
    async with state.proxy()as file_test:
        cur_test.execute('INSERT INTO test_url(test_kuni,test_vaqti,link) VALUES(?,?,?)',(file_test['test_day'],file_test['test_time'],jk1,))
        base_test.commit()

            
