from app.database import Base, engine
import app.models  # make sure your models are imported so tables are created

Base.metadata.create_all(bind=engine)

print("✅ Tables created successfully!")
