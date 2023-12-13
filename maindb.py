import aiosqlite
async def create_tables():
    async with aiosqlite.connect("database.db") as conn:
        await conn.execute("""
            CREATE TABLE access_types (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                create_config BIT DEFAULT 0,
                delete_config BIT DEFAULT 0,
                add_admin BIT DEFAULT 0,
                delete_admin BIT DEFAULT 0,
                send_message_channel BIT DEFAULT 0,
                send_message_user BIT DEFAULT 0
            )"""
        )
        await conn.execute("""
            CREATE TABLE admins (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                role INTEGER DEFAULT 0,
                access_type_id INTEGER DEFAULT 0
            )"""
        )

        async with conn.cursor() as cursor:
            await cursor.execute("""
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    Fname varchar,
                    username varchar,
                    config_id INTEGER
                )""")
            await cursor.execute("""
                CREATE TABLE configs (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    config_id INTEGER,
                    v2ray BIT,
                    limit_cnf INTEGER,
                    start_date INTEGER,
                    end_date INTEGER
                )""")
            await cursor.execute(
                """
                CREATE TABLE prices (
                    id INTEGER PRIMARY KEY,
                    config_name INTEGER,
                    price INTEGER,
                    limit_cnf INTEGER
                )"""
            )

async def Create_User(user_id:int,Fname:str,username:str,confing_id:int):
    async with aiosqlite.connect("database.db") as conn:
        await conn.execute(
            f"""
            INSERT INTO User(user_id,Fname,username,confing_id)
            VALUES (?,?,?,?)
            """,
            (str(user_id),Fname,username,confing_id),
        )
        await conn.commit()

async def Create_Confing(user_id:int,confing_id:int,v2link:bool,limit_v2ray:int,date_start:int,date_expire:int):
    async with aiosqlite.connect("database.db") as conn:
        await conn.execute(
            f"""
            INSERT INTO Confing(user_id,confing_id,v2link,limit_v2ray,date_start,date_expire)
            VALUES (?,?,?,?,?,?)
            """,
            (str(user_id),confing_id,v2link,limit_v2ray,date_start,date_expire),
        )
        await conn.commit()

async def Create_Price(name_confing:int,price:int,limit_cnf:int):
    async with aiosqlite.connect("database.db") as conn:
        await conn.execute(
            f"""
            INSERT INTO Price(name_confing,price,limit_cnf)
            VALUES (?,?,?)
            """,
            (str(name_confing),price,limit_cnf),
        )
        await conn.commit()

async def Create_access_types(user_id:int,create_config:bool,delete_config:bool,add_admin:bool,delete_admin:bool,send_message_channel:bool,send_message_user:bool):
    async with aiosqlite.connect("database.db") as conn:
        await conn.execute(
            f"""
            INSERT INTO access_types(user_id,create_config,delete_config,add_admin,delete_admin,send_message_channel,send_message_user)
            VALUES (?,?,?,?,?,?,?)
            """,
            (str(user_id),create_config,delete_config,add_admin,delete_admin,send_message_channel,send_message_user),
        )
        await conn.commit()

async def Read_All_User():
    async with aiosqlite.connect("database.db") as conn:
        Cursor=await conn.execute("""
            SELECT * FROM User
            """)
        return await Cursor.fetchall()

async def Read_All_Confing():
    async with aiosqlite.connect("database.db") as conn:
        Cursor=await conn.execute("""
            SELECT * FROM Confing
            """)
        return await Cursor.fetchall()

async def Read_All_Price():
    async with aiosqlite.connect("database.db") as conn:
        Cursor=await conn.execute("""
            SELECT * FROM Price
            """)
        return await Cursor.fetchall()

async def Read_All_access_types():
    async with aiosqlite.connect("database.db") as conn:
        Cursor=await conn.execute("""
            SELECT * FROM access_types
            """)
        return await Cursor.fetchall()

async def Read_AccessTypes_By_UserId(user_id):
    async with aiosqlite.connect("database.db") as conn:
        Cursor = await conn.execute("""
            SELECT * FROM access_types
            WHERE user_id = ?
        """, (user_id,))
        return await Cursor.fetchone()


async def Read_User_By_Username(username:str):
    async with aiosqlite.connect("database.db") as conn:
        Cursor=await conn.execute("""
            SELECT * FROM User WHERE username=?
            """,(username,))
        return await Cursor.fetchone()

async def Read_User_By_Userid(user_id:int):
    async with aiosqlite.connect("database.db") as conn:
        Cursor=await conn.execute("""
            SELECT * FROM User WHERE user_id=?
            """,(str(user_id),))
        return await Cursor.fetchone()
async def Create_Admin(user_id, role, access_type_id):
    async with aiosqlite.connect("database.db") as conn:
        await conn.execute("""
            INSERT INTO Admins (user_id, role, access_type_id)
            VALUES (?, ?, ?)
        """, (user_id, role, access_type_id))
        await conn.commit()
async def Read_Admin(admin_id):
    async with aiosqlite.connect("database.db") as conn:
        Cursor = await conn.execute("""
            SELECT * FROM Admins
            WHERE user_id = ?
        """, (admin_id,))
        return await Cursor.fetchone()
async def Read_All_Admins():
    async with aiosqlite.connect("database.db") as conn:
        Cursor = await conn.execute("""
            SELECT * FROM Admins
        """)
        return await Cursor.fetchall()
async def Update_Admin(admin_id, role, access_type_id):
    async with aiosqlite.connect("database.db") as conn:
        await conn.execute("""
            UPDATE Admins SET
                role = ?,
                access_type_id = ?
            WHERE id = ?
        """, (role, access_type_id, admin_id))
        await conn.commit()
async def Delete_Admin(admin_id):
    async with aiosqlite.connect("database.db") as conn:
        await conn.execute("""
            DELETE FROM Admins
            WHERE id = ?
        """, (admin_id,))
        await conn.commit()
