from core.db import db

from sqlalchemy.sql import func

from slugify import slugify


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), nullable=True)
    content = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Student {self.title}>"

    def save(self):
        if not self.slug and self.title:
            self.slug = self.generate_slug(self.title)
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def generate_slug(title):
        slug = slugify(title)
        return slug
