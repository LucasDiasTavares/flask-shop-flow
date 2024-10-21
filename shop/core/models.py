import uuid
from . import database as db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, DateTime, DECIMAL, text, Float
from sqlalchemy.dialects.postgresql import UUID


class Category(db.Model):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=db.text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=db.text("CURRENT_TIMESTAMP"), onupdate=db.func.now())
    name = Column(String(100), unique=True, nullable=False)
    slug = Column(String(200), unique=True, nullable=False)
    is_active = Column(Boolean, default=False)
    parent_id = Column(Integer, ForeignKey("category.id"))

    def __repr__(self):
        return f"Category: {self.name}"


class Product(db.Model):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=db.text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=db.text("CURRENT_TIMESTAMP"), onupdate=db.func.now())
    pid = Column(UUID(as_uuid=True), unique=True, nullable=False, server_default=text("uuid_generate_v4()"))
    name = Column(String(200), unique=True, nullable=False)
    slug = Column(String(255), unique=True, nullable=False)
    description = Column(Text)
    is_digital = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    stock_status = Column(String(100), default="OUT_OF_STOCK")
    category = Column(Integer, ForeignKey("category.id"))
    seasonal_event = Column(Integer, ForeignKey("seasonal_event.id", nullable=True))

    def __repr__(self):
        return f"Product: {self.name}"


class ProductLine(db.Model):
    __tablename__ = "product_line"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=db.text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=db.text("CURRENT_TIMESTAMP"), onupdate=db.func.now())
    price = Column(DECIMAL(5, 2), default=0)
    sku = Column(UUID(as_uuid=True), default=uuid.uuid4)
    stock_qtd = Column(Integer, default=0)
    is_active = Column(Boolean, default=False)
    order = Column(Integer)
    weight = Column(Float)
    product_id = Column(Integer, ForeignKey("product.id"))

    def __repr__(self):
        return f"ProductLine: {self.id}"


class ProductImage(db.Model):
    __tablename__ = "product_image"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=db.text("CURRENT_TIMESTAMP"))
    alternative_text = Column(String(255))
    url = Column(String)
    order = Column(Integer)
    product_line_id = product_id = Column(Integer, ForeignKey("product_line.id"))

    def __repr__(self):
        return f"ProductImage: {self.id}"


class SeasonalEvent(db.Model):
    __tablename__ = "seasonal_event"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), unique=True, nullable=False)
    star_date = Column(DateTime)
    end_date = Column(DateTime)

    def __repr__(self):
        return f"SeasonalEvent: {self.name}"
