from create_bot import bot,dp
from aiogram import Dispatcher ,types,Bot
from aiogram.dispatcher import FSMContext,storage
from aiogram.dispatcher.filters.state import StatesGroup,State
from keyboards import admin_test_keyboard
from keyboards.admin_test_keyboard import url_save,admin_test_text2,admin_test_url_send,test_sendmarkup,send_markup
from keyboards import admin_inline,admin_keyboard
from keyboards.admin_inline import test_kb
from keyboards.admin_keyboard import  *
from aiogram.dispatcher.filters import Text 
from database import mytest
from database.mytest import test_add_command,select_data,into_data
from database  import myusers
from database.myusers import send_result,send_result_document,send_result_photo,send_result_video,send_result_voice,send_result_audio

class Testadmin(StatesGroup):
    test_day=State()
    test_time=State()
    rl_test=State()


class Testresult(StatesGroup):
    testday2=State()
    testtime2=State()
    testinfo=State()



ID= None


async def open_test_admin(message:types.Message()):
    global ID
    ID=message.from_user.id
    await bot.send_message(message.from_user.id,text=f"{message.from_user.full_name}: \n 🗝\n Admin https://t.me/Imperial_Termiz_bot  ")
    await bot.send_photo(message.from_user.id, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRe1X_5HZZ6w_aawNC91UE6_S5XEKRq-Ebzbw&usqp=CAU')
    await bot.send_message(message.from_user.id,text=' You can add new tests here',reply_markup=admin_test_text2)
    await message.delete()


async def cancel1(message:types.Message(),state=FSMContext):
    if message.from_user.id == ID:
        current_state_test= await state.get_state()
        if current_state_test == None:
            return
        await state.finish()
        await bot.send_message(message.from_user.id, text="Okey.You can start from the beginning ",reply_markup=admin_test_url_send)

async def add_test(message:types.Message()):
    if message.from_user.id == ID:
        await bot.send_message(message.from_user.id,"Choose",reply_markup=admin_test_url_send)           
        



async def url_dowland(message:types.Message()):
    if message.from_user.id==ID:
        await bot.send_message(message.from_user.id, text='Choose the day ',reply_markup=markup_admin_days_test)
        

async def ev_odd_test(message:types.Message()):
    if message.from_user.id==ID:
        await bot.send_message(message.from_user.id, text=f" Teacher:  {message.from_user.full_name}")
        if message.text=="🧑‍🏫Even day" or "🧑‍🏫 Odd day" :
           await Testadmin.first()
        await bot.send_message(message.from_user.id,f" You have chosen {message.text}")
                  

async def add_testadmin_dayss(message:types.Message(),state=FSMContext):
   if message.from_user.id==ID:
       async with state.proxy() as file_test:
           if message.text=="🧑‍🏫 Even day":
                file_test['test_day']="evendays"
           if  message.text=="🧑‍🏫 Odd day":
                file_test['test_day']="odddays"
       await Testadmin.next()   
       await bot.send_message(message.from_user.id, text="Select the time ",reply_markup=test_kb)


async def add_testadmin_time(callback:types.CallbackQuery(),state=FSMContext):
   if callback.from_user.id == ID:
       async with state.proxy() as file_test:
            if callback.data=="⏱ 08-10 ":
                file_test['test_time']="08-10"           
            if callback.data=="⏱ 10-12 ":
                file_test['test_time']="10-12"   
            if callback.data=="⏱ 14-16 ":
                file_test['test_time']="14-16"
            if callback.data=="⏱ 16-18 ":
                file_test['test_time']="16-18"
            if callback.data=="⏱ 18-20 ":
                file_test['test_time']="18-20"
       await Testadmin.next()                   
       await callback.answer(f" Enter URL of the prepared test \n {file_test['test_time']}-time ",show_alert=True) 
       await callback.message.answer(f"{file_test['test_day']} \n {file_test['test_time']}".capitalize())

async def input_test(message:types.Message(),state=FSMContext):
    if message.from_user.id== ID:
        async with state.proxy() as file_test:
            file_test['rl_test']='1'
            if message.text.startswith('https://'):
                await mytest.test_add_command(state,message)
                await bot.send_message(message.from_user.id, text='+')
            elif message.text=='jk':
                jk1="Tests aren’t ready yet"
                await mytest.into_data(state,message,jk1)
                await bot.send_message(message.from_user.id, text='+')
            else:
                await bot.send_message(message.from_user.id, text='You are making mistakes in entering the URL.\n Start again',reply_markup=markup_admin_days_test)        
        await state.finish()


async def test_result_send1(message:types.Message()):
    if message.from_user.id == ID:
        await bot.send_message(message.from_user.id, text='Here you can send the results of the test to the members of the group',reply_markup=send_markup)
        

async def curent_read_send(message:types.Message,state:FSMContext):
    if message.from_user.id == ID:
        current_state= await state.get_state()
        if current_state== None:
            return
        await state.finish()
        await bot.send_message(message.from_user.id, text="Okey.You can start from the beginning",reply_markup=admin_test_url_send) 


async def test_result_send2(message:types.Message,state:FSMContext):
    if message.from_user.id == ID:
        if message.text=="📤 Odd days" or "📤 Even days":
            await Testresult.first()
            await bot.send_message(message.from_user.id,f'You  have chosen {message.text}')
            await message.delete()

async def test_result_send3(message:types.Message,state:FSMContext):
    if message.from_user.id== ID:
        async with state.proxy() as sent:
            if message.text=='📤 Odd days':           
                sent['testday2']='odddays'                
                await bot.send_message(message.from_user.id, 'Choose the time',reply_markup=test_sendmarkup)
            if message.text=='📤 Even days':
                sent['testday2']='evendays'
                await bot.send_message(message.from_user.id, 'Choose the time',reply_markup=test_sendmarkup)
        await Testresult.next()
        
        
        


async def test_result_send4(callback:types.CallbackQuery,state:FSMContext):
    if callback.from_user.id== ID:
        async with state.proxy() as sent:
            if callback.data=='📤08-10':
                sent['testtime2']='08-10'
            if callback.data=='📤10-12':
                sent['testtime2']='10-12'
            if callback.data=='📤14-16':
                sent['testtime2']='14-16'
            if callback.data=='📤16-18':
                sent['testtime2']='16-18'
            if callback.data=='📤18-20':
                sent['testtime2']='18-20'
        await Testresult.next()
        await callback.answer(f"Send the results by means of ‘file’ or ‘picture’, ‘video’ and ‘voice’ \n {sent['testtime2']}-time",show_alert=True)
        await callback.message.answer(f"{sent['testday2']}\n {sent['testtime2']}".capitalize())

async def  test_result_send5(message:types.Message,state:FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as sent:
            sent['testinfo']='1'
            if message.text:
                await myusers.send_result(state,message)
                await bot.send_message(message.from_user.id, text='+')          
            if message.photo:
                photo_id=message.photo[-1].file_id
                await myusers.send_result_photo(state,message,photo_id)
                await bot.send_message(message.from_user.id,text='+')
            if message.video:
                video_id=message.video.file_id
                await myusers.send_result_video(state,message,video_id)
                await bot.send_message(message.from_user.id, text='+')
            if message.document:
                document_id=message.document.file_id
                await myusers.send_result_document(state,message,document_id)
                await bot.send_message(message.from_user.id,text='+')
            if message.voice:
                voice_id=message.voice.file_id
                await myusers.send_result_voice(state,message,voice_id)
                await bot.send_message(message.from_user.id,text='+')
            if message.audio:
                audio_id=message.audio.file_id
                await  myusers.send_result_audio(state, message, audio_id)
                await bot.send_message(message.from_user.id,text='+')
                                   
                                             
        await state.finish()
                                       








def register_handler_admin_test(dp:Dispatcher):
    dp.register_message_handler(open_test_admin,commands='Question',is_chat_admin=True)
    dp.register_message_handler(cancel1,commands='Cancel_test',state='*')
    dp.register_message_handler(cancel1,Text(equals='Cancel_test',ignore_case=True),state='*')
    dp.register_message_handler(add_test,Text(startswith="Add or ",ignore_case=True))
    dp.register_message_handler(url_dowland,Text(equals='Upload or update URL',ignore_case=True))
    dp.register_message_handler( ev_odd_test,Text(startswith=["🧑‍🏫 Even ","🧑‍🏫 Odd"],ignore_case=True))
    dp.register_message_handler(add_testadmin_dayss,state=Testadmin.test_day)
    dp.register_callback_query_handler(add_testadmin_time,state=Testadmin.test_time)
    dp.register_message_handler(input_test,state=Testadmin.rl_test)
    dp.register_message_handler(test_result_send1,Text(startswith='Share ',ignore_case=True))
    dp.register_message_handler(curent_read_send,commands='Cancel_test',state='*')
    dp.register_message_handler(curent_read_send,Text(equals='Cancel_test',ignore_case=True),state='*')
    dp.register_message_handler(test_result_send2,Text(equals=['📤 Odd days','📤 Even days'],ignore_case=True))
    dp.register_message_handler(test_result_send3,state=Testresult.testday2)
    dp.register_callback_query_handler(test_result_send4,state=Testresult.testtime2)
    dp.register_message_handler(test_result_send5,state=Testresult.testinfo,content_types=['text','video','voice','photo','document','audio'])

   
