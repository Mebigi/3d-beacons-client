"""empty message

Revision ID: 3e3a83a3b309
Revises: ee87d846bd15
Create Date: 2020-03-08 12:45:23.723901

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3e3a83a3b309'
down_revision = 'ee87d846bd15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('model_structure',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('original_path', sa.String(), nullable=False),
    sa.Column('identity', sa.Numeric(), nullable=True),
    sa.Column('similarity', sa.Numeric(), nullable=True),
    sa.Column('oligo_state', sa.String(), nullable=True),
    sa.Column('coverage', sa.Numeric(), nullable=True),
    sa.Column('qmean_version', sa.String(), nullable=True),
    sa.Column('qmean_avg_local_score', sa.Numeric(), nullable=True),
    sa.Column('model_data', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('pdb_created_at', sa.DateTime(), nullable=True),
    sa.Column('mmcif_created_at', sa.DateTime(), nullable=True),
    sa.Column('qmean_created_at', sa.DateTime(), nullable=True),
    sa.Column('model_data_created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('structure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('structure',
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('pdb_path', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('mmcif_path', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('quality_scores_path', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='structure_pkey')
    )
    op.drop_table('model_structure')
    # ### end Alembic commands ###