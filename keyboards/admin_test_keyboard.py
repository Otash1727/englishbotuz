from  aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from aiogram import types
from keyboards import admin_keyboard 


Text2=KeyboardButton("Add or change tests")
admin_test_text2=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
admin_test_text2.add(Text2)


url_save=KeyboardButton('Upload or update URL')
result_send=KeyboardButton('Share the results')
admin_test_url_send=ReplyKeyboardMarkup(resize_keyboard=True)
admin_test_url_send.row(url_save,result_send)


test_send_1=InlineKeyboardButton('📤 08-10',callback_data='📤08-10')
test_send_2=InlineKeyboardButton('📤 10-12',callback_data='📤10-12')
test_send_3=InlineKeyboardButton('📤 14-16',callback_data='📤14-16')
test_send_4=InlineKeyboardButton('📤 16-18',callback_data='📤16-18')
test_send_5=InlineKeyboardButton('📤 18-20',callback_data='📤18-20')
test_sendmarkup=InlineKeyboardMarkup(row_width=2).add(test_send_1,test_send_2).add(test_send_3,test_send_4).add(test_send_5)

send_day=KeyboardButton('📤 Odd days')
send_day2=KeyboardButton('📤 Even days')
back_test=KeyboardButton('Cancel_test')
send_markup=ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).row(send_day,send_day2).add(back_test)




