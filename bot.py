from create_bot import dp ,bot
from aiogram import executor,Dispatcher
from database import mydb,mytest,myusers


async def on_startup(_):
    print('Bot:online')
    mydb.sql_start()
    mytest.sql_test()
    myusers.sql_users()


from handlers import client
client.register_handler_client(dp)


from handlers import admin
admin.register_handler_admin(dp)


from handlers import admin_test
admin_test.register_handler_admin_test(dp)





executor.start_polling(dp,skip_updates=True,on_startup=on_startup)
