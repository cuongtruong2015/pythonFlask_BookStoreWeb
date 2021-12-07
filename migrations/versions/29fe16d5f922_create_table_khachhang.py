"""create table KhachHang

Revision ID: 29fe16d5f922
Revises: 
Create Date: 2021-12-01 10:29:23.099424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29fe16d5f922'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chi_tiet_hoa_don',
    sa.Column('MaCTHD', sa.Integer(), nullable=False),
    sa.Column('MaSach', sa.String(length=200), nullable=True),
    sa.Column('SoLuongMua', sa.Integer(), nullable=True),
    sa.Column('MaHoaDon', sa.Integer(), nullable=True),
    sa.Column('damua', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('MaCTHD')
    )
    op.create_table('hoa_don',
    sa.Column('MaHoaDon', sa.Integer(), nullable=False),
    sa.Column('MaKH', sa.Integer(), nullable=True),
    sa.Column('NgayMua', sa.DateTime(), nullable=True),
    sa.Column('damua', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('MaHoaDon')
    )
    op.create_table('khach_hang',
    sa.Column('MaKH', sa.Integer(), nullable=False),
    sa.Column('HoTen', sa.String(length=200), nullable=True),
    sa.Column('DiaChi', sa.String(length=200), nullable=True),
    sa.Column('SDT', sa.String(length=200), nullable=True),
    sa.Column('Email', sa.String(length=100), nullable=False),
    sa.Column('Username', sa.String(length=100), nullable=False),
    sa.Column('_password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('MaKH'),
    sa.UniqueConstraint('Email'),
    sa.UniqueConstraint('Username')
    )
    op.create_table('loai',
    sa.Column('MaLoai', sa.String(length=200), nullable=False),
    sa.Column('TenLoai', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('MaLoai')
    )
    op.create_table('sach',
    sa.Column('MaSach', sa.String(length=200), nullable=False),
    sa.Column('TenSach', sa.String(length=200), nullable=True),
    sa.Column('SoLuong', sa.Integer(), nullable=True),
    sa.Column('Gia', sa.Integer(), nullable=True),
    sa.Column('MaLoai', sa.String(length=200), nullable=True),
    sa.Column('SoTap', sa.String(length=200), nullable=True),
    sa.Column('Anh', sa.String(length=200), nullable=True),
    sa.Column('NgayNhap', sa.DateTime(), nullable=True),
    sa.Column('TacGia', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('MaSach')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sach')
    op.drop_table('loai')
    op.drop_table('khach_hang')
    op.drop_table('hoa_don')
    op.drop_table('chi_tiet_hoa_don')
    # ### end Alembic commands ###
