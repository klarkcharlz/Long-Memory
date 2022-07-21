# coding: utf-8
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, SmallInteger, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class UsersCustomuser(Base):
    __tablename__ = 'users_customuser'

    id = Column(Integer, primary_key=True)
    password = Column(String(128), nullable=False)
    last_login = Column(DateTime)
    is_superuser = Column(Boolean, nullable=False)
    username = Column(String(150), nullable=False)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    is_staff = Column(Boolean, nullable=False)
    is_active = Column(Boolean, nullable=False)
    date_joined = Column(DateTime, nullable=False)
    email_reminders = Column(Boolean, nullable=False)
    email = Column(String(254), nullable=False)
    telegram_reminders = Column(Boolean, nullable=False)
    telegram_id = Column(String(255), nullable=False)
    vk_reminders = Column(Boolean, nullable=False)
    vk_id = Column(String(255), nullable=False)
    avatar = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False)


class NotificationsNotification(Base):
    __tablename__ = 'notifications_notifications'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    description = Column(Text, nullable=False)
    period_type = Column(SmallInteger, nullable=False)
    next_notifications = Column(DateTime, nullable=False)
    is_active = Column(Boolean, nullable=False)
    created_at = Column(DateTime, nullable=False)
    user_id_id = Column(ForeignKey('users_customuser.id'), nullable=False, index=True)

    user_id = relationship('UsersCustomuser')
