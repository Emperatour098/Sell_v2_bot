from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton ,ReplyKeyboardMarkup, ReplyKeyboardRemove
def key_start_sudo():
        keyboard=ReplyKeyboardMarkup(
                                        [["ساخت کانفینگ","حذف کانفینگ 🛍"],
                                        ["ارسال پیام به یوزر","ارسال پیام به چنل"],
                                        ["اضاف کردن ادمین","حذف ادمین"],
                                        ["حساب کاربری 🔐","دسترسی ها"],
                                        ["لیست مشتریان و گزارشات"],
                                        ],
                                        resize_keyboard=True
                                )
        return keyboard

def key_start_admin():
        keyboard=ReplyKeyboardMarkup(
                                        [["ساخت کانفینگ","حذف کانفینگ 🛍"],
                                        ["ارسال پیام به یوزر","ارسال پیام به چنل"],
                                        ["اضاف کردن ادمین","حذف ادمین"],
                                        ["حساب کاربری 🔐"],["برگشت"]],
                                        resize_keyboard=True
                                    )
        return keyboard
def key_start_user():
        keyboard=ReplyKeyboardMarkup(
                                        [["سرویس تستی [رایگان] 🎁","خرید سرویس 🛍"],
                                        ["تعرفه خدمات 🗂","حساب کاربری 🔐"],
                                        ["اطلاعات سرویس من ⚙️","راهنما و قوانین 📚"],
                                        ['افزایش موجودی 🛒',"پشتیبانی☎"]],
                                        resize_keyboard=True
                                    )
        return keyboard

        
def key_myservice():
        keyboard=InlineKeyboardMarkup(
                [
                        [InlineKeyboardButton(text=f"نام اکانت :{0}", callback_data="salam")],
                        
                        [InlineKeyboardButton(text="وضعیت اکانت⚙️", callback_data="salam")],
                        
                        [InlineKeyboardButton(text="اپلود⬆️", callback_data="salam"),InlineKeyboardButton(text="دانلود⬇️", callback_data="salam")],
                        
                        [InlineKeyboardButton(text="میزان مصرف⌛️", callback_data="salam")],
                        
                        [InlineKeyboardButton(text="حجم باقی مانده📡", callback_data="salam")],
                        
                        [InlineKeyboardButton(text="زمانی باقی مانده🕘", callback_data="salam")],
                        
                        [InlineKeyboardButton(text="حجم کل🌐", callback_data="salam")],  
                ]
                                    )
        
        return keyboard

def key_price():
        keyboard=InlineKeyboardMarkup(
                [
                        
                        [InlineKeyboardButton(text="10 GB یک ماه: 20 تومان", callback_data="x"),
                        InlineKeyboardButton(text="20 GB یک ماه: 30تومان", callback_data="x")],
        
                        [InlineKeyboardButton(text="30 GB یک ماه: 40 تومان", callback_data="x"),
                        InlineKeyboardButton(text="40 GB یک ماه: 50 تومان", callback_data="x")],
                                        
                        [InlineKeyboardButton(text="50 GB یک ماه: 60 تومان", callback_data="x"),
                        InlineKeyboardButton(text="نامحدود یک ماه : 100تومان", callback_data="x")],
                                        
                        [InlineKeyboardButton(text="10 GB دو ماه: 20 تومان", callback_data="x"),
                         InlineKeyboardButton(text="20 GB دو ماه: 30تومان", callback_data="x")],
                        
                        [InlineKeyboardButton(text="30 GB دو ماه: 40 تومان", callback_data="x"),
                        InlineKeyboardButton(text="40 GB دو ماه: 50 تومان", callback_data="x")],
                                        
                        [InlineKeyboardButton(text="50 GB دو ماه: 60 تومان", callback_data="x"),
                        InlineKeyboardButton(text="نامحدود دو ماه : 100تومان", callback_data="x")],
                                        
                        [InlineKeyboardButton(text="10 GB سه ماه: 20 تومان", callback_data="x"),
                        InlineKeyboardButton(text="20 GB سه ماه: 30تومان", callback_data="x")],
                                        
                        [InlineKeyboardButton(text="30 GB سه ماه: 40 تومان", callback_data="x"),
                        InlineKeyboardButton(text="40 GB سه ماه: 50 تومان", callback_data="x")],
                                        
                        [InlineKeyboardButton(text="50 GB سه ماه: 60 تومان", callback_data="x"),
                        InlineKeyboardButton(text="نامحدود سه ماه : 100تومان", callback_data="x")]
                                        
                ]
                                        )
        return keyboard

def key_buy_service():
        return None

def key_which_app():
        keyboard=InlineKeyboardMarkup(
                [
                        [InlineKeyboardButton(text="V2rayng", callback_data="salam")],
                        [InlineKeyboardButton(text="napsternetv", callback_data="salam")],
                        [InlineKeyboardButton(text="open connect", callback_data="salam")],
                        [InlineKeyboardButton(text="v2ray windows", callback_data="salam")],
                        [InlineKeyboardButton(text="cisgo", callback_data="salam")],
                        [InlineKeyboardButton(text="Game", callback_data="salam")]
                ]
                                        )
        return keyboard

def key_how_pay():
            keyboard=InlineKeyboardMarkup(
                    
                    [[InlineKeyboardButton(text="پرداخت ریالی", callback_data="y1"),
                      InlineKeyboardButton(text="پرداخت تتر", callback_data="y1")],
                     
                        [InlineKeyboardButton(text="کارت به کارت", callback_data="y1")]
                    ]
                                        )
            return keyboard
