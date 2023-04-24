from  create_bot import  dp,bot
from aiogram import types,Dispatcher
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardRemove


admin_1= InlineKeyboardButton(text='✏️ 08-10 ',callback_data='✏️08-10')
admin_2= InlineKeyboardButton(text='✏️ 10-12 ',callback_data='✏️10-12')
admin_3= InlineKeyboardButton(text='✏️ 14-16  ',callback_data='✏️14-16')
admin_4= InlineKeyboardButton(text='✏️ 16-18  ',callback_data='✏️16-18')
admin_5= InlineKeyboardButton(text='✏️ 18-20  ',callback_data='✏️18-20')
admin_kb = InlineKeyboardMarkup(row_width=2).row(admin_1,admin_2).row(admin_3,admin_4).add(admin_5)


insert_students=InlineKeyboardButton(text="insert",callback_data="insert")
remove_students=InlineKeyboardButton(text="remove",callback_data="remove")
insert_remove_students=InlineKeyboardMarkup(row_width=1).add(insert_students).add(remove_students)


test_1= InlineKeyboardButton(text='⏱ 08-10 ',callback_data='⏱ 08-10 ')
test_2= InlineKeyboardButton(text='⏱ 10-12 ',callback_data='⏱ 10-12 ')
test_3= InlineKeyboardButton(text='⏱ 14-16 ',callback_data='⏱ 14-16 ')
test_4= InlineKeyboardButton(text='⏱ 16-18 ',callback_data='⏱ 16-18 ')
test_5= InlineKeyboardButton(text='⏱ 18-20 ',callback_data='⏱ 18-20 ')
test_kb = InlineKeyboardMarkup(row_width=2).row(test_1,test_2).row(test_3,test_4).add(test_5)

menu_studens=InlineKeyboardButton(text='menu', callback_data='menu')
reply_studenst= InlineKeyboardButton(text='reply',callback_data='reply')
menu_reply=InlineKeyboardMarkup(row_width=1).row(menu_studens).row(reply_studenst)



info_1= InlineKeyboardButton(text='🔍08-10',callback_data='🔍08-10')
info_2= InlineKeyboardButton(text='🔍10-12',callback_data='🔍10-12')
info_3= InlineKeyboardButton(text='🔍14-16',callback_data='🔍14-16')
info_4= InlineKeyboardButton(text='🔍16-18',callback_data='🔍16-18')
info_5= InlineKeyboardButton(text='🔍18-20',callback_data='🔍18-20')
info_kb = InlineKeyboardMarkup(row_width=2).row(info_1,info_2).row(info_3,info_4).add(info_5)



delete_info2=InlineKeyboardButton(text='delete_users',callback_data='delete_users')
delete_kb=InlineKeyboardMarkup(row_width=1).add(delete_info2)



