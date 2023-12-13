from pyrogram import Client,types,filters,idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton ,ReplyKeyboardMarkup, ReplyKeyboardRemove , CallbackQuery
from pyromod import listen
import ConstText
from keys import *
import maindb

api_id = 2631644
api_hash = "2a0dec0b80b84e501c5d9806248eb235"
bot_token = "6446414609:AAH3oNre18WZuM8QBNHoLOF9WwWJF1VffDw"
proxy = {
     "scheme": "http",
     "hostname": "127.0.0.1",
     "port": 10809,
 }

sell_v2ray_bot=Client(name="Manager",api_id=api_id,api_hash=api_hash,bot_token=bot_token,proxy=None)

@sell_v2ray_bot.on_message(filters.private & filters.command("start"))
async def start_bot(_:sell_v2ray_bot , m:types.Message):
        userid=m.from_user.id
        anyadmin=await maindb.Read_Admin(userid)
        rolle=None
        if anyadmin:
                rolle=anyadmin[2]
        if rolle==1:
            await m.reply_text(ConstText.StartMsg_sudo.format(m.from_user.first_name , m.date),reply_markup=key_start_sudo())
        elif rolle==0:
            await m.reply_text(ConstText.StartMsg_admin.format(m.from_user.first_name , m.date),reply_markup=key_start_admin())
        else:
            await m.reply_text(ConstText.StartMsg.format(m.from_user.first_name , m.date),reply_markup=key_start_user())
                
    
@sell_v2ray_bot.on_message(filters.private & filters.regex("^اطلاعات سرویس من ⚙️$"))
async def MyAccountInfo(_:sell_v2ray_bot , m:types.Message):
            await m.reply_text(ConstText.myservice1,reply_markup=key_myservice(m.from_user.first_name))
            
@sell_v2ray_bot.on_message(filters.private & filters.regex("^تعرفه خدمات 🗂$"))
async def price_service(_:sell_v2ray_bot , m:types.Message):
            await m.reply_text(ConstText.myservice1,reply_markup=key_price())
            
@sell_v2ray_bot.on_message(filters.private & filters.regex("^حساب کاربری 🔐$"))
async def MyAccount(_:sell_v2ray_bot , m:types.Message):
            await m.reply_text(ConstText.myaccount)
            
@sell_v2ray_bot.on_message(filters.private & filters.regex("^پشتیبانی☎$"))
async def bot_support(_:sell_v2ray_bot , m:types.Message):
            await m.reply_text(ConstText.support)
            
@sell_v2ray_bot.on_message(filters.private & filters.regex("^خرید سرویس 🛍$"))
async def buy_service(_:sell_v2ray_bot , m:types.Message):
        await m.reply_text(ConstText.buyservice,reply_markup=key_buy_service())

@sell_v2ray_bot.on_message(filters.private & filters.regex("^حذف کانفینگ 🛍$"))
async def buy_service(_:sell_v2ray_bot , m:types.Message):
        await m.reply_text(ConstText.buyservice,reply_markup=key_buy_service())
        
@sell_v2ray_bot.on_callback_query()
async def on_callback(_:sell_v2ray_bot , c:CallbackQuery):
    if c.data == "y":
            await c.message.edit(ConstText.which_app,reply_markup=key_which_app())
    elif c.data =="salam":
            await c.message.edit(ConstText.card,reply_markup=key_how_pay())

async def run():
        # await maindb.create_tables()
        
        for i in [6603885706]:
                if await maindb.Read_Admin(i) is None:
                        await maindb.Create_access_types(i,1,1,1,1,1,1)
                        ra=await maindb.Read_AccessTypes_By_UserId(i)
                        await maindb.Create_Admin(i,1,ra[0])

        print("Run")
        
        
# import asyncio
# asyncio.run(run())
sell_v2ray_bot.start()
idle()