"""empty message

Revision ID: 286cbab279ba
Revises: 65c80af2ef5d
Create Date: 2020-11-14 06:15:30.907874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '286cbab279ba'
down_revision = '65c80af2ef5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=30), nullable=False),
    sa.Column('username', sa.VARCHAR(length=30), nullable=True),
    sa.Column('secure_password', sa.VARCHAR(length=120), nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), nullable=False),
    sa.Column('role', sa.VARCHAR(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###