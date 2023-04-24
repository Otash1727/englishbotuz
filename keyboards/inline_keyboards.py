from create_bot import bot,dp
from aiogram import types,Dispatcher
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


k_1 = InlineKeyboardButton(text='🕗08:00-10:00',callback_data='🕗08-10')
k_2 = InlineKeyboardButton(text='🕘10:00-12:00',callback_data='🕘10-12')
k_3 = InlineKeyboardButton(text='🕑14:00-16:00',callback_data='🕑14-16')
k_4 = InlineKeyboardButton(text='🕓16:00-18:00',callback_data='🕓16-18')
k_5 = InlineKeyboardButton(text='🕕18:00-20:00',callback_data='🕕18-20')
i_kb = InlineKeyboardMarkup(row_width=2).row(k_1,k_2).row(k_3,k_4).add(k_5)
