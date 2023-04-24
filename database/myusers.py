import sqlite3 as sq 
from create_bot import bot
from database import mydb
from keyboards import keyboard_reply 
from keyboards.keyboard_reply import account_markup,contact_markup
import re

 
base_test=sq.connect('test_url.db')
cur_test=base_test.cursor()

def  sql_users():
    global base,cur
    base=sq.connect('list_users.db')
    cur=base.cursor()
    if base:
        print('Data_users connect')
    base.execute('CREATE TABLE IF NOT EXISTS list_users(users_days TEXT,users_time ,users_name TEXT,users_contact INTEGER,users_tg_id )')    
    base.commit()
    cur.execute("INSERT INTO list_users(users_days,users_time,users_name,users_contact,users_tg_id) VALUES(NULL,NULL,NULL,NULL,NULL)")
    base.commit()



async def tekshiruv_2(message):
    royhat_2=cur.execute("SELECT users_tg_id FROM list_users").fetchall()
    for iii in royhat_2:
        iii    
    if   message.from_user.id in iii :
        await message.answer('You registered before \n Press the button ‘My account’ to start the test',reply_markup=account_markup)    
    else:
        await  message.answer('Send your phone number to use the bot',reply_markup=contact_markup) 
       



async def open_list_users(message):
    ry_id=[]
    royhat_3=cur.execute("SELECT users_days,users_time FROM list_users WHERE users_tg_id=?",(message.from_user.id,)).fetchall()
    for ry in royhat_3:
        ry_id.append(ry)
    for gg_test in cur.execute("SELECT users_days,users_time FROM list_users WHERE users_tg_id=?",(message.from_user.id,)).fetchall():
        gg_test
    if ry_id !=[]:            
        royhat_4=cur_test.execute('SELECT link FROM  test_url WHERE test_kuni=? AND test_vaqti=?',(gg_test)).fetchall()
        for ry_4 in royhat_4:
            await message.answer(re.sub("[(),'']",'',str(ry_4)))
    else:
        await message.answer("Your information wasn’t found. Register again. ",reply_markup=contact_markup)  

async def add_users_info(state,message):
    async with state.proxy() as dd:
        foo_group=[]
        base_admin=sq.connect('list_group.db')
        cur_admin=base_admin.cursor()
        
        for www in   cur_admin.execute('SELECT * FROM list_group WHERE dars_kuni=? AND dars_vaqti=? AND ism_familiya=?',(dd['kun'],dd['vaqt'],dd['ism'])).fetchall():
            foo_group.append(www)
        if foo_group != []:
            cur.execute("INSERT INTO list_users(users_days,users_time,users_name,users_contact,users_tg_id) VALUES(?,?,?,?,?)",tuple(dd.values()))
            base.commit()
            await message.answer('You have registered \n Press the button ‘My account’ to start the test',reply_markup=account_markup)
        else:
            await message.answer('You entered the wrong information.\nTry again. ',reply_markup=contact_markup)    
            
          
async def copy_users(message):
    bb_users=cur.execute('SELECT (users_days,users_time,users_name) FROM list_users ').fetchall()



async def send_result(state,message):    
    async with state.proxy() as sent:
        for b in (cur.execute('SELECT users_tg_id FROM list_users WHERE users_days=? AND users_time=?',(sent['testday2'],sent['testtime2'],)).fetchall()):            
            await bot.send_message(chat_id=re.sub("[(),]",'',str(b)), text=message.text)
      
async def send_result_video(state,message,video_id):
    async with state.proxy() as sent:
        for b2 in (cur.execute('SELECT users_tg_id FROM list_users WHERE users_days=? AND users_time=?',(sent['testday2'],sent['testtime2'],)).fetchall()):
            await bot.send_video(chat_id=re.sub("[(),]",'',str(b2)), video=video_id)

async def send_result_photo(state,message,photo_id):
    async with state.proxy() as sent:
        for b3 in (cur.execute('SELECT users_tg_id FROM list_users WHERE users_days=? AND users_time=?',(sent['testday2'],sent['testtime2'],)).fetchall()):                  
            await bot.send_photo(chat_id=re.sub("[(),]",'',str(b3)), photo=photo_id)


async def send_result_document(state,message,document_id):
    async with state.proxy()as sent:
        for b4 in (cur.execute('SELECT users_tg_id FROM list_users WHERE users_days=? AND users_time=?',(sent['testday2'],sent['testtime2'],)).fetchall()):       
            await bot.send_document(chat_id=re.sub("[(),]",'',str(b4)), document=document_id)


async def send_result_voice(state,message,voice_id):
    async with state.proxy() as sent:
        for b5 in (cur.execute('SELECT users_tg_id FROM list_users WHERE users_days=? AND users_time=?',(sent['testday2'],sent['testtime2'],)).fetchall()):       
            await bot.send_voice(chat_id=re.sub("[(),]",'', str(b5)), voice=voice_id)

async def send_result_audio(state,message,audio_id):
    async with state.proxy() as sent:
        for b6 in (cur.execute('SELECT users_tg_id FROM list_users WHERE users_days=? AND users_time=?',(sent['testday2'],sent['testtime2'],)).fetchall()):  
            await bot.send_audio(chat_id=re.sub("[(),]",'',str(b6)), audio=audio_id)        
                  
