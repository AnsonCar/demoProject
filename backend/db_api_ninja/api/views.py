# from ninja import NinjaAPI
# api = NinjaAPI()

from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI

api = NinjaExtraAPI(title="DataBase NinjaExtra API")
api.register_controllers(NinjaJWTDefaultController)

from .user.router import router as userRouter
# from .user.router import auth as authRouter

api.add_router("/user", userRouter)
# api.add_router("/auth", authRouter)