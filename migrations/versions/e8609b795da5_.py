"""empty message

Revision ID: e8609b795da5
Revises: 10e288e136e9
Create Date: 2024-08-23 08:59:09.270298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8609b795da5'
down_revision = '10e288e136e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('file', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.NUMERIC(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
        batch_op.alter_column('paste_id',
               existing_type=sa.NUMERIC(),
               type_=sa.String(length=9),
               existing_nullable=True)

    with op.batch_alter_table('paste', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.NUMERIC(),
               type_=sa.String(length=9),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('paste', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.String(length=9),
               type_=sa.NUMERIC(),
               existing_nullable=False)

    with op.batch_alter_table('file', schema=None) as batch_op:
        batch_op.alter_column('paste_id',
               existing_type=sa.String(length=9),
               type_=sa.NUMERIC(),
               existing_nullable=True)
        batch_op.alter_column('id',
               existing_type=sa.Integer(),
               type_=sa.NUMERIC(),
               existing_nullable=False,
               autoincrement=True)

    # ### end Alembic commands ###
