"""Uzytkownik

Revision ID: 6b3038d396e3
Revises: 
Create Date: 2020-05-30 20:17:25.736435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b3038d396e3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('uzytkownik',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_uzytkownik_username'), 'uzytkownik', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_uzytkownik_username'), table_name='uzytkownik')
    op.drop_table('uzytkownik')
    # ### end Alembic commands ###
