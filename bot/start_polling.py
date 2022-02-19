import asyncio
from utils import set_commands
from core import dispatcher, bot
import handlers


async def main(): 
    await set_commands(bot)
    
    handlers.register_command_handlers(dispatcher)
    handlers.register_products_handlers(dispatcher)
    handlers.register_home_handlers(dispatcher)
    handlers.register_auth_handlers(dispatcher)
    handlers.register_cart_handlers(dispatcher)

    print("starting")
    
    await dispatcher.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
    