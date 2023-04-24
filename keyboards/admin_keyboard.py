from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove
from aiogram import types


students_info=KeyboardButton('Add Students')
menu_info=KeyboardButton('Info')
mixx=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
mixx.row(students_info,menu_info)




even_admin=KeyboardButton("👩‍🏫 Even day")
odd_admin=KeyboardButton("👩‍🏫 Odd day")
back_admin=KeyboardButton('Cancel_admin')
markup_admin_days=ReplyKeyboardMarkup(resize_keyboard=True)
markup_admin_days.row(odd_admin,even_admin).add(back_admin)




even_admin_test=KeyboardButton("🧑‍🏫 Even day")
odd_admin_test=KeyboardButton("🧑‍🏫 Odd day")
back_test=KeyboardButton('Cancel_test')
markup_admin_days_test=ReplyKeyboardMarkup(resize_keyboard=True)
markup_admin_days_test.row(odd_admin_test,even_admin_test).add(back_test)

soat_08=KeyboardButton('⏰08-10')
soat_10=KeyboardButton('⏰10-12')
soat_14=KeyboardButton('⏰14-16')
soat_16=KeyboardButton('⏰16-18')
soat_20=KeyboardButton('⏰18-20')
soat_markup=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
soat_markup.row(soat_08,soat_10).row(soat_14,soat_16).add(soat_20)

kun_day1=KeyboardButton('🖨Even days')
kun_day2=KeyboardButton('🖨Odd days')
kun_cancel=KeyboardButton('Cancel_info')
kun_markup=ReplyKeyboardMarkup(resize_keyboard=True)
kun_markup.row(kun_day2,kun_day1).add(kun_cancel)
