"""new table

Revision ID: 6e9d2b3be90a
Revises: 51a45e3fb97a
Create Date: 2024-07-07 20:55:35.840581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e9d2b3be90a'
down_revision = '51a45e3fb97a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('filename', sa.String(), nullable=False),
    sa.Column('value', sa.String(), nullable=False),
    sa.Column('paste_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['paste_id'], ['paste.id'], name=op.f('fk_file_paste_id_paste')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_file'))
    )
    with op.batch_alter_table('file', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_file_paste_id'), ['paste_id'], unique=False)

    with op.batch_alter_table('paste', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.NUMERIC(),
               type_=sa.UUID(),
               existing_nullable=False)
        batch_op.drop_column('filename')
        batch_op.drop_column('value')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('paste', schema=None) as batch_op:
        batch_op.add_column(sa.Column('value', sa.VARCHAR(), nullable=False))
        batch_op.add_column(sa.Column('filename', sa.VARCHAR(), nullable=False))
        batch_op.alter_column('id',
               existing_type=sa.UUID(),
               type_=sa.NUMERIC(),
               existing_nullable=False)

    with op.batch_alter_table('file', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_file_paste_id'))

    op.drop_table('file')
    # ### end Alembic commands ###
