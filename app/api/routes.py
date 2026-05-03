from fastapi import APIRouter, Depends, HTTPException
from app.models.portfolio import Domain
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.schemas.schemas import AddDomain
router = APIRouter()

@router.get("/get_portfolio/{user_id}")
def get_portfolio(user_id: int, db:Session = Depends(get_db)):
    domains = db.query(Domain).filter(Domain.user_id == user_id).all()
    if not domains:
        raise HTTPException(status_code=404, detail="User not found");
    return domains

@router.post("/add_domain/")
def add_domain(add: AddDomain, db:Session = Depends(get_db)):
    
    #check if domain already exixted
    existing = db.query(Domain).filter(
        Domain.user_id == add.user_id, Domain.domain_name==add.domain_name
        ).first()
    if(existing):
        raise HTTPException(status_code=400, detail="Domain already exists")
    
    #create a new domain object
    new_domain = Domain(
        user_id=add.user_id,
        domain_name=add.domain_name,
        buy_price=add.buy_price,
        buy_date=add.buy_date
    )
    #save to database
    db.add(new_domain)
    db.commit()
    db.refresh(new_domain)

    return {
        "message": "Domain added successfully",
        "data": new_domain
    }
