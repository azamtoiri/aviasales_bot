from aiogram import Router


def setup_routers() -> Router:
    from .users import admin, start, help, echo
    from .errors import error_handler

    router = Router()

    # Agar kerak bo'lsa, o'z filteringizni o'rnating

    router.include_routers(admin.router, start.router, help.router, echo.router, error_handler.router)

    return router