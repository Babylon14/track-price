from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Базовая модель"""
    
    @property
    def id_dict(self):
        return {"id": self.id}
    
    