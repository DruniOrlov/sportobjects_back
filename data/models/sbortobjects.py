import sqlalchemy
from pydantic import BaseModel
from sqlalchemy import *
from sqlalchemy.orm import DeclarativeBase
from ..pg_connector import Base


class SportObject(Base):
    __tablename__ = 'posts'

    id = Column(
        Integer,
        primary_key=True
    )
    name_rus = Column(
        String(128)
    )
    name_eng = Column(
        String(128)
    )
    active = Column(
        Boolean
    )
    short_description_rus = Column(
        String(255)
    )
    short_description_eng = Column(
        String(255)
    )
    full_description_rus = Column(
        Text
    )
    full_description_eng = Column(
        Text
    )
    mo = Column(
        String(128)
    )
    subject_federation = Column(
        String(128)
    )
    significance = Column(
        String(64),
        nullable=True
    )
    city_rus = Column(
        String(64)
    )
    city_eng = Column(
        String(64)
    )
    address_rus = Column(
        String(255)
    )
    address_eng = Column(
        String(255)
    )
    oktmo = Column(
        BigInteger
    )
    fcp = Column(
        String(128)
    )
    actions_with = Column(
        String(64),
        nullable=True
    )
    date_begin = Column(
        Date,
        nullable=True
    )
    date_end = Column(
        Date,
        nullable=True
    )
    all_cash = Column(
        BigInteger
    )
    cash_from_federal = Column(
        BigInteger,
        nullable=True
    )
    cash_from_federal_past = Column(
        BigInteger,
        nullable=True
    )
    cash_from_subject = Column(
        BigInteger,
        nullable=True
    )
    cash_from_subject_past = Column(
        BigInteger,
        nullable=True
    )
    cash_from_municipal = Column(
        BigInteger,
        nullable=True
    )
    cash_from_municipal_past = Column(
        BigInteger,
        nullable=True
    )
    cash_from_offbudget = Column(
        BigInteger,
        nullable=True
    )
    cash_from_offbudget_past = Column(
        BigInteger,
        nullable=True
    )
    keyable = Column(
        Boolean,
        nullable=True
    )
    controller_rus = Column(
        String(128),
        nullable=True
    )
    controller_eng = Column(
        String(128),
        nullable=True
    )
    address_controller_rus = Column(
        String(255),
        nullable=True
    )
    address_controller_eng = Column(
        String(255),
        nullable=True
    )
    phone_controller = Column(
        String(16),
        nullable=True
    )
    phone = Column(
        String(16),
        nullable=True
    )
    schedule_mo_fr = Column(
        String(64),
        nullable=True
    )
    schedule_sa = Column(
        String(64),
        nullable=True
    )
    schedule_su = Column(
        String(64),
        nullable=True
    )
    square = Column(
        Integer,
        nullable=True
    )
    email = Column(
        String(64),
        nullable=True
    )
    site_url = Column(
        String(64),
        nullable=True
    )
    registration = Column(
        Boolean,
        nullable=True
    )
    type = Column(
        String(255)
    )
    grade_of_championships = Column(
        String(128),
        nullable=True
    )
    sports = Column(
        String(255)
    )
    yandex_map_x = Column(
        Double,
    )
    yandex_map_y = Column(
        Double,
    )
    yandex_map_scale = Column(
        Integer
    )
    yandex_map_centre_x = Column(
        Double
    )
    yandex_map_centre_y = Column(
        Double
    )
    mini_x = Column(
        Double,
        nullable=True
    )
    mini_y = Column(
        Double,
        nullable=True
    )
    gen_plan = Column(
        Integer
    )
    additional_plans = Column(
        Integer
    )
    photos = Column(
        Integer
    )
    photos_url = Column(
        String(255),
        nullable=True
    )
    videos = Column(
        Integer,
        nullable=True
    )
    panorama = Column(
        Integer,
        nullable=True
    )
    web_streams = Column(
        Integer,
        nullable=True
    )
    other_materials = Column(
        Text
    )
