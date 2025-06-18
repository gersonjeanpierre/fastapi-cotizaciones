# from sqlalchemy.orm import Session
# from typing import List, Optional

# from app.models import Product, ProductType, ExtraOption
# from app.schemas import (
#     ProductCreate,
#     ProductUpdate,
#     ProductTypeInDB,
#     ExtraOptionInDB,
# )

# def get_products(db: Session, product_id: int):
#     return db.query(Product).filter(Product.id == product_id).first()

# def get_all_products(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(Product).offset(skip).limit(limit).all()

# def create_product(db: Session, product: ProductCreate):
#     db_product = Product(
#         sku=product.sku,
#         name=product.name,
#         description=product.description,
#         unity_measure=product.unity_measure,
#         price=product.price,
#         image_url=product.image_url,
#     )
#     db.add(db_product)
#     db.commit()
#     db.refresh(db_product)

#     # Relaciones con ProductType
#     if product.product_type_ids:
#         for type_id in product.product_type_ids:
#             product_extra_option = ProductType(
#                 product_id=db_product.id,
#                 product_type_ihd=type_id
#             )
#             db.add(product_extra_option)
        

    

































# # from sqlalchemy.orm import Session
# # from typing import List, Optional
# # from datetime import datetime

# # from app.models import product as models # Importa el modelo Product
# # from app.schemas import product_type as schemas # Importa los esquemas de Product

# # # GET all products
# # def get_products(db: Session, skip: int = 0, limit: int = 100):
# #     return db.query(models.Product).offset(skip).limit(limit).all()

# # # GET product by ID
# # def get_product(db: Session, product_id: int):
# #     return db.query(models.Product).filter(models.Product.id == product_id).first()

# # # CREATE product
# # def create_product(db: Session, product: schemas.ProductCreate):
# #     db_product = models.Product(**product.model_dump())
# #     db.add(db_product)
# #     db.commit()
# #     db.refresh(db_product)
# #     return db_product

# # # UPDATE product
# # def update_product(db: Session, product_id: int, product_update: schemas.ProductCreate):
# #     db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
# #     if not db_product:
# #         return None

# #     for key, value in product_update.model_dump(exclude_unset=True).items():
# #         setattr(db_product, key, value)
    
# #     # SQLAlchemy gestiona updated_at automáticamente via onupdate=func.now()
# #     db.add(db_product)
# #     db.commit()
# #     db.refresh(db_product)
# #     return db_product

# # # DELETE product
# # def delete_product(db: Session, product_id: int):
# #     db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
# #     if not db_product:
# #         return None

# #     db.delete(db_product)
# #     db.commit()
# #     return db_product # Retorna el objeto eliminado, útil para confirmación