import mysql.connector as sq 
from create_bot import bot
from database import mydb
from keyboards import keyboard_reply 
from keyboards.keyboard_reply import account_markup,contact_markup
import re
from config import host,passwd,user1,database1
 


def  sql_users():
    global base,cur
    base=sq.connect(host=host,user=user1,password=passwd,database=database1)
    cur=base.cursor()
    if base:
        print('Data_users connect')
    cur.execute('CREATE TABLE IF NOT EXISTS list_users(users_days VARCHAR(255),users_time VARCHAR(255) ,users_name VARCHAR(255),users_contact VARCHAR(255),users_tg_id VARCHAR(255))')    
    base.commit()
    cur.execute("INSERT INTO list_users(users_days,users_time,users_name,users_contact,users_tg_id) VALUES(NULL,NULL,NULL,NULL,NULL)")
    base.commit()



async def tekshiruv_2(message):
    polo8=("SELECT users_tg_id FROM list_users")
    cur.execute(polo8)
    royhat_2=cur.fetchall()
    for iii in royhat_2:
        iii    
    if   message.from_user.id in iii :
        await message.answer('You registered before \n Press the button ‘My account’ to start the test',reply_markup=account_markup)    
    else:
        await  message.answer('Send your phone number to use the bot',reply_markup=contact_markup) 
       



async def open_list_users(message):
    ry_id=[]
    polo9=("SELECT users_days,users_time FROM list_users WHERE users_tg_id=%s",(message.from_user.id,))
    cur.execute(polo9)
    royhat_3=cur.fetchall()
    for ry in royhat_3:
        ry_id.append(ry)
    polo10=("SELECT users_days,users_time FROM list_users WHERE users_tg_id=%s",(message.from_user.id,))
    cur.execute(polo10)
    polo11=cur.fetchall()
    for gg_test in polo11:
        gg_test
    if ry_id !=[]:
        base_test=sq.connect(host=host,password=passwd,user=user1,database=database1)
        cur_test=base_test.cursor()            
        royhat_4=cur_test.execute('SELECT link FROM  test_url WHERE test_kuni=? AND test_vaqti=?',(gg_test)).fetchall()
        for ry_4 in royhat_4:
            await message.answer(re.sub("[(),'']",'',str(ry_4)))
    else:
        await message.answer("Your information wasn’t found. Register again. ",reply_markup=contact_markup)  

async def add_users_info(state,message):
    async with state.proxy() as dd:
        foo_group=[]
        base_admin=sq.connect(host=host,password=passwd,user=user1,database=database1)
        cur_admin=base_admin.cursor()
        
        polo12=('SELECT * FROM list_group WHERE dars_kuni=? AND dars_vaqti=? AND ism_familiya=?',(dd['kun'],dd['vaqt'],dd['ism']))
        cur_admin.execute(polo12)
        polo13=cur_admin.fetchall()
        for www in polo13:
            foo_group.append(www)
        if foo_group != []:
            cur.execute("INSERT INTO list_users(users_days,users_time,users_name,users_contact,users_tg_id) VALUES(%s,%s,%s,%s,%s)",tuple(dd.values()))
            base.commit()
            await message.answer('You have registered \n Press the button ‘My account’ to start the test',reply_markup=account_markup)
        else:
            await message.answer('You entered the wrong information.\nTry again. ',reply_markup=contact_markup)    
            
          
async def copy_users(message):
    polo14=('SELECT (users_days,users_time,users_name) FROM list_users ')
    cur.execute(polo14)
    bb_users=cur.fetchall()


async def send_result(state,message):    
    async with state.proxy() as sent:
        polo15=('SELECT users_tg_id FROM list_users WHERE users_days=%s AND users_time=%s',(sent['testday2'],sent['testtime2'],))
        cur.execute(polo15)
        polo16=cur.fetchall()            
        for b in polo16:
            await bot.send_message(chat_id=re.sub("[(),]",'',str(b)), text=message.text)
      
async def send_result_video(state,message,video_id):
    async with state.proxy() as sent:
        polo16=('SELECT users_tg_id FROM list_users WHERE users_days=%s AND users_time=%s',(sent['testday2'],sent['testtime2'],))
        cur.execute(polo16)
        polo17=cur.fetchall()
        for b2 in polo17:
            await bot.send_video(chat_id=re.sub("[(),]",'',str(b2)), video=video_id)

async def send_result_photo(state,message,photo_id):
    async with state.proxy() as sent:
        polo18=('SELECT users_tg_id FROM list_users WHERE users_days=%s AND users_time=%s',(sent['testday2'],sent['testtime2'],))
        cur.execute(polo18)
        polo19=cur.fetchall()                  
        for b3 in polo19:
            await bot.send_photo(chat_id=re.sub("[(),]",'',str(b3)), photo=photo_id)


async def send_result_document(state,message,document_id):
    async with state.proxy()as sent:
        polo20=('SELECT users_tg_id FROM list_users WHERE users_days=%s AND users_time=%s',(sent['testday2'],sent['testtime2'],))
        cur.execute(polo20)
        polo21=cur.fetchall()       
        for b4 in polo21:
            await bot.send_document(chat_id=re.sub("[(),]",'',str(b4)), document=document_id)


async def send_result_voice(state,message,voice_id):
    async with state.proxy() as sent:
        polo22=('SELECT users_tg_id FROM list_users WHERE users_days=%s AND users_time=%s',(sent['testday2'],sent['testtime2'],))
        cur.execute(polo22)
        polo23=cur.fetchall()       
        for b5 in polo23:
            await bot.send_voice(chat_id=re.sub("[(),]",'', str(b5)), voice=voice_id)

async def send_result_audio(state,message,audio_id):
    async with state.proxy() as sent:
        polo24=('SELECT users_tg_id FROM list_users WHERE users_days=%s AND users_time=%s',(sent['testday2'],sent['testtime2'],))
        cur.execute(polo24)
        polo25=cur.fetchall()  
        for b6 in polo25:
            await bot.send_audio(chat_id=re.sub("[(),]",'',str(b6)), audio=audio_id)        
                  
