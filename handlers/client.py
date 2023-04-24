from create_bot import bot,dp 
from aiogram import types ,Dispatcher
from keyboards import inline_keyboards,keyboard_reply
from keyboards.inline_keyboards import i_kb
from keyboards.keyboard_reply import kb_markup
from keyboards.keyboard_reply import contact_markup
from aiogram.dispatcher.filters    import  Text
from aiogram.types import ReplyKeyboardRemove,Contact
from aiogram.dispatcher import storage,FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import logging
from database import myusers
from database.myusers import open_list_users,add_users_info,tekshiruv_2
from database import mydb














get_telephone_number=None
class Users_info(StatesGroup):
    kun=State()
    vaqt=State()
    ism=State()
    contact_users=State()
    name_id=State()
   



async def start(message:types.Message):
    if message.text=='/start':      
        await myusers.tekshiruv_2(message)
        
        

        
async def Help(message:types.Message()):
    await message.answer('For example')
    await bot.send_video(message.from_user.id,video=open('botvideo.mp4','rb'),supports_streaming=True)          


async def delete(message:types.Message()):
    global  get_telephone_number    
    get_telephone_number=message.contact.phone_number
    await message.answer('Select your group',reply_markup=kb_markup)   
    await Users_info.first()
    await message.delete()
    

async def cancel_client_state(message:types.Message(),state:FSMContext):
    current_client_state= await state.get_state()
    if current_client_state == None:
        return
    await state.finish()
    await message.answer("You can start from the beginning",reply_markup=contact_markup)


        

async def choose_group(message:types.Message(),state:FSMContext):
    async with state.proxy() as dd:
        if message.text.lower()=='even days':
            dd['kun']='evendays'         
        if message.text.lower()=='odd days':
            dd['kun']='odddays'
    await message.answer(f"({message.text})__:Select the time",reply_markup=i_kb)
    await Users_info.next()
'''***************************************** inline knopkalar****************************************''' 

async def inline_10(callback:types.CallbackQuery,state:FSMContext):
    async with state.proxy() as dd:
            if callback.data=="🕗08-10":
                dd['vaqt']="08-10"           
            if callback.data=="🕘10-12":
                dd['vaqt']="10-12"   
            if callback.data=="🕑14-16":
                dd['vaqt']="14-16"
            if callback.data=="🕓16-18":
                dd['vaqt']="16-18"
            if callback.data=="🕕18-20":
                dd['vaqt']="18-20"
    await Users_info.next()
    await callback.answer(f"Enter your surname and name ‼️ \n {dd['vaqt']}-time",show_alert=True)
    

 
async def write_name(message:types.Message(),state:FSMContext):    
    ooo=[]
    async with state.proxy() as dd:
        dd['ism']=message.text.lower()
        dd['contact_users']=get_telephone_number    
        dd['name_id ']=message.from_user.id      
    await myusers.add_users_info(state,message)
    # await mydb.copy_group(message)
    await state.finish() 


async def my_profil(message:types.Message):
    await myusers.open_list_users(message)
    await message.pin()
    
         







# async def Help(message:types.Message):
#    await message.answer('bot haqida malumot va botni qanday ishlatishni video korsatadi')






def register_handler_client(dp):
    dp.register_message_handler(start,commands='start')
    dp.register_message_handler(Help,commands='help')
    dp.register_message_handler(delete, content_types= types.ContentTypes.CONTACT) # togirlash kk
    dp.register_message_handler(cancel_client_state,commands=['Cancel'],state="*")
    dp.register_message_handler(cancel_client_state,Text(equals='Cancel',ignore_case=True),state="*")
    dp.register_message_handler(choose_group,state=Users_info.kun)
    dp.register_callback_query_handler(inline_10,state=Users_info.vaqt)
    dp.register_message_handler(write_name,state=[Users_info.ism,Users_info.name_id,Users_info.contact_users])
    dp.register_message_handler(my_profil,Text(equals=['My account'],ignore_case=True))
    
  
