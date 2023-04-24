from aiogram import types,Dispatcher
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardRemove,ReplyKeyboardMarkup,KeyboardButton


info_new1= InlineKeyboardButton(text='🔍🔍08-10',callback_data='🔍🔍08-10')
info_new2= InlineKeyboardButton(text='🔍🔍10-12',callback_data='🔍🔍10-12')
info_new3= InlineKeyboardButton(text='🔍🔍14-16',callback_data='🔍🔍14-16')
info_new4= InlineKeyboardButton(text='🔍🔍16-18',callback_data='🔍🔍16-18')
info_new5= InlineKeyboardButton(text='🔍🔍18-20',callback_data='🔍🔍18-20')
info_new6= InlineKeyboardMarkup(row_width=2).row(info_new1,info_new2).row(info_new3,info_new4).add(info_new5)


even_new=KeyboardButton("🇺🇿 Even day")
odd_new=KeyboardButton("🇺🇿 Odd day")
back_new=KeyboardButton('Cancel_new')
markup_new_days=ReplyKeyboardMarkup(resize_keyboard=True)
markup_new_days.row(odd_new,even_new).add(back_new)

