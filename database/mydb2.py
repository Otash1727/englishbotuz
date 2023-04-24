import sqlite3 as sq
from  create_bot import bot
import re


base2=sq.connect('new_list.db')
cur2=base2.cursor()


def sql_start2():
    global base2,cur2 
    base2=sq.connect("new_list.db")
    cur2=base2.cursor()
    if base2:
        print('Data base2 extra connected OK!')
    base2.execute('CREATE TABLE IF NOT EXISTS new_list(dars_kuni TEXT, dars_vaqti , ism_familiya TEXT)')
    base2.commit()


async def sql_add_command2(state,message):    
    async with state.proxy() as neww:
        cur2.execute('INSERT INTO new_list VALUES(?,?,?)',tuple(neww.values()))
        base2.commit()


async def sql_readnew(callback,state):
    async with state.proxy() as neww:                 
        new2=[]
        for schedule  in cur2.execute('SELECT ism_familiya FROM new_list WHERE dars_kuni=? AND dars_vaqti=?',(neww['new_day'],neww['new_time'],)).fetchall():
            new2.append(schedule)
       
        if new2!=[]:
            for new3 in cur2.execute('SELECT ism_familiya FROM new_list WHERE dars_kuni=? AND dars_vaqti=?',(neww['new_day'],neww['new_time'],)).fetchall():
                await callback.message.answer(re.sub("[(),'']",'',str(f"{new3} ")))       
        else: 
            await callback.message.answer('The data of this group hasn’t been found')



async def sql_delete_command2(data):
    cur2.execute('DELETE FROM new_list WHERE ism_familiya= ? ',(data,))
    base2.commit()
    
