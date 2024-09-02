from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    name: str

    class Config:
        orm_mode = True


class CreateUser(UserBase):
    class Config:
        orm_mode = True