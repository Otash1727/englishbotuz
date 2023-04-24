from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram import types
 
even_d = KeyboardButton('Even days')
odd_d  = KeyboardButton('Odd days')
back_client=KeyboardButton('Cancel')
kb_markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True,input_field_placeholder='Select your group')
kb_markup.row(even_d,odd_d).add(back_client)

contact= KeyboardButton('send your number',request_contact=True)
contact_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(contact)


my_account=KeyboardButton('My account')
account_markup=ReplyKeyboardMarkup(resize_keyboard=True,input_field_placeholder="Press the button ‘My account’ to start the test")
account_markup.add(my_account)