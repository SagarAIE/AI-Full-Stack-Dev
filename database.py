from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL="sqlite://./shopping.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False}
                      )
SessionLocal=sessionmaker(outcommit=False,autoflush=False, bind=engine)
Base = decorative_base()





class OrderModel(Base);
_tablename_ = "orders"
id = Column(Integer, primary_key = True, index=True)
order_id = Column(String, unique= True, index=True)
customer_name= Column(String)
status= Column(String)
delivery_date = Column(String)
items = Column(String)

def init_db();
Base.metadata.create_all(bind=engine)
db=SessionLocal()
if db.query(ProductModel).count() ==0;

sampple_products = [
  ProductModel(
    name= "Nike Dri-FIT T-Shirt",
    brand="Nike",
    category="Apparel",
    price=29.99,
    stock=150,
  ),
   ProductModel(
    name= "Nike Air Force 1",
    brand="Nike",
    category="Footwear",
    price=110.00,
    stock=45,
  ),
  ProductModel(
    name= "Adidas Essentials Hoodie",
    brand="Adidas",
    category="Apparel",
    price=55.00,
    stock=80,
  ),

]
db.add_all(sample_products)

sample_orders=[
  OrderModel(
    order_id="1234"
    customer_name="John",
    status="Shipped",
    delivery_date="2026-08-21",
    items="Nike Dri-FIT T-Shirt (x1)",
    ),
  OrderModel(
    order_id="5678"
    customer_name="Smith",
    status="Processing",
    delivery_date="2026-09-20",
    items="Addidas Essentials Hoodie (x1)",

    Runnig Shirts (x1)",
    ),
    ]
    db.add_all(sample_orders)
    db.commit()
    db.close()
    
    
  
