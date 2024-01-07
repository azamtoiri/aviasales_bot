from aiogram import Router


def setup_routers() -> Router:
    from .users import admin, start, help, echo, buy_tiket, search_ticket
    from .errors import error_handler

    router = Router()

    # Agar kerak bo'lsa, o'z filteringizni o'rnating

    router.include_routers(admin.router, start.router, help.router, error_handler.router,
                           buy_tiket.router, search_ticket.router)

    return router