from aiogram.utils  import executor
from aiogram.dispatcher import  FSMContext,storage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher,Bot
from create_bot import bot,dp
from aiogram.dispatcher.filters import Text
from keyboards import admin_keyboard
from keyboards.admin_keyboard import mixx,markup_admin_days,kun_markup
from keyboards import admin_inline
from keyboards.admin_inline import admin_kb,insert_remove_students,info_kb,delete_kb
from aiogram.types import ReplyKeyboardRemove
from database import mydb
from database.mydb import sql_add_command,sql_delete_command,sql_read2,read_add_command
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup



ID=None




class FSMadmin(StatesGroup):
    dayss=State()
    time=State()
    sure_name=State()

class Read_info(StatesGroup):
    dayss_info=State()
    time_info=State()    

class New_info(StatesGroup):
    new_day=State()
    new_time=State()




'''       admin oynasiga kirish         '''
async def sign_up(message:types.Message()):
    global ID
    ID= message.from_user.id  
    await bot.send_message(message.from_user.id,f"{message.from_user.full_name}: \n 🗝\n Admin https://t.me/Imperial_Termiz_bot  ",reply_markup=mixx)
    await bot.send_photo(message.from_user.id,'https://www.google.com/imgres?imgurl=https%3A%2F%2Flookaside.fbsbx.com%2Flookaside%2Fcrawler%2Fmedia%2F%3Fmedia_id%3D104375758597740&imgrefurl=https%3A%2F%2Fwww.facebook.com%2FAdmin.FB.Vietnam%2F&tbnid=ogkq4rysS0V-AM&vet=12ahUKEwiewK-Hx979AhXBuCoKHX6xBh8QMygKegUIARD3AQ..i&docid=psDIssAwjFEjEM&w=2047&h=2047&q=admin&ved=2ahUKEwiewK-Hx979AhXBuCoKHX6xBh8QMygKegUIARD3AQ')    
    await bot.send_message(message.from_user.id,"Here you can work with students’ data")
    await message.delete()


'''   ##########   Jurnal students info ###########  '''
async def add_students(message:types.Message()):
    if message.from_user.id == ID:
        if message.text.lower()=='add students':
            await bot.send_message(message.from_user.id,f" Teacher:  {message.from_user.full_name} \n  Choose the day ",reply_markup=(markup_admin_days))
            await message.delete()
            
        

        
       

async def cancel(message:types.Message(),state:FSMContext):
    if message.from_user.id== ID:
        current_state= await state.get_state()
        if current_state== None:
            return
        await state.finish()
        await bot.send_message(message.from_user.id, text="Okey.You can start from the beginning ",reply_markup=mixx)           
''' ####### days #################'''

async def evn_or_odd(message:types.Message()):
    if message.from_user.id==ID:
        await bot.send_message(message.from_user.id, text=f" Teacher:  {message.from_user.full_name}")
        if message.text=="👩‍🏫 Even day" or "👩‍🏫 Odd day" :
           await FSMadmin.first()
           await bot.send_message(message.from_user.id,f" You have chosen {message.text} ")
           await message.delete()
                  

async def add_fsmadmin_dayss(message:types.Message(),state=FSMContext):
   if message.from_user.id==ID:
       async with state.proxy() as data:
           if message.text=="👩‍🏫 Even day":
                data['dayss']="evendays"
           if  message.text=="👩‍🏫 Odd day":
                data['dayss']="odddays"
       await bot.send_message(message.from_user.id, text="Select the time ",reply_markup=admin_kb)
       await FSMadmin.next()   
      


async def add_fsmadmin_time(callback:types.CallbackQuery(),state=FSMContext):
   if callback.from_user.id == ID:
       async with state.proxy() as data:
            if callback.data=="✏️08-10":
                data['time']="08-10"           
            if callback.data=="✏️10-12":
                data['time']="10-12"   
            if callback.data=="✏️14-16":
                data['time']="14-16"
            if callback.data=="✏️16-18":
                data['time']="16-18"
            if callback.data=="✏️18-20":
                data['time']="18-20"
       await FSMadmin.next()                   
       await callback.answer(f"Enter students’ surnames and names \n {data['time']}-time",show_alert=True) 
       await callback.message.answer(f"{data['dayss']} \n {data['time']}".capitalize())

async def input_student(message:types.Message,state=FSMContext):
    if message.from_user.id== ID:
        async with state.proxy() as data:
            data['sure_name']=message.text.lower()
        await mydb.sql_add_command(state,message)
        await bot.send_message(message.from_user.id, text='+')
        await state.finish()

async def click_info(message:types.Message):
    if message.from_user.id ==ID:
        if message.text.lower()=='info':
            await bot.send_message(message.from_user.id,"Here you can see the list",reply_markup=kun_markup)
        await message.delete()

async def click_info_return(message:types.Message(),state:FSMContext):
    if message.from_user.id== ID:
        async with state.proxy() as menu_show:
            curent_read_info= await state.get_state()
            if curent_read_info is None:
                return
            await state.finish()
        await bot.send_message(message.from_user.id,'Okey.You can start from the beginning ',reply_markup=mixx)

async def click_info_add1(message:types.Message()):
    if message.from_user.id== ID:
        if message.text=="🖨Even days":
            await Read_info.first()
            await bot.send_message(message.from_user.id," You have chosen Even days")
        if message.text=="🖨Odd days":
            await Read_info.first()
            await bot.send_message(message.from_user.id,"You have chosen Odd days")
        await message.delete()

async def click_info_add2(message:types.Message,state:FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as menu_show:
            if message.text=='🖨Even days':
                menu_show['dayss_info']='evendays'
            if message.text=='🖨Odd days':
                menu_show['dayss_info']='odddays'
        await bot.send_message(message.from_user.id,'Select the time',reply_markup=info_kb)
        await message.delete()
        await Read_info.next()

async def click_info_time_add(callback:types.CallbackQuery,state:FSMContext):
    if callback.from_user.id==ID:       
        async with state.proxy() as menu_show:
            if callback.data=='🔍08-10':
                menu_show['time_info']='08-10'
            if callback.data=='🔍10-12':
                menu_show['time_info']='10-12'               
            if callback.data=='🔍14-16':
                menu_show['time_info']='14-16'                
            if callback.data=='🔍16-18':
                menu_show['time_info']='16-18'
            if callback.data=='🔍18-20':
                menu_show['time_info']='18-20'
        await callback.message.answer(f"The data of {menu_show['dayss_info']} {menu_show['time_info']} ")
        await  mydb.read_add_command(state,callback)
        await Read_info.next()      
        


async def click_delete_users(callback:types.CallbackQuery,state:FSMContext):
    if callback.from_user.id==ID:
        async with state.proxy() as menu_show:
            hh=await mydb.sql_read2(callback,state)
            for hh2 in hh:              
                await callback.message.answer(f'{hh2[2]}',reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"del {hh2[2]}",callback_data=f'del {hh2[2]}')))
        await state.finish()



@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def def_callback_run(callback_query:types.CallbackQuery):
    await mydb.sql_delete_command(callback_query.data.replace('del ', ''))
    await mydb2.sql_delete_command2(callback_query.data.replace('del ', ''))
    # await myusers.sql_delete_command2(callback_query.data.replace('dd ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} deleted.',show_alert=True)












      
     

    
        
            
     

def register_handler_admin(dp:Dispatcher):
    dp.register_message_handler(sign_up,commands='On',is_chat_admin=True)
    dp.register_message_handler(add_students,Text(equals=['Add Students'],ignore_case=True))
    dp.register_message_handler(evn_or_odd,Text(equals=["👩‍🏫 Even day","👩‍🏫 Odd day"],ignore_case=True))
    dp.register_message_handler(cancel,commands=['Cancel_admin'],state="*")
    dp.register_message_handler(cancel,Text(equals=['Cancel_admin'],ignore_case=True),state='*')
    dp.register_message_handler(add_fsmadmin_dayss,state=FSMadmin.dayss)
    dp.register_callback_query_handler(add_fsmadmin_time,state=FSMadmin.time)
    dp.register_message_handler(input_student,state=FSMadmin.sure_name)
    dp.register_message_handler(click_info,Text(equals='Info',ignore_case=True))
    dp.register_message_handler(click_info_return,commands=['Cancel_info'],state='*')
    dp.register_message_handler(click_info_return,Text(equals=['Cancel_info'],ignore_case=True),state='*')
    dp.register_message_handler(click_info_add1,Text(equals=['🖨Even days','🖨Odd days']))
    dp.register_message_handler(click_info_add2,state=Read_info.dayss_info)
    dp.register_callback_query_handler(click_info_time_add,state=Read_info.time_info)
    dp.register_callback_query_handler(click_delete_users,Text(startswith=['delete']))
    
    
    
 
