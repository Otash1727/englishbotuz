import mysql.connector as sq
from  create_bot import bot
from keyboards import keyboard_reply 
from keyboards.keyboard_reply import account_markup,contact_markup
from database import myusers 
from database.myusers import copy_users
from keyboards import admin_inline
from keyboards.admin_inline import delete_kb
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
import re
from config import host,passwd,user1,database1





def sql_start():
    global base_admin,cur_admin 
    base_admin=sq.connect(host=host,password=passwd,user=user1,database=database1)
    cur_admin=base_admin.cursor()
    if base_admin:
        print('Data base_admin connected OK!')
    cur_admin.execute('CREATE TABLE IF NOT EXISTS list_group(dars_kuni VARCHAR(255), dars_vaqti VARCHAR(255) , ism_familiya VARCHAR(255))')
    base_admin.commit()
    


async def sql_add_command(state,message):    
    async with state.proxy() as data:
        cur_admin.execute('INSERT INTO list_group VALUES(%s,%s,%s)',tuple(data.values()))
        base_admin.commit()
        

        
        

async def read_add_command(state,callback):    
    async with state.proxy() as menu_show:                 
        jadval2=[]
        polo=('''SELECT ism_familiya FROM list_group WHERE dars_kuni=%s AND dars_vaqti=%s''')
        tt=(menu_show['dayss_info'],menu_show['time_info'],)
        cur_admin.execute(polo,tt)
        polo1=cur_admin.fetchall()
        for jadval in polo1:
            jadval2.append(jadval)
        if jadval2 !=[]:
            polo2=('''SELECT ism_familiya FROM list_group WHERE dars_kuni=%s AND dars_vaqti=%s''')
            tt2=(menu_show['dayss_info'],menu_show['time_info'],)
            cur_admin.execute(polo2,tt2)
            polo3=cur_admin.fetchall()
            for jadval3 in polo3:
                await callback.message.answer(re.sub("[(),'']",'',str(jadval3)))
            await callback.message.answer('Delete the data',reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"delete {menu_show['dayss_info']}-{menu_show['time_info']}",callback_data=f"delete {menu_show['dayss_info']}-{menu_show['time_info']}")))         
        else: 
            await callback.message.answer('The data of this group hasn’t been found')   


async def sql_delete_command(data):
    cur_admin.execute('DELETE FROM list_group WHERE ism_familiya=%s',(data,))
    base_admin.commit()
    base=sq.connect(host=host,user=user1,password=passwd,database=database1)
    cur=base.cursor()
    cur.execute('DELETE  FROM list_users WHERE users_name=%s',(data,))
    base.commit()

    

async def sql_read2(callback,state):
    async with state.proxy() as menu_show:
        polo4=('''SELECT * FROM list_group WHERE dars_kuni=%s  AND dars_vaqti=%s''')
        tt3=(menu_show['dayss_info'],menu_show['time_info'],)
        cur_admin.execute(polo4,tt3)
        polo5=cur_admin.fetchall()
        return polo5


# async def copy_group(message):
    # bb_group=cur_admin.execute('SELECT * FROM list_group').fetchall()
    # if bb_group in myusers.copy_users(message):
        # print('+')
    


