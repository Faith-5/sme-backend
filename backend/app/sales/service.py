from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.inventory.models import Product
from app.sales import models, schema


def create_sale(db: Session, sale: schema.SaleCreate):
    product = db.query(Product).filter(Product.id == sale.product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.stock_quantity < sale.quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock")

    # reduce stock
    product.stock_quantity -= sale.quantity

    total = product.selling_price * sale.quantity

    new_sale = models.Sale(
        product_id=product.id,
        quantity=sale.quantity,
        selling_price=product.selling_price,
        cost_price=product.cost_price,
        total_amount=total
    )

    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)

    return new_sale


def get_sales(db: Session):
    return db.query(models.Sale).all()